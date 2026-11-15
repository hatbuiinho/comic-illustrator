# ttpq comic blend

Style tùy chọn để test, chỉ dùng trong flow TTPQ Comic, do người dùng yêu cầu
ngày 2026-11-15. Chạy song song với `ttpq comic light` và `ttpq comic soft`;
**mặc định vẫn là light**. Chỉ dùng blend khi người dùng gọi tên style này cho
lượt hoặc spread đang làm.

Hướng: đứng chính giữa light và soft. Nhân vật vẫn là comic sạch nét, mảng
màu phẳng với cel-shading mép hơi dịu; tiền cảnh giữ mảng phẳng, trung cảnh
là mảng phẳng có chuyển sắc dịu, viễn cảnh và trời được vẽ dịu kiểu sách
truyện để cảnh có chiều sâu không khí. Cập nhật tỷ lệ ngày 2026-11-15: 50%
comic + 25% flat + 25% nền storybook.

## So với light và soft

| Khía cạnh | light | blend | soft |
| --- | --- | --- | --- |
| Pha trộn | 50% comic + 50% flat | 50% comic + 25% flat + 25% nền storybook | 60% comic + 40% nền storybook |
| Tô bóng | 2–3 tông cel, ranh giới rõ | 2–3 tông cel, mép hơi dịu | 3–4 tông, mép chuyển mềm |
| Gradient | Cấm gradient quá mức | Gradient nhẹ ở trời và viễn cảnh, rất nhẹ ở mảng lớn trung cảnh; không trên nhân vật | Gradient nhẹ cho trời, mảng đá/đất lớn, nếp y |
| Ánh sáng | Ấm dịu, phẳng | Ấm dịu, có hướng nhẹ | Nguồn sáng có hướng, viền sáng nhẹ |
| Nền | Vài mảng phẳng đơn giản | Tiền cảnh mảng phẳng; trung cảnh phẳng chuyển sắc dịu; viễn cảnh vẽ dịu, nhạt dần | Chi tiết vừa, phối cảnh không khí, texture giấy tiết chế |

## Khối STYLE (lượt màu chép nguyên; lượt nét bỏ đoạn `Color and light:`)

```text
Style name: ttpq comic blend.

Core mix: 50% Refined 2D Comic Illustration + 25% Flat Illustration + 25% Soft Storybook Background Painting, unified by Refined Hand-Drawn Line Art and Soft Cel Shading. Strictly 2D throughout.

Line art: precise, clean, confident hand-drawn outlines in black or very dark brown with natural line weight variation; slightly thicker outer contours on characters, fine facial, hand, and fabric interior lines; background lines thinner and sparser toward the distance; no cross-hatching on skin.

Characters: believable anatomy, individual expressive faces, accurate natural proportions, and culturally appropriate South Asian features where applicable; beautiful but not excessively idealized.

Color and light: clean solid flat color shapes for characters, clothing, and foreground, with harmonious, gently muted rich colors and natural skin tones; soft warm light with a gentle direction suited to the scene; 2–3 controlled cel-shading tones on skin and clothing with slightly softened edges; subtle gradients on the sky and distant background layers, only very subtle color transitions on large middle-ground masses, never on characters.

Background: foreground in simple flat color planes with selective detail; middle ground in flat color planes with gentle color transitions; distance painted in a soft, gouache-like storybook manner with layered atmospheric perspective, where far forms become lighter, cooler, and less detailed; restrained paper-like surface texture; characters stay crisper than the background.

Details: elegant simplified clothing folds, clear hair masses, crisp character silhouettes against the background.

Composition: cinematic visual storytelling, clean hierarchy, and sophisticated integrated editorial/book illustration, including safe gutters and calm, low-detail areas behind text when laying out spreads.

Exclusions: no anime, 3D/CGI, photorealism, glossy airbrushed skin, painterly brush texture on characters, heavy cross-hatching, excessive gradients, crude black shading, neon colors, strong bloom or glow.
```

## Khối LINE ART STAGE (blend)

Thay khối LINE ART STAGE của light khi lượt nét dùng blend. Nền giữ đơn giản
như light ở tiền/trung cảnh, thêm một lớp viễn cảnh nhẹ để lượt màu dựng
chiều sâu.

```text
"ttpq comic blend" LINE ART STAGE: draw only the black line art of the style above; color and cel shading come in the next stage. Most of the line work goes to the characters. Robes have about 6 to 10 main simplified folds. Hair, beards and moustaches are outlined masses left white, with a few flow lines. Background is simple in clear depth layers: the foreground is a few large simple shapes (a cliff or rock is a few contour lines with few cracks, a tree is one crown shape with a few leaf clusters, ground is a few lines), the middle ground has the main shapes of rocks, trees and buildings with a little more detail, and the distance is a few light outlines of hills or trees; sky is empty white; lines get fewer and thinner toward the distance, and areas behind text stay calm with few lines. Realistic human proportions: heads in natural size relative to the body, normal-sized eyes and adult facial bone structure. An average adult stands about 7 to 7.5 heads tall; a character whose line gives another height or build (for example taller, shorter, heavier or slighter) follows that line; children and elders have age-accurate proportions. Lines are pure black on plain white, with closed contours on characters and key props for coloring; no gray, no tone, no fill.
```

## Áp dụng

- Gọi bằng `build-prompt.py --style blend` cho cả lượt nét, màu và chỉnh;
  không ghi `--style` thì là light.
- Lượt màu blend có thể tô từ outline light hoặc soft đã chọn; không bắt buộc
  vẽ lại nét.
- Ánh sáng theo cảnh (`Thời điểm/ánh sáng` hoặc `--light`); cảnh đêm vẫn là
  đêm, gradient không đổi màu nhận diện nhân vật hay màu y theo profile.
- QA theo định nghĩa blend: nhân vật và tiền cảnh phải đọc là mảng phẳng có
  cel-shading mép hơi dịu; trung cảnh vẫn đọc là mảng phẳng, chỉ chuyển sắc
  rất nhẹ; viễn cảnh và trời được vẽ dịu, có gradient nhẹ; không có gradient
  trên nhân vật.
- Ghi `Style: ttpq comic blend` trong `record.md` cho lượt dùng blend.
- Đây là style test; sửa style blend chỉ sửa file này, script đọc hai khối
  `text` theo thứ tự trên.
