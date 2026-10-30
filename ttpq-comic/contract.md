# Contract flow ttpq-comic

## Phạm vi

- Flow độc lập. Không đọc hoặc áp quy tắc workflow, profile hay skill của
  `comic-illustrator/`, Character Studio, Image Playground, st01–st03 hoặc
  các style cũ. Style dùng chung là `ttpq comic light` theo
  `../docs/project-style-policy.md`; chỉ khi có tu sĩ mới đọc
  `../docs/monastic-robes.md`. Từ root áp các quy tắc chung của
  `AGENTS.md` (ngôn ngữ, điều cấm trong prompt, version, đường dẫn tương đối).
- Deliverable mặc định là context; có thể xuất gói prompt khi được yêu cầu.
  Flow hỗ trợ tạo/chỉnh ảnh khi người dùng yêu cầu trực tiếp ở bước outline
  hoặc màu; không tự tạo ảnh ngay sau context. Ảnh là bản minh họa nháp, chưa
  phải production. Menu và cách thực hiện thuộc skill `ttpq-comic`.
- Mặc định hiện tại chỉ xuất **khối bối cảnh truyện** (tiếng Việt) cho spread;
  gói prompt hai lượt chỉ làm khi người dùng yêu cầu rõ (xem SKILL).
- Pipeline hai lượt:
  1. **Lượt nét (ChatGPT Image):** ảnh clean outline đen trắng của cả spread,
     có chữ VI/EN ôm hình. Chữ trong ảnh chỉ để tham khảo dàn trang.
  2. **Lượt màu (Codex hoặc ChatGPT Image):** tạo minh họa màu theo style ttpq
     comic light. Theo lựa chọn người dùng ngày 2026-10-30, outline được chọn
     chỉ tham khảo scene; nhân vật lấy chuẩn từ profile gốc, không lấy identity
     từ output cũ. `SKIPPED_BY_USER` toàn flow đối với khóa mọi nét/contour và
     dùng output cũ làm chuẩn nhân vật. Giữ chữ đã ôm hình (nội dung, khổ chữ,
     vị trí, ngắt dòng, đường ôm), trừ yêu cầu đổi rõ của người dùng; không hứa
     pixel-lock khi công cụ không chứng minh được.
  Chữ trong ảnh ở cả hai lượt chỉ để tham khảo; chữ in cuối cùng do người dùng
  dàn trong InDesign, không thuộc flow.
- Ảnh được đính kèm khi chạy prompt:
  - Lượt nét: `layout-ref.png` của spread và ảnh ref profile của từng nhân vật
    có profile xuất hiện trong spread.
  - Lượt màu: ảnh nét người dùng chọn và ảnh ref profile như trên.
  Prompt ghi rõ ảnh số mấy là gì. Nhân vật quần chúng và ảnh ý tưởng của người
  dùng được mô tả bằng chữ.
- Cấm dùng output cũ làm ref khi tạo hình mới: không đính kèm, không nhắc tới
  và không mô tả theo ảnh nét/màu đã tạo trước (version cũ của spread, spread
  khác, ảnh trong `prompts/` hay thư mục output). Nhận diện chỉ lấy từ ảnh ref
  profile/setting gốc. Ngoại lệ duy nhất: lượt màu dùng ảnh nét người dùng chọn
  của chính lượt đó.
- Style: [ttpq comic light](../docs/style-ttpq-comic-light.md). Bối cảnh mặc định:
  [Ấn Độ thời Đức Phật](style/era-ancient-india.md).

## Nguồn

- Layout: PDF trong `layouts/`. Mỗi trang PDF là một spread; trang trái tiếng
  Việt, trang phải tiếng Anh. Luôn đọc bằng `read-layout.py`, không chép tay.
- Kịch bản: `story/<tập>/script.md`, toàn văn do người dùng cung cấp, chép
  nguyên văn. Từ kịch bản, flow dựng `bible.md` (nhân vật, địa điểm, tiến độ,
  đạo cụ, điểm cần quyết) và `scenes.md` (timeline cảnh: thời điểm, ánh sáng,
  nơi chốn, nhân vật, được phép, bị cấm, continuity). Mỗi dữ kiện ghi nguồn
  (chương, đoạn). Bối cảnh trong prompt chỉ lấy từ cảnh `APPROVED`; cảnh còn
  `DRAFT` thì trình người dùng duyệt trước.
- Chưa có kịch bản: dùng chữ của spread và các spread liền kề trong cùng PDF.
- Mâu thuẫn giữa kịch bản và lịch sử/era guide (ví dụ cây trồng châu Mỹ): ghi
  vào mục "Cần quyết" của `bible.md`; mặc định theo kịch bản cho tới khi người
  dùng quyết.
- Ghi chú "Hình N" trong layout là chỉ dẫn vẽ, không phải chữ in.
- Chữ EN: ưu tiên bản người dùng cung cấp, rồi bản có sẵn trong layout hoặc
  file chữ EN của spread. Nếu chưa có, agent tự dịch toàn bộ chữ VI của đúng
  spread, tự soát và lưu bản dịch có nguồn/version theo skill; không dừng hỏi
  hoặc yêu cầu duyệt riêng bản dịch. Không ghi đè bản EN hiện có. Khối bối cảnh
  mặc định không cần dịch EN.
- `SKIPPED_BY_USER` — từ 2026-10-29, phạm vi workflow TTPQ Comic: thay quy tắc
  cũ “không tự dịch, dừng hỏi nguồn EN” bằng tự dịch khi chưa có bản EN.
- Nhân vật và bối cảnh chỉ lấy từ `characters/` và `settings/` của flow. Ảnh ref
  do người dùng chỉ định được chép vào đó trước khi mô tả.
- Chỉ dùng `profile.md`/`setting.md` có trạng thái `APPROVED`. Bản `DRAFT` phải
  được người dùng duyệt trước khi đưa vào prompt.

## Thứ tự ưu tiên

1. Yêu cầu trực tiếp mới nhất của người dùng.
2. Layout của đúng spread (chữ, khổ, ghi chú Hình).
3. Scene sheet `APPROVED` và quyết định trong `bible.md`.
4. Profile/setting đã duyệt và ảnh ref của chúng.
5. [book-spec.md](book-spec.md), style và era guide của flow.
6. Giả định sáng tạo của agent.

Override rõ của người dùng ghi `SKIPPED_BY_USER` kèm phạm vi trong `record.md`.

## Version và lưu

- Mỗi spread một thư mục `spreads/<layout-slug>/p<trái>-<phải>/`.
- Gói prompt lưu `prompts/vNNN-spread.md` hoặc `prompts/vNNN-hinh-N.md`, gồm
  prompt lượt nét và lượt màu; khối bối cảnh lưu `prompts/vNNN-context.md`;
  không ghi đè version cũ.
- Ảnh tạo trực tiếp lưu trong `outputs/` của spread, có version mới cho từng
  outline/màu/revision; prompt, vai trò reference và kết quả kiểm ghi trong
  record của lượt. Không tự chuyển vào approved hoặc profile.
- `record.md` ghi mỗi lượt: nguồn đã đọc (đường dẫn, trang), mode, profile/
  setting và version dùng, lựa chọn của người dùng, kết quả tự kiểm.
- Sửa profile/setting thì tăng version mô tả và ghi lý do; prompt cũ giữ nguyên.
