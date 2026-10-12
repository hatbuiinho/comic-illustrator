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

Mỗi page trong PDF demo tương ứng một spread hai trang. Khối xanh là
`briefRegion`: vùng gợi ý nội dung/vị trí minh họa, không phải ranh giới cứng và
không mặc định là một frame ảnh độc lập.

Quy ước màu của layout Tập 53 — người dùng làm rõ ngày 2026-10-12:

- chữ màu xanh: nội dung liên quan đến hình ảnh sẽ minh họa, hướng dẫn nội dung sáng tạo;
- khối xanh: brief/vùng chờ minh họa, không phải hard mask;
- hình tròn xanh: hình chen hoặc điểm chuyển;
- chỗ hồng: nội dung của kịch bản viết thêm cần minh họa hình;
- highlight vàng: nội dung của kịch bản gốc cần minh họa hình;
- “không hình”: không tạo minh họa cho vùng đó.

Khi đọc nguồn, trích nội dung được đánh dấu và giữ riêng vai trò của ba màu
chữ/highlight trên. Đây là chỉ dẫn nội dung minh họa, không chỉ là màu nhấn
hoặc tọa độ bố cục. Không rút nội dung hồng thành nhãn “cảm xúc/hành động”
hoặc nội dung vàng thành nhãn “ý quan trọng” rồi bỏ mất yêu cầu minh họa.

Người dùng làm rõ thêm ngày 2026-10-12: diễn giải các đoạn được đánh dấu
thành các ý cần truyền bằng hình, không bám chặt câu chữ hoặc coi mỗi động tác
là một yêu cầu phải tái hiện nguyên văn. Trích nguyên văn để giữ provenance;
sau đó xác định ý nghĩa, quan hệ, cảm nhận và bằng chứng thị giác vừa đủ.
Cho phép chọn khoảnh khắc, phản ứng hoặc hàm ý phù hợp, miễn không đổi dữ kiện
và vẫn giữ hoạt động/bối cảnh cần thiết. Ví dụ “Ông quay sang bác thợ cả” dẫn
tới ý Punna chia sẻ sự quan tâm và tác động đến Nalini, không tự khóa hình vào
đúng khoảnh khắc xoay đầu.

Thiết kế output trên toàn canvas trang/spread. Nhân vật, eye path và chi tiết kể
chuyện được phép vượt `briefRegion` khi không đè vùng chữ, trim, gáy hoặc mask
thật. Background được phép chạy dưới chữ và mở rộng toàn layout; vùng dưới chữ
cần giảm tương phản/mật độ nét để dễ đọc, không bị giới hạn thành nền phụ đơn
điệu. Frame oval/tròn thật vẫn nhận output chữ nhật đầy đủ.

Sau khi người dùng chọn master, mới tách bộ InDesign đồng phiên bản gồm
background clean plate và mid+foreground có alpha, kèm text-wrap path. Không
tách layer cho option hoặc variant chưa được chọn.

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

## Contract chữ–hình cho production

Xác nhận trực tiếp của người dùng ngày 2026-10-08:

- Dùng `TEXT_PROXY_INTEGRATION` trong giai đoạn composition, generation và QA
  artwork của Tập 53.
- Không cần chữ thật hoặc proof exact capacity trước production ảnh; nội dung,
  typography và dàn chữ chính xác thuộc InDesign.
- Proxy text chỉ mô phỏng density, số dòng, nhịp đoạn và visual weight gần
  production; phải là overlay tách khỏi artwork và không được bake vào master.
- Background tiếp tục dưới vùng proxy; cấm tạo white panel hoặc hard text edge
  nếu source không có frame thật.
- Trạng thái capacity trước InDesign là `DEFERRED_TO_INDESIGN`, không phải PASS.
