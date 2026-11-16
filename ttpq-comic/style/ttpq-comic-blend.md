# ttpq comic blend

Style chỉ dùng trong flow TTPQ Comic, tạo ngày 2026-11-15. Từ 2026-11-16 là
**style mặc định của lượt màu** (kể cả `color-edit`); lượt nét và chỉnh outline
vẫn mặc định light. Lượt màu dùng light hoặc soft khi người dùng gọi tên.

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
| Nét (ảnh màu) | Đen, rõ | Viền nhân vật nâu rất đậm gần đen, nét vừa; nét trong và nét nền tô ngả theo màu mảng, đậm hơn mảng rõ | Đen hoặc nâu rất đậm |
| Ánh sáng | Ấm dịu, phẳng | Tự nhiên theo cảnh, có hướng rõ; mặt khuất và bóng đổ đọc được | Nguồn sáng có hướng, viền sáng nhẹ |
| Dải sáng tối | Chưa quy định | Đủ sáng – trung – tối; mảng tối lớn ở môi trường, nhân vật tách nền bằng độ sáng | Chưa quy định |
| Nền | Vài mảng phẳng đơn giản | Tiền cảnh mảng phẳng; trung cảnh phẳng chuyển sắc dịu; viễn cảnh vẽ dịu, nhạt dần | Chi tiết vừa, phối cảnh không khí, texture giấy tiết chế |

## Khối STYLE (lượt màu chép nguyên; lượt nét bỏ đoạn `Color and light:` và `Value and contrast:`)

```text
Style name: ttpq comic blend.

Core mix: 50% Refined 2D Comic Illustration + 25% Flat Illustration + 25% Soft Storybook Background Painting, unified by Refined Hand-Drawn Line Art and Soft Cel Shading. Strictly 2D throughout.

Line art: precise, clean, confident hand-drawn lines, medium-light weight, clearly readable but not bold; in the finished color illustration, outer contours of characters are a very dark warm brown close to black, never heavy pure black, and slightly thicker than interior lines; fine facial, hand, hair and fabric interior lines are color-tinted, a clearly darker shade of the color area they sit on (deep dark reddish brown on skin and robes, dark green on foliage); background lines are thinner and color-tinted but still visible, fading toward the distance; no cross-hatching on skin.

Characters: believable anatomy, individual expressive faces, accurate natural proportions, and culturally appropriate South Asian features where applicable; beautiful but not excessively idealized.

Color and light: clean solid flat color shapes for characters, clothing, and foreground, with harmonious, gently muted rich colors and natural skin tones; soft natural light with a clear direction, its color temperature set by the scene's time and setting (warm only for early morning, late afternoon, firelight or lamplight; neutral for full daylight; cooler in deep shade, overcast and night), so every form has a lit side and a shadow side; 2–3 controlled cel-shading tones on skin and clothing with slightly softened edges, the darkest tone clearly darker than the base color; subtle gradients on the sky and distant background layers, only very subtle color transitions on large middle-ground masses, never on characters; all line work is recolored into very dark warm brown contours and clearly darker color-tinted interior lines, with no heavy pure black outlines and no thick uniform contours.

Value and contrast: a full value range from bright highlights through mid tones to deep shadow, organized into a few large clear value groups rather than an even mid-tone spread; characters and grounded props cast clear soft-edged shadows on the ground and nearby surfaces; shadow sides of cliffs, rocks, tree trunks and buildings, deep spaces such as ravine floors, caves, doorways and forest interiors, and areas under canopies are rich deep colored shadows (cool, deep but never pure black); each focal character reads by value against the area behind it, lit against shadow or dark against light, never the same value as its background; far distance and sky stay lighter for atmospheric depth; areas behind text stay light and calm.

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

- Lượt màu và `color-edit` không ghi `--style` là blend. Lượt nét và chỉnh
  outline muốn dùng blend thì ghi `--style blend`; không ghi là light.
- Lượt màu blend có thể tô từ outline light hoặc soft đã chọn; không bắt buộc
  vẽ lại nét.
- Ánh sáng theo cảnh (`Thời điểm/ánh sáng` hoặc `--light`), không mặc định ấm
  (sửa ngày 2026-11-15): ban ngày trung tính, bóng râm/âm u/đêm ngả lạnh, chỉ
  nắng sớm/chiều hoặc ánh lửa đèn mới ấm. QA: ảnh không bị phủ đều một lớp
  vàng cam khi cảnh không phải nắng sớm/chiều. Cảnh đêm vẫn là
  đêm, gradient không đổi màu nhận diện nhân vật hay màu y theo profile.
- QA theo định nghĩa blend: nhân vật và tiền cảnh phải đọc là mảng phẳng có
  cel-shading mép hơi dịu; trung cảnh vẫn đọc là mảng phẳng, chỉ chuyển sắc
  rất nhẹ; viễn cảnh và trời được vẽ dịu, có gradient nhẹ; không có gradient
  trên nhân vật.
- QA dải sáng tối (thêm ngày 2026-11-15 sau góp ý "thiếu contrast"): nhìn
  ảnh thu nhỏ hoặc chuyển xám vẫn thấy rõ hướng sáng, bóng đổ dưới nhân vật,
  mảng tối lớn ở môi trường và nhân vật chính tách khỏi nền bằng độ sáng. Nếu
  toàn ảnh chỉ ở vùng sáng vừa và trung bình thì không đạt. Mảng tối là màu
  sâu, không phải đen tuyền; da và mặt vẫn không đổ bóng đen nặng.
- Nét nhẹ (thêm ngày 2026-11-15, chỉnh đậm lên một chút cùng ngày): lượt nét
  vẫn vẽ đen trên trắng để tô màu; lượt màu tô lại viền nhân vật thành nâu rất
  đậm gần đen, nét vừa; nét trong và nét nền ngả theo màu mảng nhưng đậm hơn
  mảng rõ. QA: viền nhân vật đọc rõ ở ảnh thu nhỏ, nét trong không chìm vào
  màu; không có viền đen đặc nặng hay viền dày đều.
- Ghi `Style: ttpq comic blend` trong `record.md` cho lượt dùng blend.
- Đây là style test; sửa style blend chỉ sửa file này, script đọc hai khối
  `text` theo thứ tự trên.
