# Style TTPQ Comic hiện hành

Mặc định dùng **[ttpq comic light](../../docs/style-ttpq-comic-light.md)**;
riêng lượt màu mặc định [ttpq comic blend](ttpq-comic-blend.md) từ 2026-11-16;
`color-edit` và lượt màu có `--recast` mặc định [ttpq real](ttpq-real.md) từ 2026-11-22.
Riêng flow này có thêm style tùy chọn **[ttpq comic soft](ttpq-comic-soft.md)**
(ánh sáng có hướng, bóng mềm, gradient nhẹ, nền có chiều sâu), chỉ dùng khi
người dùng gọi tên cho lượt hoặc spread đang làm (`build-prompt.py --style soft`),
và style test **[ttpq comic blend](ttpq-comic-blend.md)** (50% comic + 25% flat +
25% nền storybook, `--style blend`). Khối STYLE và LINE ART STAGE của soft và
blend nằm trong file riêng của từng style. Màu y và cách
quấn y theo profile và ảnh ref của từng nhân vật, không áp `docs/monastic-robes.md`.

Với light, cả hai lượt đều chép nguyên khối định nghĩa chuẩn trong tài liệu trên, để sửa
style chỉ phải sửa một chỗ:

- Lượt màu: chép nguyên khối.
- Lượt nét: chép nguyên khối nhưng bỏ đoạn `Color:`, vì lượt này chưa tô màu.
  Sau đó thêm khối điều chỉnh LINE ART STAGE bên dưới.

Khối điều chỉnh chỉ nói cách áp style ở bước nét: mật độ nét, tóc, nếp y, nền,
tỷ lệ người thật và yêu cầu kỹ thuật cho lượt màu. Viết bằng câu khẳng định; không
lặp lại định nghĩa chuẩn. `build-prompt.py` chép khối này nguyên văn; sửa khối
này là sửa mọi prompt lượt nét.

## Khối LINE ART STAGE (light)

```text
"ttpq comic light" LINE ART STAGE: draw only the black line art of the style above; color and cel shading come in the next stage. Most of the line work goes to the characters. Robes have about 6 to 10 main simplified folds. Hair, beards and moustaches are outlined masses left white, with a few flow lines. Background is a few large simple shapes: a cliff or rock is a few contour lines with few cracks, a tree is one crown shape with a few leaf clusters, ground is a few lines, sky is empty white; lines get fewer and thinner toward the distance. Realistic human proportions: heads in natural size relative to the body, normal-sized eyes and adult facial bone structure. An average adult stands about 7 to 7.5 heads tall; a character whose line gives another height or build (for example taller, shorter, heavier or slighter) follows that line; children and elders have age-accurate proportions. All figures stand on one consistent ground plane seen from one eye level: a figure's size follows where its feet touch the ground, so people at the same distance are the same size, and size decreases smoothly with distance, with no sudden jumps between neighboring figures or groups. Lines are pure black on plain white, with closed contours on characters and key props for coloring; no gray, no tone, no fill.
```
