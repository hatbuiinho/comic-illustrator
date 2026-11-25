# ttpq comic blend

Style mặc định duy nhất của toàn project từ 2026-11-25 (thay hoàn toàn
`ttpq comic light` và `ttpq comic soft`, đã bỏ): minh họa tập/page/frame,
Character Studio, Image Playground và TTPQ Comic. Tạo ngày 2026-11-15 trong
flow TTPQ Comic, là mặc định lượt màu TTPQ Comic từ 2026-11-16.

Hướng: nhân vật là comic sạch nét, mảng màu phẳng với cel-shading mép hơi
dịu; tiền cảnh giữ mảng phẳng, trung cảnh là mảng phẳng có chuyển sắc dịu,
viễn cảnh và trời được vẽ dịu kiểu sách truyện để cảnh có chiều sâu không
khí. Tỷ lệ: 50% comic + 25% flat + 25% nền storybook.

## Đặc điểm chính

| Khía cạnh | blend |
| --- | --- |
| Pha trộn | 50% comic + 25% flat + 25% nền storybook |
| Tô bóng | 2–3 tông cel, mép hơi dịu |
| Gradient | Gradient nhẹ ở trời và viễn cảnh, rất nhẹ ở mảng lớn trung cảnh; không trên nhân vật |
| Nét (ảnh màu) | Viền nhân vật nâu rất đậm gần đen, nét vừa; nét trong và nét nền tô ngả theo màu mảng, đậm hơn mảng rõ |
| Ánh sáng | Tự nhiên theo cảnh, có hướng rõ; mặt khuất và bóng đổ đọc được |
| Dải sáng tối | Đủ sáng – trung – tối; mảng tối lớn ở môi trường, nhân vật tách nền bằng độ sáng |
| Nền | Tiền cảnh mảng phẳng; trung cảnh phẳng chuyển sắc dịu; viễn cảnh vẽ dịu, nhạt dần |

## Khối STYLE (lượt màu chép nguyên; lượt nét bỏ đoạn `Color and light:` và `Value and contrast:`)

```text
Style name: ttpq comic blend.

Core mix: 50% Refined 2D Comic Illustration + 25% Flat Illustration color treatment (flat color shapes only, never flat-design figure proportions) + 25% Soft Storybook Background Painting, unified by Refined Hand-Drawn Line Art and Soft Cel Shading, with realistic adult figures about 7 to 7.5 heads tall. Strictly 2D throughout.

Line art: precise, clean, confident hand-drawn lines, medium-light weight, clearly readable but not bold; in the finished color illustration, outer contours of characters are a very dark warm brown close to black, never heavy pure black, and slightly thicker than interior lines; fine facial, hand, hair and fabric interior lines are color-tinted, a clearly darker shade of the color area they sit on (deep dark reddish brown on skin and robes, dark green on foliage); background lines are thinner and color-tinted but still visible, fading toward the distance; no cross-hatching on skin.

Characters: believable anatomy, individual expressive faces, realistic adult proportions with an average adult about 7 to 7.5 heads tall, heads in natural size relative to the body, normal-sized eyes and adult facial bone structure (children and elders age-accurate), and culturally appropriate South Asian features where applicable; beautiful but not excessively idealized.

Color and light: clean solid flat color shapes for characters, clothing, and foreground, with harmonious, gently muted rich colors and natural skin tones; soft natural light with a clear direction, its color temperature set by the scene's time and setting (warm only for early morning, late afternoon, firelight or lamplight; neutral for full daylight; cooler in deep shade, overcast and night), so every form has a lit side and a shadow side; 2–3 controlled cel-shading tones on skin and clothing with slightly softened edges, the darkest tone clearly darker than the base color; subtle gradients on the sky and distant background layers, only very subtle color transitions on large middle-ground masses, never on characters; all line work is recolored into very dark warm brown contours and clearly darker color-tinted interior lines, with no heavy pure black outlines and no thick uniform contours.

Value and contrast: a full value range from bright highlights through mid tones to deep shadow, organized into a few large clear value groups rather than an even mid-tone spread; characters and grounded props cast clear soft-edged shadows on the ground and nearby surfaces; shadow sides of cliffs, rocks, tree trunks and buildings, deep spaces such as ravine floors, caves, doorways and forest interiors, and areas under canopies are rich deep colored shadows (cool, deep but never pure black); each focal character reads by value against the area behind it, lit against shadow or dark against light, never the same value as its background; far distance and sky stay lighter for atmospheric depth; areas behind text stay light and calm.

Background: foreground in simple flat color planes with selective detail; middle ground in flat color planes with gentle color transitions; distance painted in a soft, gouache-like storybook manner with layered atmospheric perspective, where far forms become lighter, cooler, and less detailed; restrained paper-like surface texture; characters stay crisper than the background.

Details: elegant simplified clothing folds, clear hair masses, crisp character silhouettes against the background.

Composition: cinematic visual storytelling, clean hierarchy, and sophisticated integrated editorial/book illustration, including safe gutters and calm, low-detail areas behind text when laying out spreads.

Exclusions: no anime, 3D/CGI, photorealism, glossy airbrushed skin, painterly brush texture on characters, heavy cross-hatching, excessive gradients, crude black shading, neon colors, strong bloom or glow, chibi or cartoon proportions, oversized heads or eyes, rounded baby faces, simplified cartoon figures.
```

## Khối LINE ART STAGE (blend)

Dùng khi cần vẽ nét đen trắng trước rồi mới tô màu (ngoài TTPQ Comic; lượt
nét của TTPQ Comic do `build-prompt.py` gọi tên style riêng). Nền giữ đơn giản
ở tiền/trung cảnh, thêm một lớp viễn cảnh nhẹ để lượt màu dựng chiều sâu.

```text
"ttpq comic blend" LINE ART STAGE: draw only the black line art of the style above; color and cel shading come in the next stage. Most of the line work goes to the characters. Robes have about 6 to 10 main simplified folds. Hair, beards and moustaches are outlined masses left white, with a few flow lines. Background is simple in clear depth layers: the foreground is a few large simple shapes (a cliff or rock is a few contour lines with few cracks, a tree is one crown shape with a few leaf clusters, ground is a few lines), the middle ground has the main shapes of rocks, trees and buildings with a little more detail, and the distance is a few light outlines of hills or trees; sky is empty white; lines get fewer and thinner toward the distance, and areas behind text stay calm with few lines. Realistic human proportions: heads in natural size relative to the body, normal-sized eyes and adult facial bone structure. An average adult stands about 7 to 7.5 heads tall; a character whose line gives another height or build (for example taller, shorter, heavier or slighter) follows that line; children and elders have age-accurate proportions. All figures stand on one consistent ground plane seen from one eye level: a figure's size follows where its feet touch the ground, so people at the same distance are the same size, and size decreases smoothly with distance, with no sudden jumps between neighboring figures or groups. Lines are pure black on plain white, with closed contours on characters and key props for coloring; no gray, no tone, no fill.
```

## Áp dụng

- Đọc và đưa nguyên khối STYLE vào prompt; không chỉ ghi tên style. Lượt nét
  đen trắng bỏ đoạn `Color and light:` và `Value and contrast:`, thêm khối
  LINE ART STAGE.
- Định nghĩa này không cần ảnh mẫu, profile nhân vật hoặc quy chuẩn y phục
  để được dùng độc lập. Các nguồn đó, khi có, là dữ kiện riêng của tác vụ.
- Gáy an toàn và vùng chữ chỉ áp dụng khi có dàn trang/spread.
- TTPQ Comic: lượt màu không ghi `--style` là blend, kể cả `--recast`. Lượt
  nét, chỉnh outline, `color-edit` và `swap` bỏ qua `--style`: hai lượt sửa
  trên ảnh màu vẽ theo finish của ảnh đang sửa (từ 2026-11-25).
- Lượt màu blend tô từ outline đã chọn, kể cả outline cũ vẽ theo light hoặc
  soft; không bắt buộc vẽ lại nét.
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
- Tỷ lệ người thật (thêm ngày 2026-11-17 sau góp ý "lên màu nhân vật lùn,
  hoạt hình hơn"): dòng `Characters:` của khối STYLE ghi rõ 7–7.5 đầu, đầu cỡ
  tự nhiên, mắt cỡ thường, xương mặt người lớn; `Exclusions:` cấm tỷ lệ chibi/
  hoạt hình, đầu hoặc mắt quá to, mặt tròn kiểu em bé, nhân vật hoạt hình
  giản lược (không dùng chữ "picture-book": nghi gợi giấy ngả vàng, cả tranh
  ấm lên, 2026-11-18). Script thêm câu khóa tỷ lệ theo nét ở mọi lượt màu,
  chỉ khóa tỷ lệ chứ không khóa cách tô; nhân vật `--recast` lấy tỷ lệ người
  thật và cỡ đầu, mắt tự nhiên. QA: so ảnh màu với outline, cỡ
  đầu, khăn/mũ và chiều cao nhân vật không đổi.
- Tỷ lệ ngay trong style (thêm ngày 2026-11-24, theo yêu cầu "sửa từ style
  thay vì vá style sai tỷ lệ"): `Core mix` giới hạn Flat Illustration vào cách
  tô màu (`color treatment … never flat-design figure proportions`) và mang
  tỷ lệ 7–7.5 đầu; đã test tô thường cùng outline, style không đổi. Dòng
  `Characters:` của style là nguồn tỷ lệ duy nhất: lượt màu chèn cả khối
  STYLE. Script chỉ thêm câu neo cỡ theo cảnh (chiều cao theo dòng nhân vật,
  cỡ đầu bằng người cùng tầng sâu trong Image 1) cho nhân vật `--recast`.
  `color-edit` giữ cỡ nhân vật như Image 1, `swap` neo theo cỡ mặt người cũ
  (từ 2026-11-25 không còn chèn dòng `Characters:`). QA: nhân vật `--recast`
  hoặc `swap` có cỡ đầu bằng người cùng tầng sâu.
- Tỷ lệ xa gần (thêm ngày 2026-11-17 sau góp ý "nhóm người gần nhau mà
  người lớn, người rất bé"): khối LINE ART STAGE có câu một
  mặt đất, một tầm mắt; cỡ người theo vị trí chân, cùng khoảng cách thì cùng
  cỡ, nhỏ dần đều theo xa gần. Lượt màu giữ chiều cao theo nét nên lỗi phải
  sửa ở outline.
- Hiệu ứng thần thông (thêm ngày 2026-11-18 sau góp ý "giới hạn gradient
  làm hiệu ứng đơn điệu"; test Mục Kiền Liên v002 chỉ ra một dải phẳng, v003
  có ngoại lệ thì nhiều lớp hơn): khối STYLE giữ nguyên; lượt màu có hiệu ứng
  dùng `--effect "<hiệu ứng>"` của `build-prompt.py`. Cờ này nới gradient, bloom
  mềm, sương sáng và hạt sáng chỉ trong vùng hiệu ứng, sửa `Exclusions:` cho lượt
  đó và bỏ mục Avoid cấm glow. QA: hiệu ứng có lõi sáng, chuyển trong suốt và hạt
  nhiều độ sâu; nhân vật vẫn mảng cel không gradient; không che mặt/tay, không đổi
  màu da/y, không hào quang sau đầu, không neon/lóa ống kính. Ghi
  `Effect: <hiệu ứng>` trong `record.md`.
- Ghi `Style: ttpq comic blend` trong `record.md` cho lượt dùng blend.
- Sửa style blend chỉ sửa file này; `build-prompt.py` đọc khối `text` đầu
  tiên (khối STYLE).
