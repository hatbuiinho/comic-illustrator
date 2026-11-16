# ttpq comic soft

Style tùy chọn, chỉ dùng trong flow TTPQ Comic, do người dùng chốt ngày
2026-11-15. Chạy song song với `ttpq comic light`; mặc định là light cho lượt
nét và blend cho lượt màu.
Chỉ dùng soft khi người dùng gọi tên style này cho lượt hoặc spread đang làm.

Hướng: giữ nhân vật comic sạch nét như light, nhưng thêm ánh sáng có hướng,
bóng mềm và gradient nhẹ, nền kiểu sách truyện có chiều sâu không khí để
tranh có sức sống hơn.

## So với ttpq comic light

| Khía cạnh | light | soft |
| --- | --- | --- |
| Pha trộn | 50% comic + 50% flat | 60% comic + 40% nền vẽ dịu kiểu sách truyện |
| Tô bóng | 2–3 tông cel, ranh giới rõ | 3–4 tông, mép chuyển mềm |
| Gradient | Cấm gradient quá mức | Gradient nhẹ cho ánh sáng, trời, mảng đá/đất lớn, nếp y |
| Ánh sáng | Ấm dịu, phẳng | Nguồn sáng có hướng, viền sáng nhẹ |
| Nền | Vài mảng phẳng đơn giản | Chi tiết vừa, phối cảnh không khí, texture giấy tiết chế |

## Khối STYLE (lượt màu chép nguyên; lượt nét bỏ đoạn `Color and light:`)

```text
Style name: ttpq comic soft.

Core mix: 60% Refined 2D Comic Illustration for characters + 40% Soft Storybook Background Painting, unified by Refined Hand-Drawn Line Art and Soft Shading. Strictly 2D throughout.

Line art: precise, clean, confident hand-drawn outlines in black or very dark brown with natural line weight variation; slightly thicker outer contours on characters, fine facial, hand, and fabric interior lines; background lines thinner and sparser, fading toward the distance; no cross-hatching on skin.

Characters: believable anatomy, individual expressive faces, accurate natural proportions, and culturally appropriate South Asian features where applicable; beautiful but not excessively idealized.

Color and light: natural harmonious palette with gently muted earth tones and natural skin tones; a clear, soft directional light source suited to the scene; 3–4 soft shading tones on skin and clothing with gently blended edges; subtle light gradients on skies, large rock and ground surfaces, and robe folds; soft rim light on figures where the light allows.

Background: selectively detailed landscape and architecture painted in a soft gouache-like storybook manner; layered atmospheric perspective where distant forms become lighter, cooler, and less detailed; restrained paper-like surface texture; foreground and characters stay crisper than the background.

Details: elegant simplified clothing folds with soft volume, clear hair masses, crisp character silhouettes against the background.

Composition: cinematic visual storytelling, clean hierarchy, and sophisticated integrated editorial/book illustration, including safe gutters and calm, low-detail areas behind text when laying out spreads.

Exclusions: no anime, 3D/CGI, photorealism, glossy airbrushed skin, heavy impasto or rough visible brush strokes, heavy cross-hatching, crude black shading, neon colors, strong bloom or glow.
```

## Khối LINE ART STAGE (soft)

Thay khối LINE ART STAGE của light khi lượt nét dùng soft. Nền được chi tiết
hơn light một bậc để lượt màu có chỗ dựng chiều sâu.

```text
"ttpq comic soft" LINE ART STAGE: draw only the black line art of the style above; color, light and soft shading come in the next stage. Most of the line work goes to the characters. Robes have about 6 to 10 main simplified folds with soft volume. Hair, beards and moustaches are outlined masses left white, with a few flow lines. Background is moderately detailed in clear depth layers (foreground, middle ground, distance): rocks and cliffs have their main planes and a few cracks, trees have a crown shape with several leaf clusters, ground has a few lines and stones, sky is empty white; lines get fewer and thinner toward the distance, and areas behind text stay calm with few lines. Realistic human proportions: heads in natural size relative to the body, normal-sized eyes and adult facial bone structure. An average adult stands about 7 to 7.5 heads tall; a character whose line gives another height or build (for example taller, shorter, heavier or slighter) follows that line; children and elders have age-accurate proportions. Lines are pure black on plain white, with closed contours on characters and key props for coloring; no gray, no tone, no fill.
```

## Áp dụng

- Gọi bằng `build-prompt.py --style soft` cho cả lượt nét, màu và chỉnh; không
  ghi `--style` thì là light.
- Lượt màu soft có thể tô từ outline light đã chọn; không bắt buộc vẽ lại nét.
- Ánh sáng theo cảnh (`Thời điểm/ánh sáng` hoặc `--light`); cảnh đêm vẫn là
  đêm, gradient không đổi màu nhận diện nhân vật hay màu y theo profile.
- Ghi `Style: ttpq comic soft` trong `record.md` cho lượt dùng soft.
- Sửa style soft chỉ sửa file này; script đọc hai khối `text` theo thứ tự trên.
