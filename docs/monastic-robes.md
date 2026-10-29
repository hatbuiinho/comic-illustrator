# Màu y và cách quấn y của tu sĩ

Chỉ đọc và áp dụng khi ảnh cần vẽ tu sĩ. Không phải định nghĩa style.
Giữ lại hai quy chuẩn y phục đã được người dùng chọn; không lấy rendering,
identity hoặc diện mạo từ ảnh mẫu.

## Màu y

- Người dùng chọn ngày 2026-10-23: [mẫu màu y v001](../.agents/skills/comic-character-studio/assets/mau-y-chuan-v001.png)
  là chuẩn màu y chung cho các vị tu sĩ trong toàn dự án. Xem bản gốc,
  nhưng truyền [crop chỉ chứa vải](../.agents/skills/comic-character-studio/assets/mau-y-chuan-crop-v002.png) làm
  reference **chỉ màu y** khi tạo/chỉnh có y, nếu công cụ cho phép;
  ghi input thực tế. Không lấy mặt, da, tuổi, tỷ lệ, cách quấn, bố cục hoặc
  shading/rendering của mẫu; style tiếp tục theo ttpq comic light hiện hành. Phạm vi và
  provenance tại [record màu y](../.agents/skills/comic-character-studio/assets/mau-y-chuan-v001.md).
- Crop giữ pixel/màu nguyên trạng từ mẫu đã chọn, không thay chuẩn màu y hoặc
  tạo gate chọn màu mới. Không truyền toàn ảnh ref màu y chứa mặt/da để giảm
  ảnh hưởng chéo. Crop khác phải chỉ chứa vải, loại da/nền/chữ, ghi nguồn và
  toạ độ, xem lại trước khi dùng. Chỉ lấy màu, không lấy hình học bóng/rendering.
- Màu y lấy trực tiếp theo ảnh mẫu được chọn: nâu đỏ đất trầm. Bỏ mã tham
  khảo cũ chưa được xác minh; không dùng lại mã đó trong prompt mới hoặc coi
  một mô tả tên màu là chuẩn thay ảnh. Không khóa mọi vùng sáng/tối vào một mã.
- Mặc định dùng ảnh ref màu y, không bắt lập bảng màu hoặc mở gate duyệt màu
  riêng. Bảng màu chỉ là công cụ bổ trợ khi người dùng yêu cầu mã màu hoặc
  cần chẩn đoán lệch màu lặp lại: lấy mẫu vùng sáng/trung/tối đại diện trên
  vải, tránh da, nét đen và vùng bóng cực sâu; ghi vùng/toạ độ, phương pháp
  và phân biệt màu pixel quan sát với màu nền vật liệu. Bảng trích từ mẫu đã
  chọn không thay chuẩn ảnh, không tự tạo yêu cầu người dùng duyệt lại màu.
- Không tự đổi sang nâu vàng/ochre, cam tươi hay đỏ rực; giữ sắc nhất quán
  qua các góc dưới ánh sáng trung tính.
- Prompt phân vai nguồn identity, ref style và ref màu y; nêu rõ giữ nâu đỏ
  đất của mẫu, không đẩy đỏ cam hoặc làm nhạt/xám mất sắc đỏ. QA so riêng vùng
  sáng, trung và tối của y với mẫu dưới ánh sáng tương ứng; cùng tên màu hoặc
  đúng một mã midtone chưa đủ để kết luận khớp. Không sao chép hình học bóng.
- Khi chuyển style giữ màu nguồn, phân biệt màu y nguồn với mẫu chung: yêu cầu
  giữ nguyên màu nguồn rõ ràng vẫn ưu tiên và ghi `SKIPPED_BY_USER` đúng phạm vi
  màu y. Không âm thầm gọi màu của ảnh nguồn khác hoặc output thử là màu chuẩn.
- Khi không có yêu cầu giữ nguyên màu y nguồn rõ ràng, dùng mẫu màu y chung
  đã chọn; giữ nguyên thiết kế/cách quấn không đồng nghĩa giữ màu y khác mẫu.
- Reference mới về cách quấn không tự thay màu đã chốt.

## Cấu trúc y quấn

- Y phủ cả hai vai/ngực trên; không trần một vai hoặc khoét sâu nếu chưa yêu cầu.
- Vải mềm ở chân cổ, vắt chéo ngực, gom về vai; mép gấp/tà buông theo trọng lực.
- Quanh tay đọc là vải quấn/mép chồng mở, không ống tay may, cổ tay bo hay tay chuông.
- Cẳng tay có thể lộ theo cách quấn/tư thế; không mặc định phủ tới cổ tay.
- Tránh cổ áo tròn may, cổ đứng hoặc khối khăn cowl dày quanh cổ.
- Lớp vải liên tục hợp lý trước/bên/sau; không sao chép họa tiết nếp lên từng góc.
- Chuyển ref ngồi sang đứng phải dựng lại nếp theo trọng lực/tay/chân,
  không bê nguyên nếp đầu gối/lòng đùi.
- Chọn reference cách quấn cụ thể khi cần; không coi output thử chưa chọn là chuẩn.
- Mẫu quấn y chung do người dùng chọn ngày 2026-10-19:
  [ảnh mẫu v001](../.agents/skills/comic-character-studio/assets/y-quan-chuan-v001.png). Xem ảnh trước khi tạo/chỉnh
  tỳ-kheo và dùng làm reference cấu trúc y khi công cụ/yêu cầu cho phép.
- Theo mẫu: y phủ hai vai/ngực, nếp mềm quanh chân cổ và rủ qua ngực;
  mép vải ngoài gấp dọc từ vai, tà trên buông quanh hông, lớp dưới dài gần
  cổ chân có nếp dọc. Vải quanh tay phủ mềm theo cánh tay, bàn tay ra khỏi
  mép vải mở; không diễn giải thành ống tay may hoặc cổ tay bo. Đối chiếu
  đồng thời chính diện, 3/4, nghiêng và sau lưng trong mẫu.
- Mẫu này chỉ khóa cách quấn và quan hệ các lớp vải; không sao chép mặt,
  tuổi, tai, màu da, thể trạng hoặc chữ của Gavampati sang nhân vật khác.
  Màu y tiếp tục theo mục Màu y; style theo policy ttpq comic light hiện hành.
- Đây là mẫu thiết kế được chọn, không phải bằng chứng y phục lịch sử hoặc
  phê duyệt toàn bộ profile Gavampati. Không tự chuyển ảnh vào profiles.
  Nguồn: ảnh người dùng đính kèm trực tiếp; lưu bản gốc không chỉnh sửa.
- Khi không được dùng ảnh ref, chuyển cấu trúc trên thành mô tả chữ;
  không truyền ảnh mẫu trái yêu cầu. Reference mới hơn được người dùng
  chỉ định rõ vẫn ưu tiên theo phạm vi yêu cầu.
