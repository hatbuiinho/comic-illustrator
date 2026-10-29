# QA Character Studio — ttpq comic light

Người dùng chốt ngày 2026-10-29: thay toàn bộ QA cũ (bảng kiểm style theo
vùng, kiểm da ba tông, nét đen từng đoạn mũi/miệng, bảng trang sức, kiểm
vải/da phóng lớn từng vùng). Đây là nguồn QA duy nhất của Character Studio,
áp dụng cho ảnh chuyển style, sheet, variant và nhánh nét/màu khi được yêu cầu.

## Cách chạy

- **Tầng 1 — mọi lượt:** xem output cạnh ảnh gốc ở kích thước sử dụng, đi
  qua các nhóm dưới đây theo thứ tự. Đánh giá trên toàn ảnh; không crop từng vùng.
- **Tầng 2 — zoom có mục tiêu:** chỉ crop/phóng lớn vùng mà tầng 1 nghi lỗi,
  hoặc một lần trước khi lưu profile (mặt + chi tiết nhận diện). Không zoom
  hết danh sách vùng cho mỗi ảnh.
- Mỗi nhóm ghi `Đạt`, `Chưa đạt` (lỗi + vùng) hoặc `Không áp dụng`. Không ghi
  đạt khi chưa xem ảnh; chi tiết không đọc rõ thì ghi giới hạn, không đoán.
- So với ảnh gốc, không lấy output trước làm chuẩn.

## 1. Identity và tỷ lệ — chặn

- Nhận ra đúng người: hình mặt, mắt/mày, mũi, môi (cả màu môi), hàm/cằm,
  tuổi, màu da, tóc/râu.
- Tỷ lệ ngũ quan và đầu–cổ–thân–tay–chân không đổi thấy rõ. Đổi góc chỉ được
  co ngắn theo phối cảnh.
- Không lý tưởng hóa: mắt to hơn, mũi nhỏ hơn, mặt thon/cân xứng hơn, cổ dài,
  dáng mảnh, da sáng hơn, trẻ hóa. Không chibi, không mặt trẻ con.

## 2. Thiết kế — chặn

- Trang phục, viền/motif nhận diện, trang sức, phụ kiện, màu: không mất, đổi
  hoặc tự thêm. Không thay bằng thiết kế cổ trang Trung Quốc ngoài nguồn.
- Lượt chuyển style: pose, biểu cảm, góc nhìn, crop giữ theo nguồn.
- Nhân vật nữ: bụng/eo kín ở mọi hình, kể cả góc nghiêng và sau lưng.
- Tu sĩ: đầu cạo sạch, màu y và cách quấn theo `docs/monastic-robes.md`.

## 3. Style ttpq comic light — chặn khi lệch rõ

Đối chiếu với [định nghĩa style](../../../../docs/style-ttpq-comic-light.md):

- Thuần 2D; không anime, 3D/CGI, ảnh thật, painterly brush texture.
- Nét vẽ tay sạch, viền ngoài dày hơn nét trong; nét mảnh ở mặt đủ đọc mắt,
  mũi, miệng ở kích thước sử dụng.
- Màu mảng phẳng sạch, 2–3 tông cel-shading mềm trên da và vải. Mềm ở rìa
  mảng được phép; chỉ là lỗi khi gradient/blend làm khối nổi như 3D.
- Không hatching hoặc bóng đen thô trên da; texture bề mặt tiết chế; tóc
  thành mảng rõ; nếp vải giản lược nhưng còn nếp chính.
- Không đếm số tông hay độ dày nét; lệch nhỏ không đổi cảm giác style ghi
  chú, không chặn.

## 4. Sheet — chỉ khi dựng sheet

- Đủ chân dung và bốn góc theo [sheet-layout.md](sheet-layout.md); thấy trọn
  đầu/chân, các silhouette không chạm, chồng hay bị cắt.
- Các góc cùng tỷ lệ và chiều cao; identity, thiết kế nhất quán giữa các góc;
  không bóp/rút ngắn nhân vật để vừa khung.
- Chữ thông tin đúng brief, không tự thêm trường; kiểm kích thước pixel thực
  của file.

## Kết quả và bước tiếp

- **Chặn:** nhóm 1 hoặc 2 chưa đạt, hoặc nhóm 3 lệch rõ. Không dùng bản bị
  chặn làm nền dựng sheet hay lưu profile.
- **Không chặn:** lỗi nhỏ ghi chú ngắn, vẫn trình người dùng duyệt.
- Bị chặn: tự sửa một lượt từ ảnh gốc theo mục **Chỉ tạo lại từ ảnh gốc**
  của [SKILL.md](../SKILL.md); vẫn lỗi thì trình trạng thái và chờ hướng.
- Record QA chỉ cần kết quả 4 nhóm và lỗi nếu có, trong record version theo
  [contract studio](../../../../docs/studio-contract.md).
