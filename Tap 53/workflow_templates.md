# Workflow templates — Tập 53

## Storyboard QA

Trình theo thứ tự: ý nghĩa kịch bản (`sceneMeaning`); điều người đọc cần hiểu,
cảm nhận và bằng chứng cần thấy (`readerExperience`); option/thesis/beat;
`emotionalFlowMap` (người đọc đã biết gì, câu hỏi cảm
xúc, ai đang cảm, điều gì gây cảm xúc, bằng chứng cần thấy, loại chuyển cảnh,
focus transfer và điểm đọng cuối); `cinematicIntent` (người đọc đứng cùng ai,
hình bổ sung gì cho chữ, thông tin mới và điểm chuyển cảm xúc); preliminary
composition card trong layout
cho từng option, hiển thị đồng thời để user so sánh trước khi chọn; confirmed
composition card của option đã chọn;
focus/eye path theo thứ tự đọc; cử chỉ/dấu vết chính; out-of-frame;
profile/reference; context; location/shared anchors; text/spine; kết quả
semantic thumbnail, emotional-flow và background-only gate; composition
strategy, `populationPlan` (số trong cảnh / trong khung / cần đọc rõ, vai trò
các nhóm, lý do và mức linh hoạt) và `meaningPreservationCheck` trước khi trình
option, kiểm lại ở card xác nhận. Không dùng số người để thay mô tả thứ bậc
thị giác. Card tối đa ba nhãn ngắn: `Focus`, `Camera`,
`Dư âm`.

## QA checklist

### Layout
- [ ] `sourceLayout` là chính raster layout gốc có text và đọc được.
- [ ] Overlay đặt output vào đúng frame/mask trên layout gốc; không dùng nền
  trắng, layout dựng lại hoặc placeholder.
- [ ] Artwork phủ kín frame/page gốc; không thu nhỏ để né xén.
- [ ] Nếu dùng canvas mở rộng: `contentFrame` khớp frame xanh; mọi focus, mặt,
  tay, cử chỉ, hành động và đạo cụ quan trọng nằm trong vùng này.
- [ ] `blendExtension` chỉ chứa trời/đất/nền phụ liên tục; preview mask/hòa
  gradient trong layout gốc không che chi tiết chính và không làm đổi nghĩa shot.
- [ ] Overlay hiện trim và critical-safe theo phần trăm từng trục của `contentFrame` (hoặc canvas khi không có `contentFrame`).
- [ ] Mỗi mặt/tay/cử chỉ/đạo cụ đã được gán `requiredComplete`,
  `requiredReadable`, `optionalSupport` hoặc `outOfFrame` theo shot thesis;
  không tự động nâng chúng thành critical.
- [ ] `requiredComplete` nằm trọn trong critical-safe và có khoảng thở cảm nhận;
  `requiredReadable` crop có chủ ý vẫn đọc đúng, không phá cử chỉ/anatomy và
  không cắt vụng tại khớp; `optionalSupport` được phép crop hoặc bỏ.
- [ ] Recognition core của location anchor nằm an toàn; phần lặp/kéo dài có thể
  bị xén mà location vẫn đọc đúng.
- [ ] Crop buffer (trời/đất/đá/cây/gỗ phụ) phủ rộng qua mép để crop tự nhiên;
  không kéo focus sát mép chỉ để bảo vệ chi tiết phụ.
- [ ] Không co/ép thân, rút ngắn tay hay thu hẹp vai để né trim trong khi giữ
  nguyên đầu; nếu cần chỉnh, chỉ scale nhân vật nguyên khối hoặc đổi framing/
  placement và mở rộng background.
- [ ] Tỷ lệ/mask đúng; overlay đã xem ở kích thước layout.
- [ ] `intentionalCropLock` ghi rõ boundary, phần giữ/bỏ, lý do kể chuyện và vùng
  cấm cắt cho mọi subject/component chạm hoặc vượt khung.

### Style
- [ ] Line art nhất quán; flat fills; 1–2 hard cel shades.
- [ ] Không texture thật, CGI, soft shading, gradient nặng, bloom, DOF, blur.
- [ ] Nếu có chuyển màu nền: rất nhẹ, tiết chế, mang tính đồ họa, chỉ phục vụ
  thời điểm/không khí; không tạo khối, glow hoặc cảm giác digital painting.

### Location — background-only
- [ ] Che subject/effect/text vẫn nhận đúng location.
- [ ] Exterior khớp `geographyLock`: địa hình, horizon và quy mô đúng source;
  không có núi/đồi/vách/nước/rừng vô nguồn hoặc địa hình từ scene khác.
- [ ] Neo đạt mức theo cỡ máy: wide ≥3; medium = 2 mạnh hoặc 3 nhẹ; close-up/
  emotional insert = 1 shared anchor mạnh + tín hiệu không gian đủ nhận diện.
- [ ] Shared anchor khớp shot liền kề.
- [ ] Không rơi vào generic misreading; negative prompt không xóa hết neo.

### Storyboard
- [ ] Ý tưởng đi từ ý nghĩa → trải nghiệm người đọc → bằng chứng → cách kể/bố
  cục → số người; không khóa số tùy ý trước để thu hẹp cảnh.
- [ ] `readerExperience` ghi rõ điều cần hiểu/cảm nhận và bằng chứng nhìn thấy;
  không đồng nhất cảm xúc người đọc với biểu cảm nhân vật.
- [ ] `populationPlan` tách số trong cảnh, số trong khung và số cần đọc rõ;
  từng nhóm có vai trò, mức đọc và căn cứ số lượng/mức linh hoạt. Nếu không có
  người, ghi không áp dụng.
- [ ] Focus có thể là tập thể/hoạt động chung; thứ bậc được tạo bằng bố cục.
  Không mặc định ít người mới focus, cũng không thêm người chỉ để đạt số đông.
- [ ] `meaningPreservationCheck` PASS: sau giản lược vẫn đọc đúng quy mô, quan
  hệ/tính tập thể và bằng chứng cảm xúc; kiểm trên card ở G2/G3 và ảnh thực ở
  G5. Focus rõ hoặc đủ số người chưa đủ để PASS.
- [ ] Focus/meaning đúng; staging/cử chỉ/quan hệ đọc không cần chữ.
- [ ] Có `emotionalFlowMap` cho toàn chuỗi: ghi rõ trạng thái người đọc trước
  chuỗi, nguyên nhân cảm xúc, bằng chứng cần thấy, focus transfer và điểm đọng.
- [ ] Người đọc được đặt ở đúng điểm nhìn đã chốt; hình có một điểm chuyển cảm
  xúc hoặc được ghi rõ là establishing/transition.
- [ ] Mỗi shot mang thêm thông tin/cảm xúc mới; shot sau không chỉ lặp lại gương
  mặt hoặc trạng thái của nhân vật đã đọc ở shot trước.
- [ ] Người/vật/hành động gây cảm xúc đủ rõ để người đọc tự hiểu vì sao nhân vật
  thay đổi; đối tượng cần đồng cảm không bị hạ thành silhouette/background dưới
  ngưỡng đọc được.
- [ ] Eyeline, hướng chuyển và focus nối được giữa các frame; điểm kết thị giác
  trùng với nơi cảm xúc cần đọng lại.
- [ ] Bằng chứng cảm xúc đến từ chi tiết có căn cứ trong kịch bản; không dựa vào
  biểu cảm đồng loạt hoặc diễn xuất cường điệu để báo hiệu ý nghĩa.
- [ ] Focus được đọc trước; chi tiết thứ hai hoặc khoảng trống tạo ý nghĩa tiếp
  theo ở kích thước layout.
- [ ] Hình bổ sung cho chữ bằng phản ứng, dấu vết, hệ quả hoặc thông tin ngoài
  khung; không chỉ lặp lại hành động chữ đã kể.
- [ ] Composition tool phục vụ shot thesis và eye path; không ép staging vào
  grid, không ưu tiên hình học hơn emotion/text/spine/trim-safe.
- [ ] Timeline và component đúng source; số/quy mô nguồn xác nhận được giữ
  đúng, số người hiện trong khung theo `populationPlan` có căn cứ. Lựa chọn
  staging không bị ghi thành dữ kiện nguồn hay hard lock vô căn cứ.
- [ ] Profile khớp reference, không hoán đổi identity.
- [ ] Với mọi reprocess/edit/variant: đã đọc và truyền lại profile gốc trong
  chính lượt tạo hiện tại; manifest có `profileReferenceRefreshGate` PASS.
- [ ] Output mới được đối chiếu trực tiếp với profile gốc, không lấy output vòng
  trước làm baseline identity; không có dấu hiệu trôi nét qua các vòng sửa.
- [ ] Tỷ lệ đầu–cổ–vai–thân–tay tự nhiên theo profile; silhouette không có dấu
  hiệu biến dạng cục bộ để khớp vùng xén.
- [ ] Emotion và subject scale đọc được ở layout size.
- [ ] `priorityConflictGate` PASS: bảo vệ trim, tay/đạo cụ và location anchors
  không làm yếu emotion/eye path, thu nhỏ focus hoặc tạo pose minh họa.
- [ ] Beat/camera hợp shot liền kề; `emotionalFlowGate` PASS; output giữ
  composition đã duyệt.

`Không chắc` = FAIL. Source/location → G1; frame/shot/profile → G2;
composition → G3; prompt/render drift → G4.

Nếu lỗi QA cần quay lại G4 và shot có nhân vật, action sửa phải mặc định bao gồm
“đọc và truyền lại profile gốc”; không cho phép sửa nối tiếp chỉ từ output vừa
fail.

## Trade-off

```text
Trade-off cần quyết định — <page/frame/option>
| Variant | Hard locks | Emotion/acting | Sai lệch | Đánh đổi |
| ... | ... | ... | ... | ... |
```

Không tự chọn active output. Một variant duy nhất fail hard lock phải quay lại
cổng gây lỗi, không gọi là trade-off.

## Action chuẩn

Sau **mỗi G1–G6**, mỗi action một code block riêng ở cuối báo cáo; ghi nguyên
văn action người dùng chọn vào `userAction`. Không thay action bằng câu hỏi mở
hoặc nhãn nút. Với gate PASS chưa cần duyệt, phải có action để tiếp tục gate kế
tiếp; với gate FAIL, phải có action quay lại/sửa đúng gate gây lỗi.

```text
Tiếp tục G2: <page/frame>
```
```text
Quay lại G1: <page/frame> — kiểm tra lại <nguồn hoặc lock thiếu>
```
```text
Tiếp tục G4: <page/frame> — <optionId>
```
```text
Quay lại G3: <page/frame> — <optionId> — sửa composition
```
```text
Tiếp tục G5: <page/frame> — <outputId>
```
```text
Quay lại G4: <page/frame> — <outputId> — sửa <lỗi QA cụ thể>
```

```text
Chọn option: <optionId>
```
```text
Xác nhận Storyboard QA: <page/frame> — <optionId>
```
```text
Sửa Storyboard QA: <page/frame hoặc mục> — <nội dung sửa>
```
```text
Xác nhận Composition QA: <page/frame> — <optionId>
```
```text
Chọn output: <outputId hoặc đường dẫn>
```

Sau khi QA PASS và người dùng chốt lệnh này, chuyển output đã chọn vào thư mục
`approved/` cùng page, cập nhật các đường dẫn liên quan và đánh dấu
`approved-filed`.
```text
Chỉnh output: <outputId> — giữ <A>; sửa <B> thành <C>
```
```text
Tạo variant hợp nhất: giữ <A> của <variant 1>; giữ <B> của <variant 2>
```
```text
Sửa prompt: <frame/section> — <nội dung sửa>
```
```text
Quay lại storyboard: <page/frame/mục> — <nội dung>
```
```text
Dừng phương án: <optionId hoặc outputId>
```

## Artifact và bàn giao

Mọi raster/overlay mới hoặc cập nhật phải hiển thị trong chat với
page/frame/option/version, mục đích, QA status và link tuyệt đối.

Overlay QA chỉ hợp lệ khi dùng chính raster layout gốc có text làm nền và đặt
output đã tạo vào đúng frame/mask. Thiếu source layout hoặc source không đọc
được thì QA FAIL; không tạo hay trình overlay nền trắng/nền thay thế.

Màu guide chuẩn: đỏ liền = trim theo phần trăm từng trục; xanh lá liền = critical-safe theo phần trăm từng trục;
xanh dương đứt = frame/mask. Vượt trim-safe là lỗi bố cục, không được sửa bằng
cách thu nhỏ artwork gây hở mép. Chỉ kết luận FAIL sau khi phân loại semantic:
narrative-critical/recognition core/crop buffer; không bảo vệ máy móc mọi tảng
đá, khối đất hoặc vật liệu phụ.

Bàn giao chỉ khi output required tồn tại, bốn QA và `visualDeltaQa` PASS, không
còn status dang dở, và người dùng đã chọn output khi cần.
