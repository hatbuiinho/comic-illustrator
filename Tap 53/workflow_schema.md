# Workflow schema — Tập 53

Conditional lock phải ghi `applicable: true/false` và lý do.

## Core

- `sceneMeaning`: ý nghĩa cốt lõi, `scaleMeaning` (quy mô mang nghĩa),
  `relationships`, `collectiveMeaning` (tính tập thể hoặc không áp dụng),
  `sourceEvidence`, `forbiddenReadings`; tách dữ kiện xác nhận, hàm ý mạnh,
  phần chưa rõ và lựa chọn tạo hình. Không tự gán tổng số người khi nguồn
  không xác nhận con số.
- `provenance` cho mọi nhận định ảnh hưởng bố cục: `sourceFact`,
  `userConfirmed` hoặc `assistantInference`. Loại cuối không được tạo hard lock,
  giảm quy mô nguồn hoặc làm bằng chứng cho suy luận khác khi chưa được xác nhận;
  `narrativeFunction` bắt buộc có `provenance`.
- `optionAlignment`: `sourceRead`, selected option, rationale, `userAction`,
  `userConfirmed` (chỉ sau duyệt đúng option).
- `contextSnapshot`: time, present/visible characters, current state,
  already happened, forbidden future, script proof trước/hiện tại/sau.
- `narrativeInferenceLock`: explicit, strongly implied, unknown. Không dùng
  unknown để xóa hàm ý mạnh.
- `backgroundContinuityLock`: physical stage, must/may show, forbidden, proof.
- `geographyLock` cho mọi exterior: terrain class, horizon, spatial scale,
  vegetation/water only when evidenced, forbidden landforms và direct proof.
  Nếu script không xác nhận một dạng địa hình, dùng horizon trung tính phù hợp
  với các bằng chứng đã có; không thêm núi, đồi, vách, sông, hồ hoặc rừng chỉ để
  tạo chiều sâu điện ảnh.
- `visualComponentLock[]`: id/type, script term, intended class, scale anchor,
  silhouette/surface, style treatment, story role, wrong readings.
- `printTrimLock`: `trimPercent: {x: 0.0104895, y: 0.0147783}`,
  `criticalSafePercent: {x: 0.0279720, y: 0.0394089}`, `visibilityPriority[]`,
  `narrativeCritical[]`,
  `perceptualBreathingRoom`, `recognitionCores[]`, `cropBuffers[]`, artwork
  coverage và proof.
  Các tỷ lệ này được áp theo từng trục của `contentFrame` (hoặc canvas khi không
  có `contentFrame`); không dùng mm/pixel cố định. Artwork phải phủ kín `contentFrame`; toàn canvas được phép có kích thước/tỷ
  lệ khác khi đã khai báo `blendExtensionLock`. Background phụ được phép mất khi
  xén hoặc hòa lấp. Không tự động coi mặt, tay/cử chỉ hay đạo cụ là critical.
  Mỗi chi tiết dự kiến xuất hiện có đúng một cấp: `requiredComplete`,
  `requiredReadable`, `optionalSupport`, `outOfFrame`; cấp do `shotThesis` và
  `emotionLock` quyết định. Chỉ `requiredComplete` phải nằm trọn trong
  critical-safe và còn khoảng thở cảm nhận. `requiredReadable` được crop có chủ
  ý nếu vẫn đọc đúng, không phá cử chỉ/anatomy và không cắt vụng tại khớp;
  `optionalSupport` có thể crop hoặc bỏ. Với identity/shared anchor,
  chỉ `recognitionCore` cần nằm trọn trong safe; phần kéo dài/lặp lại có thể đi
  qua mép nếu sau xén location vẫn đọc đúng. Đá, đất, cây, trời, gỗ phụ mặc định
  là `cropBuffer`, trừ khi script/shot thesis biến chính nó thành focus.
- `contentFrame`: vùng nội dung chính ánh xạ vào frame xanh; chứa toàn bộ focus,
  hành động và chi tiết kể chuyện cần đọc.
- `blendExtensionLock`: `applicable`, kích thước/tỉ lệ canvas dự kiến, phần mở
  rộng theo từng cạnh, `allowedBackground`, `forbiddenContent`, cách mask/hòa
  gradient trong InDesign và bằng chứng preview không che nội dung chính.

Mọi component dùng line art rõ, flat fills, 1–2 hard cel shades; cấm texture ảnh
thật, CGI/3D/2.5D, soft airbrush, gradient nặng, volumetric light, bloom, lens
flare, DOF, bokeh và blur. Ngoại lệ duy nhất: background có thể dùng chuyển màu
rất nhẹ, tiết chế và đồ họa ở sky/horizon để gợi thời điểm hoặc không khí; không
được tạo khối, glow, nguồn sáng mềm hay cảm giác digital painting.

## Location

`geographyLock`:

- `applicable`, `terrainClass`, `horizonCharacter`, `spatialScale`;
- `mustShow[]`, `mayShow[]`, `forbiddenLandforms[]`;
- `geographyProof` từ script hoặc chỉ dẫn trực tiếp của người dùng;
- `unknownHandling`: địa hình chưa được xác nhận phải giữ trung tính, không được
  biến thành thắng cảnh trang trí.

Khóa này độc lập với kiến trúc: background có thể đúng chòi/công trình nhưng vẫn
FAIL location nếu bịa sai đồng bằng thành núi, khu đất rộng thành khoảng sân hẹp,
hoặc trộn địa hình của scene khác.

`locationIdentityLock`:

- `locationClass`;
- `identityAnchors[]`: danh mục ít nhất ba neo có silhouette/vị trí/tỷ lệ; không
  có nghĩa mọi neo đều bắt buộc xuất hiện trong mọi shot;
- `sharedArchitecturalAnchor[]`: neo nhất quán giữa shot; close-up giữ ít nhất một;
- `genericMisreadings[]`, `forbiddenDetails[]`;
- `removalRiskCheck[]`: negative prompt có xóa neo không và neo thay thế;
- `anchorRequirementByShotSize`: establishing/wide = tối thiểu 3 neo; medium =
  2 neo mạnh hoặc 3 neo nhẹ; close-up/emotional insert = 1 shared anchor mạnh
  cộng tín hiệu không gian đủ nhận diện. Không đổi sang shot rộng hơn chỉ để đủ neo;
- `locationProof` trực tiếp, không lấy output làm nguồn.

Tường đá, sàn tối, vết nứt không phải ba neo nhận diện độc lập.

`backgroundOnlyGate`: artifact, masked elements, shot size, location read,
evidence cho các neo được yêu cầu theo cỡ máy/shared anchor, generic misreading
check, status. `uncertain` = FAIL.

## Frame, shot và profile

- `frameReadabilityLock`: display context, allowed shot size, subject scale,
  minimum readable elements, forbidden scale, proof.
- `shotThesis`: dramatic meaning, moment, viewpoint, visual focus, out-of-frame;
  `focusType` là cá nhân, quan hệ, tập thể, hoạt động chung, không gian hoặc
  dấu vết. Không suy ra số người từ yêu cầu một focus.
- `readerExperience`: `intendedUnderstanding`, `intendedFeeling`,
  `visibleEvidence[]`; tách khỏi cảm xúc/biểu cảm nhân vật. Lập ở đầu G2 trước
  cỡ máy và số người; không tự bịa chuyển cảm xúc cho shot chỉ làm nhiệm vụ
  thiết lập/chuyển cảnh.
- `populationPlan`: `applicable`, lý do; `inScene` (theo nguồn, có thể chưa rõ
  con số), `inFrame` (số dự kiến hoặc khoảng), `readableSubjects` (người/nhóm
  cần đọc rõ), `groups[]` (vai trò, hoạt động/quan hệ, mức đọc, lớp không gian),
  `countPolicy` (dự kiến linh hoạt hoặc khóa chính xác), `countRationale`,
  `omissionRationale`. Lập sau ý nghĩa, trải nghiệm người đọc và tổ chức bố cục;
  con số staging không tự trở thành dữ kiện nguồn. Không có người thì ghi
  không áp dụng; không buộc dựng thêm người để điền schema.
- `meaningPreservationCheck`: giai đoạn/artifact, `sceneMeaning`,
  `readerExperience`, các phần đã giản lược, bằng chứng còn lại về quy mô,
  quan hệ/tính tập thể và cảm xúc, nguy cơ đọc sai, status và hướng sửa.
  Thực hiện cuối G2 trước trình option; chạy lại trong G3 `sceneFactGate` và
  G5 `storyboardQa`. Focus rõ nhưng mất ý nghĩa vẫn FAIL. Không thêm gate duyệt.
- `emotionalFlowMap`: sequence scope, `readerPriorState`, `openEmotionalQuestion`,
  `readerExperience`,
  `emotionSubject`, `emotionCause`, `readerVisibleEvidence[]`, `transitionType`,
  `focusTransfer` (from/to), `eyelineContinuity`, `newInformationByShot[]`,
  `emotionalEndpoint` và `visualEndpoint`. Map áp dụng cho cả chuỗi, không được
  suy ra bằng cách ghép các prompt riêng sau khi đã chọn bố cục.
- `cinematicIntent`: reader alignment/viewing position, image-to-text addition,
  exact moment, emotional turn, new information relative to previous shot,
  reader-visible evidence, first read, second read or intentional negative space,
  primary gesture/trace, deliberate out-of-frame information, adjacent-shot
  relationship, preparation for next shot, and evidence at layout size. Nếu shot
  không có thay đổi cảm xúc, ghi rõ lý do shot làm nhiệm vụ establishing/transition
  thay vì bịa một cảm xúc.
- `compositionStrategy`: `primaryTool` (một tool hoặc `none`), tối đa hai
  `supportingTools`, `storyPurpose`, `focusPlacement`, `eyePath`, `guideAsset`,
  `intentionalExceptions`. Không phải hard lock hình học; bằng chứng phải giải
  thích tool phục vụ shot thesis thế nào.
- `beatMap`: beat, transition, focus transfer, information gain và emotional
  endpoint giữa các frame.
- `emotionLock`: intended emotion, reader feeling, facial/body cues, wrong
  readings, proof at layout size.
- `profileFidelityLock[]`: character id, profile source, must-preserve về mặt,
  tóc/râu, tuổi/tỷ lệ, trang phục/màu, phụ kiện, silhouette; readability,
  distinct-from, forbidden drift, visibility, confidence, reference mapping.
- `profileReferenceRefreshGate`: áp dụng cho từng generation attempt; gồm
  attempt/version, thời điểm đọc lại, danh sách đường dẫn profile gốc, character
  → reference mapping, `mustPreserve`/`forbiddenDrift` đã đối chiếu, vai trò của
  mọi output trung gian (chỉ composition/edit target, không phải identity), cách
  truyền reference trong lượt gọi hiện tại, visual proof và status. Thiếu bằng
  chứng đọc/truyền lại profile gốc trong chính lượt sửa = FAIL.
- `characterProportionLock[]`: character id, profile source, head-to-body scale,
  neck/shoulder width, torso length, arm/hand scale, `uniformScaleOnly`,
  crop boundary, forbidden distortions và visual proof. `uniformScaleOnly` luôn
  là `true`: cấm co thân, rút tay, ép vai hoặc scale một phần cơ thể độc lập để
  né trim/safe zone trong khi giữ nguyên đầu. Nếu không vừa, đổi shot size,
  placement hoặc mở rộng background crop buffer.
- `anatomySilhouetteGate`: artifact/evidence, head–neck–shoulder–torso–arm
  continuity và status. Bất kỳ tỷ lệ đầu–thân phi tự nhiên hoặc biến dạng cục bộ
  do fit layout đều là FAIL.
- `intentionalCropLock[]`: subject/component id, visibility priority, crop
  boundary, retained portion, deliberately out-of-frame portion, story reason,
  forbidden joints/zones và proof ở layout size.
- `priorityConflictGate`: bằng chứng rằng trim, tay/đạo cụ và location anchors
  không làm yếu emotion/eye path, giảm focus scale hoặc buộc pose minh họa;
  conflict chưa giải quyết là FAIL.
- `emotionalFlowGate`: ordered-frame artifact, reader prior state, visible cause,
  evidence gained per shot, focus/eyeline transfer, visual endpoint, emotional
  endpoint, text-independent read và status. Nếu cảm xúc chỉ đọc được nhờ phần
  giải thích, nhân vật cảm xúc bị lặp mà nguyên nhân không hiện rõ, hoặc đối tượng
  đồng cảm bị giản lược dưới ngưỡng đọc được thì FAIL.
- `identityConflictCheck`: bắt buộc từ hai nhân vật trở lên.

Sai từ hai dấu hiệu profile cốt lõi hoặc nhầm identity → toàn shot FAIL.

## Conditional

- `causalStateLock`: cause, confirmed final state, drawn moment, evidence,
  forbidden contradictions.
- `materialSemanticsLock`: script term, class, scale, surface/silhouette, state,
  wrong readings. “Tảng/nguyên khối/lớn/nặng” phải thành silhouette và tỷ lệ.
- `relationalFocusLock`: shared focus, gaze, body orientation, relationship,
  forbidden readings.
- `gestureSemanticsLock`: meaning, hand shape, palm direction, target,
  supporting pose, forbidden gestures.

## Option, contract, delivery

Mỗi option: id, `sceneMeaning`, `readerExperience`, `emotionalFlowMap`,
`cinematicIntent`, focus, moment, camera, `populationPlan`,
placement, negative space, source/background proof, forbidden, layout trade-off
và `preliminaryCompositionCard`. Card sơ bộ là artifact bắt buộc tạo cùng lúc với
option, đúng tỷ lệ/vị trí frame thật, có scale, silhouette, gaze/gesture, text
reserve, spine, critical elements và negative space; phải hiển thị cho user trước
khi chọn; `meaningPreservationCheck` phải PASS trước khi trình option.
Sau khi user chọn, G3 tạo `confirmedCompositionCard` riêng từ card sơ
bộ đó; không được coi card sơ bộ là approval.

`compositionContract`: `sceneMeaning`, `readerExperience`, `populationPlan`,
camera/shot size, scale, focus, silhouettes, eye path,
reader alignment, reader prior state, image-to-text addition, emotional turn,
emotion subject/cause, reader-visible evidence, new information, focus transfer,
visual/emotional endpoint, primary gesture/trace,
negative space, visibility priority, intentional crop, out-of-frame,
readability, emotion, profile/reference,
character proportion/uniform-scale rule, location/shared anchors,
`compositionStrategy` và conditional locks áp dụng.

`delivery`: required, frame, versioned output, version, status. Status hợp lệ:
`storyboard-pending`, `approved`, `generating`, `generated`, `interrupted`,
`qa-passed`, `approved-filed`. `approved-filed` chỉ dùng sau khi người dùng chốt
rõ output đã PASS QA và file đã được chuyển từ `outputs/` vào `approved/` cùng
page; mọi đường dẫn tiêu thụ phải trỏ tới file mới.

## QA records

- `layoutQa`: `sourceLayout` bắt buộc trỏ tới raster của chính layout gốc có
  text; `sourceLayoutReadable`, frame/mask placement, ratio, spine, text reserve,
  safe zone, print-trim geometry, visibility/crop evidence, artwork coverage, overlay
  artifact và status. Overlay phải đặt output lên source layout này và hiện cả
  trim line và critical-safe theo phần trăm từng trục; kiểm thêm khoảng thở cảm nhận quanh
  `requiredComplete`, intentional crop và crop tự nhiên của crop buffers; cấm
  nền trắng, layout dựng lại hoặc placeholder. `requiredComplete` bị cắt/ép sát,
  `requiredReadable` crop sai nghĩa/cử chỉ/anatomy, recognition core
  vượt safe line, artwork không phủ kín, hoặc
  thiếu/không đọc được source layout = FAIL.
- `locationQa`: location read, shot size, mức neo tương ứng, shared-anchor
  evidence, generic-misreading/removal-risk checks, visual evidence, status.
- `visualDeltaQa`: từng contract decision → visual evidence → PASS/FAIL;
  `meaningPreservationCheck` trên ảnh thực, bằng chứng của `readerExperience`,
  mức hiện diện và vai trò các nhóm theo `populationPlan`;
  layout, style, location, focus, staging, readability, emotion, profile từng
  character, anatomy/proportion từng character, relationship/gesture khi áp
  dụng, reader alignment, first-to-second-read order, image-to-text addition,
  emotional turn, cause/evidence readability, focus transfer, information gain,
  visual/emotional endpoint, accepted changes, overall status,
  `userSelectedOutput`.

Với reprocess/edit/variant có nhân vật, `visualDeltaQa` phải có mục
`profileDriftFromOriginal`: đối chiếu từng nhân vật trực tiếp với profile gốc và
ghi rõ khuôn mặt, tóc/râu, tuổi, tỷ lệ, trang phục/màu, phụ kiện và silhouette.
Không dùng output phiên bản trước làm baseline identity.

Không lấy prompt làm evidence. Hard locks: context/timeline, location, profile
nhìn thấy, focus, readability, layout/spine/safe zone, pure 2D. Một hard lock
FAIL → overall FAIL.
