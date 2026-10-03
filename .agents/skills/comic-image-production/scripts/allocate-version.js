#!/usr/bin/env node
const fs = require("fs");
const path = require("path");

const args = process.argv.slice(2);
const reserve = args.includes("--reserve");
const clean = args.filter(arg => arg !== "--reserve");
if (clean.length < 3 || ["-h", "--help"].includes(clean[0])) {
  console.log("Usage: node allocate-version.js <outputs-dir> <base-name> <extension> [--reserve]");
  process.exit(clean.length ? 0 : 2);
}

const [dirArg, rawBase, rawExtension] = clean;
if (!/^[a-zA-Z0-9][a-zA-Z0-9._-]*$/.test(rawBase) || rawBase.includes("..")) {
  console.error("ERROR: base-name không hợp lệ.");
  process.exit(2);
}
const extension = rawExtension.replace(/^\./, "").toLowerCase();
if (!/^[a-z0-9]+$/.test(extension)) {
  console.error("ERROR: extension không hợp lệ.");
  process.exit(2);
}
const outputDir = path.resolve(dirArg);
if (path.basename(outputDir) !== "outputs") {
  console.error("ERROR: thư mục đích phải có tên outputs.");
  process.exit(2);
}
fs.mkdirSync(outputDir, { recursive: true });
const escaped = rawBase.replace(/[.*+?^${}()|[\]\\]/g, "\\$&");
const matcher = new RegExp(`^${escaped}-v(\\d+)\\.${extension}$`, "i");
let maximum = 0;
for (const name of fs.readdirSync(outputDir)) {
  const match = name.match(matcher);
  if (match) maximum = Math.max(maximum, Number(match[1]));
}

let version = maximum + 1;
let candidate;
while (true) {
  candidate = path.join(outputDir, `${rawBase}-v${version}.${extension}`);
  if (!reserve) break;
  try {
    const descriptor = fs.openSync(candidate, "wx");
    fs.closeSync(descriptor);
    break;
  } catch (error) {
    if (error.code !== "EEXIST") throw error;
    version += 1;
  }
}
console.log(JSON.stringify({ path: candidate, version, reserved: reserve }, null, 2));
