#!/usr/bin/env node
const path = require("path");
const { spawnSync } = require("child_process");

const pageDir = process.argv[2];
if (!pageDir) {
  console.error("Usage: node run-page-qa.js <page-directory>");
  process.exit(2);
}
const resolved = path.resolve(pageDir);
const qa = path.join(__dirname, "layout-frame-qa.js");
const result = spawnSync(process.execPath, [qa, path.join(resolved, "layout.json"), path.join(resolved, "qa")], { stdio: "inherit" });
process.exit(result.status ?? 1);
