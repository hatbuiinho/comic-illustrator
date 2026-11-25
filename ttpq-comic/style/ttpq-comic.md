# Style TTPQ Comic hiện hành

Mặc định dùng **[ttpq comic blend](../../docs/style-ttpq-comic-blend.md)**
(50% comic + 25% flat + 25% nền storybook), style chung của toàn project từ
2026-11-25, kể cả lượt màu có `--recast`. Style test
[ttpq real](ttpq-real.md) và [ttpq storybook](ttpq-storybook.md) chỉ dùng cho
lượt màu khi người dùng gọi tên (`--style real`, `--style storybook`).
`color-edit` và `swap` không gọi tên style: vẽ theo finish của ảnh đang sửa. `ttpq comic light` và `ttpq comic soft` đã bỏ từ
2026-11-25.

Màu y và cách quấn y theo profile và ảnh ref của từng nhân vật, không áp
`docs/monastic-robes.md`.

- Lượt màu: `build-prompt.py` chép nguyên khối STYLE của style đang dùng, để
  sửa style chỉ phải sửa một chỗ.
- Lượt nét và chỉnh outline: không chèn khối STYLE; câu mở chỉ gọi tên
  Semi-Realistic Storybook Illustration (từ 2026-11-22 và 2026-11-24), bỏ qua
  `--style`.
