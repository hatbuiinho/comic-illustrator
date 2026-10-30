---
name: ttpq-comic
description: Chuẩn bị context truyện và menu lệnh cho spread trong ttpq-comic; đọc context, đề xuất hoặc tiếp nhận phương án minh họa, tạo/chỉnh clean outline và ảnh màu theo từng yêu cầu trực tiếp. Mặc định chỉ xuất context; hỗ trợ gói prompt khi được yêu cầu. Độc lập với comic-illustrator và hai studio.
---

# TTPQ Comic — gói prompt cho spread

Đọc trước mỗi phiên: [contract](../../../ttpq-comic/contract.md),
[book-spec](../../../ttpq-comic/book-spec.md),
[style](../../../ttpq-comic/style/ttpq-comic.md),
[era guide](../../../ttpq-comic/style/era-ancient-india.md).
Không đọc hoặc gọi tài liệu, skill của `comic-illustrator/`, hai studio hay
các style cũ. Riêng style dùng chung toàn dự án là `ttpq comic light` theo
`docs/project-style-policy.md`; chỉ khi có tu sĩ mới đọc `docs/monastic-robes.md`.

Giá trị của flow là phần ChatGPT không tự biết: **bối cảnh truyện** và **ý đồ
điện ảnh**. Ảnh layout và ảnh profile lo phần chữ và nhận diện; prompt giữ ngắn
và đặt bố cục lên trước.

## Deliverable mặc định: khối bối cảnh

Hiện tại flow chỉ xuất **khối bối cảnh truyện** cho spread; người dùng tự ghép
với yêu cầu, style và ảnh layout trên ChatGPT.

- Chạy bước 0–3, rồi viết khối theo
  [mẫu khối bối cảnh](references/prompt-template.md#khối-bối-cảnh), lưu
  `prompts/vNNN-context.md`, tự kiểm theo mục "Khối bối cảnh" của
  [checklist](references/prompt-checklist.md), ghi `record.md`.
- Bỏ bước 4–6 (mode, ý đồ điện ảnh, gói prompt hai lượt). Không cần chữ VI/EN
  và không dừng khi trang phải chưa có chữ EN.
- Khi trình, trả đủ ba phần:
  1. **Khối bối cảnh** trọn trong một code block.
  2. **Hình layout của spread:** link `layout-ref.png` trong thư mục spread.
  3. **Profile nhân vật liên quan:** mỗi nhân vật có profile một dòng gồm số
     ảnh trong khối bối cảnh, link `profile.md` (trạng thái, version) và link
     ảnh ref. Nhân vật chưa có profile: ghi "chưa có profile, mô tả trong
     khối".
- Chỉ làm gói prompt hai lượt (bước 4–7) khi người dùng yêu cầu rõ.

## Hội thoại

- Flow tương tác context → đọc hiểu → phương án → outline → revision → màu:
  đọc [menu lệnh và tạo ảnh](references/interactive-flow.md) khi trình context
  hoặc xử lý một bước của flow này. Cuối phản hồi context luôn đề xuất nguyên
  câu đọc context trong reference, sau ba phần deliverable; không chèn vào
  khối bối cảnh. Chỉ hiện menu phù hợp bước hiện tại, không đổ toàn bộ menu.
  Sau khi đọc hiểu context, trình hai lựa chọn về phương án theo reference;
  chưa tự tạo phương án hoặc chuyển thẳng sang bước tạo ảnh.
  Sau mỗi bản outline mới hoặc chỉnh sửa, trình đủ menu sửa / tạo lại / dàn
  trang màu trong reference; luôn có prompt dàn trang màu nguyên văn.
- Mặc định vẫn dừng sau context. Lệnh tạo outline/màu là yêu cầu tạo ảnh trực
  tiếp trong chính flow này; không route sang workflow page hay studio và
  không hỏi lại quyền tạo ảnh. Prompt cố định của người dùng giữ nguyên văn.
- Mỗi lượt hỏi một quyết định chính; tự đọc dữ kiện có sẵn, không hỏi lại điều
  đã chốt trong `record.md`/`brief.md` còn hiệu lực.
- Khi chờ người dùng chọn, đưa mỗi câu trả lời mẫu trong một code block riêng.
- Mỗi prompt hoàn chỉnh nằm trọn trong một code block để copy.

## 0. Story bible (một lần cho mỗi tập)

Khi người dùng đưa kịch bản tập, hoặc `story/<tập>/` chưa có `bible.md`/`scenes.md`:

1. Chép nguyên văn vào `ttpq-comic/story/<tập>/script.md`.
2. Viết `bible.md` theo [mẫu story](references/story-template.md): nhân vật
   (vai trò, chương xuất hiện, profile có chưa), địa điểm và vùng, tiến độ/trạng
   thái thay đổi theo thời gian, đạo cụ xuyên suốt, điều cấm chung, **Cần quyết**
   (mâu thuẫn kịch bản–lịch sử, kịch bản tự mâu thuẫn).
3. Viết `scenes.md`: mỗi cảnh một mục `Snn` theo mẫu, trạng thái `DRAFT`.
4. Trình tóm tắt và các điểm Cần quyết; người dùng duyệt từng phần → `APPROVED`.

Dữ kiện phải có nguồn (chương, câu mở đầu đoạn); suy luận ghi rõ "suy ra".
Khi kịch bản đổi, tăng version và ghi lại cảnh bị ảnh hưởng.

## 1. Xác định spread

Khóa file layout trong `ttpq-comic/layouts/` và spread (số trang sách, ví dụ
54–55, hoặc số trang PDF). Thư mục làm việc:
`ttpq-comic/spreads/<layout-slug>/p<trái>-<phải>/` (số trang 3 chữ số).

## 2. Đọc layout và bối cảnh truyện

```bash
scripts/run-with-tools.sh -- python3 .agents/skills/ttpq-comic/scripts/read-layout.py "ttpq-comic/layouts/<file>.pdf" --folio <số trang trái> --out "ttpq-comic/spreads/<layout-slug>/p<trái>-<phải>"
```

Dùng `--page <n>` thay `--folio` nếu biết số trang PDF. Ánh xạ chữ của spread
vào cảnh `Snn` trong `scenes.md` (ghi vào `brief.md`). Chưa có story bible: đọc
thêm ít nhất một spread trước và một spread sau (bỏ `--out`, script in JSON ra stdout).

Trình snapshot ngắn:

- **Chữ:** mỗi trang — ngôn ngữ, số dòng, số đoạn.
- **Hình:** từng "Hình N" — trang, vị trí (%), ghi chú vẽ; không có ghi chú thì
  suy khoảnh khắc từ chữ.
- **Chữ tô màu:** cụm trong `marks` là dấu biên tập; nếu ý nghĩa màu chưa ghi
  trong `record.md` của layout này, hỏi người dùng một lần.
- **Bối cảnh truyện:** cảnh `Snn` tương ứng và trạng thái (`APPROVED`/`DRAFT`);
  thời điểm, nơi chốn, được phép, bị cấm, continuity lấy từ scene sheet. Cảnh
  còn `DRAFT` thì trình phần liên quan để người dùng duyệt trước khi viết prompt.
- **Cảnh báo:** từ script.

Khi cần chữ EN cho trang phải, ưu tiên bản người dùng cung cấp, rồi bản EN
đã có trong layout hoặc `text-en.md` của spread. Nếu chưa có, tự dịch toàn bộ
chữ VI của đúng spread sang tiếng Anh, không dừng để hỏi hoặc yêu cầu duyệt
riêng bản dịch. Giữ đủ nội dung, thứ tự đoạn, lời thoại, tên riêng và nghĩa
thuật ngữ Phật giáo; không dịch ghi chú Hình hoặc dấu biên tập thành chữ in.
Tự soát đối chiếu VI–EN, lưu bản dịch vào `text-en.md` (nếu đã có file thì tạo
`text-en-vNNN.md`, không ghi đè), ghi rõ agent dịch từ nguồn nào trong
`record.md` và metadata prompt. Chép nguyên bản EN đã chọn vào prompt; bản
người dùng cung cấp sau đó được ưu tiên ở version mới. Khối bối cảnh mặc định
vẫn không cần dịch EN.

## 3. Nhân vật và bối cảnh

Liệt kê nhân vật/bối cảnh xuất hiện; tìm `ttpq-comic/characters/<slug>/profile.md`
và `ttpq-comic/settings/<slug>/setting.md`.

- Có bản `APPROVED`: dùng ảnh ref (người dùng đính kèm khi chạy) và dòng nhận
  diện ngắn. Profile cũ chỉ có khối prompt dài: rút dòng nhận diện từ mục "Dấu
  hiệu bắt buộc".
- Chưa có: xin người dùng ảnh ref, chép vào thư mục đó (`ref-v001.png`), viết
  mô tả theo [mẫu profile](references/profile-template.md) /
  [mẫu setting](references/setting-template.md) ở trạng thái `DRAFT`, chờ duyệt.
- Nhân vật quần chúng: mô tả ngắn trong prompt theo chữ của truyện và era guide.

## 4. Chọn mode

Hỏi người dùng (ghi `brief.md`):

- **spread:** một gói prompt cho cả spread; các Hình gộp thành một tranh liền.
- **frame:** mỗi "Hình N" một gói prompt; chữ mỗi trang gắn với Hình lớn nhất
  trên trang đó (Hình vắt qua gáy mang chữ cả hai trang).

## 5. Ý đồ điện ảnh

Đưa 2–3 phương án (hoặc dựng từ ảnh ý tưởng nếu người dùng gửi). Mỗi phương án
tách đầu dòng:

- **Khoảnh khắc:** hành động/cảm xúc được chọn, dựa trên chữ và bối cảnh truyện.
- **Cỡ cảnh, góc máy.**
- **Vị trí:** nhân vật chính ở trang nào, khoảng x/y theo % canvas; gáy (x 45–55%)
  chỉ có nền.
- **Đường mắt:** người xem đi từ đâu tới đâu.
- **Chữ ôm hình:** phần tranh nào vươn vào vùng chữ, chữ ôm theo đường viền nào.
- **Ánh sáng:** nguồn sáng, thời điểm (theo truyện).
- **Đánh đổi.**

Người dùng chọn → ghi `brief.md` (bối cảnh truyện + ý đồ đã chọn).

## 6. Viết gói prompt

Mục này là nhánh xuất gói prompt theo yêu cầu, không tự áp thay cho flow tương
tác. Khi người dùng dùng prompt cố định outline/màu, ưu tiên reference
`interactive-flow.md`; đặc biệt lượt màu không khóa nét/identity theo outline.

Ghép theo [mẫu gói prompt](references/prompt-template.md), gồm:

- **Lượt nét — tin 1:** khối STYLE clean outline (chép nguyên).
- **Lượt nét — tin 2:** yêu cầu + DIRECTOR'S NOTES + chữ EN (nếu trang phải của
  layout là chữ giữ chỗ). Đính kèm `layout-ref.png` và ảnh ref profile.
- **Lượt màu:** một prompt: khối STYLE màu + yêu cầu giữ nét, bố cục và chữ +
  nhận diện nhân vật + ánh sáng/màu của cảnh. Đính kèm ảnh nét và ảnh ref profile.

Quy tắc viết:

- Tin 2 của lượt nét và prompt lượt màu, không tính khối chữ EN, giữ khoảng
  ≤ 4.000 ký tự. Bố cục và vị trí đặt trước; chỉ đưa chi tiết era liên quan cảnh.
- Mọi vị trí theo % canvas 1536×1024 (spread) hoặc canvas của mode frame.
- Mỗi ảnh đính kèm có dòng "Image N = …"; nói rõ ảnh profile chỉ để nhận diện,
  không chép nền, ánh sáng hay tư thế.
- Cấm ref output cũ: không đính kèm, nhắc tới hay mô tả theo ảnh nét/màu đã
  tạo trước (version cũ, spread khác). Muốn giữ ý từ ảnh cũ thì viết lại bằng
  chữ trong Director's Notes. Ngoại lệ: ảnh nét đã chọn đính kèm ở lượt màu
  của chính spread/frame đó, hoặc người dùng override rõ (ghi
  `SKIPPED_BY_USER`).
- Ghi đạo cụ và hành động dễ bị hiểu sai bằng cả điều đúng lẫn điều cấm (ví dụ
  "rolled leather plan, not a board").
- Điều cấm áp dụng (style, era, theo bối cảnh truyện) nằm trong prompt từ đầu.

Lưu `prompts/vNNN-spread.md` hoặc `prompts/vNNN-hinh-N.md`.

## 7. Tự kiểm và trình

Kiểm theo [checklist](references/prompt-checklist.md), sửa đến khi đạt. Ghi
`record.md`: nguồn đã đọc, mode, profile/setting và version, lựa chọn, kết quả
kiểm, `SKIPPED_BY_USER` nếu có. Trình gói prompt (mỗi tin một code block), ghi
rõ ảnh cần đính kèm ở mỗi lượt và rủi ro còn lại.
