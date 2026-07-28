#!/usr/bin/env node

import { mkdir, rename, writeFile } from "node:fs/promises";
import path from "node:path";
import process from "node:process";
import { fileURLToPath } from "node:url";

import { assertFeedValid, loadJson } from "./validate-feed.mjs";

export const GENERATOR_VERSION = "3.2.2";
export const CI_STATES = new Set([
  "success",
  "failure",
  "cancelled",
  "running",
  "unavailable",
]);
export const PROJECT_STATES = new Set([
  "demonstrated",
  "in-development",
  "planned",
  "archived",
]);
export const APP_STATES = new Set([
  "concept",
  "in-development",
  "testing",
  "review",
  "published",
  "paused",
  "archived",
]);

const API_VERSION = "2022-11-28";
const DEFAULT_OWNER = "JuanCarlosBP";
const DEFAULT_CONFIG = "automation/proofos/proofos-registry.json";
const DEFAULT_OUTPUT = ".proofos/feed.json";
const DEFAULT_SCHEMA = ".proofos/feed.schema.json";
const DEFAULT_COMMIT_SCAN_LIMIT = 20;
const MAX_COMMIT_SCAN_LIMIT = 100;
export const GENERATED_FEED_COMMIT_MESSAGE =
  "chore(proofos): update verified evidence feed [skip ci]";
export const GENERATED_FEED_COMMIT_IDENTITY = "proofos-feed[bot]";
export const GENERATED_FEED_PATH = ".proofos/feed.json";

function requiredText(value, name, max = 500) {
  if (typeof value !== "string" || !value.trim() || value.length > max) {
    throw new Error(`${name} must be non-empty text with at most ${max} characters`);
  }
  return value.trim();
}

function optionalText(value, name, max = 500) {
  if (value === null || value === undefined || value === "") return null;
  return requiredText(value, name, max);
}

function repositoryName(value) {
  const repository = requiredText(value, "repository", 180);
  if (!/^[A-Za-z0-9_.-]+\/[A-Za-z0-9_.-]+$/.test(repository)) {
    throw new Error(`Invalid repository: ${repository}`);
  }
  return repository;
}

function isoDate(value, fallback = null) {
  if (!value) return fallback;
  const date = new Date(value);
  return Number.isNaN(date.getTime()) ? fallback : date.toISOString();
}

function gitSha(value) {
  return typeof value === "string" && /^[a-fA-F0-9]{40}$/.test(value)
    ? value
    : null;
}

function requiredIsoDate(value, name) {
  const normalized = isoDate(value);
  if (!normalized) throw new Error(`${name} must be a valid date-time`);
  return normalized;
}

function optionalArray(value, name, max, normalize) {
  if (value === undefined || value === null) return [];
  if (!Array.isArray(value) || value.length > max) {
    throw new Error(`${name} must be an array with at most ${max} items`);
  }
  return value.map((item, index) => normalize(item, `${name}[${index}]`));
}

function commitScanLimit(value, source) {
  if (value === undefined || value === null) return DEFAULT_COMMIT_SCAN_LIMIT;
  if (
    !Number.isInteger(value) ||
    value < 1 ||
    value > MAX_COMMIT_SCAN_LIMIT
  ) {
    throw new Error(
      `${source}.commitScanLimit must be an integer between 1 and ${MAX_COMMIT_SCAN_LIMIT}`,
    );
  }
  return value;
}

export function normalizeAppConfig(input, source = "app") {
  if (!input || typeof input !== "object" || Array.isArray(input)) {
    throw new Error(`${source} must be an object`);
  }
  const status = requiredText(input.status, `${source}.status`, 40);
  if (!APP_STATES.has(status)) {
    throw new Error(`${source}.status is not supported`);
  }
  if (typeof input.verified !== "boolean") {
    throw new Error(`${source}.verified must be boolean`);
  }
  const storeUrl = optionalText(input.storeUrl, `${source}.storeUrl`, 500);
  if (status === "published" && !storeUrl) {
    throw new Error(`${source}.storeUrl is required when status is published`);
  }
  const evidence = optionalArray(
    input.evidence,
    `${source}.evidence`,
    24,
    (value, name) => requiredText(value, name, 500),
  );
  if (input.verified && evidence.length === 0) {
    throw new Error(`${source}.evidence is required when verified is true`);
  }
  return {
    id: requiredText(input.id, `${source}.id`, 80),
    name: requiredText(input.name, `${source}.name`, 120),
    platform: requiredText(input.platform, `${source}.platform`, 40),
    status,
    summary: requiredText(input.summary, `${source}.summary`, 500),
    iconUrl: optionalText(input.iconUrl, `${source}.iconUrl`, 500),
    screenshots: optionalArray(
      input.screenshots,
      `${source}.screenshots`,
      12,
      (value, name) => requiredText(value, name, 500),
    ),
    technologies: optionalArray(
      input.technologies,
      `${source}.technologies`,
      24,
      (value, name) => requiredText(value, name, 60),
    ),
    repositoryUrl: optionalText(
      input.repositoryUrl,
      `${source}.repositoryUrl`,
      500,
    ),
    storeUrl,
    privacyPolicyUrl: optionalText(
      input.privacyPolicyUrl,
      `${source}.privacyPolicyUrl`,
      500,
    ),
    version: optionalText(input.version, `${source}.version`, 80),
    releaseDate: input.releaseDate
      ? requiredIsoDate(input.releaseDate, `${source}.releaseDate`)
      : null,
    updatedAt: requiredIsoDate(input.updatedAt, `${source}.updatedAt`),
    evidence,
    verified: input.verified,
  };
}

function repositoryUrl(repository) {
  return `https://github.com/${repository}`;
}

export function normalizeProjectConfig(input, source = "project") {
  const repository = repositoryName(input.repository);
  const status = requiredText(input.status, `${source}.status`, 40);
  if (!PROJECT_STATES.has(status)) {
    throw new Error(`${source}.status is not supported`);
  }
  if (!Array.isArray(input.skills) || input.skills.length > 24) {
    throw new Error(`${source}.skills must be an array with at most 24 items`);
  }
  const workflowPath = requiredText(
    input.workflowPath,
    `${source}.workflowPath`,
    220,
  );
  if (!workflowPath.startsWith(".github/workflows/")) {
    throw new Error(`${source}.workflowPath must point inside .github/workflows`);
  }
  return {
    id: requiredText(input.id, `${source}.id`, 80),
    name: requiredText(input.name, `${source}.name`, 120),
    repository,
    summary: requiredText(input.summary, `${source}.summary`, 500),
    status,
    category: requiredText(input.category, `${source}.category`, 100),
    skills: input.skills.map((skill, index) =>
      requiredText(skill, `${source}.skills[${index}]`, 60),
    ),
    featured: Boolean(input.featured),
    defaultBranch: optionalText(
      input.defaultBranch || input.branch,
      `${source}.defaultBranch`,
      120,
    ),
    workflowName: requiredText(
      input.workflowName,
      `${source}.workflowName`,
      160,
    ),
    workflowPath,
    workflowBranch: optionalText(
      input.workflowBranch || input.branch || input.defaultBranch,
      `${source}.workflowBranch`,
      120,
    ),
    commitScanLimit: commitScanLimit(input.commitScanLimit, source),
    evidence:
      input.evidence && typeof input.evidence === "object" && !Array.isArray(input.evidence)
        ? input.evidence
        : {},
    approvalSource: input.approvalSource || "registry",
  };
}

export function mapWorkflowRun(run, config, latestCommitSha = null) {
  const base = {
    workflowName: config.workflowName,
    workflowPath: config.workflowPath,
    branch: config.workflowBranch || config.defaultBranch || "main",
    headSha: null,
    matchesLatestCommit: false,
    runId: null,
    status: "unavailable",
    conclusion: null,
    startedAt: null,
    completedAt: null,
    url: null,
  };
  if (!run) return base;

  const headSha = gitSha(run.head_sha);
  const expectedSha = gitSha(latestCommitSha);
  const matchesLatestCommit = Boolean(
    headSha && expectedSha && headSha === expectedSha,
  );
  const status = !matchesLatestCommit
    ? "unavailable"
    : ["queued", "in_progress", "waiting", "requested", "pending"].includes(
          run.status,
        )
      ? "running"
      : run.status === "completed" &&
          ["success", "failure", "cancelled"].includes(run.conclusion)
        ? run.conclusion
        : "unavailable";

  return {
    ...base,
    headSha,
    matchesLatestCommit,
    runId: Number.isInteger(run.id) ? run.id : null,
    status,
    conclusion: optionalText(run.conclusion, "workflow conclusion", 60),
    startedAt: isoDate(run.run_started_at || run.created_at),
    completedAt:
      run.status === "completed"
        ? isoDate(run.updated_at || run.completed_at)
        : null,
    url: optionalText(run.html_url, "workflow URL", 500),
  };
}

function normalizeManifest(manifest, repository, owner) {
  if (!manifest || manifest.schemaVersion !== 1 || manifest.owner !== owner) {
    throw new Error(`${repository}/portfolio.json has an invalid owner or schema`);
  }
  return normalizeProjectConfig(
    {
      ...manifest.project,
      repository,
      approvalSource: "manifest",
    },
    `${repository}/portfolio.json`,
  );
}

function topicConfig(repo, owner, registry) {
  const approvedTopics = new Set(registry.approvedTopics || []);
  const matchingTopic = (repo.topics || []).find((topic) => approvedTopics.has(topic));
  if (!matchingTopic) return null;
  return normalizeProjectConfig(
    {
      repository: repo.full_name,
      id: repo.name.toLowerCase().replace(/[^a-z0-9-]+/g, "-"),
      name: repo.name,
      summary: repo.description || `Repositorio aprobado de ${owner}.`,
      status: repo.archived ? "archived" : "in-development",
      category: "software project",
      skills: (repo.topics || []).filter((topic) => topic !== matchingTopic).slice(0, 12),
      featured: false,
      defaultBranch: repo.default_branch || "main",
      workflowName: "Repository quality",
      workflowPath: ".github/workflows/ci.yml",
      workflowBranch: repo.default_branch || "main",
      approvalSource: "topic",
    },
    `${repo.full_name} topic approval`,
  );
}

function baseHeaders(token) {
  return {
    Accept: "application/vnd.github+json",
    "X-GitHub-Api-Version": API_VERSION,
    "User-Agent": `ProofOS-feed-generator/${GENERATOR_VERSION}`,
    ...(token ? { Authorization: `Bearer ${token}` } : {}),
  };
}

export function createGitHubClient({ fetchImpl = fetch, token = "" } = {}) {
  return async function github(route, { optional = false } = {}) {
    const response = await fetchImpl(`https://api.github.com${route}`, {
      headers: baseHeaders(token),
    });
    if (optional && response.status === 404) return null;
    if (!response.ok) {
      throw new Error(`GitHub ${response.status} for ${route}`);
    }
    return response.json();
  };
}

async function readManifest(github, repository, owner) {
  const response = await github(`/repos/${repository}/contents/portfolio.json`, {
    optional: true,
  });
  if (!response || response.type !== "file" || response.encoding !== "base64") {
    return null;
  }
  const text = Buffer.from(
    String(response.content).replace(/\n/g, ""),
    "base64",
  ).toString("utf8");
  return normalizeManifest(JSON.parse(text), repository, owner);
}

async function discoverConfigs(registry, github, eventRepository, errors) {
  const owner = requiredText(registry.owner || DEFAULT_OWNER, "registry.owner", 80);
  const configured = new Map(
    registry.repositories.map((entry, index) => {
      const config = normalizeProjectConfig(entry, `repositories[${index}]`);
      return [config.repository, config];
    }),
  );

  let repositories = [];
  try {
    repositories = await github(
      `/users/${encodeURIComponent(owner)}/repos?type=owner&sort=updated&per_page=100`,
    );
  } catch (error) {
    errors.push(`Repository discovery unavailable: ${error.message}`);
    return [...configured.values()];
  }

  for (const repo of repositories) {
    if (
      !repo ||
      repo.owner?.login !== owner ||
      repo.private ||
      repo.fork ||
      Number(repo.size) === 0 ||
      configured.has(repo.full_name)
    ) {
      continue;
    }

    let manifest = null;
    try {
      manifest = await readManifest(github, repo.full_name, owner);
    } catch (error) {
      errors.push(`Ignored invalid manifest for ${repo.full_name}: ${error.message}`);
      continue;
    }
    const approved = manifest || topicConfig(repo, owner, registry);
    if (!approved) continue;
    if (repo.archived && approved.status !== "archived") continue;
    configured.set(repo.full_name, approved);
  }

  if (eventRepository && !configured.has(eventRepository)) {
    errors.push(`Ignored unapproved repository event: ${eventRepository}`);
  }
  return [...configured.values()].sort((left, right) =>
    left.repository.localeCompare(right.repository),
  );
}

async function latestConfiguredWorkflow(
  github,
  repository,
  config,
  branch,
  latestCommitSha,
  eventWorkflowHeadSha = "",
) {
  const workflowId = encodeURIComponent(config.workflowPath);
  const workflowBranch = config.workflowBranch || branch;
  const data = await github(
    `/repos/${repository}/actions/workflows/${workflowId}/runs?branch=${encodeURIComponent(workflowBranch)}&per_page=20`,
  );
  const runs = Array.isArray(data.workflow_runs) ? data.workflow_runs : [];
  const eligible = runs
    .filter(
      (run) =>
        run.head_branch === workflowBranch &&
        gitSha(run.head_sha),
    )
    .sort(
      (left, right) =>
        new Date(right.run_started_at || right.created_at || 0) -
        new Date(left.run_started_at || left.created_at || 0),
    );
  const eventHeadSha = gitSha(eventWorkflowHeadSha);
  const matchingRun = eligible.find(
    (run) =>
      run.head_sha === latestCommitSha &&
      (!eventHeadSha || run.head_sha === eventHeadSha),
  );
  const historicalRun = matchingRun
    ? null
    : eventHeadSha
      ? eligible.find((run) => run.head_sha === eventHeadSha) || eligible[0] || null
      : eligible[0] || null;
  return mapWorkflowRun(matchingRun || historicalRun, {
    ...config,
    workflowBranch,
  }, latestCommitSha);
}

function latestCommitRecord(commit) {
  if (!commit) return null;
  const sha = requiredText(commit.sha, "commit.sha", 80);
  return {
    sha,
    shortSha: sha.slice(0, 7),
    message: requiredText(
      String(commit.commit?.message || "").split("\n")[0],
      "commit.message",
      300,
    ),
    date: isoDate(commit.commit?.committer?.date || commit.commit?.author?.date),
    url: requiredText(commit.html_url, "commit.url", 500),
  };
}

function configuredCommitIdentity(commitDetails, role) {
  const embeddedName = commitDetails?.commit?.[role]?.name;
  if (typeof embeddedName === "string" && embeddedName.trim()) {
    return embeddedName.trim();
  }
  const apiLogin = commitDetails?.[role]?.login;
  return typeof apiLogin === "string" ? apiLogin.trim() : "";
}

export function isGeneratedFeedCommit(commitDetails) {
  if (!commitDetails || typeof commitDetails !== "object") return false;
  const files = commitDetails.files;
  return (
    commitDetails.commit?.message === GENERATED_FEED_COMMIT_MESSAGE &&
    configuredCommitIdentity(commitDetails, "author") ===
      GENERATED_FEED_COMMIT_IDENTITY &&
    configuredCommitIdentity(commitDetails, "committer") ===
      GENERATED_FEED_COMMIT_IDENTITY &&
    Array.isArray(files) &&
    files.length === 1 &&
    files[0]?.filename === GENERATED_FEED_PATH
  );
}

async function latestSignificantCommit(github, repository, branch, limit) {
  const recent = await github(
    `/repos/${repository}/commits?sha=${encodeURIComponent(branch)}&per_page=${limit}`,
  );
  if (!Array.isArray(recent) || recent.length === 0) {
    throw new Error(`No recent commits are available for ${branch}`);
  }

  for (const candidate of recent) {
    const sha = gitSha(candidate?.sha);
    if (!sha) {
      throw new Error(`A recent commit on ${branch} has no verifiable SHA`);
    }

    let details;
    try {
      details = await github(
        `/repos/${repository}/commits/${encodeURIComponent(sha)}`,
      );
    } catch {
      // Conservative fallback: without file details, the commit cannot be
      // classified as an internal feed-only commit.
      return candidate;
    }

    if (!isGeneratedFeedCommit(details)) return details;
  }

  throw new Error(
    `No significant commit was found within the latest ${limit} commits on ${branch}`,
  );
}

function pullRequestRecord(pull) {
  if (!pull) return null;
  return {
    number: pull.number,
    title: requiredText(pull.title, "pull request title", 300),
    mergedAt: isoDate(pull.merged_at),
    url: requiredText(pull.html_url, "pull request URL", 500),
  };
}

function releaseRecord(release) {
  if (!release) return null;
  return {
    tag: requiredText(release.tag_name, "release tag", 120),
    name: requiredText(release.name || release.tag_name, "release name", 200),
    publishedAt: isoDate(release.published_at || release.created_at),
    url: requiredText(release.html_url, "release URL", 500),
  };
}

function evidenceFor(config, repo, pull, ci) {
  const evidence = { repository: repo.html_url };
  if (Number.isInteger(config.evidence.issue)) {
    evidence.issue = `${repo.html_url}/issues/${config.evidence.issue}`;
  }
  if (Number.isInteger(config.evidence.pullRequest)) {
    evidence.pullRequest = `${repo.html_url}/pull/${config.evidence.pullRequest}`;
  }
  if (pull?.html_url) evidence.latestPullRequest = pull.html_url;
  if (ci?.url) evidence.workflowRun = ci.url;
  return evidence;
}

export async function collectProject(
  config,
  github,
  { eventWorkflowHeadSha = "" } = {},
) {
  const repository = config.repository;
  const repo = await github(`/repos/${repository}`);
  if (repo.private || repo.fork || Number(repo.size) === 0) {
    throw new Error(`${repository} is private, a fork, or empty`);
  }
  const branch = config.defaultBranch || repo.default_branch;
  const commit = await latestSignificantCommit(
    github,
    repository,
    branch,
    config.commitScanLimit,
  );
  const latestCommit = latestCommitRecord(commit);
  const [pulls, release, ci] = await Promise.all([
    github(`/repos/${repository}/pulls?state=closed&sort=updated&direction=desc&per_page=30`),
    github(`/repos/${repository}/releases/latest`, { optional: true }),
    latestConfiguredWorkflow(
      github,
      repository,
      config,
      branch,
      latestCommit.sha,
      eventWorkflowHeadSha,
    ),
  ]);
  const mergedPull = (pulls || [])
    .filter((pull) => pull.merged_at)
    .sort((left, right) => new Date(right.merged_at) - new Date(left.merged_at))[0];
  const latestMergedPullRequest = pullRequestRecord(mergedPull);
  const latestRelease = releaseRecord(release);
  const updatedAt =
    latestCommit?.date ||
    latestMergedPullRequest?.mergedAt ||
    latestRelease?.publishedAt ||
    isoDate(repo.updated_at);

  return {
    project: {
      id: config.id,
      name: config.name,
      repository,
      repositoryUrl: repo.html_url,
      defaultBranch: branch,
      status: repo.archived ? "archived" : config.status,
      category: config.category,
      summary: config.summary,
      skills: config.skills,
      featured: config.featured,
      latestCommit,
      latestMergedPullRequest,
      latestRelease,
      ci,
      evidence: evidenceFor(config, repo, mergedPull, ci),
      updatedAt,
    },
    repository: {
      repository,
      repositoryUrl: repo.html_url,
      defaultBranch: branch,
      status: repo.archived ? "archived" : "active",
      archived: Boolean(repo.archived),
      approvalSource: config.approvalSource,
      updatedAt: isoDate(repo.updated_at) || updatedAt,
    },
  };
}

function unavailableCi(config) {
  return mapWorkflowRun(null, config);
}

function fallbackProject(config, previous, now) {
  if (previous) {
    const headSha = gitSha(previous.ci?.headSha);
    return {
      ...previous,
      ci: {
        ...previous.ci,
        headSha,
        status: "unavailable",
        matchesLatestCommit: Boolean(
          headSha && headSha === previous.latestCommit?.sha,
        ),
        conclusion: null,
        completedAt: previous.ci?.completedAt || null,
      },
    };
  }
  return {
    id: config.id,
    name: config.name,
    repository: config.repository,
    repositoryUrl: repositoryUrl(config.repository),
    defaultBranch: config.defaultBranch || "main",
    status: config.status,
    category: config.category,
    summary: config.summary,
    skills: config.skills,
    featured: config.featured,
    latestCommit: null,
    latestMergedPullRequest: null,
    latestRelease: null,
    ci: unavailableCi(config),
    evidence: { repository: repositoryUrl(config.repository) },
    updatedAt: now,
  };
}

function fallbackRepository(config, previous, now) {
  return (
    previous || {
      repository: config.repository,
      repositoryUrl: repositoryUrl(config.repository),
      defaultBranch: config.defaultBranch || "main",
      status: config.status === "archived" ? "archived" : "active",
      archived: config.status === "archived",
      approvalSource: config.approvalSource,
      updatedAt: now,
    }
  );
}

function activityFromProjects(projects) {
  const activity = [];
  for (const project of projects) {
    const add = (type, title, occurredAt, url) => {
      if (!occurredAt || !url) return;
      activity.push({
        type,
        repository: project.repository,
        title,
        occurredAt,
        url,
      });
    };
    add(
      "commit",
      project.latestCommit?.message,
      project.latestCommit?.date,
      project.latestCommit?.url,
    );
    add(
      "pull_request",
      project.latestMergedPullRequest?.title,
      project.latestMergedPullRequest?.mergedAt,
      project.latestMergedPullRequest?.url,
    );
    add(
      "release",
      project.latestRelease?.name,
      project.latestRelease?.publishedAt,
      project.latestRelease?.url,
    );
    add(
      "ci",
      `${project.ci.workflowName}: ${project.ci.status}`,
      project.ci.completedAt || project.ci.startedAt,
      project.ci.url,
    );
  }
  return activity
    .sort((left, right) => new Date(right.occurredAt) - new Date(left.occurredAt))
    .slice(0, 50);
}

function comparableFeed(feed) {
  const copy = structuredClone(feed);
  delete copy.generatedAt;
  return copy;
}

function sameEffectiveContent(left, right) {
  if (!left || !right) return false;
  return JSON.stringify(comparableFeed(left)) === JSON.stringify(comparableFeed(right));
}

export async function buildFeed({
  registry,
  schema,
  previousFeed = null,
  github,
  now = new Date().toISOString(),
  eventRepository = "",
  eventWorkflowHeadSha = "",
}) {
  if (
    !registry ||
    registry.schemaVersion !== 1 ||
    !Array.isArray(registry.repositories)
  ) {
    throw new Error("ProofOS registry has an unsupported schema");
  }
  const owner = requiredText(registry.owner || DEFAULT_OWNER, "registry.owner", 80);
  const errors = [];
  const configs = await discoverConfigs(
    registry,
    github,
    eventRepository ? repositoryName(eventRepository) : "",
    errors,
  );
  const previousProjects = new Map(
    (previousFeed?.projects || []).map((project) => [project.repository, project]),
  );
  const previousRepositories = new Map(
    (previousFeed?.repositories || []).map((repo) => [repo.repository, repo]),
  );
  const projects = [];
  const repositories = [];
  const apps = (registry.apps || previousFeed?.apps || []).map((app, index) =>
    normalizeAppConfig(app, `registry.apps[${index}]`),
  );

  for (const config of configs) {
    try {
      const collected = await collectProject(config, github, {
        eventWorkflowHeadSha,
      });
      projects.push(collected.project);
      repositories.push(collected.repository);
    } catch (error) {
      errors.push(`${config.repository}: ${error.message}`);
      projects.push(
        fallbackProject(config, previousProjects.get(config.repository), now),
      );
      repositories.push(
        fallbackRepository(
          config,
          previousRepositories.get(config.repository),
          now,
        ),
      );
    }
  }

  projects.sort((left, right) => left.id.localeCompare(right.id));
  repositories.sort((left, right) =>
    left.repository.localeCompare(right.repository),
  );
  const feed = {
    schemaVersion: 1,
    generatedAt: now,
    generatorVersion: GENERATOR_VERSION,
    owner: {
      login: owner,
      profileUrl: `https://github.com/${owner}`,
    },
    projects,
    apps,
    repositories,
    activity: activityFromProjects(projects),
    degraded: errors.length > 0,
    errors: [...new Set(errors)].slice(0, 50),
  };

  assertFeedValid(feed, { schema, registry });
  if (sameEffectiveContent(feed, previousFeed)) {
    return { feed: previousFeed, changed: false };
  }
  return { feed, changed: true };
}

async function readPrevious(outputPath, schema, registry) {
  try {
    const previous = await loadJson(outputPath);
    assertFeedValid(previous, { schema, registry });
    return previous;
  } catch {
    return null;
  }
}

async function writeJsonAtomic(filename, value) {
  await mkdir(path.dirname(filename), { recursive: true });
  const temporary = `${filename}.tmp`;
  await writeFile(temporary, `${JSON.stringify(value, null, 2)}\n`, "utf8");
  await rename(temporary, filename);
}

export async function runGenerator({
  root = process.cwd(),
  configPath = process.env.PROOFOS_CONFIG || DEFAULT_CONFIG,
  outputPath = process.env.PROOFOS_OUTPUT || DEFAULT_OUTPUT,
  schemaPath = process.env.PROOFOS_SCHEMA || DEFAULT_SCHEMA,
  token = process.env.PROOFOS_GITHUB_TOKEN || process.env.GITHUB_TOKEN || "",
  eventRepository = process.env.PROOFOS_EVENT_REPOSITORY || "",
  eventWorkflowHeadSha =
    process.env.PROOFOS_EVENT_WORKFLOW_HEAD_SHA || "",
  fetchImpl = fetch,
  now = new Date().toISOString(),
} = {}) {
  const absolute = (filename) =>
    path.isAbsolute(filename) ? filename : path.join(root, filename);
  const [registry, schema] = await Promise.all([
    loadJson(absolute(configPath)),
    loadJson(absolute(schemaPath)),
  ]);
  const previousFeed = await readPrevious(absolute(outputPath), schema, registry);
  const github = createGitHubClient({ fetchImpl, token });
  const result = await buildFeed({
    registry,
    schema,
    previousFeed,
    github,
    now,
    eventRepository,
    eventWorkflowHeadSha,
  });
  await writeJsonAtomic(absolute(outputPath), result.feed);
  console.log(
    `${result.changed ? "Updated" : "Unchanged"} ProofOS feed with ${result.feed.projects.length} project(s)${result.feed.degraded ? " in degraded mode" : ""}.`,
  );
  return result;
}

const isEntryPoint =
  process.argv[1] &&
  fileURLToPath(import.meta.url) === path.resolve(process.argv[1]);

if (isEntryPoint) {
  runGenerator().catch((error) => {
    console.error(error);
    process.exitCode = 1;
  });
}
