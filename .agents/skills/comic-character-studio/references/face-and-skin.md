# Nét mặt, vùng mắt và da

> Cập nhật người dùng 2026-10-29 — `SKIPPED_BY_USER`, toàn dự án:
> style duy nhất là **ttpq comic light** (`docs/style-ttpq-comic-light.md`,
> đường dẫn từ root). Các yêu cầu rendering, bảng trang sức/ref style cũ,
> override st03 và khối prompt style cũ bên dưới đã được thay thế; không
> copy các phần đó vào prompt mới. Workflow và identity vẫn giữ; QA theo qa-checklist.md.
> Chỉ khi ảnh có tu sĩ mới đọc `docs/monastic-robes.md` cho màu/cách quấn y.


Một phần của [SKILL.md](../SKILL.md) Character Studio. Đọc khi prompt có mặt hoặc da nhìn thấy.
QA theo [qa-checklist.md](qa-checklist.md).

### Nét đen cấu trúc trên khuôn mặt

- Áp dụng cho ảnh chuyển style, ảnh màu, sheet và mọi lượt sửa có mặt nhìn
  thấy. Prompt phải chỉ rõ vị trí cần nét đen theo cấu trúc nguồn; không chỉ
  ghi “nét rõ” hoặc dùng bóng màu sẫm thay nét. Với góc khuất hoặc chi tiết
  nguồn không có, không tự thêm nét để đủ danh sách.
- Khi biên soạn prompt thực tế, tách yêu cầu **Mũi** và **Miệng** thành hai
  mục riêng theo vùng nhìn thấy; không rút gọn thành “fine dark linework”.
  Trong `Avoid/Negative constraints` phải có câu cấm dùng bóng nâu/xám,
  đường màu môi hoặc ranh giới mảng màu thay nét mực đen/near-black. Kiểm
  câu này có trong prompt đã gửi, không chỉ trong skill hay record QA.
  “Mềm”, “dịu”, “tiết chế” chỉ mô tả độ dày/đầu nét, không cho phép làm
  nhạt màu nét cấu trúc, hòa nét vào bóng da/môi hoặc blend mảng shading.
- Mắt: nét đen thanh ở bờ mí trên, khóe mắt và lông mi đang có; mí dưới chỉ
  nhấn đoạn cấu trúc theo nguồn, không mặc định viền đen kín mắt. Mày giữ
  hình, độ dày và màu theo identity, không ép mọi lông mày thành khối đen.
- Mũi: nét đen thanh ở lỗ mũi và đoạn ngắn chân/cánh mũi thực sự thấy trong
  nguồn. Không viền đen toàn bộ mũi, kéo nét dọc hai bên sống mũi hoặc làm
  mũi nhỏ/nhọn hơn. Không lấy ranh giới bóng sáng làm đường cấu trúc mới.
- Miệng: đường khép/tiếp giáp hai môi cần nét đen thanh, rõ theo đúng đường
  cong nguồn, nối về hai khóe khi nguồn thể hiện; khóe miệng nhấn ngắn và
  tiết chế, không thành hai mảng đen dày. Không chỉ giữ một đường nâu/xám
  hoặc bóng mềm rồi coi đã có nét đen. Không viền kín cả hai môi, tô môi
  thành đen hoặc thay hình môi/nụ cười. Miệng mở thì theo đúng mép miệng
  đang thấy, không tự thêm đường khép môi xuyên qua khoảng mở.
- Môi dưới: thêm nét đen/near-black thanh, ngắn, thu hai đầu ở đoạn bờ dưới
  thực sự đọc được theo cấu trúc nguồn; có thể ngắt, không nối thành viền
  kín môi. Phân biệt nét này với đường khép môi và bóng đổ dưới môi: không
  dùng bóng nâu thay nét, cũng không đồ toàn bộ mép bóng thành đường đen dài.
  Không tự thêm khi góc nhìn che khuất hoặc nguồn không cho thấy cấu trúc đó.
  Yêu cầu “không viền kín cả hai môi” không có nghĩa bỏ nét chọn lọc môi dưới.
- Tai, hàm/cằm và cổ: giữ nét đường bao và nét cấu trúc chọn lọc theo nguồn,
  phân cấp thanh–đậm với mắt/mũi/miệng; không đồ mọi nếp tuổi, rãnh má hoặc
  ranh giới mảng sáng–tối thành nét đen. Răng khi có theo mục **Răng** bên
  dưới, không viền đen kín từng chiếc.
- Răng: với nụ cười thấy răng, giữ nét đen có chủ ý ở mép đầu răng và ít nét
  kẽ ngắn theo cấu trúc, giảm shading men răng; không biến “ít chi tiết” thành
  xóa hết nét hoặc viền kín mọi chiếc. Không thêm răng/chi tiết miệng khi
  nguồn không có.
- Nét đen/near-black phải đọc như nét mực ở kích thước sử dụng, có đầu nét
  thu và độ dày tiết chế, không làm toàn bộ viền mặt đậm cứng. Giữ màu môi,
  màu da và mảng ánh sáng; tăng nét không cho phép đổi vị trí, kích thước,
  hình dạng hay tỷ lệ bộ phận. Màu biểu đạt riêng trong nguồn chỉ đổi khi
  người dùng yêu cầu rõ, ghi phạm vi; không tự thêm makeup.
- Không tự cập nhật reference style chỉ vì đã sửa skill; ref style mới cần
  người dùng chọn rõ.

Khối gợi ý tích hợp theo góc nhìn và phần thực sự xuất hiện:

```text
Eyes: fine black or near-black tapered structural ink at the visible upper
eyelids and eye corners, following the source.
Nose: distinct fine black or near-black ink at the visible nostril apertures
and short alar/nose-base edges actually shown in the source. These must read
as ink strokes at the intended viewing size, separate from colored shading.
Mouth: a fine black or near-black actual lip-separation line, including its
central segment and its connection toward the corners where the source shows
them; restrained short corner accents alone are insufficient. For an open
mouth, follow its visible edges without adding a closed-lip seam across it.
Lower lip: where the source reveals its lower structural edge, use a short,
fine black/near-black tapered stroke, optionally broken, distinct from the
lip-separation line. Do not enclose the lip or trace the entire cast shadow.
Keep source feature shapes, positions and proportions. Softness means tapered
delicate strokes only, not faded structural ink or blended shading.
Avoid/Negative constraints: do not substitute brown/gray shading, lip-colored
lines or color-patch boundaries for the required black/near-black ink. Do not
encircle the whole nose or both lips, thicken corners into black wedges, trace
every wrinkle or light/shadow boundary, or add lines on hidden features.
Preserve source anatomy and all relative proportions.
```

### Sắc vùng mắt theo identity gốc

Người dùng xác nhận ngày 2026-10-21 từ thử nghiệm Nhân vật nữ test: giữ chuyển
sắc quanh mắt theo ảnh gốc để không làm mất dấu riêng khi chuyển sang 2D.
Áp dụng khi thiết kế nhân vật Ấn Độ có nguồn tương ứng; không suy rằng mọi
người Ấn Độ đều có cùng màu hoặc mức đậm quanh mắt, không tự thêm nếu nguồn
không thể hiện. Không dùng đặc điểm này để kết luận nguồn gốc từ ảnh.

- Đọc quan hệ màu cả vùng: mí/hốc mắt, da ngay trên mí tới dưới mày, khóe mắt,
  sát mí dưới và phần chuyển về má. Không chỉ lấy màu tối ở một dải dưới mắt.
- Giữ sắc đậm riêng có trong nguồn, nhưng nối màu hợp lý với da trên mí và
  vùng xung quanh; tránh dải sáng khác hẳn ngay trên mí tối hoặc quầng dưới
  mắt tách biệt gây cảm giác thâm, mệt mỏi hay bầm mắt ngoài nguồn.
- Khi dùng bảng màu cô lập, bổ sung màu chuyển tiếp và vị trí dùng, phân biệt
  da quanh mắt với tròng mắt/lông mi. Màu tối nhất chỉ dùng đúng phạm vi nguồn;
  không phủ toàn hốc mắt hoặc tự diễn giải thành smoky makeup.
- Thể hiện bằng nét/mảng 2D phẳng, ranh giới rõ; giữ biến thiên sắc không
  đồng nghĩa sao chép tạo khối ảnh thật.
- Giữ quan hệ sắc bằng các mảng màu riêng có hình dạng rõ; “giữ chuyển sắc”
  không cho phép blend rộng từ hốc mắt sang má hoặc làm mượt toàn mặt.
  Rendering da theo cel-shading 2–3 tông của ttpq comic light.
