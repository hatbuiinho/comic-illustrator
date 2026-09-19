# Comparison card — page10-option1-visakha-stone-gesture

## Composition card đã duyệt

`page10-option1-visakha-stone-gesture.svg`

- Medium two-shot, slight high angle.
- Nalini trái, Visakha phải; Visakha hướng tay về đá.
- Eye path: Visakha → đá → Nalini.
- Output là hình chữ nhật để layout mask vào hình tròn.

## Output v2

`Tap 53/Part 1/pages/page-010/outputs/part1-page10-option1-visakha-stone-gesture-v2.png`

## Output đặt trong layout

`Tap 53/Part 1/qa/part1-spread10-restart-option1-visakha-stone-gesture-overlay.svg`

## Visual delta QA

- Camera: giữ medium two-shot, hơi cao — PASS.
- Focus: Visakha chỉ về đá, Nalini tiếp nhận — PASS.
- Profile: turban/trang phục Nalini và sari/veil Visakha khớp profile — PASS.
- Background: đá rời, xe bò gạch chưa bốc, đất công trường — PASS.
- Timeline: không có công trình hoàn thiện hay nhân vật scene sau — PASS.
- Style: line art 2D, mảng màu phẳng/cel shading; không CGI/photoreal — PASS.
- Layout: tỷ lệ output 1.103:1, frame 1.103:1; lệch 0.17% — PASS.

## Output v3 — đạt trước khi khóa readability

`Tap 53/Part 1/pages/page-010/outputs/part1-page10-option1-visakha-stone-gesture-v3.png`

- Layout: cột nền trống ở giữa, hai nhân vật tách khỏi gáy — PASS.
- Emotion: Nalini ánh mắt mềm, thân hơi hướng về Visakha, không chống cằm — PASS.
- Style/profile/context: PASS.

V3 đạt QA kỹ thuật và visual/storyboard QA, nhưng bị thay thế khi flow bổ sung
Frame Readability Lock vì cỡ frame nhỏ không phù hợp với bán toàn thân.

## Output v4 — loại

`Tap 53/Part 1/pages/page-010/outputs/part1-page10-option1-visakha-stone-gesture-v4.png`

- Cỡ nhân vật đã lớn hơn, nhưng tay/bản vẽ Nalini chạm mép trái mask — FAIL safe margin.

## Output v5 — ứng viên bàn giao

`Tap 53/Part 1/pages/page-010/outputs/part1-page10-option1-visakha-stone-gesture-v5.png`

- Readability: medium close-up hai người bán thân; mắt Nalini, tay chỉ Visakha và đá đọc được ở frame nhỏ — PASS.
- Gáy: khoảng trống dọc giữa hai nhân vật, không đặt mặt/tay/đá quan trọng vào spine — PASS.
- Focus/emotion: Visakha chân thành → Nalini lắng nghe, không full-body/establishing — PASS.
- Style/profile/context: line art thuần 2D, profile đúng, công trường đúng giai đoạn — PASS.
- Layout: tỷ lệ output 1.103:1, frame 1.103:1; lệch 0.01% — PASS.

Kết luận: output v5 đạt QA kỹ thuật và visual/storyboard QA; v2, v3, v4 không còn là ứng viên chính.
