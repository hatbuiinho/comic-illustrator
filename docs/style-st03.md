# st03 — 2D mềm, màu tự nhiên cân bằng

> LỊCH SỬ — từ 2026-10-29 đã được thay hoàn toàn bởi `ttpq comic light`
> tại `docs/style-ttpq-comic-light.md` (đường dẫn từ root). Không áp dụng
> định nghĩa, ref hoặc chỉ dẫn “hiện hành” bên dưới cho lượt mới.

Được đề xuất trong hội thoại ngày 2026-10-17 và người dùng yêu cầu lưu ngày
2026-10-18. Mục tiêu: khắc phục xanh lá hơi rực của st01 và cảm giác lạnh/ám
xanh trời của st02, giữ màu rõ, có sức sống và phù hợp nhiều bối cảnh.
Ngày 2026-10-18, người dùng chọn `st03` làm style mặc định toàn project, thay
st02, áp dụng cho mọi lượt tạo/chỉnh ảnh mới của flow minh họa, Character Studio
và Image Playground theo [policy chung](project-style-policy.md). Tài sản cũ
giữ nguyên; khi tiếp tục tạo/chỉnh thì áp dụng st03 cho version mới.

## Đặc điểm

- Cập nhật người dùng xác nhận ngày 2026-10-22: dùng cách diễn mảng sáng
  trong [reference đen trắng v001](../.agents/skills/comic-image-production/references/style-st03/portrait-bw-v001.png)
  làm chuẩn cho nét, tổ chức mảng và độ dịu của rìa mảng. Người dùng chốt dùng
  bản đen trắng làm ảnh ref style, thay bản màu Gavampati v003. Mảng sáng–trung–tối vẫn có hình dạng
  thiết kế, nhưng chênh sắc vừa, ranh giới hơi nhạt và mềm tiết chế; không
  viền đậm quanh mảng sáng hoặc làm cạnh mảng nổi thành vệt cắt gắt.
  Cho phép chuyển nhẹ cục bộ ở rìa như mẫu, không ép mọi mảng thành ô màu
  tuyệt đối phẳng/cạnh cứng. Không nối toàn bộ sáng–tối thành khối render
  bán thực. Áp dụng theo vật liệu và nguồn sáng; vẫn giữ nét cấu trúc và
  chi tiết identity đủ rõ, không làm nhạt toàn hình.
- Với da, áp dụng [giới hạn độ mềm trên da](project-style-policy.md#giới-hạn-độ-mềm-trên-da):
  mảng màu liền, hình dạng và ranh giới còn đọc rõ; chỉ dịu mép hẹp, không
  blend rộng ôm khối má–mũi–cằm–cổ. Sắc quanh mắt được giữ bằng mảng màu,
  không phải chuyển mượt toàn vùng. Đây là giới hạn của “mềm tiết chế” trên
  da, không yêu cầu tô một màu hoặc làm mọi cạnh sắc gắt.
- Giữ nét vẽ và mảng màu thiết kế của 2D animation mềm: silhouette rõ, khối nhẹ,
  cel-shading với các mảng sáng–trung–tối có thiết kế; rìa mảng có thể mềm
  tiết chế, không tạo dải chuyển ánh sáng liên tục gây cảm giác bán thực.
  Áp dụng trên mọi thành phần theo [policy ánh sáng và vật liệu](project-style-policy.md).
  Không giảm chi tiết mắt, tóc,
  nếp vải, hoa văn hoặc trang sức chỉ để làm phẳng hình.
- Cấu trúc khuôn mặt theo profile/reference gốc: giữ nét và mảng gợi gò má,
  độ đầy má, hàm và tuổi theo [policy giữ cấu trúc khuôn mặt](project-style-policy.md#giữ-cấu-trúc-khuôn-mặt-theo-nguồn).
  Nét thanh nhưng đủ đọc; không xóa đến phẳng mặt hoặc tự thêm rãnh má.
- Bề mặt màu phải sạch và liền mảng. Cấm hạt giấy, hạt màu, grain/noise,
  chấm li ti, vân giấy và texture cọ khô trên da, vải, vật thể lẫn background,
  kể cả lớp phủ rất nhẹ. Độ mềm đến từ nét, hình dạng và rìa mảng được xử lý
  tiết chế, không từ texture hạt hoặc dải shading liên tục; vẫn giữ nét và
  chi tiết thiết kế có chủ ý.
  Quy định này được người dùng bổ sung ngày 2026-10-18, áp dụng cho mọi ảnh st03 mới.
- Ánh sáng theo thời điểm, môi trường và nguồn sáng thực sự của cảnh; không mặc
  định ánh sáng ban ngày cho mọi ảnh. Ánh sáng trắng trung tính dùng cho character
  sheet hoặc cảnh ban ngày khi phù hợp. Quy định được người dùng cập nhật ngày
  2026-10-18.
- Cảnh đêm phải có nền sáng tổng thể thấp hơn ban ngày, phân biệt vùng nhận sáng
  từ trăng, đèn hoặc lửa với vùng khuất tối. Giữ hình đọc được bằng nét, silhouette
  và tổ chức mảng sáng–tối; không nâng sáng đồng loạt thành cảnh ban ngày.
- Màu ánh sáng và bóng được thay đổi có chủ đích theo nguồn sáng: ánh trăng có
  thể lạnh nhẹ, đèn/lửa có thể ấm cục bộ. Không phủ xanh lam/cyan vào toàn ảnh
  hoặc mặc định mọi vùng bóng; không dùng lớp vàng/cam để bù ám xanh. Không dùng
  bloom, volumetric light hoặc tạo khối kiểu render để diễn đạt nguồn sáng.
- Điều chỉnh riêng từng nhóm màu thay vì giảm saturation hoặc đổi nhiệt độ màu
  đồng loạt. Giữ quan hệ màu nhận diện của từng vật thể trong sáng và bóng;
  màu nhìn thấy được phép đổi theo cường độ và màu nguồn sáng của cảnh.
- Xanh lá tự nhiên có độ bão hòa vừa; giảm vàng chanh ở lá sáng, tránh xanh ngọc/cyan
  và xanh neon. Lá vẫn tươi, không thành olive xám hoặc bạc màu.
- Với cảnh ban ngày, trời xanh nhạt, ít cyan; núi xa có thể dùng xám tím nhẹ hoặc xám trung tính theo
  cảnh. Sắc lạnh tập trung ở khoảng xa khi hợp lý, không lan sang da, áo và đất.
- Da giữ sắc độ, sắc màu và độ bão hòa theo profile/reference gốc; không mặc
  định tăng độ ấm. Prompt phải cấm tăng vàng/cam riêng trên da, không chỉ cấm
  lớp phủ vàng/cam toàn ảnh; không tự dùng “warm skin tone” thay khóa màu nguồn.
  Không lấy màu da từ ref style hoặc ref vật liệu. QA so riêng vùng sáng–trung–tối
  của mặt, cổ và tay/chân với nguồn; nền trắng không chứng minh da đúng màu.
  Áo kem đọc như ngà sạch;
  bóng be xám nhẹ dưới ánh sáng trung tính. Trong cảnh đêm hoặc nguồn sáng có màu,
  điều chỉnh có căn cứ theo nguồn sáng, vẫn giữ phân biệt màu da và y phục.
  Không ép mọi nhân vật về cùng một màu da.
- Đất nâu be dịu. Vàng cổ, đỏ gạch và tím có độ đậm vừa; chỉ vài chi tiết trọng tâm
  có màu mạnh. Không để vàng/cam hoặc xanh trời chi phối toàn cảnh.
- Giữ midtone chắc, nét và mảng tối rõ, tương phản vừa; giảm độ rực không được làm
  hình nhạt, xám đục hoặc mất chiều sâu kể chuyện.
- Background cùng ngôn ngữ đồ họa 2D với nhân vật. Các giới hạn về 3D/CGI, bán hiện
  thực, texture, ánh sáng và ngoại lệ nền trời theo [policy chung](project-style-policy.md).

## Mẫu tham chiếu và vai trò

- [Reference đen trắng v001](../.agents/skills/comic-image-production/references/style-st03/portrait-bw-v001.png):
  **ảnh ref style mặc định hiện hành**, người dùng chốt ngày 2026-10-22 sau
  lượt thử [Mục Kiền Liên v002](../studios/playground/outputs/muc-kien-lien-st03/portrait-v002.md).
  Lấy nét, cách chia mảng sáng–trung–tối, tương quan sắc độ và độ dịu rìa mảng
  trên da/vải theo policy. Không lấy khuôn mặt, tuổi, nếp nhăn, tỷ lệ, thiết kế
  y phục hoặc bố cục. Không chuyển output sang grayscale trừ khi được yêu cầu;
  màu vẫn theo nguồn từng đối tượng và định nghĩa st03.
  [Record và prompt gốc](../studios/playground/outputs/chan-dung-den-trang/portrait-v001.md)
  giữ provenance; việc chọn ref không phải duyệt profile/canon nhân vật mẫu.
- [Tôn giả Gavampati v003](../.agents/skills/comic-image-production/references/style-st03/gavampati-v003.png):
  mẫu màu lịch sử, được thay vai trò ref mặc định bằng bản đen trắng ở trên.
  Người dùng từng chọn ngày 2026-10-22 làm mẫu cho **cách diễn mảng sáng và độ dịu
  của rìa mảng**, nhất là da và vải. [Prompt](../studios/playground/outputs/gavampati-st03/prompt-v003.md)
  và [record](../studios/playground/outputs/gavampati-st03/portrait-v003.md)
  giữ provenance. Chỉ lấy thuộc tính ánh sáng này; không lấy khuôn mặt,
  nếp áo, màu da/áo hoặc sai khác chi tiết nguồn làm chuẩn cho nhân vật khác.
  Xác nhận này không phải duyệt toàn ảnh hoặc profile Gavampati.
- [Công trường v001](../.agents/skills/comic-image-production/references/style-st03/cong-truong-v001.png):
  mẫu thử tổng thể cho màu lá dịu, phân biệt nhóm màu và cảnh đông theo st03.
  [Prompt](../studios/playground/outputs/cong-truong-st03/prompt-v001.md) và
  [record](../studios/playground/outputs/cong-truong-st03/scene-v001.md) giữ provenance.
- [Cảnh rắn cắn v001](../.agents/skills/comic-image-production/references/style-st03/ran-can-v001.png):
  mẫu bổ trợ cho nét/mảng 2D, cách hòa hình chữ và tương phản cảm xúc trong cảnh đông.
  [Prompt](../studios/playground/outputs/ran-can-st03/prompt-v001.md) và
  [record](../studios/playground/outputs/ran-can-st03/spread-v001.md) giữ provenance.
- Hai mẫu vẫn có da/đất hơi ấm; mẫu rắn cắn có sari xanh và vàng khá đậm, mẫu công
  trường có một số lá sáng ngả vàng. Không kế thừa các điểm này như yêu cầu bắt buộc.
  Khi có khác biệt, ưu tiên định nghĩa màu ở trên thay vì sao chép toàn bộ màu ảnh mẫu.
- [st01](style-st01.md) chỉ bổ trợ nét, mảng và độ mềm; không kế thừa độ rực.
  [st02](style-st02.md) chỉ bổ trợ mức tiết chế; không kế thừa cảm giác ám xanh.

Lưu tên style không đồng nghĩa duyệt từng output. Ảnh mẫu không thay profile
identity, không trở thành canon, master hoặc asset approved của tập. Lỗi anatomy,
dấu cắn hoặc chữ raster trong mẫu không phải đặc điểm style.
