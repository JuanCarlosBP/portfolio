#!/usr/bin/env node

import { readFile } from "node:fs/promises";
import path from "node:path";
import process from "node:process";
import { fileURLToPath } from "node:url";

export async function loadJson(filename) {
  return JSON.parse(await readFile(filename, "utf8"));
}

function resolveReference(reference, rootSchema) {
  if (!reference.startsWith("#/")) {
    throw new Error(`Unsupported external schema reference: ${reference}`);
  }
  return reference
    .slice(2)
    .split("/")
    .reduce(
      (value, key) =>
        value?.[key.replaceAll("~1", "/").replaceAll("~0", "~")],
      rootSchema,
    );
}

function matchesType(value, type) {
  if (type === "null") return value === null;
  if (type === "array") return Array.isArray(value);
  if (type === "object") {
    return value !== null && typeof value === "object" && !Array.isArray(value);
  }
  if (type === "integer") return Number.isInteger(value);
  return typeof value === type;
}

function validFormat(value, format) {
  if (format === "uri") {
    try {
      const url = new URL(value);
      return url.protocol === "https:";
    } catch {
      return false;
    }
  }
  if (format === "date-time") {
    return (
      /^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}(?:\.\d+)?(?:Z|[+-]\d{2}:\d{2})$/.test(
        value,
      ) && !Number.isNaN(new Date(value).getTime())
    );
  }
  return true;
}

function validateNode(value, schema, rootSchema, location, errors) {
  if (schema.$ref) {
    validateNode(
      value,
      resolveReference(schema.$ref, rootSchema),
      rootSchema,
      location,
      errors,
    );
    return;
  }
  if (schema.anyOf) {
    const matched = schema.anyOf.some((candidate) => {
      const candidateErrors = [];
      validateNode(value, candidate, rootSchema, location, candidateErrors);
      return candidateErrors.length === 0;
    });
    if (!matched) errors.push(`${location} does not match any allowed schema`);
    return;
  }
  if (schema.allOf) {
    for (const candidate of schema.allOf) {
      validateNode(value, candidate, rootSchema, location, errors);
    }
  }
  if (schema.if) {
    const conditionErrors = [];
    validateNode(value, schema.if, rootSchema, location, conditionErrors);
    if (conditionErrors.length === 0 && schema.then) {
      validateNode(value, schema.then, rootSchema, location, errors);
    } else if (conditionErrors.length > 0 && schema.else) {
      validateNode(value, schema.else, rootSchema, location, errors);
    }
  }
  if (schema.const !== undefined && value !== schema.const) {
    errors.push(`${location} must equal ${JSON.stringify(schema.const)}`);
  }
  if (schema.enum && !schema.enum.includes(value)) {
    errors.push(`${location} has an unsupported value`);
  }
  if (schema.type) {
    const types = Array.isArray(schema.type) ? schema.type : [schema.type];
    if (!types.some((type) => matchesType(value, type))) {
      errors.push(`${location} must be ${types.join(" or ")}`);
      return;
    }
  }
  if (typeof value === "string") {
    if (schema.minLength !== undefined && value.length < schema.minLength) {
      errors.push(`${location} is shorter than ${schema.minLength}`);
    }
    if (schema.maxLength !== undefined && value.length > schema.maxLength) {
      errors.push(`${location} is longer than ${schema.maxLength}`);
    }
    if (schema.pattern && !new RegExp(schema.pattern).test(value)) {
      errors.push(`${location} has an invalid format`);
    }
    if (schema.format && !validFormat(value, schema.format)) {
      errors.push(`${location} is not a valid ${schema.format}`);
    }
  }
  if (typeof value === "number" && schema.minimum !== undefined) {
    if (value < schema.minimum) errors.push(`${location} is below the minimum`);
  }
  if (Array.isArray(value)) {
    if (schema.minItems !== undefined && value.length < schema.minItems) {
      errors.push(`${location} has too few items`);
    }
    if (schema.maxItems !== undefined && value.length > schema.maxItems) {
      errors.push(`${location} has too many items`);
    }
    if (schema.uniqueItems) {
      const unique = new Set(value.map((item) => JSON.stringify(item)));
      if (unique.size !== value.length) errors.push(`${location} has duplicate items`);
    }
    if (schema.items) {
      value.forEach((item, index) =>
        validateNode(item, schema.items, rootSchema, `${location}[${index}]`, errors),
      );
    }
  }
  if (value && typeof value === "object" && !Array.isArray(value)) {
    for (const name of schema.required || []) {
      if (!(name in value)) errors.push(`${location}.${name} is required`);
    }
    for (const [name, child] of Object.entries(value)) {
      if (schema.properties?.[name]) {
        validateNode(
          child,
          schema.properties[name],
          rootSchema,
          `${location}.${name}`,
          errors,
        );
      } else if (schema.additionalProperties === false) {
        errors.push(`${location}.${name} is not allowed`);
      } else if (
        schema.additionalProperties &&
        typeof schema.additionalProperties === "object"
      ) {
        validateNode(
          child,
          schema.additionalProperties,
          rootSchema,
          `${location}.${name}`,
          errors,
        );
      }
    }
  }
}

export function validateAgainstSchema(feed, schema) {
  const errors = [];
  validateNode(feed, schema, schema, "$", errors);
  return errors;
}

function semanticErrors(feed, registry) {
  const errors = [];
  const projectIds = new Set();
  const projectRepositories = new Set();
  const appIds = new Set();
  const repositories = new Map();
  const configured = new Set(
    (registry?.repositories || []).map((entry) => entry.repository),
  );

  for (const repo of feed.repositories || []) {
    if (repositories.has(repo.repository)) {
      errors.push(`Duplicate repository entry: ${repo.repository}`);
    }
    repositories.set(repo.repository, repo);
    if (
      !configured.has(repo.repository) &&
      !["manifest", "topic"].includes(repo.approvalSource)
    ) {
      errors.push(`Repository is not approved: ${repo.repository}`);
    }
  }

  for (const project of feed.projects || []) {
    if (projectIds.has(project.id)) {
      errors.push(`Duplicate project id: ${project.id}`);
    }
    if (projectRepositories.has(project.repository)) {
      errors.push(`Duplicate project repository: ${project.repository}`);
    }
    projectIds.add(project.id);
    projectRepositories.add(project.repository);
    if (!repositories.has(project.repository)) {
      errors.push(`Project repository is absent from repositories: ${project.repository}`);
    }
    const ci = project.ci || {};
    const latestSha = project.latestCommit?.sha || null;
    const headSha = ci.headSha || null;
    const validHeadSha =
      headSha === null ||
      (typeof headSha === "string" && /^[a-fA-F0-9]{40}$/.test(headSha));
    const exactMatch = Boolean(
      latestSha &&
        headSha &&
        /^[a-fA-F0-9]{40}$/.test(latestSha) &&
        headSha === latestSha,
    );
    if (!validHeadSha) {
      errors.push(`CI head SHA is invalid: ${project.id}`);
    }
    if (typeof ci.matchesLatestCommit !== "boolean") {
      errors.push(`CI matchesLatestCommit must be boolean: ${project.id}`);
    } else if (ci.matchesLatestCommit !== exactMatch) {
      errors.push(`CI commit binding does not match latestCommit: ${project.id}`);
    }
    if (
      ["success", "failure", "cancelled", "running"].includes(ci.status) &&
      (!Number.isInteger(ci.runId) ||
        ci.runId <= 0 ||
        !validHeadSha ||
        !ci.headSha ||
        ci.matchesLatestCommit !== true ||
        !ci.url)
    ) {
      errors.push(`CI state has no matching identifiable run: ${project.id}`);
    }
    if (
      ci.status === "success" &&
      (ci.conclusion !== "success" || !ci.completedAt)
    ) {
      errors.push(`CI success has no identifiable successful run: ${project.id}`);
    }
    if (
      ci.status === "running" &&
      (!ci.startedAt || ci.completedAt !== null)
    ) {
      errors.push(`CI running has no identifiable active run: ${project.id}`);
    }
    if (
      ["failure", "cancelled"].includes(ci.status) &&
      (ci.conclusion !== ci.status || !ci.completedAt)
    ) {
      errors.push(`CI terminal state is inconsistent: ${project.id}`);
    }
  }

  for (const app of feed.apps || []) {
    if (appIds.has(app.id)) {
      errors.push(`Duplicate application id: ${app.id}`);
    }
    appIds.add(app.id);
    if (app.status === "published" && !app.storeUrl) {
      errors.push(`Published application requires storeUrl: ${app.id}`);
    }
    if (app.verified === true && (!Array.isArray(app.evidence) || app.evidence.length === 0)) {
      errors.push(`Verified application requires evidence: ${app.id}`);
    }
  }
  return errors;
}

export function assertFeedValid(feed, { schema, registry = null }) {
  const errors = [
    ...validateAgainstSchema(feed, schema),
    ...semanticErrors(feed, registry),
  ];
  if (errors.length) {
    throw new Error(`Invalid ProofOS feed:\n- ${errors.join("\n- ")}`);
  }
  return true;
}

export async function validateFeedFiles({
  root = process.cwd(),
  feedPath = ".proofos/feed.json",
  schemaPath = ".proofos/feed.schema.json",
  registryPath = "automation/proofos/proofos-registry.json",
} = {}) {
  const absolute = (filename) =>
    path.isAbsolute(filename) ? filename : path.join(root, filename);
  const [feed, schema, registry] = await Promise.all([
    loadJson(absolute(feedPath)),
    loadJson(absolute(schemaPath)),
    loadJson(absolute(registryPath)),
  ]);
  assertFeedValid(feed, { schema, registry });
  console.log(`Valid ProofOS feed: ${feed.projects.length} project(s).`);
  return feed;
}

const isEntryPoint =
  process.argv[1] &&
  fileURLToPath(import.meta.url) === path.resolve(process.argv[1]);

if (isEntryPoint) {
  validateFeedFiles({
    feedPath: process.argv[2] || ".proofos/feed.json",
    schemaPath: process.argv[3] || ".proofos/feed.schema.json",
    registryPath:
      process.argv[4] || "automation/proofos/proofos-registry.json",
  }).catch((error) => {
    console.error(error);
    process.exitCode = 1;
  });
}
