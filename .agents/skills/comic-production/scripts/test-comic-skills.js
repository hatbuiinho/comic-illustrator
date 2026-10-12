#!/usr/bin/env node
const fs = require("fs");
const os = require("os");
const path = require("path");
const crypto = require("crypto");
const { spawnSync } = require("child_process");

const root = path.resolve(__dirname, "../..");
const workspace = path.resolve(root, "../..");
const temporary = fs.mkdtempSync(path.join(os.tmpdir(), "comic-skills-test-"));
const results = [];
function run(name, command, args, expected = 0) {
  const result = spawnSync(command, args, { cwd: workspace, encoding: "utf8" });
  const passed = result.status === expected;
  results.push({ name, passed, status: result.status, expected, output: (result.stdout || result.stderr || "").trim().slice(0, 500) });
}
try {
  const context = path.join(root, "comic-continuity-manager/scripts/comic-context.py");
  const ledger = path.join(root, "comic-continuity-manager/tests/ledger.fixture.yaml");
  run("continuity validate", "python3", [context, "validate", ledger]);
  run("continuity valid event", "python3", [context, "commit-event", ledger, path.join(root, "comic-continuity-manager/tests/event.fixture.yaml")]);
  run("continuity rejects inference", "python3", [context, "commit-event", ledger, path.join(root, "comic-continuity-manager/tests/invalid-inference-event.fixture.yaml")], 2);
  run("page-state v2 valid", "python3", [context, "validate", path.join(root, "comic-continuity-manager/tests/page-state-v2/page-state.yaml")]);
  run("page-state rejects legacy schema", "python3", [context, "validate", path.join(root, "comic-continuity-manager/tests/page-state-legacy/page-state.yaml")], 1);
  run("page-state rejects production before composition", "python3", [context, "validate", path.join(root, "comic-continuity-manager/tests/page-state-gate-skip/page-state.yaml")], 1);
  const episode = path.join(temporary, "episode");
  fs.mkdirSync(path.join(episode, "continuity"), { recursive: true });
  fs.writeFileSync(path.join(episode, "episode.json"), '{}\n');
  fs.writeFileSync(path.join(episode, "source.txt"), "before\n");
  const sourceHash = `sha256:${crypto.createHash("sha256").update("before\n").digest("hex")}`;
  const artifactA = path.join(episode, "continuity", "a.json");
  fs.writeFileSync(artifactA, `${JSON.stringify({ schemaVersion: 1, scope: { episode: "fixture" }, status: "CURRENT", generatedFrom: [{ path: "source.txt", fingerprint: sourceHash }] }, null, 2)}\n`);
  const artifactHash = `sha256:${crypto.createHash("sha256").update(fs.readFileSync(artifactA)).digest("hex")}`;
  fs.writeFileSync(path.join(episode, "continuity", "b.json"), `${JSON.stringify({ schemaVersion: 1, scope: { episode: "fixture" }, status: "CURRENT", generatedFrom: [{ path: "continuity/a.json", fingerprint: artifactHash }] }, null, 2)}\n`);
  fs.writeFileSync(path.join(episode, "source.txt"), "after\n");
  run("continuity detects stale", "python3", [context, "check-stale", artifactA], 1);
  const invalidation = spawnSync("python3", [context, "invalidate-dependents", episode, path.join(episode, "source.txt")], { cwd: workspace, encoding: "utf8" });
  const invalidationPassed = invalidation.status === 0 && invalidation.stdout.includes('"artifact": "continuity/a.json"') && invalidation.stdout.includes('"artifact": "continuity/b.json"');
  results.push({ name: "transitive invalidation", passed: invalidationPassed, status: invalidation.status, expected: 0, output: invalidation.stdout.trim().slice(0, 500) });

  const outputs = path.join(temporary, "outputs");
  const allocate = path.join(root, "comic-image-production/scripts/allocate-version.js");
  run("version reserve v1", process.execPath, [allocate, outputs, "page001-option1", "png", "--reserve"]);
  run("version reserve v2", process.execPath, [allocate, outputs, "page001-option1", "png", "--reserve"]);
  if (!fs.existsSync(path.join(outputs, "page001-option1-v2.png"))) results.push({ name: "version increments", passed: false, status: null, expected: 0, output: "Thiếu v2" });
  else results.push({ name: "version increments", passed: true, status: 0, expected: 0, output: "v2 exists" });

  const preview = path.join(temporary, "composition.png");
  run("semantic composition preview PNG", process.execPath, [path.join(root, "comic-shot-design/scripts/render-composition-preview.js"), path.join(root, "comic-shot-design/tests/semantic-composition.fixture.svg"), path.join(root, "comic-shot-design/tests/semantic-composition.fixture.json"), preview]);
  if (!fs.existsSync(preview) || fs.statSync(preview).size === 0) results.push({ name: "preview non-empty", passed: false, output: "PNG missing/empty" });
  const debugPreview = path.join(temporary, "composition-debug.png");
  run("composition debug PNG", process.execPath, [path.join(root, "comic-shot-design/scripts/render-composition-debug.js"), path.join(root, "comic-shot-design/tests/composition.fixture.json"), debugPreview]);
  run("semantic gate rejects debug-box", process.execPath, [path.join(root, "comic-shot-design/scripts/render-composition-preview.js"), debugPreview.replace(/\.png$/, ".svg"), path.join(root, "comic-shot-design/tests/semantic-composition.fixture.json"), path.join(temporary, "must-not-exist.png")], 1);

  run("visual QA completeness", process.execPath, [path.join(root, "comic-visual-qa/scripts/validate-visual-qa.js"), path.join(root, "comic-visual-qa/tests/visual-qa.fixture.json")]);
  run("layout QA and PNG overlay", process.execPath, [path.join(root, "comic-layout-qa/scripts/layout-frame-qa.js"), path.join(root, "comic-layout-qa/tests/spine-skip.fixture.json"), path.join(temporary, "layout-qa")]);
  const overlays = fs.existsSync(path.join(temporary, "layout-qa")) ? fs.readdirSync(path.join(temporary, "layout-qa")).filter(name => name.endsWith("-overlay.png")) : [];
  results.push({ name: "layout overlay PNG exists", passed: overlays.length > 0, status: overlays.length ? 0 : 1, expected: 0, output: overlays.join(", ") });
  const autoLayoutManifest = path.join(temporary, "auto-layout.json");
  fs.writeFileSync(autoLayoutManifest, `${JSON.stringify({
    defaults: { checks: { hardFrame: "NOT_APPLICABLE", ratio: "NOT_APPLICABLE", subjectExclusion: "REQUIRED", textReadability: "REQUIRED", textIntegrity: "REQUIRED", printSafe: "NOT_APPLICABLE", spine: "NOT_APPLICABLE" } },
    spreads: [{ id: "auto-layout", canvas: { width: 900, height: 600 }, pageImage: "composition.png", artworks: [{ id: "fluid-art", layoutMode: "AUTO_LAYOUT", output: "composition.png", proposedTextFrames: [{ x: 0.05, y: 0.05, width: 0.3, height: 0.2 }], subjectExclusionZones: [{ x: 0.04, y: 0.04, width: 0.32, height: 0.22 }], subjectBounds: [{ id: "subject", box: { x: 0.55, y: 0.3, width: 0.3, height: 0.5 } }], readingOrder: ["body-1"], fixedTextElements: ["page-number"], textReadability: { status: "PASS", evidence: "Clean preview readable" }, textIntegrity: { status: "PASS", evidence: "Content and reading order preserved" } }] }]
  }, null, 2)}\n`);
  run("AUTO_LAYOUT rejects unverified reflow", process.execPath, [path.join(root, "comic-layout-qa/scripts/layout-frame-qa.js"), autoLayoutManifest, path.join(temporary, "auto-layout-qa")], 1);
  run("text reflow evidence checks", process.execPath, ["--test", path.join(root, "comic-layout-qa/tests/text-reflow.test.js")]);
  run("proxy fidelity artifact and region checks", process.execPath, ["--test", path.join(root, "comic-layout-qa/tests/proxy-fidelity.test.js")]);
  run("delivery preflight", process.execPath, [path.join(root, "comic-delivery/scripts/validate-delivery.js"), path.join(root, "comic-delivery/tests/valid.fixture.json")]);
  const deliveryDir = path.join(temporary, "delivery");
  fs.mkdirSync(path.join(deliveryDir, "outputs"), { recursive: true });
  fs.writeFileSync(path.join(deliveryDir, "outputs", "art-v1.png"), "fixture");
  fs.writeFileSync(path.join(deliveryDir, "consumer.json"), '{"image":"outputs/art-v1.png"}\n');
  const deliveryManifest = path.join(deliveryDir, "delivery.json");
  fs.writeFileSync(deliveryManifest, `${JSON.stringify({
    output: "outputs/art-v1.png",
    approvedDir: "approved",
    projectRoot: ".",
    userSelectedOutput: true,
    checks: { visualQa: "PASS", layoutQa: "NOT_APPLICABLE" },
    pathUpdates: [{ file: "consumer.json", from: "outputs/art-v1.png", to: "approved/art-v1.png" }]
  }, null, 2)}\n`);
  run("delivery transaction", process.execPath, [path.join(root, "comic-delivery/scripts/execute-delivery.js"), deliveryManifest, "--execute"]);
  const delivered = fs.existsSync(path.join(deliveryDir, "approved", "art-v1.png"));
  const updated = fs.readFileSync(path.join(deliveryDir, "consumer.json"), "utf8").includes("approved/art-v1.png");
  results.push({ name: "delivery file and path updated", passed: delivered && updated, status: delivered && updated ? 0 : 1, expected: 0, output: `delivered=${delivered} updated=${updated}` });

  const layeredDir = path.join(temporary, "layered-delivery");
  fs.mkdirSync(path.join(layeredDir, "outputs"), { recursive: true });
  for (const name of ["page-v3-master.png", "page-v3-bg.png", "page-v3-mgfg.png", "page-v3-wrap.svg", "page-v3-layout-preview.png"]) fs.writeFileSync(path.join(layeredDir, "outputs", name), "fixture");
  const layeredManifest = path.join(layeredDir, "delivery.json");
  fs.writeFileSync(layeredManifest, `${JSON.stringify({
    outputs: ["outputs/page-v3-master.png", "outputs/page-v3-bg.png", "outputs/page-v3-mgfg.png", "outputs/page-v3-wrap.svg", "outputs/page-v3-layout-preview.png"],
    approvedDir: "approved",
    projectRoot: ".",
    userSelectedOutput: true,
    status: "layer-package-ready",
    checks: { visualQa: "PASS", layoutQa: "PASS", layerPackage: "PASS" }
  }, null, 2)}\n`);
  run("layer package preflight", process.execPath, [path.join(root, "comic-delivery/scripts/validate-delivery.js"), layeredManifest]);
  run("layer package delivery", process.execPath, [path.join(root, "comic-delivery/scripts/execute-delivery.js"), layeredManifest, "--execute"]);
  const layeredDelivered = ["page-v3-master.png", "page-v3-bg.png", "page-v3-mgfg.png", "page-v3-wrap.svg", "page-v3-layout-preview.png"].every(name => fs.existsSync(path.join(layeredDir, "approved", name)));
  results.push({ name: "layer package files delivered together", passed: layeredDelivered, status: layeredDelivered ? 0 : 1, expected: 0, output: `delivered=${layeredDelivered}` });
} finally {
  fs.rmSync(temporary, { recursive: true, force: true });
}
for (const result of results) console.log(`${result.passed ? "PASS" : "FAIL"}: ${result.name}${result.output ? ` — ${result.output.replace(/\n/g, " ")}` : ""}`);
const failures = results.filter(result => !result.passed);
console.log(`\n${results.length - failures.length}/${results.length} tests passed.`);
process.exit(failures.length ? 1 : 0);
