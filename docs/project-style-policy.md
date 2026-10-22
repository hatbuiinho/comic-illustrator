# Policy phong cách toàn project

Nguồn: chuyển từ `AGENTS.md`, cập nhật theo quy chuẩn và ngoại lệ người dùng xác nhận.
Đọc policy này khi thiết kế hình, viết prompt, tạo ảnh hoặc visual QA. Các skill
tham chiếu policy chung khi thực thi; cập nhật quy chuẩn tại đây để tránh các
bản sao khác nhau. Ngoại lệ cấp tập hoặc yêu cầu trực tiếp của người dùng được
áp dụng theo thứ tự ưu tiên trong `AGENTS.md`.

Policy này cũng bắt buộc cho mọi ảnh trong Character Studio và Image Playground,
kể cả bản thử, character sheet và variant. Không cần người dùng nhắc lại trong
từng prompt; reference đầu vào không tự tạo ngoại lệ phong cách.

## Phong cách mặc định

Style mặc định toàn project là **[st03 — 2D mềm, màu tự nhiên cân bằng](style-st03.md)**,
được người dùng chọn ngày 2026-10-18, thay st02. Đọc định nghĩa và vai trò ảnh mẫu
tại tài liệu đó cùng policy này. st01 và st02 được giữ làm tham chiếu lịch sử.

Áp dụng st03 cho mọi lượt tạo/chỉnh ảnh mới trong flow minh họa tập/page/frame,
Character Studio và Image Playground, gồm bản thử, character sheet và variant;
không cần người dùng gọi lại tên style. Giữ identity theo profile gốc, thể hiện
bằng st03; không tự đổi thiết kế hoặc ghi đè profile.

### Thực thi trong prompt và QA

- Resolve style hiện hành trước thiết kế, viết prompt, tạo/chỉnh ảnh và QA.
  Prompt phải mô tả các yêu cầu st03 phù hợp cảnh, không chỉ ghi tên style:
  2D mềm với nét/mảng rõ, bề mặt sạch không hạt, màu tự nhiên cân bằng,
  xanh lá dịu khi xuất hiện và ánh sáng theo thời điểm/nguồn sáng thực tế.
  Nêu rõ cách diễn ánh sáng bằng mảng màu sáng–trung–tối có thiết kế trên
  mọi thành phần xuất hiện; cấm chuyển sáng–tối liên tục tạo cảm giác bán thực.
  Mô tả nét và mảng sáng dịu, hơi nhạt, chênh sắc vừa theo reference đen trắng
  được chọn trong [st03](style-st03.md); không viền đậm hoặc cắt gắt các mảng.
- QA kiểm các yêu cầu trên ở từng nhóm hình đang có, đặc biệt grain/noise,
  ám xanh lam/cyan toàn cảnh, màu bị phủ vàng/cam và cảnh đêm sáng như ban ngày;
  đánh giá theo định nghĩa st03, không coi lỗi trong ảnh mẫu là đặc điểm cần giữ.
  Chuyển nhẹ cục bộ ở rìa mảng theo mẫu đã chọn là hợp lệ; không đánh lỗi chỉ
  vì mảng không tuyệt đối phẳng/cạnh cứng. Kiểm hình dạng mảng còn đọc được,
  nét cấu trúc còn rõ và ánh sáng không nối thành khối bán thực.
- Khi tiếp tục tác vụ cũ, cập nhật phần style của prompt/qaLocks cho lượt mới
  theo policy hiện hành; ghi style st03 và thay đổi so với lượt trước trong
  record. Prompt cũ và output trước không khóa style cũ cho lượt mới.
- Giữ nguyên ảnh, prompt, record và kết quả duyệt trước đây; không hồi tố kết
  quả QA hoặc tự chuyển đổi tài sản cũ. Output chỉnh mới luôn có version mới
  và qua bước chọn/duyệt đang áp dụng của workflow tương ứng.
- Nếu người dùng yêu cầu ngoại lệ rõ, ghi `SKIPPED_BY_USER` cùng phạm vi theo
  AGENTS.md; reference có style khác không tự tạo ngoại lệ.

2D animation với nét và mảng màu thiết kế dẫn hình; cel-shading là nền tảng.
Ánh sáng và thể tích được diễn bằng các mảng màu sáng–trung–tối có chủ ý,
đọc được hình dạng và ranh giới mảng. Không bắt mọi bề mặt phải tuyệt đối
phẳng hoặc mọi cạnh bóng phải cứng; có thể tiết chế độ mềm ở rìa mảng,
nhưng không nối các vùng thành dải chuyển sáng–tối liên tục tạo khối bán thực.
Giữ chi tiết đồ họa có giá trị: mắt, tóc, nếp vải, hoa văn và trang sức; không
giản lược chúng chỉ để đạt nhãn “phẳng”.

Người dùng chốt ngày 2026-10-22: dùng [reference đen trắng v001](../studios/playground/outputs/chan-dung-den-trang/portrait-v001.png)
làm ảnh ref style hiện hành của st03 trên toàn project, thay vai trò ref mặc định
của bản màu Gavampati v003. Chỉ lấy cách diễn nét, tổ chức mảng sáng–trung–tối
và độ dịu của rìa mảng; không lấy identity, tuổi, nếp nhăn, thiết kế trang phục
hoặc bố cục của nhân vật mẫu. Reference đen trắng không yêu cầu output đen trắng:
màu sắc vẫn theo nguồn của từng đối tượng và policy màu st03.
Ranh giới mảng hơi nhạt,
chênh sắc vừa và mềm tiết chế; không bắt cạnh cứng hoặc viền đậm quanh mảng.
Cho phép chuyển nhẹ cục bộ ở rìa, giữ hình dạng mảng và cấu trúc nguồn.
Xem ảnh và phạm vi tham chiếu tại [định nghĩa st03](style-st03.md).
Đây là cập nhật style mặc định cho lượt mới, không hồi tố QA cũ hoặc duyệt
toàn ảnh mẫu; các giới hạn rendering còn lại tiếp tục có hiệu lực.

Người dùng xác nhận ngày 2026-10-22: nguyên tắc diễn ánh sáng bằng mảng màu
áp dụng cho toàn bộ cách tạo hình — mặt/da, tóc/râu, vải, trang sức, đạo cụ
và background — trong mọi workflow tạo/chỉnh ảnh. Kiểm tổng thể và từng vùng,
không chỉ tập trung vào vật liệu vừa được nhắc đến. Ngoại lệ nền trời bên dưới
tiếp tục có hiệu lực trong đúng phạm vi.

### Giữ cấu trúc khuôn mặt theo nguồn

Người dùng xác nhận ngày 2026-10-22, áp dụng toàn project: khi chuyển hoặc thể
hiện nhân vật bằng style dự án, giữ cấu trúc khuôn mặt theo profile/reference
gốc, gồm gò má, độ đầy má, hàm và tuổi. Chuyển cách diễn nét và mảng sang 2D,
không tự thay giải phẫu để làm mặt phẳng hơn hoặc có vẻ sâu hơn.

- Không xóa các nét và chuyển mảng gợi cấu trúc có trong nguồn khiến mặt mất
  độ sâu hoặc dấu nhận diện. Nét thanh vẫn phải đủ rõ ở kích thước sử dụng;
  không đồng nhất “mềm” với nhạt đến mức không thấy.
- Giữ hình dạng, vị trí và mức nhấn theo nguồn, có xét góc nhìn, biểu cảm và
  ánh sáng. Với gò má thanh, dùng nét/mảng tiết chế, chuyển nhẹ và đầu nét mềm
  khi phù hợp; không tự thêm cặp nét đối xứng, vệt chéo, rãnh má hoặc bóng
  khoét dưới gò má làm nhân vật hóp má, hốc hác hay già hơn nguồn. Không bắt
  mọi khuôn mặt phải có nét gò má riêng.
- Độ sâu đến từ nét có chủ ý và các mảng sáng–trung–tối thiết kế theo cấu trúc
  nguồn; không thay bằng chuyển sáng–tối liên tục hoặc tạo khối kiểu render.
- Trong prompt, khóa cấu trúc và độ đầy mặt theo nguồn gốc, nêu rõ điều cần
  giữ và cấm tự thêm nét/rãnh không có trong thiết kế. Không chỉ yêu cầu
  “thêm nét gò má” hoặc mặc định số lượng/vị trí nét mới.
- QA đối chiếu trực tiếp với nguồn gốc: kiểm cả mất cấu trúc do giản lược
  lẫn cấu trúc bị thêm/nhấn quá mức; kiểm riêng gò má, độ đầy má, hàm và tuổi.
  Output đã lệch không thay nguồn identity, kể cả khi dùng làm ảnh đích sửa.

### Vật liệu và giới hạn rendering

Người dùng xác nhận ngày 2026-10-22: trong mọi workflow tạo/chỉnh ảnh, khi
ảnh có trang sức, bắt buộc xem và truyền kèm
[ảnh ref bảng trang sức v003](../studios/playground/outputs/punna-trang-suc-den-trang/board-v003.png)
vào mỗi lượt ImageGen, kể cả bản thử, chuyển style, sheet, variant và sửa lỗi.
Mô tả bằng chữ không thay thế input ảnh này. Nếu không truyền được, báo giới
hạn trước lượt tạo, không âm thầm bỏ ref. Chỉ miễn khi người dùng chỉ định rõ.

Bảng chỉ hướng dẫn cách diễn vật liệu giảm bóng bằng nét/mảng 2D, không cung
cấp thiết kế hay màu trang sức. Ảnh/profile gốc vẫn quyết định hình, vị trí,
motif, connector, số hàng hạt, số lượng/độ rộng vòng và màu vàng–đá–ngọc.
Không sao chép sai khác thiết kế hoặc bóng cầu/điểm sáng lặp còn trong bảng;
không chuyển output màu thành grayscale. Ghi file và vai trò trong prompt,
record; QA kiểm riêng fidelity thiết kế và cách diễn vật liệu. Không dùng
bảng này thay ref style chung hoặc thêm trang sức vào vùng nguồn không có.

Giữ chi tiết có giá trị không có nghĩa tăng mật độ trang trí. Mức chi tiết
theo thiết kế nguồn, kích thước sử dụng và trọng tâm hình; trang sức không
tự thêm hoa văn/hạt/nét khắc để bù việc giảm bóng render. Chuyển style thay
cách thể hiện vật liệu, không tự thiết kế lại vật liệu hoặc phụ kiện.

Giữ khả năng nhận biết vật liệu bằng hình dạng, nét và các mảng màu sáng–trung–tối
được thiết kế. Trang sức/kim loại vẫn có thể có mảng sáng mạnh hoặc highlight
đồ họa để gợi chất liệu; không cấm trắng/gần trắng một cách máy móc, không tô
lì một màu khiến mất chất liệu. Mức sáng theo nguồn sáng và hierarchy của ảnh.
Không dùng vi texture dày hoặc vân mô phỏng ảnh thật.

Cấm dải chuyển sáng–tối liên tục, bóng cầu chuyển mượt, phản chiếu chuyển sắc
liền mạch hoặc airbrush tạo cảm giác vật liệu/thể tích bán thực. Đánh giá cách
tổ chức ánh sáng thành mảng trên toàn hình, không chỉ độ sáng hay sự có mặt
của highlight. Mảng sáng rõ không tự là lỗi; bỏ highlight cũng không bảo đảm
đạt style nếu shading còn liên tục kiểu render.

Cấm 2.5D/3D, CGI, bán hiện thực, texture ảnh, gradient nặng, bloom, volumetric
light, DOF và bokeh. Background cùng ngôn ngữ đồ họa với nhân vật; mức chi tiết
và độ mềm thay đổi theo lớp sâu và focus, không được bán thực hơn nhân vật.

Nguồn cập nhật: người dùng xác nhận nới nhẹ 2D để chi tiết mềm hơn và triển khai
vào workflow chung ngày 2026-10-11. Đây là mặc định mới của project, không chỉ
là override cho một page. Profile gốc tiếp tục là chuẩn identity.

## Giới hạn độ mềm trên da

Người dùng yêu cầu siết nhẹ độ mềm trên da ngày 2026-10-22, áp dụng cho lượt
tạo/chỉnh mới. Mảng sáng–trung–tối phải liền bên trong và còn đọc rõ hình dạng;
chỉ làm dịu cục bộ trong phạm vi hẹp sát mép, không tán chuyển sắc lan rộng
ôm khối má, mũi, cằm hoặc cổ. Giữ sắc vùng mắt bằng các mảng màu có thiết kế,
không diễn giải “giữ chuyển sắc” thành blend rộng quanh mắt hoặc toàn mặt.

Prompt phải nêu giới hạn này và cấm broad blending, airbrush, bóng cầu hoặc
dải sáng–tối liên tục trên da. QA kiểm các vùng da riêng ở kích thước sử dụng;
nét đen rõ không bù được chuyển sắc còn tạo cảm giác 3D. Không ép da thành một
màu, tăng bóng tối, làm mọi cạnh sắc gắt hoặc đổi cấu trúc nguồn để giảm độ mềm.
Giới hạn này làm rõ phạm vi các câu “mềm tiết chế”, “ranh giới hơi nhạt” ở trên;
không hồi tố QA cũ hoặc thay reference style hiện hành.

## Ngoại lệ nền trời

Người dùng xác nhận ngày 2026-10-02, phạm vi toàn project:
`SKIPPED_BY_USER` đối với việc cấm tuyệt đối nền trời mềm. Nền trời được phép
có chuyển màu mềm nhẹ và tiết chế để gợi thời điểm hoặc không khí. Ngoại lệ
không tự cấp phép shading cho nhân vật hay vật thể; các thành phần đó theo
mặc định cập nhật ở trên. Ngoại lệ không cho phép tạo khối kiểu render,
gradient nặng, bloom, volumetric light, DOF, bokeh, CGI hoặc bán hiện thực.
