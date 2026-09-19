from pathlib import Path
import json
base=Path('/workspace/Tap 53/Part 1/tmp/page004/confirm_option4.py').read_text()
# Lấy mã nguồn card đã xác nhận hướng kể, không chạy bước xuất phiên bản cũ.
exec(base[:base.index('exec(s)')])
s=s.replace('confirmed-composition-v1.png','confirmed-composition-v2.png')
needle="  # Le ruban de terre suit une courbe; aucune division en cases ou étapes."
extra='''  # Các tổ xa tiếp diễn ngang mép, hình dáng và công việc còn phân biệt được.
  d.polygon([(0,524),(480,487),(657,498),(642,510),(0,554)],fill='#c1ad88')
  d.polygon([(733,500),(1400,488),(1400,514),(755,519)],fill='#c6b590')
  for j,(x,y) in enumerate([(15,491),(47,498),(85,484),(119,493),(161,482),(202,490),(236,479),(269,488),(310,479),(351,491),(391,477),(427,489),(593,482),(625,492),(654,481),(752,479),(783,489),(1010,481),(1050,489),(1091,477),(1131,489),(1173,481),(1214,490),(1255,478),(1294,488),(1335,479),(1375,489)]):
   if j%3==0:woman(d,x,y,.30,'gather','#a9987e')
   elif j%3==1:person(d,x,y,.30,'dig','#9c947f',-1)
   else:person(d,x,y,.33,'dig','#a18c71')
  # Các cụm giữa gắn với hố móng và nơi gom vật liệu, không xếp hàng đều.
  for x,y,sc in [(33,551,.48),(85,539,.46),(133,552,.48),(176,538,.43),(226,557,.49),(271,540,.42)]:
   person(d,x,y,sc,'dig','#978a70',-1 if x%2 else 1)
  for x,y,sc in [(36,616,.67),(108,617,.60),(142,582,.52),(234,581,.48),(601,554,.51),(638,581,.53)]:
   woman(d,x,y,sc,'gather','#a38d74')
  woman(d,575,530,.46,'carry','#a29170')
  woman(d,752,557,.45,'carry','#a99878')
  woman(d,996,560,.5,'carry','#a08b73')
  woman(d,1330,600,.57,'gather','#a18b72')
  woman(d,1372,642,.61,'gather','#a59478')
  d.polygon([(1346,614),(1400,589),(1400,606),(1353,628)],fill='#ad9774')
  person(d,1362,591,.50,'wood','#929b80')
  # Tuyến đất phụ đi qua gáy là nền thấp tương phản, không chứa chi tiết chính.
  d.polygon([(504,604),(739,596),(946,654),(920,670),(734,617),(538,627)],fill='#d3bf9a')
'''
s=s.replace(needle,extra+needle)
s=s.replace("[(70,775),(345,609),(513,604),(560,638),(259,841)]", "[(-30,831),(345,609),(513,604),(560,638),(130,928),(-30,970)]")
s=s.replace("[(70,775),(345,609),(513,604)]", "[(-30,831),(345,609),(513,604)]")
s=s.replace("  woman(d,347,759,1.34,'gather','#b17e69');woman(d,532,682,.99,'gather','#9b8a75')", """  woman(d,584,625,.72,'gather','#a38c73')
  woman(d,627,650,.71,'gather','#9e8d79')
  woman(d,448,711,1.0,'gather','#b08d70')
  woman(d,347,759,1.34,'gather','#b17e69');woman(d,532,682,.99,'gather','#9b8a75')
  person(d,89,826,1.0,'dig','#947956')""")
s=s.replace("  woman(d,817,672,1.08,'carry','#b48d5d');woman(d,998,725,1.17,'carry','#987769')", """  woman(d,838,611,.70,'carry','#b09976')
  woman(d,1097,651,.78,'carry','#b49a78')
  woman(d,817,672,1.08,'carry','#b48d5d');woman(d,998,725,1.17,'carry','#987769')""")
s=s.replace("d.ellipse((1090,827,1350,906),fill='#c6b38d')", "d.polygon([(1090,873),(1130,830),(1338,821),(1400,796),(1400,925),(1280,914)],fill='#c6b38d')")
s=s.replace("  title='4 · Nhịp đất chuyền qua nhiều bàn tay'", "  title='4 · Nhịp chung sức — bố cục sửa lần 2'")
exec(s)
path=make(4)
mp=root/'Tap 53/Part 1/scripts/layout_frames.json';data=json.loads(mp.read_text());frame=next(v for v in data['spreads'] if v['id']=='part1-spread04-community-work')['frames'][0]
opt=next(o for o in frame['options'] if o['id']=='page004-option4')
opt['confirmedCompositionCard']=path;opt['compositionUserConfirmed']=False
opt['revisionRequired']=None
frame['optionAlignment']['userAction']='Sửa bố cục trang 4 — phương án 4: tăng lớp người và mật độ theo nhóm, cho công trường tiếp diễn ngoài khung; giữ rõ nhịp đào–gom–gánh–san.'
frame['optionAlignment']['confirmationScope']='Đã chọn hướng kể và yêu cầu sửa quy mô; bản G3 phiên bản 2 chờ duyệt.'
frame['meaningPreservationCheck']={'status':'pending','artifact':path,'reason':'Đã dựng lại lớp người và hoạt động tiếp diễn; chờ kiểm tra trực quan bản v2.'}
mp.write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n')
