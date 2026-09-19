from pathlib import Path
import json
p=Path('/workspace/Tap 53/Part 1/tmp/page004/build_extra.py')
s=p.read_text().split('paths=[make(3),make(4)]')[0]
s=s.replace("woman(d,1199,800,1.13,'gather','#ac9476')",'''# Người nghiêng thúng đổ đất xuống vùng trũng: hình khối riêng, không lặp tư thế gom.
  d.polygon([(1160,774),(1183,766),(1200,791),(1173,816),(1148,804)],fill='#ac9476')
  d.polygon([(1153,801),(1178,805),(1200,851),(1131,850)],fill='#796f66')
  d.ellipse((1182,752,1203,775),fill='#b88360',outline='#594738',width=2)
  d.arc((1182,752,1203,775),150,340,fill='#483c33',width=5)
  d.line([(1188,783),(1210,795),(1232,787)],fill='#a87352',width=7)
  d.line([(1172,789),(1194,814),(1217,812)],fill='#a87352',width=7)
  d.polygon([(1210,792),(1239,779),(1257,805),(1228,817)],fill='#aa8b53',outline='#806840')
  d.polygon([(1245,806),(1268,842),(1240,842)],fill='#957b55')
  d.polygon([(1220,857),(1260,835),(1303,858)],fill='#ae9067')
  d.line([(1146,851),(1130,860)],fill='#a87352',width=6)
  d.line([(1190,849),(1206,859)],fill='#a87352',width=6)''')
s=s.replace("fn=out/f'page004-option{n}-composition-v1.png'", "fn=out/f'page004-option{n}-confirmed-composition-v1.png'")
exec(s)
path=make(4)
mp=root/'Tap 53/Part 1/scripts/layout_frames.json';data=json.loads(mp.read_text());frame=next(v for v in data['spreads'] if v['id']=='part1-spread04-community-work')['frames'][0]
frame['optionAlignment']={'selectedOption':'page004-option4','userAction':'Chọn option: page004-option4','userConfirmed':True,'confirmationScope':'Chọn hướng kể ở G2; chưa duyệt bản bố cục G3.'}
opt=next(o for o in frame['options'] if o['id']=='page004-option4');opt.update({'userConfirmed':True,'confirmedCompositionCard':path,'compositionUserConfirmed':False,'status':'storyboard-pending'})
mp.write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n')
