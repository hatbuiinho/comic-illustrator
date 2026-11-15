# Mẫu profile nhân vật

Lưu tại `ttpq-comic/characters/<slug>/profile.md`. Viết từ ảnh ref đã xem trực
tiếp; chỉ mô tả điều thấy được hoặc người dùng cung cấp, không đoán. Ảnh ref
được đính kèm khi chạy prompt; `build-prompt.py` đọc 3 trường `Tên trong prompt`,
`Ref prompt`, `Dòng prompt`. Phần mô tả còn lại dùng để duyệt.

~~~markdown
# <Tên nhân vật>

- Trạng thái: DRAFT | APPROVED
- Version mô tả: v001
- Ảnh ref: ref-v001.png
- Tên trong prompt: <tên tiếng Anh dùng trong prompt, ví dụ Punna, the monks>
- Ref prompt: <ảnh ref mặc định đính kèm, ví dụ ref-v001.png>
- Dòng prompt: <12–15 từ tiếng Anh: tuổi/vai và 2–3 dấu hiệu bắt buộc; không tả tư thế>
- Vai trò trong truyện: <ví dụ: tỳ kheo, thợ xây, thầy thuốc>

## Mô tả (tiếng Việt, để duyệt)

- **Tuổi, giới:**
- **Vóc dáng, tỉ lệ:** chiều cao tương đối, gầy/đầy đặn, tư thế quen.
- **Khuôn mặt:** hình mặt, gò má, độ đầy má, hàm/cằm, mắt, mày, mũi, môi.
- **Da:** tông màu.
- **Tóc/râu:** kiểu, độ dài, màu (hoặc đầu cạo).
- **Trang phục:** từng lớp, màu, chất liệu, cách quấn.
- **Phụ kiện/trang sức, đạo cụ:**
- **Biểu cảm/thần thái mặc định:**

## Dấu hiệu bắt buộc

2–4 đặc điểm phải luôn có để nhận ra nhân vật.

## Không được nhầm

Đặc điểm dễ lẫn với nhân vật khác hoặc dễ bị vẽ sai (tuổi, màu y, phụ kiện).

## Lịch sử

| Version | Ngày | Thay đổi | Người duyệt |
| --- | --- | --- | --- |
~~~
