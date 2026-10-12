// Measure source PDF and isolated SVG text with the same Poppler renderer.
const fs=require('fs'),os=require('os'),path=require('path');
const {execFileSync}=require('child_process');
const attr=(s,k)=>s.match(new RegExp(`\\b${k}=["']([^"']+)["']`))?.[1];
const median=a=>{a=[...a].sort((x,y)=>x-y);return a.length?a.length%2?a[(a.length-1)/2]:(a[a.length/2-1]+a[a.length/2])/2:null;};
function pdfLines(file,page){
  const zoom=2; // Poppler clamps zoom above 3; use a supported explicit value.
  const xml=execFileSync('pdftohtml',['-f',String(page),'-l',String(page),'-zoom',String(zoom),'-xml','-stdout','-i','-noroundcoord',file],{encoding:'utf8',maxBuffer:20*1024*1024,stdio:['ignore','pipe','pipe']});
  const p=xml.match(/<page\b[^>]*>/)?.[0];if(!p)throw Error('Không đọc được trang PDF.');
  const fonts=new Map([...xml.matchAll(/<fontspec\b[^>]*>/g)].map(m=>[attr(m[0],'id'),{size:Number(attr(m[0],'size'))/zoom,family:attr(m[0],'family')}]));
  const rows=[...xml.matchAll(/<text\b([^>]*)>([\s\S]*?)<\/text>/g)].map(m=>({x:Number(attr(m[1],'left'))/zoom,y:Number(attr(m[1],'top'))/zoom,w:Number(attr(m[1],'width'))/zoom,h:Number(attr(m[1],'height'))/zoom,font:fonts.get(attr(m[1],'font')),text:m[2].replace(/<[^>]*>/g,'').trim()})).filter(r=>r.text);
  return {widthPt:Number(attr(p,'width'))/zoom,heightPt:Number(attr(p,'height'))/zoom,rows};
}
function summarize(rows,file,page){
  const groups=[];for(const r of rows){let g=groups.find(v=>Math.abs(v.y-r.y)<.3);if(!g){g={y:r.y,rows:[]};groups.push(g);}g.rows.push(r);}
  groups.sort((a,b)=>a.y-b.y);
  const lines=groups.map(g=>({y:g.y,width:Math.max(...g.rows.map(r=>r.x+r.w))-Math.min(...g.rows.map(r=>r.x)),height:Math.max(...g.rows.map(r=>r.h)),size:median(g.rows.map(r=>r.font?.size).filter(Number.isFinite))}));
  // PDF FontDescriptor boxes differ between InDesign and Cairo even for the
  // same font. Measure visible ink at 144 dpi, retaining descriptor bounds
  // separately, instead of mistaking those metadata boxes for glyph height.
  const ppm=execFileSync('pdftoppm',['-f',String(page),'-l',String(page),'-r','144','-singlefile',file],{maxBuffer:40*1024*1024,stdio:['ignore','pipe','pipe']});
  const header=ppm.subarray(0,100).toString().match(/^P6\s+(\d+)\s+(\d+)\s+255\s/);if(!header)throw Error('Không đọc được raster typography PPM.');
  const width=Number(header[1]),height=Number(header[2]),offset=Buffer.byteLength(header[0]);
  const inkHeights=groups.map(g=>{let top=Infinity,bottom=-Infinity;for(const r of g.rows){for(let y=Math.max(0,Math.floor(r.y*2));y<Math.min(height,Math.ceil((r.y+r.h)*2));y++)for(let x=Math.max(0,Math.floor(r.x*2));x<Math.min(width,Math.ceil((r.x+r.w)*2));x++){const i=offset+(y*width+x)*3;const rgb=[ppm[i],ppm[i+1],ppm[i+2]];if(Math.max(...rgb)<245&&Math.min(...rgb)<180){top=Math.min(top,y);bottom=Math.max(bottom,y);}}}return bottom>=top?(bottom-top+1)/2:0;});
  // Cairo can split one line across font subsets. Count every adjacent run,
  // while ignoring duplicate highlight runs occupying the same PDF interval.
  const contentUnits=groups.reduce((sum,g)=>{
    const accepted=[];
    for(const r of [...g.rows].sort((a,b)=>b.w-a.w)){
      if(accepted.some(a=>Math.min(a.x+a.w,r.x+r.w)-Math.max(a.x,r.x)>.8*Math.min(a.w,r.w)))continue;
      accepted.push(r);
    }
    return sum+accepted.reduce((n,r)=>n+r.text.replace(/&[^;]+;/g,'x').replace(/\s/g,'').length,0);
  },0);
  return {contentUnits,lineCount:lines.length,fontSizePt:median(lines.map(l=>l.size)),glyphHeightPt:median(inkHeights),glyphDescriptorHeightPt:median(lines.map(l=>l.height)),glyphMeasurement:'visible ink at 144 dpi; PDF descriptor bounds reported separately',leadingPt:median(lines.slice(1).map((l,i)=>l.y-lines[i].y)),lineTopsPt:lines.map(l=>l.y),lineWidthsPt:lines.map(l=>l.width),textAreaPt2:lines.reduce((a,l,i)=>a+l.width*inkHeights[i],0),blockHeightPt:lines.length?lines.at(-1).y+lines.at(-1).height-lines[0].y:0,fonts:[...new Set(rows.map(r=>r.font?.family))]};
}
function measure(svgFile,sourceFile,page,regions,proxyRegions,renderEnvironment={}){
 const svg=fs.readFileSync(svgFile,'utf8'),root=svg.match(/<svg\b[^>]*>/)?.[0];
 const vb=(attr(root||'','viewBox')||'').trim().split(/[ ,]+/).map(Number);
 const source=pdfLines(sourceFile,page);if(vb.length!==4||vb[0]!==0||vb[1]!==0||!(vb[2]>0&&vb[3]>0))throw Error('viewBox phải là 0 0 width height.');
 const sx=vb[2]/source.widthPt,sy=vb[3]/source.heightPt;
 if(Math.abs(sx/sy-1)>.005)throw Error('Tỷ lệ canvas/PDF theo X và Y không khớp.');
 if(/<style\b|<tspan\b|textLength=|lengthAdjust=/i.test(svg))throw Error('CSS/tspan/textLength cần exporter đo chuyên biệt; không được fallback PASS.');
 const temp=fs.mkdtempSync(path.join(os.tmpdir(),'proxy-typography-'));
 try{
  const results={};
  for(const region of regions){
   const b=region.boundsPt;if(!Array.isArray(b)||b.length!==4||!b.every(Number.isFinite)||b[2]<=0||b[3]<=0)throw Error(`Region ${region.id} thiếu boundsPt nguồn [x,y,width,height].`);
   const sourceRows=source.rows.filter(r=>r.x+r.w/2>=b[0]&&r.x+r.w/2<=b[0]+b[2]&&r.y+r.h/2>=b[1]&&r.y+r.h/2<=b[1]+b[3]);
   const proxy=proxyRegions.find(r=>r.sourceRegionId===region.id);if(!proxy)continue;
   // Keep ancestor groups so inherited font and transforms are measured too.
   const stack=[];let fragment=null;
   for(const m of svg.matchAll(/<\/?g\b[^>]*>/g)){if(m[0].startsWith('</')){stack.pop();continue;}const item={tag:m[0],index:m.index};
    if(attr(m[0],'id')===proxy.svgGroupId){let depth=1,end=m.index+m[0].length;const rest=svg.slice(end);for(const n of rest.matchAll(/<\/?g\b[^>]*>/g)){depth+=n[0].startsWith('</')?-1:1;if(!depth){end+=n.index+n[0].length;break;}}fragment=stack.map(v=>v.tag).join('')+svg.slice(m.index,end)+'</g>'.repeat(stack.length);break;}stack.push(item);}
   if(!fragment)throw Error(`Không tìm thấy group ${proxy.svgGroupId}.`);
   const texts=[...fragment.matchAll(/<text\b([^>]*)>([\s\S]*?)<\/text>/g)];
   const paragraphIds=texts.map(m=>attr(m[1],'data-paragraph-id'));
   if(paragraphIds.some(v=>!v))throw Error(`Group ${proxy.svgGroupId} thiếu data-paragraph-id.`);
   const isolated=`<svg xmlns="http://www.w3.org/2000/svg" width="${source.widthPt}pt" height="${source.heightPt}pt" viewBox="${vb.join(' ')}">${svg.match(/<defs\b[\s\S]*?<\/defs>/)?.[0]||''}${fragment}</svg>`;
   const inFile=path.join(temp,'text.svg'),outFile=path.join(temp,'text.pdf');fs.writeFileSync(inFile,isolated);
   const backend=renderEnvironment.pangoCairoBackend;
   if(backend&&!['fc','coretext'].includes(backend))throw Error('pangoCairoBackend không hợp lệ.');
   execFileSync('rsvg-convert',['-f','pdf','-o',outFile,inFile],{env:backend?{...process.env,PANGOCAIRO_BACKEND:backend}:process.env,stdio:['ignore','pipe','pipe']});
   const rendered=summarize(pdfLines(outFile,1).rows,outFile,1);
   results[region.id]={source:summarize(sourceRows,sourceFile,page),rendered,paragraphIds,svgTextCount:texts.length};
  }
  return {scale:{x:sx,y:sy,method:'viewBox / measured PDF page points; DPI ignored'},regions:results};
 }finally{fs.rmSync(temp,{recursive:true,force:true});}
}
module.exports={measure,median};
