const test = require("node:test");
const assert = require("node:assert/strict");
const fs = require("fs"), os = require("os"), path = require("path"), crypto = require("crypto");
const { verify } = require("../scripts/verify-proxy-fidelity.js");
const hash = file => crypto.createHash("sha256").update(fs.readFileSync(file)).digest("hex");

function fixture(change = () => {}) {
  const dir = fs.mkdtempSync(path.join(os.tmpdir(), "proxy-fidelity-"));
  const source = path.join(dir, "source.pdf"), svg = path.join(dir, "composition.svg"), preview = path.join(dir, "preview.png");
  fs.writeFileSync(source, "source-layout-page-10"); fs.writeFileSync(preview, "preview-v1");
  const lines = (id, count, size = 16.188) => `<g id="${id}" data-render-kind="rendered-placeholder-text">${Array.from({ length: count }, (_, i) => `<text y="${i * 18}" font-size="${size}pt">placeholder</text>`).join("")}</g>`;
  fs.writeFileSync(svg, `<svg xmlns="http://www.w3.org/2000/svg" data-dpi="160" viewBox="0 0 1802 1279">${lines("text-left", 23)}${lines("text-right", 21)}</svg>`);
  const proof = { schemaVersion: 3, contract: "TEXT_PROXY_INTEGRATION", spatialComparisonIgnored: true,
    artifacts: { source: { path: "source.pdf", page: 10, sha256: hash(source) }, semanticSvg: { path: "composition.svg", dpi: 160, sha256: hash(svg) }, preview: { path: "preview.png", sha256: hash(preview) } },
    sourceTextRegions: [{ id: "left-vietnamese", lineCount: 23, medianGlyphHeightPt: 16.188 }, { id: "right-translation-placeholder", lineCount: 21, medianGlyphHeightPt: 16.188 }],
    proxyTextRegions: [{ id: "proxy-left", sourceRegionId: "left-vietnamese", svgGroupId: "text-left" }, { id: "proxy-right", sourceRegionId: "right-translation-placeholder", svgGroupId: "text-right" }],
    readingContinuity: "PASS", readability: "PASS", artisticIntegration: "PASS", paragraphRhythmReview: "PASS", typesettingFeasibility: "PASS", wrapReview: "PASS" };
  change({ source, svg, preview, proof }); fs.writeFileSync(path.join(dir, "proof.json"), JSON.stringify(proof));
  return verify(path.join(dir, "proof.json"));
}

test("legacy schema 3 cannot open composition gate", () => assert.equal(fixture().status, "LAYOUT_COMPOSITION_NEEDS_REVISION"));
test("fails when right occurrence is omitted", () => { const r = fixture(({ proof }) => proof.proxyTextRegions.pop()); assert.equal(r.status, "LAYOUT_COMPOSITION_NEEDS_REVISION"); assert.match(r.errors.burden.join(" "), /right-translation-placeholder/); });
test("legacy fake PDF and self-declared metrics fail closed", () => assert.match(fixture().errors.artifact.join(" "), /typography đo trực tiếp/));
test("fails when preview changes after proof", () => { const r = fixture(({ preview }) => fs.appendFileSync(preview, "-changed")); assert.match(r.errors.artifact.join(" "), /preview.*SHA-256 không khớp/); });
