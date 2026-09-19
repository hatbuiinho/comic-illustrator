#!/usr/bin/env node
/** Run layout QA for one isolated page package. */
const path = require('path');
const { spawnSync } = require('child_process');

const pageDir = process.argv[2];
if (!pageDir) {
  console.error('Usage: node run-page-qa.js pages/page-010');
  process.exit(2);
}
const resolved = path.resolve(pageDir);
const layout = path.join(resolved, 'layout.json');
const qa = path.join(__dirname, 'layout-frame-qa.js');
const result = spawnSync(process.execPath, [qa, layout, path.join(resolved, 'qa')], { stdio: 'inherit' });
process.exit(result.status ?? 1);
