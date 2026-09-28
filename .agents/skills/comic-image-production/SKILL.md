---
name: comic-image-production
description: Tạo, chỉnh sửa hoặc tạo variant ảnh truyện tranh từ prompt/composition đã chốt, dùng đúng profile và lưu output có version. Không dùng để duyệt hoặc chuyển ảnh vào approved.
---

# Sản xuất ảnh

Trước mỗi lượt tạo/chỉnh có nhân vật, đọc lại profile gốc từ filesystem và
truyền đúng reference trong chính lượt đó. Đọc
[profile-refresh.md](references/profile-refresh.md).

Đọc [reference-selection.md](references/reference-selection.md) để chọn asset.
Khi tạo variant hoặc sửa output, đọc [variant-policy.md](references/variant-policy.md).

Tạo từng shot/variant riêng. Lưu vào đúng `<thu-muc-tap>/.../outputs/` với tên
version mới; không ghi đè. Không dùng ảnh trong `outputs/` làm style reference
mặc định và không coi output trước là nguồn identity.

Sau khi tạo, bàn giao đường dẫn, version và những override đã áp dụng. Không tự
đánh dấu QA PASS và không chuyển file vào `approved/`.
