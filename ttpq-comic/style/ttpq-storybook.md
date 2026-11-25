# ttpq storybook

Style test, chỉ dùng trong flow TTPQ Comic, tạo ngày 2026-11-22. Là nhánh của
[ttpq comic blend](../../docs/style-ttpq-comic-blend.md): thay phần 50% Refined 2D Comic
Illustration bằng 40% Semi-Realistic Storybook Illustration, phần còn lại là
35% Flat Illustration + 25% nền storybook (sửa ngày 2026-11-22).
Chỉ dùng khi người dùng gọi tên
`ttpq storybook` (`--style storybook`); mặc định lượt màu vẫn là blend.

Hướng: nhân vật được vẽ bán tả thực kiểu sách truyện (khối mềm, tô bóng chuyển
dịu, da và vải có độ dày tự nhiên) thay cho mảng cel comic; tiền cảnh và trung
cảnh là mảng màu phẳng, viễn cảnh và trời vẽ dịu kiểu gouache storybook với
gradient nhẹ, lớp xa nhạt và lạnh dần, texture giấy tiết chế. Các mục ánh sáng theo cảnh, dải
sáng tối, nét ngả màu, tỷ lệ người thật giữ như blend.

## So với blend

| Khía cạnh | blend | storybook |
| --- | --- | --- |
| Pha trộn | 50% comic + 25% flat + 25% nền storybook | 40% semi-realistic storybook + 35% flat + 25% nền storybook |
| Tô nhân vật | Mảng phẳng, 2–3 tông cel mép hơi dịu, không gradient | Khối mềm bán tả thực, 3–4 tông chuyển dịu trên da và y, không bóng bẩy |
| Nét (ảnh màu) | Viền nâu rất đậm gần đen, nét trong ngả màu | Giữ như blend, nét trong có thể chìm nhẹ hơn vào khối |
| Nền | Tiền/trung cảnh phẳng, viễn cảnh vẽ dịu | Tiền và trung cảnh mảng phẳng sạch; viễn cảnh và trời vẽ dịu kiểu gouache, gradient nhẹ; texture giấy tiết chế chỉ ở nền |
| Ánh sáng, sáng tối | Theo cảnh, đủ dải sáng – trung – tối | Giữ như blend |

## Khối STYLE (lượt màu chép nguyên)

```text
Style name: ttpq storybook.

Core mix: 40% Semi-Realistic Storybook Illustration + 35% Flat Illustration + 25% Soft Storybook Background Painting, unified by Refined Hand-Drawn Line Art and Soft Shading. Strictly 2D throughout.

Line art: precise, clean, confident hand-drawn lines, medium-light weight, clearly readable but not bold; in the finished color illustration, outer contours of characters are a very dark warm brown close to black, never heavy pure black, and slightly thicker than interior lines; fine facial, hand, hair and fabric interior lines are color-tinted, a clearly darker shade of the color area they sit on (deep dark reddish brown on skin and robes, dark green on foliage), and may sink slightly into the modeled forms; background lines are thinner and color-tinted but still visible, fading toward the distance; no cross-hatching on skin.

Characters: semi-realistic storybook rendering with believable anatomy, gently modeled three-dimensional forms, individual expressive faces, realistic adult proportions with an average adult about 7 to 7.5 heads tall, heads in natural size relative to the body, normal-sized eyes and adult facial bone structure (children and elders age-accurate), and culturally appropriate South Asian features where applicable; beautiful but not excessively idealized.

Color and light: characters painted with soft volume in 3–4 smoothly blended shading tones on skin and clothing, natural matte skin with subtle warmth in cheeks, ears and hands, and cloth with gentle fold volume, the darkest tone clearly darker than the base color; foreground, middle ground and props in clean solid flat color shapes, with harmonious, gently muted rich colors; soft natural light with a clear direction, its color temperature set by the scene's time and setting (warm only for early morning, late afternoon, firelight or lamplight; neutral for full daylight; cooler in deep shade, overcast and night), so every form has a lit side and a shadow side; subtle gradients only in the distance and sky; all line work is recolored into very dark warm brown contours and clearly darker color-tinted interior lines, with no heavy pure black outlines and no thick uniform contours.

Value and contrast: a full value range from bright highlights through mid tones to deep shadow, organized into a few large clear value groups rather than an even mid-tone spread; characters and grounded props cast clear soft-edged shadows on the ground and nearby surfaces; shadow sides of cliffs, rocks, tree trunks and buildings, deep spaces such as ravine floors, caves, doorways and forest interiors, and areas under canopies are rich deep colored shadows (cool, deep but never pure black); each focal character reads by value against the area behind it, lit against shadow or dark against light, never the same value as its background; far distance and sky stay lighter for atmospheric depth; areas behind text stay light and calm.

Background: foreground and middle ground in clean flat color planes with selective detail; distance painted in a soft, gouache-like storybook manner with layered atmospheric perspective, where far forms become lighter, cooler and less detailed; restrained paper-like surface texture in the background only; characters stay more detailed and crisper than the background.

Details: elegant naturally draped clothing folds with soft volume, clear hair masses with a few soft strands, crisp character silhouettes against the background.

Composition: cinematic visual storytelling, clean hierarchy, and sophisticated integrated editorial/book illustration, including safe gutters and calm, low-detail areas behind text when laying out spreads.

Exclusions: no anime, 3D/CGI, photorealism, glossy airbrushed skin, heavy impasto or rough visible brush strokes, painterly brush texture on characters, heavy cross-hatching, excessive gradients, crude black shading, neon colors, strong bloom or glow, chibi or cartoon proportions, oversized heads or eyes, rounded baby faces, simplified cartoon figures.
```

## Áp dụng

- Gọi bằng `build-prompt.py --pass color --style storybook`; `color-edit` và
  `swap` sửa ảnh storybook theo finish của ảnh, không cần ghi style. Lượt nét không đổi (đã chỉ gọi tên
  Semi-Realistic Storybook Illustration ở câu mở), nên file này không có khối
  LINE ART STAGE; tô từ outline đã chọn như blend.
- Ánh sáng theo cảnh, dải sáng tối, nét ngả màu, tỷ lệ người thật, `--effect`:
  áp dụng và QA như blend.
- QA riêng: nhân vật đọc là khối mềm bán tả thực, không phải mảng cel phẳng;
  không thành ảnh chụp, 3D hay da bóng airbrush; tiền và trung cảnh là mảng
  phẳng, chỉ viễn cảnh và trời vẽ dịu kiểu gouache có gradient nhẹ; texture
  giấy tiết chế, không lên nhân vật; nhân vật vẫn chi tiết và sắc hơn nền.
- Ghi `Style: ttpq storybook` trong `record.md`.
- Đây là style test; sửa chỉ sửa file này, script đọc khối `text` đầu tiên.
