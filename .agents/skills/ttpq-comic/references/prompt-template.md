# Mẫu prompt

Prompt ảnh do `scripts/build-prompt.py` ghép. Agent chỉ viết **file body**: vài
câu tiếng Anh tự nhiên, không nhãn viết hoa, không luật vá. Script ghép theo
thứ tự GPT đọc: việc cần làm → body (cảnh) → nhân vật → STYLE (trừ lượt nét) → trang sách
(lề, bleed, gáy) → chữ → Avoid. Script tự thêm:

- khối STYLE theo `--style` (không ghi: `real` cho `color-edit` và lượt màu có
  `--recast` (từ 2026-11-22), `blend` cho lượt màu thường, `light` cho chỉnh
  outline; style khác chỉ khi người dùng gọi tên), chép định
  nghĩa chuẩn của style (light: `docs/style-ttpq-comic-light.md`; soft, blend, real:
  khối đầu trong `ttpq-comic/style/`). Từ 2026-11-19 **lượt nét không chèn khối
  STYLE** (cả định nghĩa lẫn LINE ART STAGE), theo yêu cầu người dùng;
- câu mở lượt nét cố định, gọi tên style (từ 2026-11-22, theo yêu cầu người
  dùng; không chèn định nghĩa): "Use case: illustration-story. Create an
  outline illustration in a Semi-Realistic Storybook Illustration style, pure
  white background. Image 1 is the page layout."; không ghi "finished" hay
  "black and white" (làm GPT đánh bóng xám, nét tối đậm);
- lượt nét bỏ rule head tall (từ 2026-11-22): không có câu
  "body height and proportions follow the character lines below", lọc cụm
  "about N heads tall" khỏi `Dòng prompt` (profile giữ nguyên), nhân vật không
  ref không có câu "same realistic human proportions". Riêng "In line art" của
  profile vẫn chèn (bỏ đi thì `thin close jaw beard` ra râu quai nón, p048-049 v066);
- câu mở lượt màu: light là mảng màu phẳng, 2–3 tông cel-shading ranh giới rõ,
  nền vài mảng phẳng; soft là ánh sáng có hướng, 3–4 tông bóng chuyển mềm,
  gradient nhẹ, nền có lớp xa gần; blend là mảng phẳng, 2–3 tông cel mép hơi dịu,
  tiền/trung cảnh phẳng (trung cảnh chuyển sắc dịu), viễn cảnh/trời vẽ dịu với gradient nhẹ, không gradient trên nhân vật. Cả ba giữ nét đen; tông xám trong Image 1
  không phải ánh sáng; sau đó luôn có câu khóa tỷ lệ (giữ chiều cao, cỡ đầu,
  tỷ lệ đầu/thân, mặt, cỡ mắt, khăn/mũ như Image 1; không phóng to đầu hay vẽ
  hoạt hình; thêm 2026-11-17). Câu này chỉ khóa tỷ lệ, không ghi "color inside
  the lines"/"do not stylize" vì làm ảnh nhạt, mất bóng đổ. Nhân vật `--recast`
  vẽ lại theo sheet nhưng vẫn tỷ lệ người thật 7–7.5 đầu, cỡ đầu và mắt tự nhiên;
- câu về layout, ô hình placeholder và dải bleed xám hai bên (lấy từ `layout.json`);
- lượt nét: tự tạo `layout-ref-canvas-v003.png` 1536×1024 (spread ở giữa, dải
  bleed xám trơn 47 px mỗi bên, để trống; hậu kỳ nối nền bằng Photoshop/AI)
  cùng khổ ảnh ra; prompt giữ mặt, tay và hành động chính lùi vào trong trang,
  xa dải xám; thân, y và nền được chạy tới mép xén và bị cắt ở đó, để GPT không kéo giãn layout; đính kèm file
  này làm Image 1 thay `layout-ref.png`;
- dòng `Image N = <tên>: <dòng prompt>` cho từng nhân vật, lấy từ dòng
  **Profile:** của cảnh hoặc `--cast`, cùng câu tương phản cho cặp dễ nhầm.
  Không có `--cast` mà cast của cảnh quá 3 ảnh ref thì script dừng; có
  `--cast` mà quá 3 ảnh thì cảnh báo;
- câu chữ: mở bằng mục tiêu chữ và tranh đan vào nhau; chỉ khóa **cỡ chữ/giãn
  dòng** (số đo từ `sizePx`, `leadingPx`) và **vị trí dòng đầu** mỗi cột (theo
  Image 1, không ghi tọa độ % vì GPT không đo pixel); độ dài dòng, ngắt dòng, số
  dòng và dáng khối để tự do, cột có thể dài xuống; VI trái, EN giữ chỗ bên phải; chữ đen, không
  khung, giữ nguyên highlight màu của layout theo dòng đã reflow, không đè mặt, gáy để trống. Không khóa thêm số dòng, dáng khối
  hay khoảng cách đoạn: các khóa đó làm tranh né vùng chữ;
- câu gáy (cả ba lượt): gáy ở x 50%, nền vẽ liền qua gáy; nhân vật (thân, y, đạo cụ
  cầm tay) nằm trọn một trang, được vẽ sát gáy từ phía mình; mặt và bàn tay làm
  hành động chính ngoài 7% giữa chiều ngang (30 pt mỗi bên gáy). Chỉ giữ hai con
  số: gáy x 50% và 7%. Vật cần đi liền qua gáy (thanh gỗ nhiều người khiêng…)
  dùng `--across`. Spread
  hai cảnh riêng dùng `--two-scenes` ở cả ba lượt: gáy bị đóng sách che nên
  không hòa hai cảnh; mỗi cảnh vẽ/tô trọn trang mình tới sát gáy rồi dừng, không
  vùng chuyển tiếp, không dải trắng; nhân vật mỗi cảnh ở trang của mình. Không
  dùng chung với `--across`/`--split`. Spread một cảnh: lượt màu tô liền qua gáy,
  chỉ hai dải bleed xám để trống;
  không thay câu gáy bằng câu nền/vignette riêng; spread hai tranh tách nhau có dải giấy
  trắng ở gáy (theo brief/outline) thì dùng `--split` ở cả ba lượt: lượt nét
  đổi câu gáy thành hai tranh riêng, dải giấy trắng 7% giữa; lượt màu giữ dải trắng;
- dòng Avoid: "Avoid" (tiếng Anh) của cảnh, "Avoid trong prompt" của bible (dòng
  `[khi: …]` chỉ chèn khi cảnh chứa từ khóa); cảnh chỉ có "Cấm" tiếng Việt thì
  script bỏ qua và cảnh báo; cộng `--avoid`. Áp cho cả lượt nét, màu và chỉnh.
  Script tách mục theo `;`, bỏ mục trùng hoặc nằm trọn trong mục khác, và cảnh
  báo cặp mục gần trùng (ví dụ "modern objects or…" và "modern objects, furniture…")
  để gộp tại nguồn;
  GPT không có negative prompt thật, mỗi từ trong Avoid vẫn gợi ra thứ đó: điều
  muốn có viết thành câu khẳng định trong body; Avoid chỉ giữ lỗi model hay mắc
  thật; quá 7 mục thì script cảnh báo;
- lượt màu: ánh sáng lấy từ `--light` (tiếng Anh, ưu tiên), nếu không thì từ
  "Thời điểm/ánh sáng" của cảnh; trường này là tiếng Việt thì script bỏ qua và
  cảnh báo. Spread hồi tưởng hoặc khác thời điểm với cảnh luôn dùng `--light`;
  giữ highlight màu sau chữ như Image 1;
- lượt màu: bỏ dòng `Text wrap:` của body; cảnh báo nếu body còn chỉ dẫn góc máy;
- lượt chỉnh: mở bằng "chỉ đổi điều liệt kê, giữ nguyên phần còn lại", thêm
  một dòng khóa style nét. Nhân vật khớp sheet ở mặt, tóc, trang phục; tỷ lệ cơ
  thể theo dòng prompt, không theo tư thế sheet. Giữ chữ, cỡ chữ, dòng đầu; chỉ
  các dòng cạnh vùng sửa được reflow ôm hình mới;
- nhân vật: lượt nét và chỉnh outline dùng `Dòng prompt` ngắn; lượt màu và
  `color-edit` dùng khối `Dòng nhận diện tiếng Anh` đầy đủ của profile (thiếu
  thì cảnh báo, dùng dòng ngắn). Profile có `Nét mặt cố định` thì mọi lượt giữ
  nét mặt đó, thay cho "biểu cảm theo khoảnh khắc". Profile có `Nét vẽ line art`
  thì lượt nét và chỉnh outline thêm câu "In line art: …" (cách vẽ nét cho dấu
  hiệu dễ sai khi chuyển sheet màu sang nét đen, ví dụ râu mờ thành ria và chòm
  râu có viền);
- lượt màu `--recast <slug> …`: nhân vật vẽ lại từ profile, outline chỉ giữ vị
  trí, dáng, cử chỉ, hướng nhìn, hành động, đạo cụ và thứ tự chồng; mặt, đầu,
  tai, tóc/râu, da, vóc dáng, trang phục lấy từ sheet; vóc dáng khác outline
  thì giữ chân trên cùng mặt đất và vẽ lại nền quanh dáng mới. Dùng cho outline
  chưa đúng profile; nền và chữ vẫn tô theo nét. Tối đa 2 người mỗi lượt;
- lượt chỉnh outline `--pass edit --recast <slug>`: xóa và vẽ lại cả đầu, mặt,
  tai, tóc/râu, cổ áo của nhân vật theo sheet, bỏ qua mặt đã vẽ trong Image 1;
  chỉ giữ vị trí đầu, hướng quay đầu, hướng nhìn, tư thế, cử chỉ, đạo cụ, thứ
  tự chồng. Body không được khóa cứng đầu ("exactly the existing", "same angle",
  "only identity features") vì lệnh giữ nguyên của edit khiến GPT chỉ sửa nhẹ
  mặt cũ; script cảnh báo khi gặp. Cast nên gồm cả người đứng cạnh (có thể
  `--no-ref`) để có câu tương phản trong "Cặp dễ nhầm";
  script thêm câu chốt "Final check…" ở cuối prompt (sau Avoid) cho từng nhân
  vật recast: thay toàn bộ đầu và cổ áo, mặt cũ là sai, được đổi silhouette
  đầu, giữ vị trí/hướng quay/cử chỉ, nhắc lại `Nét vẽ line art`. Chi tiết đếm
  được (số nét râu, số nếp cổ áo) viết trong profile, không thêm tay vào prompt.
  Câu mạnh làm nền và chữ dễ đổi theo: soát chữ và nền sau mỗi lượt;
- lượt `color-edit`: Image 1 là ảnh màu đang sửa; chỉ sửa nhân vật trong
  `--cast` (mỗi lượt một người), giữ nguyên người khác, nền, ánh sáng, màu, nét
  và chữ; phần giữ từ Image 1 và phần lấy từ sheet như `--recast`. Body có thể
  trống hoặc thêm dòng `Change:`/`Keep:`. Không thêm khối STYLE hay dòng đòi vẽ
  lại style cả tranh (script cảnh báo): muốn đổi style thì chạy lại lượt màu;
- nhiều nhân vật recast hoặc color-edit: script gộp phần giữ/lấy từ sheet thành
  một đoạn chung, không lặp từng người;
- body ghi `{slug}` (ví dụ `{moggallana}`) khi cần trỏ tới ảnh ref; script thay
  bằng `Image N` đúng theo cast, dừng nếu slug không có trong cast, cảnh báo nếu
  body ghi cứng `Image N`.

Lệnh chung (đường dẫn `--body`/`--out` tính theo thư mục spread):

```bash
scripts/run-with-tools.sh -- python3 .agents/skills/ttpq-comic/scripts/build-prompt.py \
  --spread ttpq-comic/spreads/<layout-slug>/p<trái>-<phải> --scenes <Snn> [<Snn>] \
  --pass <outline|color|edit|color-edit> --body prompts/vNNN-<pass>.body.txt \
  [--cast <slug> …] [--no-ref <slug> …] [--recast <slug> …] [--avoid "<không vẽ, tiếng Anh>"] \
  --out prompts/vNNN-<pass>.txt
```

- `--cast`: người thật sự có mặt trong spread (thường khác dòng Profile của cả cảnh); slug
  có thể kèm ảnh, ví dụ `duc-phat:ref-v001-ngoi-thien.png`.
- `--no-ref`: nhân vật ở xa, nhỏ hoặc nhóm quần chúng; chỉ tả bằng chữ.
- `--avoid`: mục "Không vẽ" của brief, dịch ngắn sang tiếng Anh.
- `--light`: ánh sáng tiếng Anh của spread cho lượt màu, ví dụ
  `"bright midday sun in a dry forest; the ravine floor in cool shade"`.
- `--two-scenes`: spread có hai cảnh riêng, mỗi cảnh vẽ trọn trang mình tới gáy, không hòa, không dải trắng.
- `--across "<vật>"`: ngoại lệ của câu gáy cho một vật đi liền qua gáy (ví dụ
  `"the long wooden beam"` khi nhiều người khiêng từ trang này sang trang kia).
  Người vẫn nằm trọn trang của mình; trong 7% giữa vật chỉ là một đoạn trơn,
  không tay, dây buộc, mối nối hay mặt. Truyền ở cả ba lượt; không dùng với `--split`.
- `--effect "<hiệu ứng>"`: ngoại lệ cho vùng hiệu ứng thần thông ở lượt `color` và
  `color-edit` (tiếng Anh, nêu màu và vị trí, ví dụ
  `"the jade-green psychic force swirling around the floating beams and earth slab"`).
  Script thêm đoạn `Supernatural effect` sau khối STYLE (gradient trong suốt từ lõi sáng,
  bloom mềm ở mép, sương sáng, hạt sáng nhiều độ sâu, ánh phản nhẹ lên vật gần; không
  che mặt/tay, không đổi màu da/y, không hào quang sau đầu), sửa `Exclusions:` thành
  chỉ cấm gradient/glow ngoài vùng hiệu ứng, và bỏ khỏi Avoid mục có glow, bloom,
  gradient, magic effect, light rays (có cảnh báo; mục "halo" vẫn giữ). `color-edit`
  thêm câu giữ nguyên hiệu ứng của Image 1. Lượt nét không nhận cờ này: vùng hiệu ứng
  vẽ bằng vài nét mảnh trong body. Không ghi cờ thì style giữ nguyên.
- `--no-text`: Hình không có chữ (mode frame).
- Script in danh sách ảnh đính kèm theo thứ tự Image; gửi đúng thứ tự đó.

## Body lượt nét

Lấy từ phương án active, viết văn xuôi, theo thứ tự:

- **STORY (bắt buộc):** một câu mở đầu nêu ai, ở đâu, lúc nào, chuyện gì vừa
  xảy ra hoặc chưa xảy ra. Đây là phần GPT không tự biết.
- **Từng trang/scene:** từ mục "Khung hình" của brief: điểm nhìn, cỡ cảnh, rồi
  bố cục (vật tiền cảnh làm khung, đường dẫn mắt về focus, lớp xa gần, khoảng
  trống phía chữ); focus (một chủ thể, một hành động), vai phụ phản ứng ra sao.
  Tư thế và đạo cụ chép đúng brief. Viết bằng lời bố cục, không dùng từ nhiếp
  ảnh (photo, photograph, lens, mm, bokeh, depth of field, f-stop): GPT sẽ vẽ ra
  ảnh chụp thật; script cảnh báo khi gặp.
- **Biểu cảm (bắt buộc):** mọi nhân vật có tên có một cụm biểu cảm và hướng
  nhìn, khoảng 12 từ trở xuống, ví dụ `a slight gentle smile, looking at Punna's spoon`.
  Thiếu cụm này, GPT tự vẽ nụ cười tươi mặc định. Không tả mặt, tuổi hay màu.
- **Text wrap (bắt buộc):** từ mục "Chữ ôm hình" của brief: phần tranh nào
  (đầu gậy, tán cây, mép vách…) vươn vào cạnh những dòng nào của cột nào.
  Không nhắc cỡ chữ, dòng đầu, ngôn ngữ, màu chữ hay độ rộng dòng: script đã lo
  và câu lặp dễ mâu thuẫn. Thiếu câu này, tranh nằm yên dưới chữ.
- **Mood:** một câu cảm xúc của spread.

Mỗi lượt nét viết body mới từ brief, kể cả khi chỉ cập nhật phương án; không
sửa chồng lên body/prompt trước. Lưu body vào `prompts/vNNN-outline.body.txt`
để truy được prompt đã lấy gì từ brief.

Gọi nhân vật bằng `Tên trong prompt` trong profile. Quần chúng không có profile
thì tả số lượng và hành động ngay trong câu. Lỗi từng gặp của spread đưa vào
"Không vẽ" của brief (đi qua `--avoid`), không viết câu vá vào body.

```text
<STORY: một câu>.
Left page (main): <điểm nhìn, cỡ cảnh>; <bố cục: vật tiền cảnh làm khung, đường dẫn mắt về focus, khoảng trống phía chữ>; <chủ thể> <một hành động>, <biểu cảm, hướng nhìn>; <vai phụ: hành động, biểu cảm, hướng nhìn>.
Right page (secondary): <điểm nhìn, cỡ cảnh, bố cục>; <focus, biểu cảm, hướng nhìn>.
Text wrap: <phần tranh> rises beside the <lower/middle> <left/right> lines.
Mood: <một câu>.
```

## Body lượt màu

Không chép body lượt nét: góc máy và Text wrap khiến GPT dựng lại bố cục. Chỉ
gồm STORY, màu/ánh sáng từng trang và Mood; ánh sáng chung đi qua `--light`.

```text
<STORY: một câu>.
Left page: <tông chủ đạo, ai/vật gì trong sáng hay bóng, điểm nhấn ở focus>.
Right page: <như trên>.
Mood: <một câu>.
```

## Body chỉnh outline

Chỉ ghi điều cần đổi: dịch comment của người dùng sang tiếng Anh, mỗi comment
một dòng `Change:`, gọi rõ vị trí và chủ thể. Không chép lại `Left/Right page:`
của lượt nét (GPT sẽ vẽ lại cả trang). `--cast` chỉ gồm nhân vật bị sửa. Image 1
là outline người dùng đang comment.

Phần cần giữ nguyên ngoài câu mở chung (nền, nhóm người, đạo cụ dễ bị đổi theo)
ghi thành dòng `Keep:` riêng, không viết nối vào cuối dòng `Change:`; script gom
thành khối "Keep unchanged:" ngay sau các dòng Change. Mỗi lượt 1–2 dòng Change
rồi soát ảnh; từ 3 dòng script cảnh báo.

```text
Change: <chủ thể, trang/vị trí>: <thay đổi>.
Keep: <phần phải giữ nguyên>.
```

## Chỉnh màu

Chạy lại lượt màu từ outline được chọn, thêm comment của người dùng vào cuối
body. Không đính kèm ảnh màu đã tạo, trừ lượt `color-edit`.

Nhân vật lệch profile:

- Outline vẽ sai mặt, tai, chiều cao hoặc trang phục: chạy lại lượt màu với
  `--recast <slug>`, hoặc sửa outline bằng `--pass edit --recast <slug>` khi
  cần outline đúng trước khi lên màu.
- Ảnh màu đã ổn, chỉ một nhân vật còn sai: `--pass color-edit --cast <slug>`
  với Image 1 là ảnh màu đó; body trống hoặc vài dòng `Change:` cho lỗi cụ thể.

## Khối bối cảnh

Deliverable mặc định. Viết tiếng Việt, chỉ lấy dữ kiện từ scene sheet, bible và
profile; không đưa chữ, bố cục hay khối STYLE. File `prompts/vNNN-context.md`
gồm metadata và khối trong một code block.

~~~markdown
# Prompt <vNNN> — <layout-slug> p<trái>-<phải> — khối bối cảnh

- Nguồn: `story/<tập>/scenes.md` <Snn> (<trạng thái>), `bible.md` (<mục>),
  profile <slug@vNNN>.
- Hình layout: [layout-ref.png](../layout-ref.png)
- Profile liên quan:
  - Ảnh <N> — <TÊN>: [profile.md](../../../../characters/<slug>/profile.md),
    ảnh ref [<ref>](../../../../characters/<slug>/<ref>)

```text
BỐI CẢNH CẢNH — trang <trái>–<phải>, truyện cuộc đời Đức Phật, miền Bắc Ấn Độ, khoảng thế kỷ 5 trước Công nguyên.

CHUYỆN TRƯỚC ĐÓ
<1–3 câu>

DIỄN BIẾN TRONG CHỮ (để hiểu, không vẽ hết)
<mỗi beat một dòng ngắn>
Hình chỉ vẽ một khoảnh khắc với một hành động focus; các beat còn lại nằm trong chữ.

KHOẢNH KHẮC ĐƯỢC VẼ
<5 mục của phương án active, hoặc "Chưa chọn; chờ phương án.">

THỜI ĐIỂM & ÁNH SÁNG
<thời điểm; cường độ đúng chữ nguồn; hướng sáng; bóng đổ chính>

NƠI CHỐN
<địa hình, tiến độ công trình, vật dụng>

CON NGƯỜI
<nhóm người, nhận diện tĩnh; nhân vật có profile ghi số ảnh>

KHÔNG ĐƯỢC
<việc chưa/không xảy ra, đạo cụ dễ hiểu sai, niên đại liên quan>
```
~~~
