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
const discover = spawnSync(process.execPath, [path.join(__dirname, "discover-layout.js"), resolved], { encoding: "utf8" });
if (discover.status !== 0) {
  process.stderr.write(discover.stdout || discover.stderr);
  process.exit(discover.status || 1);
}
const found = JSON.parse(discover.stdout);
const result = spawnSync(process.execPath, [qa, path.join(resolved, found.selected), path.join(resolved, "qa")], { stdio: "inherit" });
process.exit(result.status ?? 1);
