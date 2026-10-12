const test=require('node:test'),assert=require('node:assert/strict');
const fs=require('fs'),os=require('os'),path=require('path'),crypto=require('crypto'),{execFileSync}=require('child_process');
const {verify}=require('../scripts/verify-proxy-fidelity.js');
const hash=f=>crypto.createHash('sha256').update(fs.readFileSync(f)).digest('hex');
function fixture(change=()=>{}){
 const dir=fs.mkdtempSync(path.join(os.tmpdir(),'proxy-typography-test-'));
 try{
  const source=path.join(dir,'source.pdf'),svg=path.join(dir,'composition.svg'),preview=path.join(dir,'preview.png');
  const lines=(id,x,n)=>`<g id="${id}" font-family="DejaVu Sans" data-render-kind="rendered-placeholder-text">${Array.from({length:n},(_,i)=>`<text x="${x}" y="${160+i*37.786}" font-size="26.672px" data-paragraph-id="${id}-p${i<4?1:2}">Words that occupy real typography space.</text>`).join('')}</g>`;
  const content=`<svg xmlns="http://www.w3.org/2000/svg" width="810.709pt" height="575.433pt" viewBox="0 0 1802 1279">${lines('left',80,23)}${lines('right',1010,21)}</svg>`;
  const sourceSvg=path.join(dir,'source.svg');fs.writeFileSync(sourceSvg,content);execFileSync('rsvg-convert',['-f','pdf','-o',source,sourceSvg]);
  fs.writeFileSync(svg,content);execFileSync('rsvg-convert',['-o',preview,svg]);
  const proof={schemaVersion:4,contract:'TEXT_PROXY_INTEGRATION',spatialComparisonIgnored:true,
   artifacts:{source:{path:'source.pdf',page:1,sha256:hash(source)},semanticSvg:{path:'composition.svg',dpi:96,sha256:hash(svg)},preview:{path:'preview.png',sha256:hash(preview)}},
   sourceTextRegions:[{id:'left',lineCount:23,medianGlyphHeightPt:16,boundsPt:[0,0,405,575],paragraphOrder:['left-p1','left-p2'],paragraphLineCounts:[4,19]},{id:'right',lineCount:21,medianGlyphHeightPt:16,boundsPt:[405,0,405,575],paragraphOrder:['right-p1','right-p2'],paragraphLineCounts:[4,17]}],
   proxyTextRegions:[{id:'l',sourceRegionId:'left',svgGroupId:'left'},{id:'r',sourceRegionId:'right',svgGroupId:'right'}],
   readingContinuity:'PASS',readability:'PASS',artisticIntegration:'PASS',paragraphRhythmReview:'PASS',typesettingFeasibility:'PASS',wrapReview:'PASS'};
  change({source,svg,preview,proof,dir});proof.artifacts.semanticSvg.sha256=hash(svg);
  fs.writeFileSync(path.join(dir,'proof.json'),JSON.stringify(proof));return verify(path.join(dir,'proof.json'));
 }finally{fs.rmSync(dir,{recursive:true,force:true});}
}
test('correct scale ignores misleading 96 DPI',()=>{const r=fixture();assert.equal(r.status,'PROXY_COMPOSITION_PASS',JSON.stringify(r));});
test('Page 10 regression: 21.584 px font and 26 px leading fail',()=>{
 const r=fixture(({svg})=>fs.writeFileSync(svg,fs.readFileSync(svg,'utf8').replaceAll('26.672px','21.584px').replace(/y="([\d.]+)"/g,(_,v)=>`y="${160+(Number(v)-160)*26/37.786}"`)));
 assert.match(r.errors.layout.join(' '),/fontSizePt/);assert.match(r.errors.layout.join(' '),/leadingPt/);assert.equal(r.status,'LAYOUT_COMPOSITION_NEEDS_REVISION');
});
test('compressed leading fails with correct font',()=>assert.match(fixture(({svg})=>fs.writeFileSync(svg,fs.readFileSync(svg,'utf8').replace(/y="([\d.]+)"/g,(_,v)=>`y="${160+(Number(v)-160)*.69}"`))).errors.layout.join(' '),/leadingPt/));
test('compressed paragraph gap fails despite unchanged median leading',()=>assert.match(fixture(({svg})=>fs.writeFileSync(svg,fs.readFileSync(svg,'utf8').replace(/y="([\d.]+)"([^>]*data-paragraph-id="(?:left|right)-p2")/g,(_,v,tail)=>`y="${Number(v)-18}"${tail}`))).errors.layout.join(' '),/khoảng nghỉ/));
test('moving text preserves fidelity',()=>{const r=fixture(({svg})=>fs.writeFileSync(svg,fs.readFileSync(svg,'utf8').replace('id="left"','transform="translate(20 10)" id="left"').replace('id="right"','transform="translate(-20 20)" id="right"')));assert.equal(r.status,'PROXY_COMPOSITION_PASS',JSON.stringify(r));});
test('ancestor scale cannot hide shrinking',()=>assert.equal(fixture(({svg})=>fs.writeFileSync(svg,fs.readFileSync(svg,'utf8').replace('<g id="left"','<g transform="scale(.7)"><g id="left"').replace('</g><g id="right"','</g></g><g id="right"'))).status,'LAYOUT_COMPOSITION_NEEDS_REVISION'));
test('missing occurrence fails',()=>assert.equal(fixture(({proof})=>proof.proxyTextRegions.pop()).status,'LAYOUT_COMPOSITION_NEEDS_REVISION'));
test('missing paragraph fails',()=>assert.equal(fixture(({svg})=>fs.writeFileSync(svg,fs.readFileSync(svg,'utf8').replace(/<text[^>]*data-paragraph-id="left-p1"[^>]*>[\s\S]*?<\/text>/g,''))).status,'LAYOUT_COMPOSITION_NEEDS_REVISION'));
test('legacy proof cannot pass',()=>assert.equal(fixture(({proof})=>proof.schemaVersion=3).status,'LAYOUT_COMPOSITION_NEEDS_REVISION'));
test('changed preview hash fails',()=>assert.match(fixture(({preview})=>fs.appendFileSync(preview,'changed')).errors.artifact.join(' '),/SHA-256/));
test('missing geometry cannot be repaired by handwritten PASS',()=>assert.equal(fixture(({proof})=>delete proof.sourceTextRegions[0].boundsPt).status,'LAYOUT_COMPOSITION_NEEDS_REVISION'));
const project=path.resolve(__dirname,'../../../..');
const actualPdf=path.join(project,'Tap 53/Part 1/layouts/T53_Part 1_test 2.pdf');
test('real Page 10: independently measured source rejects composition v4', {skip:!fs.existsSync(actualPdf)||!fs.existsSync(path.join(project,'Tap 53/Part 1/pages/page-010/storyboards/page010-d1-quiet-consent-v4-proxy-fidelity.json'))},()=>{
 const dir=fs.mkdtempSync(path.join(os.tmpdir(),'page010-regression-'));
 try{
  const base=path.join(project,'Tap 53/Part 1/pages/page-010/storyboards');
  const proof=JSON.parse(fs.readFileSync(path.join(base,'page010-d1-quiet-consent-v4-proxy-fidelity.json')));
  proof.schemaVersion=4;
  for(const a of Object.values(proof.artifacts))a.path=path.resolve(base,a.path);
  Object.assign(proof.sourceTextRegions[0],{boundsPt:[40,60,320,440],paragraphLineCounts:[4,1,4,2,5,2,1,4]});
  Object.assign(proof.sourceTextRegions[1],{boundsPt:[460,60,315,410],paragraphLineCounts:[4,1,4,2,5,1,1,3]});
  const file=path.join(dir,'proof.json');fs.writeFileSync(file,JSON.stringify(proof));const r=verify(file);
  assert.equal(r.status,'LAYOUT_COMPOSITION_NEEDS_REVISION');
  const m=r.metrics.regions['left-printed-22-measurement'];
  assert.equal(m.source.fontSizePt,12);assert.ok(Math.abs(m.source.leadingPt-17)<.1);
  assert.ok(m.fontSizePtRatio<.9);assert.ok(m.leadingPtRatio<.75);
 }finally{fs.rmSync(dir,{recursive:true,force:true});}
});

function rewrapLeft(svg){
 const s=fs.readFileSync(svg,'utf8');
 const m=s.match(/(<g id="left"[^>]*>)([\s\S]*?)(<\/g>)/);
 const rows=[...m[2].matchAll(/<text([^>]*)>([\s\S]*?)<\/text>/g)].map(v=>({attrs:v[1],text:v[2]}));
 for(const at of [6,4]){rows[at].text+=' '+rows[at+1].text;rows.splice(at+1,1);}
 const next=rows.map((r,i)=>'<text'+r.attrs.replace(/y="[\d.]+"/,'y="'+(160+i*37.786)+'"')+'>'+r.text+'</text>').join('');
 fs.writeFileSync(svg,s.replace(m[0],m[1]+next+m[3]));
}
test('art-directed wrapping preserves burden without copying source line counts',()=>{
 const r=fixture(({svg,proof})=>{proof.layoutComparison='ART_DIRECTED';rewrapLeft(svg);});
 assert.equal(r.status,'PROXY_COMPOSITION_PASS',JSON.stringify(r));assert.ok(r.warnings.length);
 assert.equal(r.artisticApproval,'NOT_EVALUATED_BY_SCRIPT');
});
test('art-directed mode still rejects removed content',()=>{
 const r=fixture(({svg,proof})=>{proof.layoutComparison='ART_DIRECTED';fs.writeFileSync(svg,fs.readFileSync(svg,'utf8').replaceAll('Words that occupy real typography space.','Words'));});
 assert.equal(r.status,'LAYOUT_COMPOSITION_NEEDS_REVISION');assert.match(r.errors.burden.join(' '),/nội dung/);
});
test('art-directed mode still rejects small type',()=>{
 const r=fixture(({svg,proof})=>{proof.layoutComparison='ART_DIRECTED';fs.writeFileSync(svg,fs.readFileSync(svg,'utf8').replaceAll('26.672px','21.584px'));});
 assert.equal(r.status,'LAYOUT_COMPOSITION_NEEDS_REVISION');assert.match(r.errors.layout.join(' '),/fontSizePt/);
});
