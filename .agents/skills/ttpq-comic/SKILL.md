---
name: ttpq-comic
description: Chuẩn bị context truyện và menu lệnh cho spread trong ttpq-comic; đọc context, đề xuất hoặc tiếp nhận phương án minh họa, tạo/chỉnh clean outline và ảnh màu theo từng yêu cầu trực tiếp. Mặc định chỉ xuất context; hỗ trợ gói prompt khi được yêu cầu. Độc lập với comic-illustrator và hai studio.
---

# TTPQ Comic

Đọc trước mỗi phiên: [contract](../../../ttpq-comic/contract.md),
[book-spec](../../../ttpq-comic/book-spec.md),
[style](../../../ttpq-comic/style/ttpq-comic.md),
[style blend](../../../docs/style-ttpq-comic-blend.md) khi lên màu (mặc
định của lượt màu) hoặc khi người dùng gọi `ttpq comic blend`,
[style real](../../../ttpq-comic/style/ttpq-real.md) chỉ khi người dùng gọi `ttpq real`,
[era guide](../../../ttpq-comic/style/era-ancient-india.md). Không đọc tài liệu
hay skill của `comic-illustrator/`, hai studio hay `docs/monastic-robes.md`.

Giá trị của flow là phần GPT không tự biết: **bối cảnh truyện**, **ý đồ điện
ảnh** và **đúng profile theo cảnh**. Style, ảnh ref và điều cấm do
`scripts/build-prompt.py` ghép tự động. Agent chỉ viết vài câu tả cảnh, giữ
prompt ngắn và tự nhiên như văn xuôi.

## Đọc tiết kiệm

- `prompt-template.md`: chỉ đọc mục của lượt đang làm.
- `record.md` của spread: chỉ đọc file chính. Khi file vượt khoảng 15 KB,
  chuyển các lượt cũ sang cuối `record-archive.md`.

## Hội thoại

- Menu từng bước theo [interactive-flow](references/interactive-flow.md). Chỉ
  hiện menu đúng bước hiện tại, mỗi câu trả lời mẫu trong một code block riêng.
- Lệnh tạo outline/màu là yêu cầu tạo ảnh trực tiếp; không hỏi lại quyền tạo
  ảnh, không route sang workflow khác. Prompt cố định của người dùng giữ nguyên.
- Mỗi lượt hỏi một quyết định chính; không hỏi lại điều đã chốt trong
  `brief.md`/`record.md`.

## 0. Story bible (một lần cho mỗi tập)

Khi người dùng đưa kịch bản, hoặc `story/<tập>/` chưa có `bible.md`/`scenes.md`:

1. Chép nguyên văn vào `ttpq-comic/story/<tập>/script.md`.
2. Viết `bible.md` và `scenes.md` theo [mẫu story](references/story-template.md),
   gồm dòng **Profile:** cho mỗi cảnh, mục "Avoid trong prompt" và "Cặp dễ nhầm".
3. Trình tóm tắt và các điểm Cần quyết để người dùng duyệt.

## 1. Xác định spread và đọc layout

Thư mục làm việc: `ttpq-comic/spreads/<layout-slug>/p<trái>-<phải>/` (số trang
3 chữ số).

```bash
scripts/run-with-tools.sh -- python3 .agents/skills/ttpq-comic/scripts/read-layout.py "ttpq-comic/layouts/<file>.pdf" --folio <số trang trái> --out "ttpq-comic/spreads/<layout-slug>/p<trái>-<phải>"
```

Dùng `--page <n>` nếu biết số trang PDF. Ánh xạ chữ của spread vào cảnh `Snn`
và ghi vào `brief.md`. Chỉ đọc spread liền kề khi chưa có bible hoặc chữ không
ánh xạ chắc vào một cảnh. Cụm chữ tô màu trong `marks` là dấu biên tập; nếu
nghĩa của màu chưa có trong record, hỏi một lần.

## 2. Nhân vật

- Lấy nhân vật từ dòng **Profile:** của cảnh. Cảnh chưa có dòng này thì thêm
  vào `scenes.md` trước.
- Profile cần 3 trường `Tên trong prompt`, `Ref prompt`, `Dòng prompt` theo
  [mẫu profile](references/profile-template.md).
- Chưa có profile: xin ảnh ref, chép vào `characters/<slug>/ref-v001.png`, viết
  profile `DRAFT`, chờ duyệt. Quần chúng không có profile: tả bằng chữ trong
  phần cảnh.
- Đính kèm ảnh ref cho mọi nhân vật có tên **thấy rõ mặt**. Chỉ người ở xa,
  nhỏ hoặc nhóm quần chúng mới tả bằng chữ (`--no-ref`).

## 3. Khối bối cảnh (deliverable mặc định)

Viết theo [mẫu khối bối cảnh](references/prompt-template.md#khối-bối-cảnh), lưu
`prompts/vNNN-context.md`, ghi `record.md`. Khi trình:

1. **Khối bối cảnh** trọn trong một code block.
2. **Layout:** link `layout-ref.png` của spread.
3. **Profile liên quan:** mỗi nhân vật một dòng gồm số ảnh, link `profile.md`
   và link ảnh ref; nhân vật chưa có profile ghi "mô tả trong khối".

Cuối phản hồi trình menu sau context (interactive-flow mục 1).

## 4. Phương án điện ảnh

**Một khoảnh khắc – một focus.** Mỗi scene là một tích tắc. Trong scene chỉ có
một hành động chính, các nhân vật khác phối hợp với hành động đó. Spread có
nhiều scene thì ghi rõ scene nào là chính; scene còn lại hạ một bậc.

**Vai nhiếp ảnh gia.** Khi đề xuất hoặc hoàn thiện phương án, agent nghĩ như
một nhiếp ảnh gia nghệ thuật chuyên nghiệp đang chọn khung hình để dàn trang
sách: chọn khoảnh khắc quyết định, điểm đứng máy và khoảng cách có chủ ý, bố
cục có lớp tiền–trung–hậu cảnh, đường dẫn mắt về focus, và khoảng thở cho cột
chữ. Mỗi lựa chọn có lý do cảm xúc. Vai này chỉ đổi cách chọn khung hình: tranh
vẫn là minh họa nét 2D, body không dùng từ nhiếp ảnh (photo, photograph, lens,
mm, bokeh, depth of field, f-stop); `build-prompt.py` cảnh báo khi gặp.

Mỗi phương án gồm đúng 5 mục, mỗi mục 1–2 câu:

- **Cảm xúc:** người xem cần cảm thấy gì.
- **Khoảnh khắc & focus:** một chủ thể và một hành động; vai phụ chỉ phản ứng.
- **Khung hình:** cho từng trang/scene: điểm đứng máy và cỡ cảnh, lớp
  tiền–trung–hậu cảnh, đường dẫn mắt về focus, khoảng thở cho chữ; kèm lý do
  cảm xúc.
- **Không vẽ:** beat chỉ có trong chữ.
- **Chữ ôm hình:** phần tranh nào vươn vào vùng chữ.

Phương án agent đề xuất có thêm một dòng **Đánh đổi**. `brief.md` chỉ giữ khối
"Phương án active" khoảng 10 dòng (context, cast, 5 mục). Đổi phương án thì
chuyển bản cũ sang "Lịch sử phương án" trong `record.md`.

Mode mặc định là spread: một tranh liền cho cả spread. Chỉ dùng mode frame
(mỗi Hình một ảnh) khi người dùng yêu cầu.

## 5. Viết và chạy prompt ảnh

Theo [mẫu prompt](references/prompt-template.md): agent viết file body (2–4 câu
tiếng Anh) rồi chạy `build-prompt.py` để ghép prompt. Script in danh sách ảnh
cần đính kèm theo đúng thứ tự Image. Gửi đúng file prompt script ghi ra, kèm
các ảnh đó. Trước khi gửi tạo ảnh, tự kiểm prompt theo
[checklist](references/prompt-checklist.md).

- Hiển thị ảnh ngay khi công cụ trả kết quả. Sau khi đã hiển thị, tự động
  kiểm tra ảnh theo prompt, layout và profile liên quan. Lưu phiên bản mới,
  ghi kết quả kiểm tra vào `record.md` và báo ngắn các điểm lệch nếu có.

Ảnh lượt nét có hai dải bleed xám trống (47 px mỗi bên). Khi đưa vào InDesign:
nối nền vào hai dải bằng Photoshop/AI, đặt ảnh để phần spread 1443 px khớp
khổ spread, bleed 0.3 cm lấy từ phần đã nối.

Khi người dùng xin "gói prompt" để tự chạy: dùng cùng script, trình mỗi prompt
trong một code block kèm danh sách ảnh đính kèm.
