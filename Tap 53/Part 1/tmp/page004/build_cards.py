from pathlib import Path
from PIL import Image, ImageDraw, ImageFont
import json, math

root=Path('/workspace')
out=root/'Tap 53/Part 1/pages/page-004/storyboards'
font='/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf'
def person(d,x,y,s,job,color='#9b684d',flip=1):
    def p(a,b):return (x+a*s*flip,y+b*s)
    def line(points,c,w):d.line([p(*v) for v in points],fill=c,width=max(1,int(w*s)))
    def poly(points,c):d.polygon([p(*v) for v in points],fill=c)
    lean=12 if job in ['dig','gather','sweep'] else 0
    # Chân và y phục là các khối liên tục; dáng người nghiêng theo công việc.
    line([(-7,49),(-12,73),(-23,90)],'#624839',7)
    line([(8,48),(16,70),(26,87)],'#624839',7)
    poly([(-14,28),(13,28),(16,58),(-15,58)],'#e5d5ac')
    poly([(lean-12,1),(lean+12,2),(14,35),(-13,35)],color)
    hx,hy=p(lean,-12);r=10*s
    d.ellipse((hx-r,hy-r,hx+r,hy+r),fill='#b97f56',outline='#493e32',width=max(1,int(s)))
    d.arc((hx-r,hy-r,hx+r,hy+r),180,345,fill='#3e342a',width=max(2,int(4*s)))
    if job=='dig':
        line([(lean+7,8),(27,22),(36,14)],'#b97f56',6)
        line([(lean-8,9),(11,30),(28,27)],'#b97f56',6)
        line([(36,6),(19,73)],'#65513b',3)
        poly([(17,68),(33,74),(25,81),(12,76)],'#5d6661')
    elif job=='carry':
        line([(-7,5),(-25,15),(-35,2)],'#b97f56',6)
        line([(8,6),(25,16),(33,1)],'#b97f56',6)
        line([(-52,-2),(52,-2)],'#77583a',4)
        for a in [-48,48]:
            line([(a,-2),(a-9,49)],'#68583d',1.5)
            line([(a,-2),(a+10,49)],'#68583d',1.5)
            poly([(a-15,48),(a+15,48),(a+10,64),(a-9,64)],'#a17e49')
    elif job=='wood':
        line([(-7,8),(-21,21),(-29,5)],'#b97f56',6)
        line([(9,8),(24,20),(33,4)],'#b97f56',6)
    else:
        line([(lean-8,8),(20,29),(36,49)],'#b97f56',6)
        line([(lean+8,8),(31,22),(37,46)],'#b97f56',6)
        if job=='sweep':
            line([(30,30),(50,79)],'#735d40',3)
            poly([(47,69),(62,88),(41,88)],'#af9059')
        else:
            poly([(24,52),(52,52),(47,65),(29,65)],'#a17e49')

def card(n):
 im=Image.open(out/'page004-layout-source.png').convert('RGB');d=ImageDraw.Draw(im)
 W,H=im.size; Y=round(H*255.827/575.433)
 d.rectangle((1,Y,W-2,H-1),fill='#e2d3b0')
 d.polygon([(1,Y),(W-2,Y),(W-2,Y+110),(1010,Y+100),(800,Y+119),(550,Y+83),(1,Y+126)],fill='#c0c5a0')
 for x in [65,200,400,930,1140,1300]:
  d.line((x,Y+8,x-10,Y+100),fill='#8c8a66',width=7)
  d.ellipse((x-55,Y-3,x+48,Y+45),fill='#a5b78c')
 # Hố móng dở và lối đi giữa: neo cảnh công trường chưa dựng công trình.
 for pts in [[(85,680),(420,610),(493,626),(160,714)],[(820,720),(1200,620),(1260,642),(881,754)]]:
  d.polygon(pts,fill='#b49a73');d.line(pts[:3],fill='#8f795a',width=5)
 for x,y in [(86,680),(420,610),(820,720),(1200,620)]:d.line((x,y-24,x,y+8),fill='#79654b',width=3)
 # Lán tạm nhỏ ở xa, không có tường/cột công trình mới.
 d.polygon([(510,490),(565,463),(626,495)],fill='#a5936c')
 for x in [525,610]:d.line((x,492,x,540),fill='#8a7655',width=4)
 if n==1:
  for x,y,s in [(150,615,.83),(260,598,.76),(378,575,.68),(472,567,.59)]:person(d,x,y,s,'dig', '#8b765a')
  for x,y,s in [(1030,660,.88),(1150,638,.8),(1210,565,.56)]:person(d,x,y,s,'gather','#917369',-1)
  for x,y,s in [(910,730,1.05),(1090,798,1.17)]:person(d,x,y,s,'carry','#a8754e',-1)
  d.polygon([(205,760),(457,720),(464,738),(211,779)],fill='#8c6443')
  for x,y in [(265,764),(402,744)]:person(d,x,y,1.25,'wood','#5a7970')
  for x,y in [(1170,512),(1230,508),(1280,519)]:person(d,x,y,.42,'sweep','#a18a58')
  for x,y in [(880,552),(967,539),(1020,522),(320,541)]:person(d,x,y,.48,'dig','#9c9279')
 else:
  # Góc thấp hơn: việc phối hợp chuyền gỗ thành điểm vào của toàn cảnh chung.
  d.polygon([(108,742),(470,676),(480,698),(115,767)],fill='#8c6443')
  for x,y in [(195,746),(420,704)]:person(d,x,y,1.63,'wood','#5a7970')
  for x,y,s in [(130,568,.62),(270,560,.57),(375,535,.48),(482,534,.45)]:person(d,x,y,s,'dig','#8b765a')
  for x,y,s in [(930,676,1.15),(1135,592,.83)]:person(d,x,y,s,'carry','#a8754e',-1)
  for x,y,s in [(1120,780,1.3),(1225,703,.97),(1050,549,.52)]:person(d,x,y,s,'gather','#917369',-1)
  for x,y in [(1180,511),(1250,527),(1300,505)]:person(d,x,y,.44,'sweep','#a18a58')
  for x,y in [(840,540),(906,516),(972,504)]:person(d,x,y,.45,'dig','#9c9279')
 # Guide phác: gáy luôn đi qua lối đất, không xuyên hành động.
 d.rectangle((W*.485,Y,W*.515,H),outline='#b45c60',width=2)
 for inset,c in [(.0104895,'#c77365'),(.027972,'#54836c')]:
  iy=.0147783 if inset<.02 else .0394089
  d.rectangle((W*inset,Y+(H-Y)*iy,W*(1-inset),H-(H-Y)*iy),outline=c,width=2)
 title=['1 · Cùng làm nên công trường','2 · Sức nặng được sẻ chia'][n-1]
 labels=[('Trọng tâm: '+title,(750,90)),('Góc nhìn: '+('chếch cao, toàn cảnh' if n==1 else 'gần ngang người lao động'),(750,136)),('Dư âm: mỗi nhóm góp một phần',(750,182))]
 for t,pos in labels:d.text(pos,t,font=ImageFont.truetype(font,21),fill='#39483e')
 path=out/f'page004-option{n}-composition-v1.png'; im.save(path)
 return str(path.relative_to(root))

paths=[card(1),card(2)]
box={'x':.5/810.709,'y':255.827/575.433,'width':809.708/810.709,'height':319.606/575.433}
frame={'id':'page004-community-work','shape':'rect','box':box,'textReserve':[],
 'spine':{'x':.485,'y':0,'width':.03,'height':1},
 'narrativeFunction':'Toàn cảnh cộng đồng chung tay lao động',
 'sourceMeasurement':{'pdfPage':4,'bookPages':[10,11],'boxPoints':[.5,255.827,810.208,575.433],'aspectRatio':809.708/319.606},
 'safeZone':{'x':.027972,'y':.0394089,'width':.944056,'height':.9211822},
 'visibilityPriority':[],
 'options':[{'id':f'page004-option{i+1}','preliminaryCompositionCard':p,'userConfirmed':False} for i,p in enumerate(paths)],
 'status':'storyboard-pending'}
mp=root/'Tap 53/Part 1/scripts/layout_frames.json'
data=json.loads(mp.read_text())
assert not any(s.get('id')=='part1-spread04-community-work' for s in data['spreads'])
data['spreads'].append({'id':'part1-spread04-community-work','canvas':{'width':810.709,'height':575.433},'pageImage':'../pages/page-004/storyboards/page004-layout-source.png','frames':[frame]})
mp.write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n')
(out/'page004-frame-map-v1.json').write_text(json.dumps(frame,ensure_ascii=False,indent=2)+'\n')
