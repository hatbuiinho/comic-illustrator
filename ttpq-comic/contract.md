# Contract flow ttpq-comic

## Phạm vi

- Flow độc lập. Không đọc hoặc áp quy tắc workflow, profile hay skill của
  `comic-illustrator/`, Character Studio, Image Playground hay các style cũ.
  Style mặc định là `ttpq comic light` theo `../docs/project-style-policy.md`,
  riêng lượt màu mặc định `ttpq comic blend`
  (`style/ttpq-comic-blend.md`) từ 2026-11-16; `color-edit` và lượt màu có
  `--recast` mặc định `ttpq real` (`style/ttpq-real.md`) từ 2026-11-22; lượt màu dùng light hoặc
  `ttpq comic soft` (`style/ttpq-comic-soft.md`) khi người dùng gọi tên. Ghi
  tên style đã dùng trong `record.md`.
  Không áp `../docs/monastic-robes.md`; màu y và cách quấn y lấy theo profile
  và ảnh ref của từng nhân vật. Từ root chỉ áp quy tắc chung của `AGENTS.md`
  (ngôn ngữ, điều cấm trong prompt, version, đường dẫn tương đối).
- Deliverable mặc định là **khối bối cảnh** tiếng Việt của spread. Flow tạo
  hoặc chỉnh ảnh khi người dùng yêu cầu trực tiếp. Ảnh là bản nháp để dàn trang,
  chưa phải production. Menu và cách làm thuộc skill `ttpq-comic`.
- Pipeline hai lượt:
  1. **Lượt nét:** clean outline đen trắng cả spread, chữ ôm hình.
  2. **Lượt màu:** vẽ màu theo style từ outline người dùng chọn. Outline dùng
     cho scene và chữ; nhận diện nhân vật theo profile gốc.
- Chữ trong ảnh chỉ để dàn trang tương đối, sẽ bị bỏ trước khi đưa vào
  InDesign. Trang trái giữ chữ VI của layout; trang phải là chữ tiếng Anh giữ
  chỗ cùng độ dài, do model tự sinh. Không dịch và không lưu bản EN.
- Chỉnh ảnh theo cách tự nhiên: đính kèm ảnh người dùng đang comment và ghi
  comment đó. Lượt màu sửa bằng cách vẽ lại từ outline được chọn, không sửa
  trên ảnh màu, trừ khi người dùng yêu cầu rõ.
- Không dùng output cũ làm chuẩn nhân vật. Nhận diện chỉ lấy từ ảnh ref
  profile/setting. Ảnh được phép đính kèm: layout (lượt nét), outline được
  chọn (lượt màu), outline đang sửa (chỉnh outline) và ảnh ref profile.

## Nguồn

- Layout: PDF trong `layouts/`, mỗi trang PDF là một spread. Luôn đọc bằng
  `read-layout.py`, không chép tay. Ghi chú "Hình N" là chỉ dẫn vẽ, không
  phải chữ in.
- Kịch bản: `story/<tập>/script.md`, chép nguyên văn. Từ kịch bản dựng
  `bible.md` và `scenes.md`. Mỗi dữ kiện ghi nguồn (chương, dòng).
- Mỗi cảnh `Snn` có dòng **Profile:** liệt kê slug nhân vật có profile. Đây là
  nguồn để script ghép prompt tự lấy ảnh ref. `bible.md` có mục "Avoid trong
  prompt" và "Cặp dễ nhầm" cho script dùng.
- Chưa có kịch bản: dùng chữ của spread và các spread liền kề.
- Mâu thuẫn giữa kịch bản và lịch sử/era guide: ghi vào "Cần quyết" của
  `bible.md`; mặc định theo kịch bản cho tới khi người dùng quyết.
- Nhân vật và bối cảnh chỉ lấy từ `characters/` và `settings/`. Chỉ dùng
  profile/setting `APPROVED`; bản `DRAFT` phải được duyệt trước.

## Thứ tự ưu tiên

1. Yêu cầu trực tiếp mới nhất của người dùng.
2. Layout của đúng spread (chữ, khổ, ghi chú Hình).
3. Cảnh trong `scenes.md` và quyết định trong `bible.md`.
4. Profile/setting đã duyệt và ảnh ref.
5. [book-spec.md](book-spec.md), style và era guide.
6. Giả định sáng tạo của agent.

Override rõ của người dùng ghi `SKIPPED_BY_USER` kèm phạm vi trong `record.md`.

## Version và lưu

- Mỗi spread một thư mục `spreads/<layout-slug>/p<trái>-<phải>/`.
- Khối bối cảnh lưu `prompts/vNNN-context.md`; prompt ảnh lưu
  `prompts/vNNN-<outline|color|edit>.txt`; ảnh lưu `outputs/` với version mới.
  Không ghi đè.
- `record.md` ghi ngắn mỗi lượt: file prompt, ảnh đính kèm, file ảnh ra và
  comment của người dùng. Không tự chuyển ảnh vào approved hoặc profile.
- Sửa profile/setting thì tăng version mô tả và ghi lý do.
