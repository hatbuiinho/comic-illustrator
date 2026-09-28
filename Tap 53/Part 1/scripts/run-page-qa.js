#!/usr/bin/env node
// Wrapper tương thích; implementation dùng chung nằm trong repo skill.
const path = require("path");
const { spawnSync } = require("child_process");
const target = path.resolve(__dirname, "../../../.agents/skills/comic-layout-qa/scripts/run-page-qa.js");
const result = spawnSync(process.execPath, [target, ...process.argv.slice(2)], { stdio: "inherit" });
process.exit(result.status ?? 1);
