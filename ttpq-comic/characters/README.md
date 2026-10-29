# Nhân vật

Mỗi nhân vật một thư mục `characters/<slug>/`:

- `ref-vNNN.png` — ảnh ref identity do người dùng chỉ định (chép vào đây).
- `profile.md` — mô tả theo mẫu
  `.agents/skills/ttpq-comic/references/profile-template.md`.

Khi chạy prompt, người dùng đính kèm `ref-vNNN.png` và prompt ghi "Image N =
<tên>"; `profile.md` giữ dòng nhận diện ngắn để nhắc các dấu hiệu bắt buộc.

Chỉ profile có `Trạng thái: APPROVED` được đưa vào prompt.
