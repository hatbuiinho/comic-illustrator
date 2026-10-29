# Vải, trang sức và mức chi tiết

> Cập nhật người dùng 2026-10-29 — `SKIPPED_BY_USER`, toàn dự án:
> style duy nhất là **ttpq comic light** (`docs/style-ttpq-comic-light.md`,
> đường dẫn từ root). Các yêu cầu rendering, bảng trang sức/ref style cũ,
> override st03 và khối prompt style cũ bên dưới đã được thay thế; không
> copy các phần đó vào prompt mới. Workflow và identity vẫn giữ; QA theo qa-checklist.md.
> Chỉ khi ảnh có tu sĩ mới đọc `docs/monastic-robes.md` cho màu/cách quấn y.


Một phần của [SKILL.md](../SKILL.md) Character Studio. Đọc khi ảnh có trang phục hoặc trang sức.
QA theo [qa-checklist.md](qa-checklist.md).

## Chuyển style và mức chi tiết

- **Vải phẳng, sạch:** áp dụng cho chuyển style, ảnh màu, sheet và lượt sửa
  có trang phục. Giữ silhouette, cách quấn, mép chồng, nếp gấp chính và màu
  theo nguồn; diễn bề mặt bằng mảng màu rộng, liền và ít chia vụn. Bóng theo
  nếp chính, chênh sắc vừa, mảng phẳng ranh giới rõ, không blend; không làm từng nếp
  nhỏ thành khối nổi hoặc phủ các vệt sáng–tối li ti lên toàn mặt vải.
- Phân biệt **hoa văn thiết kế** với **texture vật liệu** trước viết prompt:
  giữ hình, vị trí và nhịp lặp của viền/motif nhận diện đọc được; bỏ vân dệt,
  sợi vải, lưới nhỏ, hatching, nét xước, hạt và vệt loang mô phỏng bề mặt.
  Không hiểu “giữ nguyên chi tiết” là sao chép hoặc tăng rõ mọi vân vật liệu.
  Hoa văn thân vải thực sự có trong nguồn được diễn bằng nét/mảng 2D tiết chế,
  không tăng mật độ hay độ tương phản để lấp vùng trống. Chi tiết không đọc
  rõ thì ghi giới hạn, không đoán motif, biến vân dệt thành họa tiết mới hoặc
  xóa viền nhận diện để làm phẳng vải.
- Prompt thực tế phải nêu riêng phần giữ và phần bỏ ở vải; đưa các texture
  bị loại vào `Avoid/Negative constraints` ngay từ đầu. Khối gợi ý, điều chỉnh
  theo trang phục đang có:

  ```text
  Fabric: preserve the source garment silhouette, wrap, overlaps, main folds,
  colors and readable identifying border/motif shapes and spacing. Use broad,
  clean, uninterrupted 2D color areas and restrained designed shadow shapes
  following the main folds, with moderate contrast, flat color inside each
  shape and clear boundaries; no gradient blends.
  Avoid/Negative constraints: no woven microtexture, visible threads, fine
  crosshatch/grid, grain, scratches, mottling, dense tiny crease lines or
  fragmented highlight/shadow streaks across the fabric. Do not turn weave
  texture into invented motifs, amplify faint patterns, add decoration, or
  erase/change identifying borders and motifs to obtain a flatter surface.
  ```
- Trước lượt tạo đầu, tách thiết kế cần giữ khỏi cách thể hiện cần chuyển:
  identity, silhouette, cấu trúc trang phục/trang sức theo nguồn; nét, màu,
  shading và mức nhấn theo policy. Không chờ output lệch rồi mới bổ sung
  yêu cầu vật liệu vào prompt.
- Trang sức phải phục vụ nhận diện và địa vị nhưng không tranh trọng tâm với
  mặt. Giữ hình chính, vị trí và dấu riêng theo nguồn; không tự tăng mật độ
  hạt, viền, nét khắc hay hoa văn để diễn đạt “giàu có”, “tinh xảo” hoặc “2D”.
  Chi tiết nhỏ cần đọc ở kích thước sheet, không chỉ khi phóng lớn.
- Khi giảm cảm giác render, đổi cách chia sáng/tối trên cùng thiết kế.
  Không thay bóng sáng bằng họa tiết trang trí, thêm hình lá/hoa, hoặc hiểu
  “giữ chi tiết” là phải viền/vẽ rõ mọi hạt. Cũng không xóa dấu riêng hay
  làm toàn ảnh phẳng và nhạt. Nếu cần giảm chính thiết kế trang sức đã khóa,
  nêu đó là thay đổi thiết kế, không âm thầm gọi là chỉnh style.
- Prompt nêu cụ thể phần giữ, phần đổi và mức chi tiết theo vùng đang có;
  tránh các yêu cầu chung như “rich details”, “intricate” khiến mô hình
  tự trang trí thêm.
