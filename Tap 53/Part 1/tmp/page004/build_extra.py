from pathlib import Path
from PIL import Image, ImageDraw, ImageFont
import json
root=Path('/workspace');out=root/'Tap 53/Part 1/pages/page-004/storyboards'
# Chỉ tái sử dụng hàm vẽ ký hiệu, không chạy lại phần xuất hay sửa manifest cũ.
source=(root/'Tap 53/Part 1/tmp/page004/build_cards.py').read_text()
exec(source[:source.index('def card(n):')])
F=lambda n:ImageFont.truetype(font,n)

def woman(d,x,y,s,job,clr='#aa795d'):
 def p(a,b):return (x+a*s,y+b*s)
 def poly(a,c):d.polygon([p(*v) for v in a],fill=c)
 def line(a,c,w):d.line([p(*v) for v in a],fill=c,width=max(1,int(w*s)))
 if job=='gather':
  poly([(-26,17),(-11,5),(12,18),(22,34),(3,50),(-34,49)],clr)
  poly([(-27,40),(4,43),(19,72),(-41,72)],'#796f66')
  hx,hy=p(16,6)
  line([(7,25),(30,38),(32,55)],'#a87352',6)
  line([(-7,24),(12,40),(20,54)],'#a87352',6)
  poly([(13,56),(48,56),(40,75),(19,75)],'#aa8b53')
  for a,b in [(20,54),(30,53),(39,54)]:
   xx,yy=p(a,b);d.ellipse((xx-4*s,yy-3*s,xx+4*s,yy+3*s),fill='#877456')
 else:
  poly([(-13,8),(13,8),(20,40),(-15,43)],clr)
  poly([(-15,36),(17,35),(28,76),(-22,77)],'#796f66')
  hx,hy=p(0,-10)
  line([(-9,16),(-25,24),(-36,3)],'#a87352',6)
  line([(9,16),(26,25),(35,3)],'#a87352',6)
  line([(-55,1),(55,1)],'#795c3f',4)
  for a in [-50,50]:
   line([(a,2),(a-12,49)],'#7d6b4c',1)
   line([(a,2),(a+12,49)],'#7d6b4c',1)
   poly([(a-17,49),(a+17,49),(a+11,66),(a-11,66)],'#aa8b53')
  line([(-13,76),(-24,86)],'#a87352',5);line([(17,76),(30,83)],'#a87352',5)
 r=9*s;d.ellipse((hx-r,hy-r,hx+r,hy+r),fill='#b88360',outline='#594738',width=2)
 d.arc((hx-r,hy-r,hx+r,hy+r),150,340,fill='#483c33',width=max(2,int(5*s)))
 d.ellipse((hx-r-5*s,hy-3*s,hx-r+3*s,hy+5*s),fill='#483c33')

def child(d,x,y,s,job,c):
 # Tỷ lệ trẻ nhỏ và tư thế riêng: không thu nhỏ máy móc hình người lớn.
 def p(a,b):return (x+a*s,y+b*s)
 def line(a,c,w):d.line([p(*v) for v in a],fill=c,width=max(1,int(w*s)))
 def poly(a,c):d.polygon([p(*v) for v in a],fill=c)
 bend=job=='pick'; hx,hy=p(17 if bend else 0,0);r=12*s
 d.ellipse((hx-r,hy-r,hx+r,hy+r),fill='#bd8961',outline='#594738',width=2)
 d.arc((hx-r,hy-r,hx+r,hy+r),170,345,fill='#493c32',width=max(2,int(4*s)))
 poly([(8,12),(25,16),(7,37),(-13,31)] if bend else [(-11,13),(11,13),(15,39),(-13,39)],c)
 line([(-7,37),(-15,55),(-23,60)],'#a77450',5)
 line([(7,38),(17,49),(24,61)],'#a77450',5)
 if bend:
  line([(20,20),(31,39),(34,53)],'#b88360',5)
  d.ellipse((*p(32,53),*p(44,58)),fill='#99814f')
 else:
  line([(-7,18),(11,29),(31,30)],'#b88360',5)
  line([(8,18),(25,24),(37,22)],'#b88360',5)
  line([(37,16),(20,60)],'#806343',3)
  poly([(22,51),(9,68),(31,68)],'#aa905c')

def wood(d,x,y,s):
 d.polygon([(x-52*s,y),(x+155*s,y-24*s),(x+155*s,y-12*s),(x-52*s,y+13*s)],fill='#93714f')
 for xx in [x,x+113*s]:person(d,xx,y+9*s,s,'wood','#748779')

def make(n):
 im=Image.open(out/'page004-layout-source.png').convert('RGB');d=ImageDraw.Draw(im);W,H=im.size;Y=442
 d.rectangle((1,Y,1398,993),fill='#e5d5b4')
 if n==3:
  d.polygon([(0,442),(1400,442),(1400,540),(880,513),(430,562),(0,600)],fill='#c8cbb1')
  # Regard depuis la lisière vers le chantier : arbres proches uniquement à gauche.
  for x in [32,100]:
   d.polygon([(x,442),(x+23,442),(x+5,860),(x-12,860)],fill='#8b8269')
  d.polygon([(0,442),(290,442),(180,475),(40,495),(0,490)],fill='#8eaa86')
  for pts in [[(775,662),(1170,563),(1300,579),(863,704)],[(405,612),(558,558),(618,570),(480,644)]]:
   d.polygon(pts,fill='#b6a07b');d.line(pts[:3],fill='#927956',width=4)
  for x,y,s in [(846,604,.82),(986,570,.71),(1140,536,.63),(1250,530,.53),(479,558,.55)]:person(d,x,y,s,'dig','#8b826e')
  wood(d,355,617,.72)
  woman(d,860,695,.88,'gather');woman(d,1040,656,.8,'gather','#9c8374')
  woman(d,1135,735,1.04,'carry');woman(d,1270,674,.75,'carry','#b39369')
  # Les enfants sont l'entrée émotionnelle, dans une même action collective.
  child(d,231,780,1.48,'sweep','#bd9759')
  child(d,383,797,1.38,'pick','#8c9b82')
  child(d,542,734,1.12,'sweep','#b8836d')
  child(d,470,652,.75,'pick','#bda778')
  for x,y in [(305,905),(429,894),(549,847),(180,873)]:
   d.line((x,y,x+22,y-7),fill='#a18f64',width=3)
   d.ellipse((x+10,y-11,x+24,y-5),fill='#a5a071')
  title='3 · Những bàn tay nhỏ cũng góp sức';camera='Góc nhìn: từ góc rừng, ngang tầm trẻ';echo='Dư âm: ai cũng có phần việc của mình'
 else:
  d.polygon([(0,442),(1400,442),(1400,515),(1090,526),(850,494),(390,512),(0,540)],fill='#c5cbb0')
  for x in [73,201,348,1110,1230,1330]:
   d.line((x,455,x+8,537),fill='#9a967b',width=4)
   d.ellipse((x-40,445,x+43,476),fill='#a9b995')
  # Le ruban de terre suit une courbe; aucune division en cases ou étapes.
  d.polygon([(70,775),(345,609),(513,604),(560,638),(259,841)],fill='#b39a72')
  d.line([(70,775),(345,609),(513,604)],fill='#8f7453',width=5)
  for x,y,s in [(181,706,1.03),(302,635,.92),(445,590,.76)]:person(d,x,y,s,'dig','#85755f')
  woman(d,347,759,1.34,'gather','#b17e69');woman(d,532,682,.99,'gather','#9b8a75')
  # Le raccord au pli est une zone de sol, sans bras ou charges traversant le dos.
  woman(d,817,672,1.08,'carry','#b48d5d');woman(d,998,725,1.17,'carry','#987769')
  d.ellipse((1090,827,1350,906),fill='#c6b38d')
  woman(d,1199,800,1.13,'gather','#ac9476')
  wood(d,842,540,.64);wood(d,474,523,.5)
  for x,y in [(1120,548),(1205,558),(1280,537)]:child(d,x,y,.65,'sweep' if x!=1205 else 'pick','#a19378')
  title='4 · Nhịp đất chuyền qua nhiều bàn tay';camera='Góc nhìn: chếch dọc tuyến đào–gom–gánh';echo='Dư âm: việc người này tiếp sức người kia'
 for text,y in [(title,88),(camera,134),(echo,180)]:d.text((743,y),text,font=F(20),fill='#405246')
 d.rectangle((679,442,721,993),outline='#bb7978',width=2)
 for ins,iy,c in [(.0104895,.0147783,'#c57e72'),(.027972,.0394089,'#659079')]:d.rectangle((1400*ins,Y+552*iy,1400*(1-ins),994-552*iy),outline=c,width=2)
 fn=out/f'page004-option{n}-composition-v1.png';assert not fn.exists();im.save(fn)
 return str(fn.relative_to(root))
paths=[make(3),make(4)]
p=root/'Tap 53/Part 1/scripts/layout_frames.json';data=json.loads(p.read_text());sp=next(v for v in data['spreads'] if v['id']=='part1-spread04-community-work');f=sp['frames'][0]
for i,path in zip([3,4],paths):
 assert not any(o['id']==f'page004-option{i}' for o in f['options'])
 f['options'].append({'id':f'page004-option{i}','preliminaryCompositionCard':path,'userConfirmed':False,'status':'storyboard-pending'})
p.write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n')
(out/'page004-frame-map-v2.json').write_text(json.dumps(f,ensure_ascii=False,indent=2)+'\n')
