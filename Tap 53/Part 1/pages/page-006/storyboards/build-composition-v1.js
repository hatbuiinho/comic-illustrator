// Dựng bản phác vector trên đúng raster PDF; không tạo ảnh minh họa cuối.
const fs = require('fs');
const path = require('path');
const sharp = require('/home/node/.cache/codex-runtimes/codex-primary-runtime/dependencies/node/node_modules/sharp');
const dir = __dirname;
const W = 1200, H = 575.433 / 810.709 * W;
const Y = 229.606 / 810.709 * W, AH = H - Y;
const ink = '#4a3c33';
const svg = (body) => `<svg xmlns="http://www.w3.org/2000/svg" width="1200" height="${H+92}" viewBox="0 0 1200 ${H+92}">${body}</svg>`;
const face = (worker=false) => `<path d="M-19 28 L-18 46 L20 46 L18 25" fill="#bb865d"/><path d="M-27-7 Q-34 16-21 32 Q1 44 23 30 L25 19 L35 14 L26 4 L24-20 L-18-24Z" fill="#ce9b71"/><path d="M-29-7 Q-33-35-7-35 Q21-37 29-10 L20-15 L8-24 L-16-18 L-15 19 L-25 23Z" fill="${worker?'#37312d':'#77726a'}"/><ellipse cx="-14" cy="11" rx="6" ry="9" fill="#ce9b71"/>${worker?'<path d="M-20 19 Q0 31 23 20 L21 33 Q1 47-20 31Z" fill="#37312d"/><path d="M-32-14 Q-33-43 4-44 Q29-42 33-22 L26-9 Q1-19-32-14Z" fill="#a56348"/><path d="M-30-23 L26-33 M-23-13 L30-24" fill="none"/>':''}<path d="M-1 1 L9-1 M18-1 L25 1 M13 7 L16 15 L23 16 M7 26 Q15 30 23 25" fill="none"/><path d="M0 7 L10 7 M18 6 L26 6" stroke="#faf4df" stroke-width="5"/><circle cx="9" cy="7" r="2.5" fill="${ink}"/><circle cx="25" cy="6" r="2.3" fill="${ink}"/>`;
function seated(x,y,s,worker,flip=false) {
 return `<g transform="translate(${x} ${y}) scale(${flip?-s:s} ${s})" stroke="${ink}" stroke-width="2.5" stroke-linejoin="round" stroke-linecap="round">
 <path d="M-39 155 Q-108 178-97 201 Q-77 220 0 211 Q91 219 100 200 Q107 179 44 156Z" fill="${worker?'#77604e':'#958f7e'}"/>
 <path d="M-74 200 Q-32 186 15 201 M12 201 L57 180" fill="none"/>
 <path d="M-16 37 Q-44 40-48 66 L-41 160 Q-4 178 48 157 L44 64 Q33 43 17 38Z" fill="${worker?'#e5d8b8':'#8c8b96'}"/>
 <path d="M-16 41 L-1 89 L20 40 M-35 130 L-24 80 M14 102 L31 149" fill="none"/>
 <path d="M-43 66 Q-65 111-39 143 L7 153 L13 138 L-26 126 L-26 80" fill="#ce9b71"/>
 <path d="M39 70 Q57 95 63 123 L35 131 L32 117 L44 111 L27 81" fill="#ce9b71"/>
 <path d="M29 116 L48 116 L45 137 L32 137Z" fill="#b98361"/>
 ${worker?'<path d="M-42 151 Q2 164 45 150 L45 171 L-43 171Z" fill="#c59b4c"/>':''}
 ${face(worker)}
 </g>`;
}
function server(x,y,s,water=false) {
 return `<g transform="translate(${x} ${y}) scale(${s})" stroke="#827665" stroke-width="2.2" stroke-linejoin="round">
 <path d="M-17 99 L-24 163 L-7 164 L5 110 L18 155 L34 156 L21 96" fill="#b29f81"/><path d="M-24 163 L-29 170 L-5 171 L-7 164 M18 155 L17 163 L42 164 L34 156" fill="#b99071"/>
 <path d="M-8 28 L-30 47 L-26 107 L29 106 L26 46 L9 28Z" fill="${water?'#b7a996':'#a0aaa3'}"/>
 <path d="M-25 46 L-35 81 L2 87 L4 74 L-19 70 L-12 48 M22 49 L39 76 L19 85 L13 76 L25 69 L12 48" fill="#b99071"/>
 <ellipse cx="0" cy="7" rx="18" ry="24" fill="#b99071"/><path d="M-19 6 Q-21-22 2-22 Q24-20 18 5 L7-8 L-10-7Z" fill="#665d52"/>
 ${water?'<path d="M-1 65 L-1 73 Q-17 79-13 94 Q-6 106 13 98 Q23 86 11 75 L10 65Z" fill="#b68c66"/>':'<path d="M-18 77 L-12 98 L27 96 L33 74Z" fill="#c9ad7b"/><ellipse cx="7" cy="75" rx="26" ry="8" fill="#e1c68d"/><path d="M-12 75 Q-8 63-1 73 M3 74 Q11 60 16 73 M17 72 Q26 61 28 74" fill="#ccaa6b"/>'}
 </g>`;
}
function basket(x,y,s=1) {return `<g transform="translate(${x} ${y}) scale(${s})" stroke="${ink}" stroke-width="2"><path d="M-56 0 L-43 39 Q0 51 44 39 L58 0Z" fill="#bb9565"/><ellipse cy="0" rx="57" ry="16" fill="#8f704e"/><path d="M-48 20 L48 20 M-25 10 L-22 40 M0 12 L0 43 M25 10 L23 40" fill="none"/><ellipse cx="-21" cy="-5" rx="20" ry="9" fill="#e5c68b"/><ellipse cx="14" cy="1" rx="19" ry="8" fill="#e5c68b"/><circle cx="31" cy="-10" r="8" fill="#ad9a5f"/><circle cx="3" cy="-12" r="8" fill="#c99466"/></g>`;}
function background(close=false) {
 return `<rect width="1200" height="${AH}" fill="#e9dfc7"/><path d="M0 118 L1200 118 L1200 ${AH} L0 ${AH}Z" fill="#d7c4a2"/>
 <path d="M0 0 L1200 0 L1200 58 L970 48 L721 77 L477 50 L202 86 L0 67Z" fill="#b0a378" stroke="#807457" stroke-width="3"/>
 <path d="M0 46 L1200 25 M35 72 L28 0 M131 65 L119 0 M258 64 L244 0 M389 54 L375 0 M716 60 L703 0 M1015 44 L1002 0" fill="none" stroke="#8e805f" stroke-width="2"/>
 <path d="M61 60 L75 ${AH} L94 ${AH} L78 59 M1114 42 L1123 ${AH} L1140 ${AH} L1130 42" fill="#a28a63" stroke="#78654e" stroke-width="3"/>
 <path d="M59 86 L83 90 M60 93 L84 97 M1114 66 L1134 68 M1115 72 L1136 76" stroke="#645c47" stroke-width="4"/>
 <path d="M${close?40:705} 148 l150 -21 l99 16 l-144 34 Z" fill="#b6a587" stroke="#958568" stroke-width="2"/>
 <path d="M${close?45:710} 131 v29 m145 -52 v30 m107 -15 v28" fill="none" stroke="#8c7a5d" stroke-width="3"/>
 <path d="M0 340 Q350 225 610 315 T1200 360 L1200 ${AH} L0 ${AH}Z" fill="#c4b291"/>
 <path d="M90 465 Q411 440 605 472 M638 377 Q805 370 996 400" fill="none" stroke="#b19d7d" stroke-width="2"/>`;
}
function guides(crit) {
 const tx=W*.0104895,ty=AH*.0147783,sx=W*.027972,sy=AH*.0394089;
 return `<g fill="none" stroke-width="1.5"><rect x="1" y="${Y+1}" width="1198" height="${AH-2}" stroke="#1885b1" stroke-dasharray="8 6"/><rect x="${tx}" y="${Y+ty}" width="${W-2*tx}" height="${AH-2*ty}" stroke="#cc5954"/><rect x="${sx}" y="${Y+sy}" width="${W-2*sx}" height="${AH-2*sy}" stroke="#549462"/><path d="M564 ${Y} V${H} M636 ${Y} V${H}" stroke="#bb787a" stroke-dasharray="5 7"/>${crit.map(c=>`<rect x="${c[0]}" y="${Y+c[1]}" width="${c[2]}" height="${c[3]}" rx="10" stroke="#4c9264" stroke-dasharray="3 5"/>`).join('')}</g>`;
}
async function main(){
 const source=fs.readFileSync(path.join(dir,'page006-layout-source-v1.png')).toString('base64');
 const sourceImage=`<image href="data:image/png;base64,${source}" width="1200" height="${H}"/>`;
 const configs=[
 {id:'page006-option1-bua-nghi-chung',title:'1 · Ngồi chung một bữa',camera:'Góc hơi cao · 4 người',tail:'Người lạ trở nên gần gũi',crit:[[154,151,79,88],[352,159,80,89]],
 scene:background()+server(887,160,.72)+server(1008,178,.69,true)+seated(195,199,1.08,true)+seated(394,207,1.04,false,true)+basket(293,412,1.04)+`<g stroke="${ink}" stroke-width="3" fill="#b08861"><path d="M113 340 L113 359 Q78 378 96 412 Q120 433 145 410 Q158 383 132 360 L132 340Z"/><ellipse cx="123" cy="340" rx="10" ry="4"/></g>`},
 {id:'page006-option2-cau-chuyen-ben-chen-nuoc',title:'2 · Câu chuyện bên chén nước',camera:'Ngang tầm · trung-cận · 4 người',tail:'Một người nói, một người lắng nghe',crit:[[704,142,97,117],[947,155,96,117]],
 scene:background(true)+server(226,177,.69)+server(348,188,.66,true)+seated(754,210,1.65,true)+seated(999,222,1.59,false,true)+basket(870,475,1.05)}
 ];
 for(const c of configs){
 const footer=`<rect y="${H}" width="1200" height="92" fill="#faf8f1"/><g font-family="DejaVu Sans,sans-serif" fill="#39372f"><text x="24" y="${H+27}" font-size="21" font-weight="bold">Trọng tâm: ${c.title}</text><text x="24" y="${H+59}" font-size="18">Góc nhìn: ${c.camera}</text><text x="650" y="${H+59}" font-size="18">Dư âm: ${c.tail}</text></g>`;
 const body=`<defs><clipPath id="frame"><rect width="1200" height="${AH}"/></clipPath></defs>${sourceImage}<g transform="translate(0 ${Y})" clip-path="url(#frame)">${c.scene}</g>${guides(c.crit)}${footer}`;
 const out=svg(body);
 fs.writeFileSync(path.join(dir,c.id+'-composition-v2.svg'),out);
 await sharp(Buffer.from(out)).png().toFile(path.join(dir,c.id+'-composition-v2.png'));
 }
 const frame={id:'rest-meal',shape:'rect',box:{x:0,y:229.606/575.433,width:810.708/810.709,height:345.827/575.433},contentFrame:{x:0,y:0,width:1,height:1},aspectRatio:810.708/345.827,textReserve:[],spine:{x:.47,y:229.606/575.433,width:.06,height:345.827/575.433},narrativeFunction:'Hệ quả của sự chăm lo: người lao động gần gũi trong bữa nghỉ',safeZone:{x:.027972,y:.0394089,width:.944056,height:.9211822},visibilityPriority:[],recognitionCores:['cột buộc dây dưới mái lá nhẹ','đất liên tục ra công trường','hố móng và cọc ở ngoài lán'],cropBuffers:['đất','mái lá phụ','phần kéo dài của cột'],delivery:{required:true,status:'storyboard-pending'},optionAlignment:{userAction:'process page 6 ạ',userConfirmed:false,selectedOption:null,sourceRead:['Tap 53/notes.md','Tap 53/shot_notes.md','Tap 53/workflow.md','Tap 53/workflow_schema.md','Tap 53/workflow_templates.md','Tap 53/storyboard_composition_reference.md','Tap 53/Part 1/scripts/chapter1.md','Tap 53/Part 1/layouts/TẬP 53 _ PART 1 _ DEMO DÀN TRANG_PTg full 12.08.26.pdf','Tap 53/characters/thợ phụ.png','Tap 53/characters/Gia nhân.png'],sourceContext:'storyboards/page006-g1-source-context-v1.md'},storyboardQa:{status:'g2-options-ready',options:configs.map(c=>({id:c.id,preliminaryCompositionCard:'storyboards/'+c.id+'-composition-v1.png',details:'storyboards/page006-g2-options-v1.md',userConfirmed:false}))}};
 const spread={id:'part1-page006-process-20260918',canvas:{width:810.709,height:575.433},pageImage:'storyboards/page006-layout-source-v1.png',textReserve:[{x:0,y:0,width:1,height:229.606/575.433}],frames:[frame]};
 const layout={defaults:{ratioTolerance:.015,printTrim:{trimPercent:{x:.0104895,y:.0147783},criticalSafePercent:{x:.027972,y:.0394089}}},spreads:[spread]};
 fs.writeFileSync(path.join(dir,'../layout.json'),JSON.stringify(layout,null,2)+'\n');
 fs.writeFileSync(path.join(dir,'../manifest.json'),JSON.stringify({page:6,part:1,episode:'Tap 53',status:'g2-options-ready',userAction:'process page 6 ạ',userConfirmed:false,selectedOption:null,sourceContext:'storyboards/page006-g1-source-context-v1.md',optionsDocument:'storyboards/page006-g2-options-v1.md',options:frame.storyboardQa.options,delivery:[{frame:'rest-meal',required:true,status:'storyboard-pending'}],continuityInput:'Script và PDF 5–7: chăm lo cho người lao động → bữa nghỉ chung → khảo sát buổi chiều; không dùng output page khác.'},null,2)+'\n');
 const indexPath=path.resolve(dir,'../../../scripts/layout_frames.json');
 const index=JSON.parse(fs.readFileSync(indexPath,'utf8'));
 frame.storyboardQa.options.forEach(o=>o.preliminaryCompositionCard=o.preliminaryCompositionCard.replace('-v1.png','-v2.png'));
 fs.writeFileSync(path.join(dir,'../layout.json'),JSON.stringify(layout,null,2)+'\n');
 const pageManifest=JSON.parse(fs.readFileSync(path.join(dir,'../manifest.json'),'utf8'));
 pageManifest.options=frame.storyboardQa.options;
 fs.writeFileSync(path.join(dir,'../manifest.json'),JSON.stringify(pageManifest,null,2)+'\n');
 const indexed=JSON.parse(JSON.stringify(spread));
 indexed.pageImage='../pages/page-006/storyboards/page006-layout-source-v1.png';
 indexed.pageLayout='../pages/page-006/layout.json';
 indexed.frames[0].storyboardQa.options.forEach(o=>o.preliminaryCompositionCard='../pages/page-006/'+o.preliminaryCompositionCard);
 const previousIndex=index.spreads.findIndex(s=>s.id===spread.id);
 if(previousIndex<0) index.spreads.push(indexed); else index.spreads[previousIndex]=indexed;
 fs.writeFileSync(indexPath,JSON.stringify(index,null,2)+'\n');
 console.log(JSON.stringify({page:6,ratio:frame.aspectRatio,frame:frame.box,cards:configs.map(c=>c.id),status:'g2-options-ready'},null,2));
}
main().catch(e=>{console.error(e);process.exit(1)});
