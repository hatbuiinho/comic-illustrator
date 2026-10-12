const { test } = require('node:test');
const assert = require('node:assert/strict');
const fs = require('fs');
const os = require('os');
const path = require('path');
const crypto = require('crypto');
const { verify } = require('../scripts/verify-text-reflow');
function fixture(change = () => {}) {
  const dir = fs.mkdtempSync(path.join(os.tmpdir(), 'reflow-'));
  try {
    const style = { fontFamily: 'Example', fontStyle: 'Regular', fontSizePt: 12, leadingPt: 15, tracking: 0, scaleX: 1, scaleY: 1, color: '#000000', highlight: null };
    const source = { provenance: { path: 'script.txt', locator: 'p1' }, paragraphs: [{ id: 'p1', runs: [{ text: 'Chữ Việt.', style }] }] };
    const rendered = { paragraphs: structuredClone(source.paragraphs), renderer: 'test fixture', overflowCount: 0, fontSubstitutions: [], lines: [{ paragraphId: 'p1', start: 0, end: 9, boundsPt: [10, 10, 80, 15], availableBoundsPt: [10, 10, 90, 15] }] };
    const bytes = 'fixture artifact';
    const hash = 'sha256:' + crypto.createHash('sha256').update(bytes).digest('hex');
    const proof = { schemaVersion: 1, source: 'source.json', rendered: 'rendered.json', preview: 'preview.png', previewSha256: hash, wrapPath: 'wrap.svg', wrapSha256: hash };
    change({ source, rendered, proof });
    for (const [name, value] of Object.entries({ source, rendered, proof })) fs.writeFileSync(path.join(dir, name + '.json'), JSON.stringify(value));
    for (const name of ['preview.png', 'wrap.svg']) fs.writeFileSync(path.join(dir, name), bytes);
    return verify(path.join(dir, 'proof.json'));
  } finally { fs.rmSync(dir, { recursive: true, force: true }); }
}
test('preserves Vietnamese content and measured fit', () => assert.equal(fixture().status, 'PASS'));
test('allows different run segmentation after wrap', () => assert.equal(fixture(({ rendered }) => { const r = rendered.paragraphs[0].runs[0]; rendered.paragraphs[0].runs = [{ text: 'Chữ ', style: r.style }, { text: 'Việt.', style: r.style }]; }).status, 'PASS'));
for (const [name, change] of [
  ['changed accent', ({ rendered }) => { rendered.paragraphs[0].runs[0].text = 'Chu Việt.'; }],
  ['font shrink', ({ rendered }) => { rendered.paragraphs[0].runs[0].style.fontSizePt = 11; }],
  ['overflow', ({ rendered }) => { rendered.overflowCount = 1; }],
  ['outside wrap', ({ rendered }) => { rendered.lines[0].boundsPt[2] = 100; }],
  ['missing text coverage', ({ rendered }) => { rendered.lines[0].end = 8; }],
  ['stale preview', ({ proof }) => { proof.previewSha256 = 'old'; }],
  ['font fallback', ({ rendered }) => { rendered.fontSubstitutions = ['fallback']; }],
  ['missing metrics', ({ rendered }) => { delete rendered.lines; }],
  ['missing style', ({ source, rendered }) => { delete source.paragraphs[0].runs[0].style.leadingPt; delete rendered.paragraphs[0].runs[0].style.leadingPt; }]
]) test('rejects ' + name, () => assert.equal(fixture(change).status, 'FAIL'));
