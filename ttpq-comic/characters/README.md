# Nhân vật

Mỗi nhân vật một thư mục `characters/<slug>/`:

- `ref-vNNN.png` — ảnh ref identity do người dùng chỉ định (chép vào đây).
- `profile.md` — mô tả theo mẫu
  `.agents/skills/ttpq-comic/references/profile-template.md`.

`build-prompt.py` đọc 3 trường `Tên trong prompt`, `Ref prompt`, `Dòng prompt`
trong `profile.md` và tự ghi "Image N = <tên>: <dòng prompt>" theo dòng
**Profile:** của cảnh trong `scenes.md`. Mục "Dòng nhận diện" cũ chỉ để tham khảo.

Chỉ profile có `Trạng thái: APPROVED` được đưa vào prompt.
