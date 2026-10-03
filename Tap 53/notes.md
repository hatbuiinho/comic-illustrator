# Tập 53 — Dữ kiện và ngoại lệ

File này chỉ chứa nguồn sự thật riêng của Tập 53. Workflow dùng chung nằm trong
`.agents/skills/` ở root repository.

## Bối cảnh

- Mạch truyện đặt tại Ấn Độ cổ đại, xấp xỉ thế kỷ 5 TCN, trong bối cảnh cuộc
  đời Đức Phật, các vị Thánh, tín chủ và cộng đồng đương thời.
- Hình thể, gương mặt, kiến trúc và y phục không được lai sang Việt Nam, Trung
  Hoa hoặc fantasy Đông Á.
- Trang phục ưu tiên y phục quấn, draped garments, vải mộc và cấu trúc đơn giản.
- Nhân vật nữ cần kín đáo, phù hợp bối cảnh; không hở bụng hoặc mang cảm giác
  gợi cảm hiện đại.

## Nguồn layout

- `Part 1/layouts/TẬP 53 _ PART 1 _ DEMO DÀN TRANG_PTg full 12.08.26.pdf`
- `Part 2/layouts/Tập 53_Chương 5_Chánh Nghiêm_Phước Thịnh_đàn trang demo_07.09.pdf`

Mỗi page trong PDF demo tương ứng một spread hai trang. Khối xanh là vùng liên
quan minh họa hoặc brief, không mặc định luôn là một frame ảnh độc lập.

Quy ước màu của layout Tập 53:

- xanh: brief/vùng chờ minh họa;
- hình tròn xanh: hình chen hoặc điểm chuyển;
- chữ hồng: cảm xúc hoặc hành động cần chú ý;
- highlight vàng: ý quan trọng từ kịch bản;
- “không hình”: không tạo minh họa cho vùng đó.

Frame xanh là `contentFrame` của nội dung chính. Output có thể dùng canvas mở
rộng nếu phần mở rộng chỉ chứa nền phụ liên tục để mask/hòa trong InDesign.
Frame oval/tròn vẫn nhận output chữ nhật đầy đủ.

Tỷ lệ in tham chiếu của tập: `286 × 203 mm`. Khi layout QA yêu cầu print-safe,
dùng tỷ lệ chuẩn hóa:

```json
{
  "trimPercent": { "x": 0.0104895, "y": 0.0147783 },
  "criticalSafePercent": { "x": 0.027972, "y": 0.0394089 }
}
```

Không áp trực tiếp số mm hoặc pixel này lên canvas có kích thước khác.

## Profile và asset

- Profile nhân vật nằm trong `characters/` và là nguồn identity chính.
- Không mượn khuôn mặt, tóc, khăn, màu y phục, trang sức hoặc silhouette đặc
  trưng của Nalini, Visakha, Punna hay nhân vật chính khác cho nhân vật phụ.
- Nhân vật phụ lặp lại và cần nhận diện phải có profile riêng trước khi tạo hàng
  loạt shot.
- Tập này hiện chưa có `style_refs/approved/` hoặc `style_refs/rejected/`; không
  coi output chưa được người dùng duyệt là style reference.

## Tổ chức output

- Output của một page nằm trong `Part <n>/pages/page-XXX/outputs/`.
- Bản được chốt nằm trong `Part <n>/pages/page-XXX/approved/`.
- QA artifact nằm trong thư mục `qa/` tương ứng.
- Không mặc định dùng manifest, script hoặc output của Part 1 cho Part 2.

## Ngoại lệ hiện tại

Không có ngoại lệ cấp tập đối với khóa thuần 2D. Yêu cầu trực tiếp của người
dùng đối với một deliverable, ví dụ “không cần tránh gáy”, được ghi
`SKIPPED_BY_USER` trong đúng phạm vi và ưu tiên hơn mặc định của skill.

- Áp dụng ngoại lệ toàn project trong `../AGENTS.md`: `SKIPPED_BY_USER` đối với
  việc cấm tuyệt đối nền trời mềm. Nền trời được phép chuyển màu mềm nhẹ, tiết
  chế; nhân vật và vật thể vẫn giữ line art rõ, flat fills và 1–2 cấp hard
  cel-shading. Xác nhận trực tiếp của người dùng ngày 2026-10-02.
