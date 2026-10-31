# Mẫu prompt gọn

Dùng cho cả prompt ImageGen nội bộ của flow tương tác và nhánh gói prompt.
Khối bối cảnh riêng viết tiếng Việt; khối STYLE và chữ EN chép nguyên văn.
Thay mọi `<...>` bằng giá trị thật, xóa phần không áp dụng. File lưu gồm metadata và từng prompt trong code
block riêng.

~~~markdown
# Prompt <vNNN> — <layout-slug> p<trái>-<phải> — <spread | Hình N>

- Mode: spread | frame
- Canvas: <1536x1024 | 1024x1536 | 1024x1024>
- Nguồn: layout.json (+ spread liền kề), profile <slug@vNNN>, brief.md, text-en.md
- Thay đổi so với version trước: <...>

## Lượt nét — ChatGPT Image

Đính kèm ở tin 2: Image 1 = `layout-ref.png`; Image 2 = `<ref profile>`; …

### Tin 1 — style

```text
<khối STYLE clean outline>
```

### Tin 2 — yêu cầu

```text
<PROMPT LƯỢT NÉT>
```

## Lượt màu — Codex hoặc ChatGPT Image

Đính kèm: Image 1 = ảnh nét đã chọn; Image 2 = `<ref profile>`; …

```text
<PROMPT LƯỢT MÀU>
```
~~~

## Quy tắc viết (nguồn duy nhất)

- Viết mới từ mẫu mỗi version, chỉ từ `brief.md` (phương án active) và
  context active; không sửa từ prompt version trước.
- Chỉ dùng đúng các khối trong mẫu, không thêm khối khác. INTENT mỗi
  trang/scene 1–2 câu.
- Nhân vật có profile: không mô tả lại identity bằng chữ (ảnh ref lo phần
  này); chỉ thêm một cụm cho chi tiết hay bị vẽ sai (ví dụ "robe covers both
  shoulders"). Nhân vật chưa có profile: một câu nhận diện.
- Không thêm luật vá từ ảnh trước ("heads below y…", "reduce scale",
  "keep feet visible", "do not invent a different composition"…). Lỗi bố cục
  sửa ở brief.
- Không đính kèm, nhắc tới hay mô tả theo output cũ. Ngoại lệ: ảnh nét đã chọn
  ở lượt màu của chính spread, hoặc người dùng override rõ (`SKIPPED_BY_USER`).
- DO NOT một dòng: beat "Không vẽ" và điều cấm truyện/era liên quan cảnh.

## Prompt lượt nét

Tin 1 là khối STYLE clean outline chép nguyên từ `style/ttpq-comic.md`. Khi
gọi ImageGen một lượt, đặt khối STYLE ngay trước tin 2.

```text
Draw pages <trái>–<phải> of a picture book about the life of the Buddha (ancient northern India) as one <W>x<H> spread.
Image 1 = the page layout. Image <N> = <TÊN>: use only for identity (face, hair, clothing, accessories); ignore pose, background and color.

STORY: <1–2 câu: ai, ở đâu, chuyện gì vừa/chưa xảy ra>.

INTENT: <cảm xúc>.
- <Trang/scene chính>, <góc máy, cỡ cảnh>: <focus — một chủ thể, một hành động>. <vai phụ chỉ phản ứng/nhìn>.
- <Trang/scene phụ nếu có>, <góc máy, cỡ cảnh khác scene chính>: <...>.
- Center fold: quiet background only.

TEXT: Left page Vietnamese exactly as in Image 1; right page the English below. Keep the font size and each page's first line exactly where Image 1 has them; lines may reflow downward and wrap around <phần tranh vươn vào vùng chữ> inside the column. Black text, no boxes.<Có chữ tô màu/ô màu: Colored text and <màu> areas are editor's marks only.>

DO NOT: <không vẽ + điều cấm truyện/era>.

ENGLISH TEXT (copy exactly):
<chữ EN>
```

## Prompt lượt màu

```text
<khối STYLE màu>

Color Image 1, the line art of pages <trái>–<phải>, in the ttpq comic light style above. Use it for the scene and text; characters must match their profile images exactly. Image <N> = <TÊN>: identity only; ignore pose, background and color.

INTENT: <cảm xúc>; <thời điểm, nguồn sáng, bảng màu theo truyện>, keeping the soft 2D rendering of ttpq comic light. Calm light background behind the text.

TEXT: keep every word, line break and wrap from Image 1; crisp near-black, no boxes.

DO NOT: <điều cấm truyện/era>; no new or colored text.
```

## Mode frame

Canvas và vị trí % theo vùng của Hình. Hình không gắn chữ: bỏ phần chữ ở cả
hai lượt, thêm `No text of any kind in the image.`

## Khối bối cảnh

Deliverable mặc định (xem SKILL). Viết tiếng Việt, chỉ lấy dữ kiện từ scene
sheet, bible và profile; không đưa chữ VI/EN, bố cục hay khối STYLE. File lưu
`prompts/vNNN-context.md` gồm metadata và khối trong một code block.

~~~markdown
# Prompt <vNNN> — <layout-slug> p<trái>-<phải> — khối bối cảnh

- Dùng: gửi context trước để đọc hiểu cùng ảnh layout và ảnh profile
  (<Image N = TÊN>); sau đó gửi yêu cầu minh họa riêng. Có thể dùng trong Codex
  hoặc ChatGPT.
- Nguồn: `story/<tập>/scenes.md` <Snn> (<trạng thái>), `story/<tập>/bible.md`
  (<mục>), profile <slug@vNNN>.
- Quyết định áp dụng: <ví dụ: không vẽ đồi; SKIPPED_BY_USER …>
- Hình layout: [layout-ref.png](../layout-ref.png)
- Profile liên quan:
  - Ảnh <N> — <TÊN>: [profile.md](../../../../characters/<slug>/profile.md)
    (<trạng thái> <vNNN>), ảnh ref [<ref-vNNN.png>](../../../../characters/<slug>/<ref-vNNN.png>)
  - <Nhân vật chưa có profile>: chưa có profile, mô tả trong khối.

```text
BỐI CẢNH CẢNH — trang <trái>–<phải>, truyện cuộc đời Đức Phật, miền Bắc Ấn Độ, khoảng thế kỷ 5 trước Công nguyên.

CHUYỆN TRƯỚC ĐÓ
<1–3 câu: cảnh liền trước>

DIỄN BIẾN TRONG CHỮ (để hiểu, không vẽ hết)
<các beat trên spread theo thứ tự, mỗi beat một dòng ngắn, theo chữ và scene sheet>
Hình chỉ vẽ một khoảnh khắc với một hành động focus, chọn ở bước phương án; các beat còn lại chỉ nằm trong chữ.

KHOẢNH KHẮC ĐƯỢC VẼ
<Khi đã có phương án active: chép 5 mục từ brief.md. Chưa có phương án: "Chưa chọn; chờ phương án.">

THỜI ĐIỂM & ÁNH SÁNG
<thời điểm, nguồn sáng, sương/bóng đổ>

NƠI CHỐN
<địa hình, tiến độ công trình, vật dụng, chân trời>

CON NGƯỜI
<nhóm người, dấu hiệu nhận diện tĩnh (tuổi, dáng, tóc, trang phục theo era); dòng nhận diện nhân vật có profile và ảnh số mấy, bỏ qua nền và tư thế của ảnh. Hành động theo chữ để ở DIỄN BIẾN, không gắn vào nhận diện.>

KHÔNG ĐƯỢC
<việc chưa/không xảy ra, đạo cụ dễ hiểu sai, ngoại lệ profile, niên đại liên quan>
```
~~~
