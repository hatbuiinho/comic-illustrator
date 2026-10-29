# Decision log Character Studio

Lịch sử quyết định người dùng đã chốt, để truy vết. Rule hiện hành nằm trong
[SKILL.md](../SKILL.md) và các file reference; khi log và rule khác nhau, rule
hiện hành có hiệu lực. Thêm dòng mới ở cuối, không sửa dòng cũ.

| Ngày | Quyết định | Áp dụng tại |
|---|---|---|
| 2026-10-19 | Chọn mẫu quấn y chung `assets/y-quan-chuan-v001.png`. | [monk-standard.md](monk-standard.md) |
| 2026-10-21 | Trang phục nữ che kín bụng/eo ở mọi góc, áp dụng mọi nhân vật nữ. | [SKILL.md](../SKILL.md) mục Trang phục nữ kín đáo |
| 2026-10-21 | Giữ chuyển sắc vùng mắt theo ảnh gốc (từ thử nghiệm Nhân vật nữ test). | [face-and-skin.md](face-and-skin.md) |
| 2026-10-21 | Chốt phương pháp nhánh màu: line art → bảng màu → tô bằng line art + bảng màu + user style. | [line-color-branch.md](line-color-branch.md) |
| 2026-10-21 | Cách tô tóc theo user style 01 là hướng chuẩn; bổ sung user style 02, dùng cả hai. | [line-color-branch.md](line-color-branch.md), [style-user-v001.md](../assets/style-user-v001.md), [style-user-v002.md](../assets/style-user-v002.md) |
| 2026-10-21 | Chọn mẫu line art `assets/line-art-user-v001.png`. | [line-color-branch.md](line-color-branch.md), [line-art-user-v001.md](../assets/line-art-user-v001.md) |
| 2026-10-22 | Workflow mặc định đổi thành chuyển trực tiếp ảnh gốc sang style dự án; nhánh nét/màu chỉ chạy khi được yêu cầu rõ. | [SKILL.md](../SKILL.md) mục Workflow mặc định |
| 2026-10-23 | Chốt prompt 2D mặc định; @ skill kèm ảnh gốc là đủ khởi động chuyển style. Rendering mảng phẳng, da khoảng ba tông, không gradient (override st03 trong Character Studio). | [default-2d-prompt.md](default-2d-prompt.md), [SKILL.md](../SKILL.md) |
| 2026-10-23 | Chọn mẫu màu y `assets/mau-y-chuan-v001.png`; truyền crop chỉ chứa vải `mau-y-chuan-crop-v002.png`. | [monk-standard.md](monk-standard.md), [mau-y-chuan-v001.md](../assets/mau-y-chuan-v001.md) |
| 2026-10-24 | Thêm rule giữ màu môi gốc vào prompt 2D mặc định. | [default-2d-prompt.md](default-2d-prompt.md) |
| 2026-10-24 | Tách SKILL.md thành các file reference; thống nhất khối prompt da/vải/nét mặt theo rendering mảng phẳng; thêm checklist lắp prompt và mục công cụ tạo ảnh. | [SKILL.md](../SKILL.md) |
| 2026-10-24 | Chỉ tạo lại từ ảnh gốc: không dùng output trước làm ảnh đích/ref cho lượt sau, không tự chỉnh trực tiếp trên output (chuỗi edit nối tiếp làm giảm chất lượng). Ngoại lệ: sheet dùng ảnh chuyển style đã duyệt cùng ảnh gốc. | [SKILL.md](../SKILL.md) mục Chỉ tạo lại từ ảnh gốc; docs/studio-contract.md; docs/visual-review-contract.md |
| 2026-10-24 | Copy mọi output của lượt studio (ảnh tạo, crop nguồn, ảnh so sánh QA) vào thư mục output của đúng studio; không để ở cache/tmp/scratchpad, chỉ trình bản trong thư mục đó. | docs/studio-contract.md mục Lưu trữ; [SKILL.md](../SKILL.md) mục Kiểm tra và bàn giao |
| 2026-10-24 | Thu hẹp rule copy output: ảnh so sánh/overlay/zoom chỉ dùng cho QA không cần lưu vào thư mục output của studio. | docs/studio-contract.md mục Lưu trữ; [SKILL.md](../SKILL.md) |
| 2026-10-24 | Khi dựng sheet, tự mở rộng canvas để chứa đủ hình và khoảng trắng giữa các góc; kích thước mặc định không phải trần. Không bóp/rút ngắn/đổi tỷ lệ nhân vật để khớp sheet; prompt và QA phải kiểm điều này. | [sheet-layout.md](sheet-layout.md), [SKILL.md](../SKILL.md) checklist |
| 2026-10-29 | Bỏ toàn bộ QA cũ (kiểm style theo vùng, da ba tông, nét đen từng đoạn, bảng trang sức, zoom từng vùng); thay bằng checklist QA hai tầng theo ttpq comic light. | [qa-checklist.md](qa-checklist.md), [SKILL.md](../SKILL.md), docs/studio-contract.md |
