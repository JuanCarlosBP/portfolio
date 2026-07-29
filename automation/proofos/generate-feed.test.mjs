import assert from "node:assert/strict";
import { readFile } from "node:fs/promises";
import test from "node:test";

import { buildFeed } from "./generate-feed.mjs";

const registry = JSON.parse(
  await readFile(
    new URL("./proofos-registry.json", import.meta.url),
    "utf8",
  ),
);

const schema = JSON.parse(
  await readFile(
    new URL("../../.proofos/feed.schema.json", import.meta.url),
    "utf8",
  ),
);

const REAL_SHA =
  "9bbc9cb39bafc1530d404561dbcb32054880cbfc";

const REAL_DATE =
  "2026-07-28T23:58:41Z";

function commitFixture() {
  return {
    sha: REAL_SHA,
    commit: {
      message:
        "feat(jcbp): install verified evidence feed automation (#5)",
      author: {
        name: "Juan Carlos Bohórquez Plato",
        date: REAL_DATE,
      },
      committer: {
        name: "Juan Carlos Bohórquez Plato",
        date: REAL_DATE,
      },
    },
    author: {
      login: "JuanCarlosBP",
    },
    committer: {
      login: "JuanCarlosBP",
    },
    files: [
      {
        filename:
          "automation/proofos/generate-feed.mjs",
        status: "modified",
      },
    ],
    html_url:
      `https://github.com/JuanCarlosBP/portfolio/commit/${REAL_SHA}`,
  };
}

function githubFixture(repositoryUpdatedAt) {
  const commit = commitFixture();

  const repository = {
    full_name: "JuanCarlosBP/portfolio",
    name: "portfolio",
    owner: {
      login: "JuanCarlosBP",
    },
    html_url:
      "https://github.com/JuanCarlosBP/portfolio",
    private: false,
    fork: false,
    archived: false,
    size: 100,
    topics: [],
    default_branch: "main",
    updated_at: repositoryUpdatedAt,
  };

  return async function github(route) {
    if (
      route.startsWith(
        "/users/JuanCarlosBP/repos?",
      )
    ) {
      return [repository];
    }

    if (
      route ===
      "/repos/JuanCarlosBP/portfolio"
    ) {
      return repository;
    }

    if (
      route.startsWith(
        "/repos/JuanCarlosBP/portfolio/commits?sha=main&per_page=",
      )
    ) {
      return [commit];
    }

    if (
      route ===
      `/repos/JuanCarlosBP/portfolio/commits/${REAL_SHA}`
    ) {
      return commit;
    }

    if (
      route.startsWith(
        "/repos/JuanCarlosBP/portfolio/pulls?",
      )
    ) {
      return [
        {
          number: 5,
          title:
            "feat(jcbp): install verified evidence feed automation",
          merged_at: REAL_DATE,
          html_url:
            "https://github.com/JuanCarlosBP/portfolio/pull/5",
        },
      ];
    }

    if (
      route ===
      "/repos/JuanCarlosBP/portfolio/releases/latest"
    ) {
      return null;
    }

    if (
      route.startsWith(
        "/repos/JuanCarlosBP/portfolio/actions/workflows/",
      )
    ) {
      return {
        workflow_runs: [],
      };
    }

    if (
      route ===
      "/repos/JuanCarlosBP/portfolio/contents/portfolio.json"
    ) {
      return null;
    }

    throw new Error(
      `Unexpected fixture route: ${route}`,
    );
  };
}

test(
  "feed-bot repository metadata does not create another effective feed change",
  async () => {
    const first = await buildFeed({
      registry,
      schema,
      github: githubFixture(
        "2026-07-28T23:59:20Z",
      ),
      now:
        "2026-07-29T00:01:45.328Z",
    });

    const second = await buildFeed({
      registry,
      schema,
      previousFeed: first.feed,
      github: githubFixture(
        "2026-07-29T00:05:00Z",
      ),
      now:
        "2026-07-29T06:17:00.000Z",
    });

    assert.equal(
      first.changed,
      true,
    );

    assert.equal(
      second.changed,
      false,
    );

    assert.equal(
      second.feed.generatedAt,
      first.feed.generatedAt,
    );

    assert.equal(
      first.feed.repositories[0].updatedAt,
      first.feed.projects[0].updatedAt,
    );

    assert.equal(
      second.feed.repositories[0].updatedAt,
      first.feed.repositories[0].updatedAt,
    );
  },
);
