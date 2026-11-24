# Prompt chân dung trong `ref-v002.png`

- Tạo ngày 2026-11-24 bằng Codex CLI (`codex exec -i`), 1 lượt, người dùng duyệt.
- Ảnh khung tỷ lệ, chân dung cũ và ảnh kết quả trung gian đã xoá sau khi duyệt; prompt giữ làm record.

## Prompt

```text
Redraw a chest-up character portrait of THE ELDER OF KASSAPA'S ERA.

STRICT PROHIBITIONS (apply from the start):
- Do NOT enlarge the head. Head size relative to neck, shoulders and chest must match Image 1 exactly; the previous portrait (Image 2) had the head drawn too big, do not copy its proportions.
- Do NOT change identity: keep face shape, brows, eyes, nose, mouth, ears, facial hair, hair, skin tone and clothing colours/wrap exactly as in Image 2 and Image 3. Do not lengthen the beard; keep it short and trimmed. Keep the face lines and wrinkles of Image 2.
- No added jewelry, accessories, props, text, labels, borders, frames or background scenery.
- Do not copy the blur, softness or upscaling artifacts of Image 1.
- No anime, 3D/CGI, photorealism, painterly brush texture, heavy cross-hatching, excessive gradients or crude black shading.

IMAGES:
- Image 1 = proportion and framing guide: an upscaled crop of this character's own front full-body view. Follow its head size, neck length, shoulder width, shoulder slope, crop line and placement exactly.
- Image 2 = previous portrait: use only for facial detail, line quality and rendering finish.
- Image 3 = approved profile sheet: identity reference.

TASK: Redraw Image 1 as a crisp, finished chest-up portrait with the same level of detail and line quality as Image 2. Front view facing the viewer, self-assured faint smile, heavy-lidded eyes. Keep Image 1's framing: top of the head near the top edge, both shoulders fully inside the frame, crop at mid-chest. Plain white background; soft rounded-bottom crop edge like Image 2.

CHARACTER: ELDER OF KASSAPA'S ERA: thin monk aged 60–70, shaved head, long lined face, bushy white brows, heavy-lidded eyes, long earlobes, short trimmed white beard, self-assured faint smile. Very dark reddish-brown robe covering both shoulders, as in Image 2.

STYLE: match the existing sheet exactly — ttpq comic light, strictly 2D: precise clean hand-drawn outlines with natural line-weight variation, clean flat colour shapes with 2–3 soft cel-shading tones, natural skin tones, soft warm light.

OUTPUT: one image, portrait orientation (2:3), the character only on white.
```
