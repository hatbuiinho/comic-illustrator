# st03 — 2D mềm, màu tự nhiên cân bằng

Được đề xuất trong hội thoại ngày 2026-10-17 và người dùng yêu cầu lưu ngày
2026-10-18. Mục tiêu: khắc phục xanh lá hơi rực của st01 và cảm giác lạnh/ám
xanh trời của st02, giữ màu rõ, có sức sống và phù hợp nhiều bối cảnh.
Ngày 2026-10-18, người dùng chọn `st03` làm style mặc định toàn project, thay
st02, áp dụng cho mọi lượt tạo/chỉnh ảnh mới của flow minh họa, Character Studio
và Image Playground theo [policy chung](project-style-policy.md). Tài sản cũ
giữ nguyên; khi tiếp tục tạo/chỉnh thì áp dụng st03 cho version mới.

## Đặc điểm

- Giữ nét vẽ và mảng màu thiết kế của 2D animation mềm: silhouette rõ, khối nhẹ,
  cel-shading và chuyển sắc mềm cục bộ, tiết chế. Không giảm chi tiết mắt, tóc,
  nếp vải, hoa văn hoặc trang sức chỉ để làm phẳng hình.
- Bề mặt màu phải sạch và liền mảng. Cấm hạt giấy, hạt màu, grain/noise,
  chấm li ti, vân giấy và texture cọ khô trên da, vải, vật thể lẫn background,
  kể cả lớp phủ rất nhẹ. Độ mềm đến từ chuyển sắc cục bộ sạch và tiết chế,
  không từ texture hạt; vẫn giữ nét và chi tiết thiết kế có chủ ý.
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
- Da giữ sắc riêng theo profile, ấm vừa và không cam. Áo kem đọc như ngà sạch;
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

- [Công trường v001](../studios/playground/outputs/cong-truong-st03/scene-v001.png):
  mẫu thử tổng thể cho màu lá dịu, phân biệt nhóm màu và cảnh đông theo st03.
  [Prompt](../studios/playground/outputs/cong-truong-st03/prompt-v001.md) và
  [record](../studios/playground/outputs/cong-truong-st03/scene-v001.md) giữ provenance.
- [Cảnh rắn cắn v001](../studios/playground/outputs/ran-can-st03/spread-v001.png):
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
