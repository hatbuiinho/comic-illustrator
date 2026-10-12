#!/usr/bin/env node
const fs = require('fs');
const path = require('path');
const crypto = require('crypto');
const { isDeepStrictEqual } = require('util');

function verify(proofPath) {
  const errors = [];
  const check = (ok, message) => { if (!ok) errors.push(message); };
  try {
    const base = path.dirname(path.resolve(proofPath));
    const read = name => JSON.parse(fs.readFileSync(path.resolve(base, name), 'utf8'));
    const proof = JSON.parse(fs.readFileSync(proofPath, 'utf8'));
    check(proof.schemaVersion === 1, 'schemaVersion phải là 1');
    for (const [file, hash] of [['preview', 'previewSha256'], ['wrapPath', 'wrapSha256']]) {
      const bytes = fs.readFileSync(path.resolve(base, proof[file]));
      check(bytes.length > 0 && proof[hash] === 'sha256:' + crypto.createHash('sha256').update(bytes).digest('hex'), `${file}: rỗng hoặc hash không khớp`);
    }
    const source = read(proof.source), rendered = read(proof.rendered);
    check(Boolean(source.provenance?.path && source.provenance?.locator), 'Thiếu provenance text nguồn');
    check(typeof rendered.renderer === 'string' && rendered.renderer.trim().length > 0, 'Thiếu renderer');
    check(rendered.overflowCount === 0, 'Overflow hoặc thiếu số đo overflow');
    check(Array.isArray(rendered.fontSubstitutions) && rendered.fontSubstitutions.length === 0, 'Font substitution hoặc thiếu kết quả');
    const requiredStyle = ['fontFamily', 'fontStyle', 'fontSizePt', 'leadingPt', 'tracking', 'scaleX', 'scaleY', 'color', 'highlight'];
    function expand(doc, label) {
      if (!Array.isArray(doc.paragraphs) || !doc.paragraphs.length) throw Error(`${label}: thiếu paragraphs`);
      const ids = new Set();
      return doc.paragraphs.map(p => {
        check(typeof p.id === 'string' && p.id.length > 0 && !ids.has(p.id), `${label}: ID đoạn thiếu/trùng`);
        ids.add(p.id);
        if (!Array.isArray(p.runs) || !p.runs.length) throw Error(`${label}: thiếu runs`);
        const chars = p.runs.flatMap(r => {
          if (typeof r.text !== 'string') throw Error(`${label}: text không hợp lệ`);
          check(requiredStyle.every(k => Object.hasOwn(r.style || {}, k)), `${label}: thiếu style`);
          check(['fontSizePt', 'leadingPt', 'scaleX', 'scaleY'].every(k => Number.isFinite(r.style?.[k]) && r.style[k] > 0) && Number.isFinite(r.style?.tracking), `${label}: thông số typography không hợp lệ`);
          check(['fontFamily', 'fontStyle', 'color'].every(k => typeof r.style?.[k] === 'string' && r.style[k].length > 0), `${label}: font/màu thiếu`);
          return Array.from(r.text, char => ({ char, style: r.style }));
        });
        return { id: p.id, chars };
      });
    }
    const original = expand(source, 'source'), actual = expand(rendered, 'rendered');
    check(isDeepStrictEqual(original, actual), 'Nội dung, thứ tự đoạn hoặc typography bị thay đổi');
    if (!Array.isArray(rendered.lines) || !rendered.lines.length) throw Error('Thiếu số đo lines');
    let lineIndex = 0;
    const box = b => Array.isArray(b) && b.length === 4 && b.every(Number.isFinite) && b[2] > 0 && b[3] > 0;
    for (const p of actual) {
      let offset = 0;
      while (lineIndex < rendered.lines.length && rendered.lines[lineIndex].paragraphId === p.id) {
        const line = rendered.lines[lineIndex++];
        check(Number.isInteger(line.start) && Number.isInteger(line.end) && line.start === offset && line.end > line.start && line.end <= p.chars.length, `${p.id}: coverage dòng sai`);
        offset = line.end;
        const b = line.boundsPt, a = line.availableBoundsPt;
        check(box(b) && box(a), `${p.id}: thiếu bounds hợp lệ`);
        if (box(b) && box(a)) check(b[0] >= a[0] - 0.01 && b[1] >= a[1] - 0.01 && b[0] + b[2] <= a[0] + a[2] + 0.01 && b[1] + b[3] <= a[1] + a[3] + 0.01, `${p.id}: dòng vượt vùng khả dụng`);
      }
      check(offset === p.chars.length, `${p.id}: chữ chưa được dàn hết`);
    }
    check(lineIndex === rendered.lines.length, 'Dòng thừa hoặc sai thứ tự đọc');
  } catch (error) { errors.push(error.message); }
  return { status: errors.length ? 'FAIL' : 'PASS', errors };
}
module.exports = { verify };
if (require.main === module) {
  const result = verify(process.argv[2]);
  console.log(JSON.stringify(result, null, 2));
  process.exitCode = result.errors.length ? 1 : 0;
}
