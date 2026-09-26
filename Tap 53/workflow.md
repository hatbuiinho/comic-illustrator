# Workflow tạo shot — Tập 53

Đây là router quy trình duy nhất. Quy tắc nội dung nằm trong `notes.md`, ngôn
ngữ điện ảnh trong `shot_notes.md`, schema trong `workflow_schema.md`, mẫu
duyệt/QA trong `workflow_templates.md`.

Ưu tiên: yêu cầu mới nhất → `notes.md` → `shot_notes.md` → file này → file phụ.

## Tooling đọc và kiểm chứng

Khi server có sẵn tool tương ứng, ưu tiên dùng tool native để lấy bằng chứng,
không suy đoán từ preview chat: `pdfinfo`/`pdftotext` kiểm tra metadata và text
PDF; `pdftoppm`/`pdftocairo` rasterize đúng trang layout; `qpdf --check` kiểm tra
cấu trúc PDF; Tesseract (`vie`, `eng`, `osd`) OCR khi text layer thiếu hoặc cần
đối chiếu; ImageMagick (`identify`, `convert`, `montage`) kiểm tra/kết hợp ảnh;
WebP tools xử lý định dạng WebP; `exiftool` và `file` xác nhận metadata/định dạng
thực. Kết quả đọc được phải ghi vào `sourceRead` hoặc artifact QA liên quan.

## Nguyên tắc

- Mỗi ảnh là một shot có một focus và một ý nghĩa kịch tính.
- Chiều sâu là kết quả của thiết kế không gian 2D: chồng lớp khi cần, chênh lệch
  tỉ lệ, silhouette, khoảng trống và giảm chi tiết theo khoảng cách. Không dùng
  blur, DOF, tia sáng thể tích, texture hay render để thay thế bố cục. Mọi shot
  phải có chủ đích không gian và hierarchy, nhưng không buộc phải có đủ ba lớp
  vật lý hoặc một vật che khung.
- Focus chỉ quyết định thứ bậc nhìn, không được loại chi tiết kịch bản bắt buộc.
  Thành phần ngoài focus phải có vai trò rõ; chi tiết bắt buộc có thể giản lược
  ở lớp nền nhưng vẫn phải đọc đúng ý nghĩa.
- Focus có thể là cá nhân, quan hệ, tập thể, hoạt động chung, không gian hoặc
  dấu vết. Không mặc định ít người mới rõ focus. Thứ tự thiết kế là ý nghĩa
  kịch bản → trải nghiệm người đọc → bằng chứng thị giác → cách kể và bố cục
  → số người hiện trong khung; không dùng một con số chọn trước để thu hẹp ý tưởng.
- Sáu cổng chạy tuần tự; `FAIL`, `pending`, `chưa chắc` hoặc thiếu nguồn chặn cổng.
- Lỗi ở đâu quay lại cổng sớm nhất gây lỗi; không vá prompt hay đổi status.
- “Tiếp tục/triển khai/process” không cho phép bỏ cổng. Ngoại lệ phải được người
  dùng chỉ rõ và ghi cùng rủi ro.
- Hard lock luôn bắt buộc. Conditional lock phải ghi `applicable` và lý do.
- PASS dựa trên nguồn hoặc bằng chứng nhìn thấy, không dựa vào prompt/manifest
  ghi đúng tên.

### Khóa nguồn và suy luận

- Mỗi nhận định phải là `sourceFact`, `userConfirmed` hoặc `assistantInference`.
- Layout chỉ cung cấp hình học, frame, text, gáy và safe zone; không tự suy
  focus, cảm xúc, số người hay `narrativeFunction` từ hình học layout.
- `assistantInference` chỉ là đề xuất; chưa được xác nhận thì không được tạo
  hard lock, giảm quy mô nguồn hoặc làm căn cứ cho suy luận tiếp theo.
- “Nhẹ/chuyển cảnh/không khí” được xử lý bằng cỡ cảnh, scale, khoảng trống và
  hierarchy, không mặc định giảm số người. Gáy chỉ buộc từng recognition core
  tránh vùng nguy hiểm, không buộc toàn bộ chủ thể về một phía.

## Action bắt buộc sau mỗi gate

Sau báo cáo của **mọi G1–G6**, phải luôn đưa một hoặc nhiều action hoàn chỉnh để
người dùng copy trực tiếp. Mỗi action nằm trong **một code block riêng**, không
chỉ là câu hỏi hoặc nhãn nút mô phỏng.

- Gate PASS nhưng chưa cần người dùng quyết định: đưa action tiếp tục sang gate
  kế tiếp, ví dụ `Tiếp tục G2: <page/frame>`.
- Gate cần chọn option, xác nhận storyboard/composition hoặc chọn output: đưa
  action chính xác tương ứng trong `workflow_templates.md`; không dùng câu
  mơ hồ như “bạn xác nhận nhé”.
- Gate FAIL hoặc thiếu bằng chứng: đưa tối thiểu một action sửa/quay lại đúng
  gate gây lỗi và một action giữ/dừng nếu người dùng muốn xem lại. Không tự đi
  tiếp qua gate FAIL.
- Khi có 2–3 lựa chọn thực tế, liệt kê ngắn theo số trước, rồi đặt từng action
  copy riêng bên dưới. Action phải dùng tiếng Việt tự nhiên và chứa page/frame,
  option hoặc output cụ thể, không để placeholder trong câu trả lời cho user.
- Ghi nguyên văn action người dùng đã chọn vào `userAction`; chỉ action rõ ràng
  mới được coi là xác nhận.

## Routing bắt buộc

| Việc | Phải đọc |
| --- | --- |
| Mọi frame | `notes.md`, `shot_notes.md`, script, layout/PDF, phần Core của `workflow_schema.md` |
| Có nhân vật | Phần Profile của `workflow_schema.md` và profile art |
| Có background | Phần Location của `workflow_schema.md` |
| Có hậu quả/vật liệu/quan hệ/cử chỉ | Conditional lock tương ứng |
| Thiết kế composition | `storyboard_composition_reference.md`; guide cần dùng trong `composition_guides/` |
| Duyệt hoặc QA | `workflow_templates.md` |

Ghi file thực sự đã đọc vào `optionAlignment.sourceRead`.

## G1 — Source và context

Trước hết lập `sceneMeaning`: ý nghĩa cốt lõi, quy mô, quan hệ và tính chất tập
thể nếu có; ghi bằng chứng từ script và những cách hiểu sai phải tránh. Tách
điều nguồn xác nhận, hàm ý mạnh, phần chưa rõ và lựa chọn tạo hình. Nguồn nói
"nhiều người" thì giữ ý nghĩa về quy mô, không tự suy ra tổng số chính xác.

Đọc đúng tập/part/page, script trước-sau, layout, profile và asset. Lập
`contextSnapshot`, `narrativeInferenceLock`, `backgroundContinuityLock`,
`locationIdentityLock`, `visualComponentLock`; với exterior bắt buộc lập
`geographyLock` (địa hình, đường chân trời, quy mô không gian, vegetation/water
có bằng chứng và landform bị cấm); thêm `causalStateLock` và
`materialSemanticsLock` khi áp dụng. Lập `printTrimLock` cho mọi output bằng
tỷ lệ chuẩn hoá theo từng trục: `trimPercent: {x: 1,049%, y: 1,478%}` và
`criticalSafePercent: {x: 2,797%, y: 3,941%}`. Đây là quy đổi từ khổ gốc
`286 × 203 mm` (tương ứng 3 mm xén và 8 mm critical-safe), chỉ dùng làm nguồn
tỷ lệ; không ghi hoặc áp trực tiếp mm/pixel lên canvas hay frame có kích thước
khác. Phân loại theo ý nghĩa thay vì tên vật thể:
`narrativeCritical` (chỉ các chi tiết được shot thesis xác nhận là thiết yếu),
`recognitionCore` của location anchor, và `cropBuffer` (trời, đất, đá, cây, gỗ
phụ). Narrative-critical phải nguyên vẹn và có `perceptualBreathingRoom`;
recognition core phải an toàn nhưng phần kéo dài/lặp lại của anchor có thể bị
xén; crop buffer nên được vẽ rộng qua mép.

G1 ghi hình học vùng xén và dữ kiện nguồn; việc chốt chi tiết hiện trong khung,
`narrativeCritical`, `visibilityPriority` và crop boundary thực hiện ở G2 sau
khi đã lập trải nghiệm người đọc và shot thesis. Không tự động coi mặt, bàn tay,
cử chỉ hay đạo cụ là critical. Khi chốt, mỗi chi tiết có đúng một cấp:

- `requiredComplete`: bắt buộc thấy trọn vì mang focus/ý nghĩa chính;
- `requiredReadable`: chỉ cần đủ hình dạng và ngữ nghĩa; được crop có chủ ý;
- `optionalSupport`: có thể crop hoặc bỏ nếu làm shot rõ và giàu cảm xúc hơn;
- `outOfFrame`: chủ động không xuất hiện.

`shotThesis` và `emotionLock` quyết định cấp này trước khi áp dụng trim-safe;
không nâng cấp chi tiết chỉ vì nó là mặt, tay hoặc đạo cụ.

Với nhân vật, lập `characterProportionLock`: tỷ lệ đầu–cổ–vai–thân–tay theo
profile, scale đồng nhất của toàn nhân vật và crop boundary. Cấm tuyệt đối việc
co/ép thân hoặc rút ngắn tay để lọt safe zone trong khi giữ nguyên kích thước
đầu. Xử lý xén chỉ bằng đổi cỡ máy, dịch chuyển hoặc scale **toàn bộ nhân vật
đồng nhất**, và/hoặc mở rộng crop buffer của background.

Location lock phải lập danh mục ít nhất ba neo nhận diện không chỉ là vật liệu
chung; mỗi shot chỉ bắt buộc hiển thị số neo tương ứng với cỡ máy. Ghi một
`sharedArchitecturalAnchor` cho shot cùng nơi, generic misreadings và
`removalRiskCheck` cho negative prompt.

Exit: timeline, người có mặt, trạng thái, location và component không mơ hồ,
có proof trực tiếp; `sceneMeaning` giữ đúng quy mô và quan hệ của nguồn. Thiếu
proof cho một khẳng định thì dừng khẳng định đó, không sáng tác thành fact;
số người chưa xác định trong nguồn được ghi chưa rõ, không tự nó chặn G2.

## G2 — Frame và shot design

Thiết kế theo thứ tự dưới đây; các mục chi tiết phía sau phục vụ thứ tự này:

1. Đọc `sceneMeaning` và hình học frame đã đo ở G1.
2. Lập `emotionalFlowMap`, ghi riêng `readerExperience`: người đọc cần hiểu gì,
   cảm nhận gì và bằng chứng nhìn thấy nào dẫn đến điều đó. Không lấy biểu cảm
   nhân vật làm câu trả lời thay cho cảm nhận của người đọc.
3. Từ bằng chứng cần thấy, xác định focus, vai trò các nhóm, khoảnh khắc, điểm
   nhìn và cỡ cảnh cho các hướng kể khác nhau; chưa áp trần số người tùy ý.
4. Lập `compositionStrategy` và `spatialDepthPlan`: tổ chức thứ bậc bằng tỷ lệ,
   vị trí, tương phản màu phẳng, hướng nhìn, cử chỉ, chồng lớp, nhịp nhóm và
   khoảng trống. Chọn các cách có ích cho shot, không buộc dùng đủ mọi cách.
5. Lập `populationPlan`, chốt mức hiện diện, visibility và crop để phác card.
   Ghi số dự kiến hoặc khoảng linh hoạt có lý do; khóa chính xác chỉ khi có
   căn cứ từ script hoặc bố cục. Số người trên card là phương án staging,
   không tự động là tổng số trong câu chuyện hay hard lock của mọi variant.
6. Chạy `meaningPreservationCheck` trên từng card trước khi trình option.
   Đây là kiểm tra bên trong G2, không thêm một gate duyệt của người dùng.

`populationPlan` phân biệt số tồn tại trong cảnh, số hiện trong khung và số cần
đọc rõ. Mỗi nhóm có vai trò, hoạt động/quan hệ và mức đọc cần thiết; nhóm mang
ý nghĩa cộng đồng không được biến thành chấm nền vô nghĩa. Không buộc thấy toàn
bộ đám đông hoặc từng gương mặt nếu bằng chứng còn lại truyền đúng ý nghĩa.
Khi không có người, ghi không áp dụng và lý do.

`meaningPreservationCheck` đối chiếu card với `sceneMeaning` và
`readerExperience`: đã giản lược gì; bằng chứng nào vẫn giữ quy mô, quan hệ và
cảm xúc; còn nguy cơ đọc sai gì? FAIL nếu focus rõ nhưng mất bản chất cảnh.
Sửa cách kể/bố cục trước khi trình; không chữa bằng thêm người máy móc. Ví dụ,
bữa nghỉ chung của nhiều người xa lạ phải còn đọc được tính cộng đồng; một cặp
trò chuyện chỉ đủ khi cách dựng cảnh vẫn cung cấp bằng chứng về bữa nghỉ chung.

Ghi frame vào `layout_frames.json`: box/shape/tỷ lệ, text reserve, spine, safe
zone, vùng xén theo `trimPercent`, critical-safe theo `criticalSafePercent`, visibility priority,
recognition cores và crop buffers. Artwork vẫn phủ kín frame/page gốc; không
thu nhỏ ảnh để né xén. Safe geometry là mức tối thiểu kỹ thuật, không phải mục
tiêu đặt chủ thể: nhân vật/focus phải có khoảng thở cảm nhận phù hợp với shot,
không để `requiredComplete` bị cắt hoặc silhouette bị ép sát mép. Chi tiết
`requiredReadable` được crop có chủ ý nếu vẫn đọc đúng và không cắt vụng tại
khớp; `optionalSupport` có thể ra khỏi khung. Background
phụ được phép và nên kéo rộng qua vùng xén khi điều đó tạo crop tự nhiên. Lập `frameReadabilityLock`,
`shotThesis`, `emotionLock`, `profileFidelityLock`; thêm `beatMap`,
`identityConflictCheck`, `relationalFocusLock`, `gestureSemanticsLock` khi áp dụng.
`narrativeFunction` chỉ được ghi kèm nguồn; nếu là `assistantInference` thì
không được coi là dữ kiện hoặc dùng để giới hạn bố cục.

Frame xanh được coi là `contentFrame` — vùng nội dung chính — thay vì biên cứng
của toàn canvas. Khi cần, lập `blendExtensionLock` để cho phép canvas rộng/cao
hơn frame: ghi phần mở rộng ở từng cạnh, loại nền được phép dùng, vùng dự kiến
mask/hòa gradient trong InDesign và các chi tiết tuyệt đối không được đi vào
vùng này. Mọi `requiredComplete`, `requiredReadable`, focus, gương mặt, bàn tay,
cử chỉ và đạo cụ kể chuyện phải nằm an toàn trong `contentFrame`.

Trước khi chọn cỡ cảnh hoặc phác composition, lập `emotionalFlowMap` cho toàn
chuỗi frame liên quan. Map phải ghi: người đọc đã biết/đã thấy gì ở shot trước;
câu hỏi cảm xúc còn mở; nhân vật đang trải qua cảm xúc; người/vật/hành động gây
ra cảm xúc; bằng chứng cụ thể người đọc cần trực tiếp nhìn thấy; loại chuyển
cảnh (`người nhìn → điều được nhìn`, `hành động → phản ứng`, `chi tiết → ý nghĩa
rộng hơn`, `nguyên nhân → hệ quả`, hoặc loại khác có căn cứ); focus được chuyển
từ đâu sang đâu; và nơi ánh nhìn/cảm xúc cần đọng lại ở cuối chuỗi.

Không mặc định nhân vật chính phải giữ focus hoặc xuất hiện trong mọi frame.
Nếu một người/nhóm người là đối tượng người đọc cần hiểu hoặc đồng cảm, không
được giản lược họ thành silhouette/background chỉ để bảo vệ hierarchy, trừ khi
ý đồ là giữ họ vô danh và vẫn có đủ bằng chứng thị giác khác cho cảm xúc. Cảm
xúc phải nảy sinh từ chi tiết quan sát được trong kịch bản — tư thế, cử chỉ,
khoảng cách, dấu vết đời sống, trạng thái không gian — thay vì chỉ dựa vào biểu
cảm báo hiệu như cùng cười, cùng khóc hoặc cùng chắp tay.

Sau đó viết `cinematicIntent` cho từng shot: người đọc đứng cùng ai (hoặc vị
trí quan sát trung tính), khoảnh khắc cụ thể, focus duy nhất, thông tin/cảm xúc
mới so với shot trước, bằng chứng thị giác, thứ tự đọc hình, một cử chỉ/dấu vết
chính, phần thông tin chủ động để ngoài khung, và cách shot chuẩn bị cho shot
sau. Nếu shot chỉ lặp lại cảm xúc/thông tin đã có, hoặc người đọc không thể thấy
vì sao nhân vật xúc động, phải chọn lại khoảnh khắc, cỡ cảnh hoặc điểm nhìn.

Lập thêm `spatialDepthPlan` cho từng option trước khi vẽ card, gồm:

- `foregroundLayer`: vật/khối ở gần khung **hoặc chủ ý để trống**, nếu có thì
  ghi mức che khung và vai trò dẫn mắt;
- `midgroundLayer`: focus hoặc hành động chính **hoặc chủ ý để trống**, scale và
  silhouette đọc được;
- `backgroundLayer`: neo bối cảnh/cảnh xa **hoặc mảng không gian chính**, mức
  giảm chi tiết và vai trò tạo quy mô hay khoảng lặng;
- `depthOrder`: thứ tự chồng lớp, các đường dẫn mắt và tương phản mảng phẳng
  đưa mắt về focus;
- `negativeSpace`: vùng trống có chủ đích, ý nghĩa cảm xúc và tương thích text;
- `hierarchyCheck`: cách người đọc nhận ra trọng tâm và đọc tiếp các lớp hỗ trợ;
  nếu focus là tập thể, nêu cách các nhóm hợp thành một trọng tâm. Giữ nhóm
  mang bằng chứng đủ rõ, không loại người chỉ để giảm cạnh tranh thị giác.

Chọn số lớp theo `shotThesis`, không khí và tỷ lệ frame; hai lớp, một lớp rộng
có chủ ý, hoặc ba lớp đều hợp lệ nếu hierarchy, eye path và ý nghĩa vẫn rõ.
`spatialDepthPlan` phải ghi các lớp có mặt và các lớp cố ý vắng mặt, cùng lý do
(`depthRationale`); không coi việc ít hơn ba lớp là ngoại lệ hay lỗi. Lớp gần có
thể là vai/lưng nhân vật, khung cửa, cột, mép mái, cây, đạo cụ hoặc silhouette
kiến trúc, nhưng không thêm vật che khung chỉ để đạt đủ lớp. Background xa tạo
độ sâu bằng tỉ lệ và độ giản lược đồ họa, không được làm mờ kiểu ống kính.

Đối chiếu shot liền kề bằng `shotVariationCheck`: cự ly, điểm nhìn hoặc hướng
quan sát phải thay đổi có lý do theo nhịp kể. Hai shot liên tiếp chỉ khác vị trí
nhân vật trong cùng góc ngang/toàn thân bị coi là lặp shot và phải thiết kế lại,
trừ khi sự lặp lại là chủ ý được ghi rõ để tạo nhịp. Biến thiên máy quay tự nó
không tạo flow: chuỗi chỉ PASS khi mỗi shot mang thông tin mới, focus transfer
rõ và điểm kết thị giác khớp điểm đọng cảm xúc trong `emotionalFlowMap`.

Lập `intentionalCropLock` cho mọi nhân vật/đạo cụ chạm hoặc vượt khung: crop
boundary, phần được giữ, phần chủ động ngoài khung, lý do kể chuyện, vùng/khớp
cấm cắt và bằng chứng crop tự nhiên ở kích thước layout.

Trước khi duyệt composition, kiểm `anatomySilhouetteGate`: đặt đầu, cổ, vai,
thân và tay trên cùng một hệ tỷ lệ tự nhiên theo profile. Nếu cần đưa critical
vào safe zone mà phải biến dạng riêng một phần cơ thể, composition FAIL và phải
đổi framing/placement; không được coi đó là giải pháp trim.

Chạy `priorityConflictGate`: nếu việc bảo vệ tay, đạo cụ, location anchor hoặc
trim làm yếu emotion/eye path, làm focus quá nhỏ hay buộc tư thế tạo dáng, card
FAIL. Hạ chi tiết hỗ trợ xuống cấp phù hợp, bỏ khỏi khung hoặc đổi framing; không
hy sinh shot thesis để giữ đủ mọi thành phần.

Profile art là nguồn identity chính. Nếu công cụ hỗ trợ visual reference, phải
truyền đúng profile và ghi mapping. Không generate shot identity-sensitive bằng
text-only khi thiếu reference.

Profile phải được đọc lại từ file gốc trước **mỗi lần** tạo mới, reprocess,
chỉnh sửa hoặc tạo variant có nhân vật; việc đã đọc profile ở vòng trước không
được coi là còn hiệu lực cho vòng hiện tại. Output gần nhất, ảnh trung gian,
composition card và overlay chỉ được dùng làm reference cho bố cục hoặc phần
cần sửa, tuyệt đối không được dùng thay profile để xác định khuôn mặt, nét tóc,
tuổi, tỷ lệ, trang phục hay silhouette. Nếu công cụ sửa ảnh hỗ trợ nhiều
reference, phải truyền lại profile gốc cùng ảnh cần sửa và ghi rõ mapping:
`profile gốc = identity/style nhân vật`, `output hiện tại = composition/phần cần
sửa`. Nếu không thể truyền đồng thời profile gốc, không được tiếp tục kiểu sửa
nối tiếp; phải tạo lại từ composition contract với profile gốc.

Lập `compositionStrategy`: một công cụ chính hoặc `none`, tối đa hai công cụ hỗ
trợ, mục đích kể chuyện, focus/eye path và ngoại lệ có chủ ý. Công cụ bố cục chỉ
phục vụ shot thesis; không được lấn át emotion, profile/location continuity,
text, spine hay print-trim safe.

Đề xuất 2–3 option kể chuyện khác nhau, trừ khi người dùng đã chỉ định shot.
Mỗi option nêu ý nghĩa, trải nghiệm người đọc, bằng chứng cần thấy, cinematic
intent, focus, camera, `populationPlan`, placement, khoảng trống, proof,
forbidden và trade-off layout. Ít nhất một option phải thử
một thay đổi có ý nghĩa về khoảnh khắc, cỡ cảnh hoặc điểm nhìn; không chỉ đổi vị
trí nhân vật trong cùng một ý tưởng. Đồng thời phải tạo một **preliminary
composition card** cho từng option: card đúng tỷ lệ và vị trí frame trong layout
thật, thể hiện scale, silhouette, gaze/gesture, text reserve, spine, critical
elements, quan hệ không gian đã chọn của `spatialDepthPlan`, đường dẫn mắt và negative
space. Các card phải được hiển thị cùng lúc với option text
để người dùng chọn trực quan; không chỉ mô tả bố cục bằng chữ hoặc chờ chọn xong
mới tạo card.

Exit: frame đọc được ở kích thước layout; nhân vật phân biệt được; option không
vi phạm G1; `spatialDepthPlan`, hierarchy và biến thiên với shot liền kề đều
đọc được và phục vụ shot thesis; `meaningPreservationCheck` PASS trước khi
người dùng chọn. Các option khác nhau về cách kể nhưng đều giữ ý nghĩa nguồn.

## G3 — Composition và duyệt storyboard

Sau khi người dùng chọn option, lấy preliminary composition card của đúng option
đó làm base, hoàn thiện/sửa khi cần và tạo **confirmed composition card** đúng tỷ
lệ trong layout. Card xác nhận thể hiện scale, focus, silhouette, gaze/gesture,
text reserve, spine, critical elements, quan hệ không gian đã chọn, đường dẫn mắt và
negative space. Nếu
`compositionStrategy` dùng guide, đặt guide SVG thành layer review bật/tắt; không
đưa guide vào output cuối. Card sơ bộ của option không được chọn chỉ phục vụ so
sánh ở G2, không được dùng thay card xác nhận của option đã chọn.

Chạy trên card:

1. `sceneFactGate`: mọi chi tiết bắt buộc của kịch bản đều có cách hiện diện
   cụ thể và còn đọc đúng; FAIL nếu framing, negative space hoặc lệnh cấm làm
   mất một chi tiết đó. Chạy lại `meaningPreservationCheck` trên card xác nhận:
   kiểm cả quy mô, quan hệ, tính tập thể và bằng chứng của `readerExperience`,
   không chỉ đếm đủ nhân vật/đạo cụ. Mất nghĩa thì quay lại G2.
2. `semanticThumbnailGate`: focus, silhouette, vật liệu và style còn đọc đúng;
   ở kích thước layout, mắt vẫn đi đến focus trước rồi đọc được chi tiết thứ hai
   hoặc khoảng trống đã định. Cử chỉ/dấu vết chính phải còn rõ mà không cần dựa
   vào chữ để giải thích.
3. `spatialDepthGate`: kiểm quan hệ không gian theo `spatialDepthPlan`: số lớp
   đã chọn (một, hai hoặc ba), khoảng trống, scale, chồng lớp khi có, mức chi
   tiết và đường dẫn mắt phải phục vụ shot thesis mà không cần hiệu ứng ống
   kính. PASS khi lớp cố ý vắng mặt làm shot rõ hoặc giàu không khí hơn. FAIL
   nếu không gian vô tình phẳng, mọi thành phần cùng độ nổi/cùng tranh focus,
   hoặc có vật che khung chỉ để “đủ lớp”; quay lại G2 để đổi staging, framing
   hay loại chi tiết phụ.
4. `emotionalFlowGate`: xem các frame theo đúng thứ tự và ở kích thước layout;
   xác nhận shot đầu thiết lập nguyên nhân/điểm nhìn, shot sau bổ sung thông tin
   mới và đưa mắt đến đúng đối tượng hoặc hệ quả cảm xúc. PASS khi người đọc có
   thể tự hiểu vì sao cảm xúc thay đổi từ bằng chứng nhìn thấy, focus transfer
   rõ, eyeline/hướng chuyển không bị cụt và điểm kết thị giác đúng nơi cảm xúc
   cần đọng lại. FAIL nếu chỉ lặp mặt nhân vật đang cảm xúc, đối tượng gây cảm
   xúc bị biến thành nền không đọc được, hoặc flow chỉ tồn tại trong phần mô tả.
5. `backgroundOnlyGate`: che người, đạo cụ focus, hiệu ứng và chữ; background
   vẫn đọc đúng location, không rơi vào generic misreading và giữ shared anchor.
   Mức bằng chứng theo cỡ máy: establishing/wide cần ít nhất 3 identity anchors;
   medium cần 2 neo mạnh hoặc 3 neo nhẹ; close-up/emotional insert cần 1 shared
   anchor mạnh cùng tín hiệu không gian đủ nhận diện. Không mở rộng shot chỉ để
   nhét đủ số neo.

Storyboard raster chỉ dùng cho staging phức tạp hoặc khi người dùng yêu cầu.
Trình duyệt theo `workflow_templates.md`. Chỉ sau xác nhận đúng option mới đặt
`optionAlignment.userConfirmed: true` và `approved`.

Exit: card PASS năm gate và được người dùng xác nhận. Output/prompt cũ hoặc xác
nhận option khác không thay thế cổng này.

## G4 — Prompt và generation

Tạo `compositionContract`. Prompt khóa layout/composition; context/background;
`Location identity proof`; profile block và reference riêng từng nhân vật;
pure 2D cho từng component; conditional locks và forbidden readings.
Chuyển nguyên vẹn `sceneMeaning`, `readerExperience` và `populationPlan` đã
duyệt vào contract: vai trò các nhóm, mức đọc cần thiết và căn cứ của mọi giới
hạn số lượng. Không tự thêm lệnh "đúng N người, không thêm người nền" nếu số
đó chỉ là dự kiến linh hoạt của card. Khi cần khóa để giữ staging, ghi rõ đây
là khóa bố cục của shot, không phải dữ kiện tổng số người trong cảnh.

Trước mỗi lượt gọi công cụ tạo/chỉnh ảnh, chạy `profileReferenceRefreshGate`:
đọc lại trực tiếp mọi file profile gốc của các nhân vật xuất hiện; đối chiếu lại
`mustPreserve`, `forbiddenDrift` và `characterProportionLock`; truyền lại các
profile đó trong chính lượt gọi hiện tại; ghi timestamp/lượt sửa, đường dẫn file
và mapping vào manifest. Gate này áp dụng cả lần tạo đầu, reprocess, edit,
inpaint/outpaint và variant sau QA. Thiếu một profile bắt buộc, dùng output vòng
trước làm identity reference, hoặc chỉ nhắc profile bằng chữ là FAIL và không
được generate.

Khi sửa một lỗi QA cục bộ, prompt phải khóa lại toàn bộ identity từ profile gốc,
không chỉ mô tả phần đang sửa. Mỗi vòng sửa phải so với profile gốc và
composition đã duyệt, không so chuỗi `v1 → v2 → v3` như nguồn chuẩn. Ưu tiên tạo
lại từ source/reference gốc khi chỉnh sửa nối tiếp đã gây trôi nét; không tiếp
tục chồng thêm edit lên một output đã có dấu hiệu lệch profile.

Nếu có `blendExtensionLock`, prompt phải tách rõ `Main content region` và
`Blend extension`: dựng đầy đủ shot trong vùng nội dung chính; chỉ mở rộng bằng
trời/đất/nền phụ liên tục ở vùng ngoài. Không đặt thêm nhân vật, gương mặt, tay,
hành động, đạo cụ hay location anchor thiết yếu trong vùng dành cho hòa lấp.
Không dùng crop hậu kỳ để biến một ảnh sai bố cục thành ảnh vừa frame.

`compositionContract` phải chuyển nguyên vẹn `emotionalFlowMap` và
`cinematicIntent` thành chỉ dẫn nhìn thấy: trạng thái người đọc trước shot,
thông tin mới của shot, chủ thể trải qua cảm xúc, nguyên nhân/bằng chứng tạo cảm
xúc, focus transfer, vị trí người đọc/điểm nhìn, eyeline, khoảnh khắc chuyển,
cử chỉ hoặc dấu vết chính, khoảng trống có chủ đích, điều để ngoài khung và điểm
kết thị giác. Không dùng tính từ cảm xúc chung chung thay cho bằng chứng có thể
vẽ và kiểm tra được.

`Location identity proof` gồm location class, danh mục ít nhất ba identity
anchors, các neo được chọn để hiển thị theo cỡ máy, shared anchor, generic
misreadings và removal-risk check. Với exterior, prompt phải có `Geography
contract` riêng: terrain, horizon, spatial scale và forbidden landforms; không
dùng phong cảnh vô nguồn để tạo cinematic depth.

Tạo file version mới trong `Part 1/pages/page-XXX/outputs/`, không ghi đè.
Ledger: `approved → generating → generated`; lần tạo dừng ghi `interrupted`.

Exit: mọi delivery required có output versioned và đường dẫn manifest khớp.

## G5 — QA output

Mọi output mới/reprocess/edit/variant phải chạy lại toàn bộ, không kế thừa PASS:

1. `layoutQa`: script + overlay bắt buộc dùng chính raster của layout gốc có
   text làm nền, rồi đặt output vào đúng frame/mask; tỷ lệ, mask, spine, text,
   safe zone, visibility priority. Overlay phải hiện đường xén và critical-safe theo tỷ lệ phần trăm từng trục.
   `requiredComplete` bị cắt/ép sát hoặc thiếu khoảng thở cảm nhận;
   `requiredReadable` bị crop làm sai nghĩa, sai cử chỉ hoặc cắt vụng tại khớp;
   recognition core vượt critical-safe; hay artwork không phủ kín frame/page là
   FAIL. Không FAIL chỉ vì phần expendable của đất/đá/cây/gỗ hoặc phần lặp của
   anchor đi qua đường xén. Thiếu/không đọc được layout gốc thì FAIL và không được tạo overlay nền
   trắng hay nền thay thế.
   Với canvas mở rộng, QA phải hiển thị thêm biên `contentFrame` và vùng
   `blendExtension`, đồng thời tạo preview mask/hòa lấp ngay trong layout gốc.
   PASS khi nội dung chính nằm an toàn trong frame xanh và phần bị che/hòa chỉ
   là nền phụ; không yêu cầu toàn canvas trùng tỉ lệ frame.
2. `styleQa`: mọi component thuần 2D; texture thật, CGI, soft shading, gradient
   nặng, bloom, volumetric light, DOF hoặc blur là FAIL. Chỉ background được
   phép chuyển màu rất nhẹ, tiết chế và đồ họa (như sky/horizon transition) để
   xác lập thời điểm/không khí; không được dùng nó để tạo khối, glow, nguồn sáng
   mềm hay cảm giác digital painting.
3. `locationQa`: background-only trên output; kiểm số neo theo cỡ máy, shared
   anchor, generic misreading và `geographyLock` cho exterior. Núi/đồi/vách/nước/
   rừng vô nguồn hoặc quy mô không gian trái script là FAIL. Chỉ FAIL khi không đạt mức bằng chứng tương ứng
   hoặc location thực sự đọc sai/generic; close-up không phải tự thân là lỗi.
4. `storyboardQa`: chạy lại `meaningPreservationCheck` trên output thực so với
   `sceneMeaning`, `readerExperience` và `populationPlan`; kiểm bằng chứng về
   quy mô/quan hệ/tính tập thể, không dùng đếm đầu người thay việc đọc nghĩa.
   Mất nghĩa do thiết kế thì quay G2; do ảnh lệch contract thì quay G4.
   Kiểm focus, meaning, staging, profile, emotion, gesture,
   relationship, readability, beat, tỷ lệ giải phẫu đầu–thân–tay, cinematic
   intent và composition đã duyệt. Xác nhận điểm nhìn đặt người đọc đúng vị trí,
   shot có một điểm chuyển cảm xúc, eye path đọc theo thứ tự đã chốt, và hình bổ
   sung cho chữ thay vì lặp lại nó. Chạy lại `emotionalFlowGate` trên toàn chuỗi
   output theo thứ tự layout: mỗi shot phải thêm bằng chứng/thông tin mới, người
   đọc thấy được nguyên nhân cảm xúc, focus và eyeline chuyển liền mạch, và điểm
   kết thị giác vẫn trùng điểm đọng cảm xúc. Kiểm lại `spatialDepthPlan`: số lớp đã chọn,
   scale, chồng lớp khi có, giảm chi tiết ở xa khi có, khoảng trống, hierarchy
   và biến thiên với shot liền kề còn giữ đúng card đã duyệt. Kiểm lại từng chi
   tiết kịch bản bắt buộc: được phép ở lớp phụ nhưng không được biến mất hoặc
   đổi nghĩa vì ưu tiên cinematic. FAIL nếu ảnh lặp biểu cảm mà không cho thấy
   nguyên nhân, biến đối tượng cần đồng cảm thành nền không đọc được, hoặc trở
   thành nhân vật đặt trước nền, dàn nhân vật đồng đều, không gian phẳng ngoài ý
   đồ, hoặc dùng hiệu ứng render để thay cho chiều sâu bố cục. Review công cụ bố
   cục theo hiệu quả kể chuyện, không FAIL chỉ vì chủ thể lệch grid/spiral.

Với output được tạo sau một yêu cầu sửa, QA phải kiểm thêm bằng chứng của
`profileReferenceRefreshGate` cho đúng lượt tạo đó và đối chiếu trực tiếp output
mới với profile gốc, không chỉ với output trước. Nếu nét nhân vật trôi thêm dù
lỗi QA mục tiêu đã được sửa, `storyboardQa` và `visualDeltaQa` đều FAIL; quay lại
G4 từ profile gốc thay vì tiếp tục sửa nối tiếp trên ảnh vừa fail.

Dựng comparison card: composition → output → output được đặt trong chính layout
gốc có text. Ghi
`visualDeltaQa` bằng bằng chứng nhìn thấy. Một hard lock FAIL thì toàn shot FAIL.
Checklist và quy tắc artifact nằm trong `workflow_templates.md`.

Khi có variant/trade-off, trình bảng so sánh và để người dùng chọn; không tự đổi
active output. Mọi raster/overlay mới hoặc cập nhật phải hiển thị trong chat.

Exit: bốn QA PASS, comparison card đã trình, không còn delivery dang dở.

## G6 — Chọn output và bàn giao

Chỉ đặt `userSelectedOutput: true` sau lệnh chọn rõ khi có variant/trade-off.
Chọn output không thay QA. Chỉ đặt `qa-passed` khi mọi delivery tồn tại;
`layoutQa`, `styleQa`, `locationQa`, `storyboardQa`, `visualDeltaQa` PASS; và
output cuối đã được chọn khi cần.

Sau khi người dùng chốt rõ output `qa-passed`, tạo `approved/` trong đúng thư
mục page nếu cần và **chuyển** file đã chọn từ `outputs/` vào đó. Giữ nguyên tên
version; nếu tên đã tồn tại thì dừng để tạo tên version mới, không ghi đè. Cập
nhật mọi `delivery.output`, manifest, layout, QA artifact hoặc tài liệu đang
tham chiếu đường dẫn cũ, rồi đặt delivery thành `approved-filed`. Không chuyển
variant chưa được chốt và không để đồng thời một bản sao trong `outputs/` như
hai nguồn chuẩn.

Bàn giao nêu output active, kết quả QA và lỗi còn tồn tại ảnh hưởng page.

## Mapping workflow cũ

| Cũ | Mới |
| --- | --- |
| Bước 1–2b | G1 + schema Core/Location |
| Bước 3–5c | G2 + schema Frame/Profile/Conditional |
| Bước 5a, 6 | G3/G5 + templates |
| Bước 7–8 | G4 + schema Contract/Delivery |
| Bước 9–10 | G5–G6 + templates |
