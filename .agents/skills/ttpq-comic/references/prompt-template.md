# Mẫu gói prompt hai lượt

Đây là nhánh xuất gói prompt riêng. Với flow tương tác và hai câu prompt cố
định của người dùng, dùng [interactive-flow.md](interactive-flow.md). Quy tắc
lượt màu mới ưu tiên profile gốc và outline chỉ tham khảo scene; khối khóa
mọi outline bên dưới chỉ dùng khi người dùng yêu cầu rõ giữ nét chính xác.

Khối bối cảnh truyện (STORY CONTEXT / khối bối cảnh riêng) viết bằng tiếng Việt
để người dùng đọc và sửa; khối STYLE chép nguyên văn; chữ EN giữ nguyên văn.
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

## Prompt lượt nét (tin 2)

```text
Using the line-art style above, draw the illustration and page layout for this two-page book spread (pages <trái>–<phải>) of a picture book about the life of the Buddha. Characters are ancient Indian people of the Buddha's time. One image, <W>x<H> px.

ATTACHED IMAGES
- Image 1 = the page layout. Keep its text blocks, font size and line spacing; the text may reflow so the lines wrap vividly around the artwork. Left page Vietnamese, right page English. <Trang phải là chữ giữ chỗ: replace the Vietnamese placeholder on the right page with the English text below.> <Có chữ tô màu: colored text is only an editor's mark — all text black.> The <màu> rectangle is the illustration area; replace it with art, which may rise above it so the text wraps around it.
- Image <N> = <TÊN> — use only for identity (face, hair, beard, headwear, clothing); redraw in this line-art style, ignore its background, lighting and pose.

STORY CONTEXT
<2–4 câu: ai, ở đâu, khi nào, chuyện vừa xảy ra, chuyện chưa xảy ra.>

DIRECTOR'S NOTES
- Moment: <một tích tắc, một động từ chính>.
- Focus: <chủ thể> <một hành động> — the only action in the scene; clearest, highest-contrast point where the eye lands.
- Supporting (reacting only): <nhân vật>: <nhìn về focus | phản ứng | khung tiền cảnh | nền>. No one else performs a separate action.
- Not shown (text only): <beat chỉ có trong chữ>.
- <Vùng 1 (x a–b%)>: <cỡ cảnh, góc máy, nhân vật, hành động, hướng nhìn>.
- <Gáy (x 45–55%)>: <chỉ nền>.
- <Vùng 2 (x c–d%)>: <...>.
- Eye flow: <từ đâu tới đâu>, ending on the focus.
- Text wrap: <phần nào vươn vào vùng chữ, chữ ôm theo đâu>.
- Background: <bối cảnh, độ xa>.

CHARACTERS
- <dòng nhận diện của nhân vật có profile>
- <nhân vật phụ/quần chúng: mô tả ngắn>

DO NOT
<điều cấm theo truyện: việc chưa xảy ra, đạo cụ sai>; <era liên quan>; no second competing action or focal point; nothing important at the center fold; no "Hình" notes or labels; text never over faces or hands.

ENGLISH TEXT FOR THE RIGHT PAGE (copy exactly)
"""
<chữ EN>
"""
```

## Prompt lượt màu

```text
<khối STYLE màu>

Color Image 1 (the approved line art of a two-page picture-book spread) in the ttpq comic light style above.

KEEP EXACTLY FROM IMAGE 1
- The composition, every figure's position, pose and gesture, and all outlines.
- All text: same words, positions, line breaks and the way it wraps around the art. Text stays crisp near-black on a calm light background. Do not re-typeset, translate or move it.

CHARACTERS
- Image <N> = <TÊN>: <dòng nhận diện>. Correct his/her face, hair and costume to match Image <N> exactly; ignore its background, lighting and pose.
- <nhân vật phụ: màu trang phục, tông da>

LIGHT & COLOR
- <thời điểm, nguồn sáng, bảng màu theo truyện>. Use this scene lighting while retaining the soft lighting and 2D rendering of ttpq comic light.
- Behind the text: <nền nhạt, phẳng>.

DO NOT
<điều cấm theo truyện và era liên quan>; no new text, no colored text, no text boxes.
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
<Khi đã có phương án active: Focus — chủ thể + một hành động; Phối hợp — vai của từng nhân vật khác so với focus; Không vẽ — beat chỉ có trong chữ. Chưa có phương án: "Chưa chọn; chờ phương án.">

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
