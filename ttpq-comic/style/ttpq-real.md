# ttpq real

Style test, chỉ dùng trong flow TTPQ Comic, tạo ngày 2026-11-22. Là nhánh của
[ttpq comic blend](../../docs/style-ttpq-comic-blend.md): thay phần 50% Refined 2D Comic
Illustration bằng 50% Semi-Realistic Comic Illustration, giữ 25% Flat
Illustration + 25% nền storybook. Từ 2026-11-22 tới 2026-11-24 là mặc định
của `color-edit` và lượt màu có `--recast`; từ 2026-11-25 chỉ dùng khi người
dùng gọi tên `ttpq real` (`--style real`) cho lượt màu.

Hướng: nhân vật vẫn là comic có nét rõ và tô bóng theo mảng, nhưng giải phẫu,
xương mặt, cơ tay, nếp vải được dựng sát người thật hơn; tô bóng 3 tông cel
có khối rõ, mép bóng chính sắc, chuyển tiếp phụ dịu. Nền giữ như blend: tiền
cảnh phẳng, trung cảnh phẳng chuyển sắc dịu, viễn cảnh và trời vẽ dịu kiểu
storybook. Ánh sáng theo cảnh, dải sáng tối, nét ngả màu, tỷ lệ người thật
giữ như blend.

## So với blend

| Khía cạnh | blend | real |
| --- | --- | --- |
| Pha trộn | 50% comic + 25% flat + 25% nền storybook | 50% semi-realistic comic + 25% flat + 25% nền storybook |
| Dựng hình nhân vật | Comic tinh gọn, giải phẫu đáng tin | Giải phẫu và xương mặt sát người thật hơn: gò má, hốc mắt, sống mũi, khớp tay, gân cổ đọc được |
| Tô nhân vật | Mảng phẳng, 2–3 tông cel mép hơi dịu, không gradient | 3 tông cel dựng khối rõ, mép bóng chính sắc, chuyển tiếp phụ dịu; vẫn không gradient trơn, không da bóng |
| Nét (ảnh màu) | Viền nâu rất đậm gần đen, nét trong ngả màu | Giữ như blend; nét trong ít hơn, khối do bóng gánh nhiều hơn |
| Nếp y | 6–10 nếp giản lược | Nếp rủ theo trọng lượng vải, có khối, vẫn chọn lọc |
| Nền, ánh sáng, sáng tối | Như định nghĩa blend | Giữ như blend |

## Khối STYLE (lượt màu chép nguyên)

```text
Style name: ttpq real.

Core mix: 50% Semi-Realistic Comic Illustration + 25% Flat Illustration + 25% Soft Storybook Background Painting, unified by Refined Hand-Drawn Line Art and Cel Shading. Strictly 2D throughout.

Line art: precise, clean, confident hand-drawn lines, medium-light weight, clearly readable but not bold; in the finished color illustration, outer contours of characters are a very dark warm brown close to black, never heavy pure black, and slightly thicker than interior lines; interior lines are fewer and selective, letting shading carry the form, and are color-tinted, a clearly darker shade of the color area they sit on (deep dark reddish brown on skin and robes, dark green on foliage); background lines are thinner and color-tinted but still visible, fading toward the distance; no cross-hatching on skin.

Characters: semi-realistic comic drawing with accurate anatomy and real adult bone structure: readable cheekbones, brow ridge, eye sockets, nose bridge, jaw, neck tendons, knuckles and wrist joints; individual expressive faces with natural, non-stylized features; realistic adult proportions with an average adult about 7 to 7.5 heads tall, heads in natural size relative to the body, normal-sized eyes (children and elders age-accurate), and culturally appropriate South Asian features where applicable; beautiful but not idealized, like real people drawn by a comic artist.

Color and light: characters, clothing and foreground in clean color shapes with harmonious, gently muted rich colors and natural matte skin tones; soft natural light with a clear direction, its color temperature set by the scene's time and setting (warm only for early morning, late afternoon, firelight or lamplight; neutral for full daylight; cooler in deep shade, overcast and night), so every form has a lit side and a shadow side; 3 controlled cel-shading tones on skin and clothing that model the form clearly, with a crisp main shadow edge and gently softened secondary transitions, the darkest tone clearly darker than the base color; subtle gradients on the sky and distant background layers, only very subtle color transitions on large middle-ground masses, never smooth airbrushed gradients on characters; all line work is recolored into very dark warm brown contours and clearly darker color-tinted interior lines, with no heavy pure black outlines and no thick uniform contours.

Value and contrast: a full value range from bright highlights through mid tones to deep shadow, organized into a few large clear value groups rather than an even mid-tone spread; characters and grounded props cast clear soft-edged shadows on the ground and nearby surfaces; shadow sides of cliffs, rocks, tree trunks and buildings, deep spaces such as ravine floors, caves, doorways and forest interiors, and areas under canopies are rich deep colored shadows (cool, deep but never pure black); each focal character reads by value against the area behind it, lit against shadow or dark against light, never the same value as its background; far distance and sky stay lighter for atmospheric depth; areas behind text stay light and calm.

Background: foreground in simple flat color planes with selective detail; middle ground in flat color planes with gentle color transitions; distance painted in a soft, gouache-like storybook manner with layered atmospheric perspective, where far forms become lighter, cooler, and less detailed; restrained paper-like surface texture; characters stay crisper and more detailed than the background.

Details: naturally draped clothing folds that follow the weight of the cloth, with clear volume but still selective; clear hair masses with a few defined strands; crisp character silhouettes against the background.

Composition: cinematic visual storytelling, clean hierarchy, and sophisticated integrated editorial/book illustration, including safe gutters and calm, low-detail areas behind text when laying out spreads.

Exclusions: no anime, 3D/CGI, photorealism, glossy airbrushed skin, painterly brush texture on characters, heavy cross-hatching, excessive gradients, crude black shading, neon colors, strong bloom or glow, chibi or cartoon proportions, oversized heads or eyes, rounded baby faces, simplified cartoon figures.
```

## Áp dụng

- Gọi bằng `--pass color --style real` (kể cả khi có `--recast`). Sửa ảnh đã
  tô real bằng `color-edit` hoặc `swap` thì không cần ghi style: hai lượt này
  theo finish của ảnh đang sửa. Lượt nét không đổi, nên file này không có khối LINE ART
  STAGE; tô từ outline đã chọn như blend.
- Ánh sáng theo cảnh, dải sáng tối, nét ngả màu, tỷ lệ người thật, `--effect`:
  áp dụng và QA như blend.
- QA riêng: nhân vật đọc là comic bán tả thực (xương mặt, khớp tay, nếp vải có
  khối) với 3 tông cel mép chính sắc; không thành ảnh chụp, 3D, tranh sơn dầu
  hay da bóng airbrush; không trôi về khối mềm kiểu `ttpq storybook`; nền vẫn
  như blend; nhân vật vẫn sắc và chi tiết hơn nền.
- Ghi `Style: ttpq real` trong `record.md`.
- Đây là style test; sửa chỉ sửa file này, script đọc khối `text` đầu tiên.
