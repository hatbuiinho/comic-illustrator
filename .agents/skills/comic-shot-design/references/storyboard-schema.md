# Schema hướng kể và storyboard

Áp [art-first-policy.md](art-first-policy.md). Chỉ ghi field có ích cho deliverable;
không tạo dữ liệu rỗng hoặc marker giả để đủ schema. Khóa ý đồ, không từng contour.

## Narrative direction trước composition

Direction để người dùng chọn là artifact nhẹ hoặc dữ liệu hội thoại, không cần
preview. Mỗi direction gồm:

- `directionId`;
- `readerFeeling`: `primary`, `aftertaste`, `avoid`;
- `emotionalThesis`: trái tim của hình trong một câu;
- `imageMeaning`: điều cần đọng lại, không phải danh sách sự việc;
- `selectedMoment`;
- `emotionalAnchor`: subject/quan hệ và `visibleSignal` dự kiến;
- `storytellingMode`;
- `proposedShotSize`: cỡ cảnh dự kiến và lý do phục vụ cảm xúc, quy mô;
- `layoutFitAssessment` khi có layout: vùng có thể vẽ, mức chiếm trang/tỷ lệ nhân vật dự kiến, quan hệ chữ–hình và khả năng reflow theo contract; nguồn đánh giá và phần chưa kiểm nếu có;
- `tradeoff` và `omitToProtectEmotion`.

Cho phép đề xuất cỡ cảnh và đánh giá khả năng bố trí định tính để người dùng
chọn direction. Chưa khóa camera, staging, scale, crop hoặc tọa độ; chưa dựng
composition preview hay layout proof trước khi direction được chọn. Trạng thái sau khi chọn direction là
`confirmed.narrativeDirection: true`, `confirmed.composition: false` trong
page-state; `active.compositionStatus` phản chiếu `selectedPageComposition.status`.

## Storyboard đầy đủ cho direction đã chọn

Composition được dựng gồm:

- `optionId`;
- `sceneMeaning`;
- `readerExperience`: điều cần hiểu, cảm nhận và bằng chứng;
- `readerFeeling`: `primary`, `aftertaste` và cảm nhận sai cần tránh;
- `emotionalThesis`: ý cảm xúc chi phối mọi quyết định thị giác;
- `emotionalAnchor`: subject/quan hệ và tín hiệu nhìn thấy như ánh mắt, bàn tay,
  khoảng cách, tư thế hoặc khoảng lặng;
- `performanceSubtext`: điều nhân vật đang cảm nhưng không nói thẳng;
- `performanceContract` theo từng nhân vật: `intendedRead`, `visibleSignals`
  gồm gaze/hand/posture/spacing, `forbiddenReads` và vai trò trong quan hệ;
- `groupEmotionalCoherence`: cảm xúc quan sát được của cả nhóm, tín hiệu có thể
  xung đột và trạng thái `PERFORMANCE_READ_PASS|COMPOSITION_NEEDS_REVISION`;
- `beautyIntent`: `pageCharacter`, `rhythm` và `livingDetail` giúp hình đẹp,
  sinh động mà không tranh focus;
- `selectiveEvidence`: `mustShow`, `canImply`, `omitToProtectEmotion`;
  - ghi mức biểu hiện cần thiết của từng thành phần: nhìn rõ, crop có ý nghĩa,
    gợi qua quan hệ hoặc ngoài khung theo nguồn/context locks. Phân biệt người
    hiện diện với người bắt buộc trong khung; không suy “phải thấy trọn” từ
    “phải có bằng chứng”. Active process bắt buộc vẫn cần đại diện và hành
    động đọc được; crop không được làm mất tín hiệu đó;
- `shotThesis`: moment, viewpoint, focus, out-of-frame;
- `cinematicIntent`;
- `shotSizeRationale`: tín hiệu cảm xúc cần đọc, không gian trang đã cân nhắc
  cùng typography/text burden, lý do chọn cỡ cảnh và phương án cạnh tranh/lý
  do không chọn khi có. Không cần tạo phương án giả để điền trường này;
- `shotReadabilityProof`: kích thước trang và diện tích hình dự kiến, tín hiệu
  kể chuyện chính, nhận xét trên preview tại kích thước đọc đó và trạng thái
  `PASS|COMPOSITION_NEEDS_REVISION`. Với shot cảm xúc, ghi riêng độ đọc mắt,
  phản ứng và gesture; crop phóng to không thay proof này;
- `populationPlan`: trong cảnh, trong khung, cần đọc rõ, vai trò nhóm;
  - `activeProcessAgents`: người đang làm hành động được nguồn nói rõ;
  - `minimumVisibleRepresentatives`: số/nhóm tối thiểu phải đọc được;
  - `cropJustification`: chỉ hợp lệ cho người hiện diện nhưng không mang hành động;
- `compositionStrategy`;
- `spatialDepthPlan`;
- `sceneExtentPlan` cho page/spread không hard frame: footprint cảnh nhìn thấy,
  lý do kể chuyện, context/process evidence tối thiểu, vùng nền giấy/khoảng thở
  chủ ý và biên hòa với chữ; không suy footprint từ kích thước canvas;
- `emotionLock`;
- `profileReferences`;
- `continuityDependencies`:
  - `reads`: các fact/lock mà option dựa vào;
  - `writesIfApproved`: thay đổi chỉ có thể ghi sau delivery/xác nhận phù hợp;
  - `mustNotChange`: trạng thái hình không được vô tình thay đổi;
  - `forbidden`: chi tiết tương lai hoặc trạng thái sai không được xuất hiện;
- `locationAnchors` khi áp dụng;
- `backgroundContextPlan` khi background mang thông tin kể chuyện:
  - `locationIdentity`: điều khiến nơi này nhận diện đúng và không chung chung;
  - `activeProcessEvidence`: dấu hiệu của hoạt động đang hoặc vừa diễn ra;
  - `spatialLayers`: quan hệ foreground, midground và background;
  - `layoutIntegrationPotential`: vùng có thể giảm tương phản/mật độ nét ở bước
    generation mà vẫn tiếp tục không gian;
  - `genericFailureMode`: cách đọc sai nếu chỉ còn vật thể neo rời rạc;
  - `topographyLock`: địa hình/đường chân trời được nguồn xác nhận hoặc `UNKNOWN`;
- `visibilityPriority`:
  - `emotionalPriority`: cảm xúc hoặc quan hệ phải chi phối trải nghiệm hình;
  - `explicitRequired`: bắt buộc nhìn thấy đủ rõ để bảo toàn ý nghĩa;
  - `implicitReadable`: không cần thể hiện trọn vẹn, nhưng tổng thể phải cho phép
    người đọc suy ra đúng;
  - `optionalSupport`: có thể giản lược nếu cạnh tranh với focus;
  - `outOfFrame`: chủ ý không xuất hiện;
- `inferencePlan`: điều người đọc tự suy ra, tín hiệu tối thiểu hỗ trợ suy luận,
  mức mơ hồ có chủ ý và cách hiểu sai cần tránh;
- `restraintCheck`: kiểm tra hình có giải thích quá mức, chi tiết phụ có tranh
  focus và có thể bớt tín hiệu nào mà vẫn giữ nguyên ý nghĩa hay không;
- `intentionalCrop` khi có;
- `meaningPreservationCheck`;
- `layoutPlan`:
  - `textIntegrationContract`: `FINAL_TEXT_REFLOW`,
    `TEXT_PROXY_INTEGRATION` hoặc `BAKED_TEXT_PROXY_CONCEPT`;
  - `mode`: `GUIDED` khi có brief/mask hoặc
    `GENERATION_LAYOUT_INTEGRATION` khi chữ sẽ được art-direct lúc tạo hình;
  - `canvasConstraints`: trim, gáy, safe zone, hard frame/mask thật và fixed
    element đã biết;
  - `typographyLock`: content, reading order, font, size, leading, tracking,
    scale, style và màu không được thay đổi;
  - `allowedTextMutations`: text-frame geometry, column width, line break do
    reflow và wrap path;
  - `provisionalTextFlowEnvelope`: contour chữ thật được reflow khi contract là
    `FINAL_TEXT_REFLOW`; với proxy, đây chỉ là flow envelope gần production,
    chưa phải wrap path hoặc bằng chứng chữ thật đã vừa;
  - `textCapacityProof`: toàn bộ chữ đã vừa, không overflow, không cột quá hẹp,
    không lỗi reading order và không ép typography;
  - `cleanCompositionMap`: map không có chữ để khóa staging khi generation;
  - `textIntegrationStatus`: `REFLOW_PREFLIGHT_PASS`,
    `PROXY_COMPOSITION_PASS` hoặc `COMPOSITION_NEEDS_REVISION`;
  - với proxy: `exactTextCapacity: DEFERRED_TO_INDESIGN`, `proxyTextPlan`,
    `productionLayoutProxy`, `backgroundValueMap`, `detailDensityMap`,
    `integrationEdgeMap`, `glyphPressureMap` và `integrationModes`;
  - `proxyFidelityProof` schema 4 theo `../comic-layout-qa/references/proxy-typography-measurement.md`: artifact path + SHA-256 cho source, semantic
    SVG và preview; `sourceTextRegions` cho mọi occurrence; ánh xạ một-một sang
    SVG text-overlay group chứa `<text>` thật, không buộc artwork là SVG; readable scale sau transform, content units, line count,
    paragraph map, leading, reading order, wrap review và
    `spatialComparisonIgnored: true`; chữ được tự do chuyển vị trí nên proof
    không chứa positional similarity;
  - `proxyBurdenStatus`: chỉ nhận `PROXY_BURDEN_PASS` hoặc `FAIL`;
  - `proxyLayoutStatus`: chỉ nhận `PROXY_LAYOUT_PASS` hoặc `FAIL`;
  - chỉ ghi `textIntegrationStatus: PROXY_COMPOSITION_PASS` khi cả hai status
    trên PASS; trường hợp khác ghi `COMPOSITION_NEEDS_REVISION`;
- `compositionPreview`:
  - `pngPath`: đường dẫn tới PNG riêng của option;
  - `previewMethod`: mặc định `IMAGEGEN_MINIMAL_PENCIL`; lưu `promptPath`, `artworkPath`, reference map và text overlay riêng khi có chữ. `semanticSvgPath` chỉ bắt buộc khi chọn SVG;
  - `debugPngPath`: overlay geometry riêng, không phải preview lựa chọn;
  - `renderMode`: mặc định `raster` với phác ImageGen; `semantic-svg`, `collage` hoặc `custom-vector` khi người dùng chọn rõ;
    `debug-box` không hợp lệ ở cổng duyệt composition;
  - `actors`: actor ID, profile reference, dấu hiệu identity lấy từ profile. Với SVG, khai semantic
    parts (`head`, `torso`, `gesture`); raster dùng reference map và review bằng mắt, không bịa marker hoặc bắt phác đơn sắc có palette màu;
  - `requiredLocationAnchors` và `requiredInteractions`;
  - `layoutBasis`: canvas trang/spread, typography/content budget, brief region,
    hard frame/mask thật, fixed element, trim, safe zone và gáy. Composition của
    direction đã chọn có shot preview và reflow preflight dùng chữ thật để chứng
    minh capacity;
    `briefRegion` không được dùng làm ranh giới cứng;
  - `legend`: các nhãn hoặc ký hiệu cần để đọc sơ đồ;
  - `previewStatus`: `READY`, `BLOCKED` hoặc `NOT_APPLICABLE`;
- Với `TEXT_PROXY_INTEGRATION`, thêm `shotMap`,
  `productionCompositionPreview` và `integrationCrop100`;
- Với `BAKED_TEXT_PROXY_CONCEPT`, thêm các artifact trên cùng `textFootprint`,
  `interactionEdges`, `bakedProxyGenerationReference`, `proxyRemovalMask`,
  `repairContextRing`, `protectedArtworkMask` và `indesignTextFootprint`;
- `contextLocks`, `forbidden` và `creativeFreedom` phải tách riêng; không dùng
  creative freedom làm hard continuity lock;
- `selectedPageComposition`: có `status: PROPOSED|CONFIRMED`, camera, shot size,
  staging, relative placement/scale/crop, silhouette, eye path và background
  depth và `sceneExtentPlan`. Chỉ `CONFIRMED` mới được bàn giao sang prompt/production;
- Với chủ thể bị cắt, `cropReadPlan` được ghi trong storyboard và
  `selectedPageComposition` theo [crop-read-contract.md](crop-read-contract.md).
  Plan phải có bằng chứng thị giác trong preview; không chỉ nhãn waist crop.
- `layerSeparationPlan`: kế hoạch hậu kỳ sau khi master được chọn, gồm vùng
  visible art sẽ khóa pixel, vùng được phép expand, nền cần clean plate, nhóm
  mid+foreground, vật/bóng đi cùng chủ thể và silhouette text wrap; chưa tạo
  layer ở giai đoạn storyboard;
- Với `BAKED_TEXT_PROXY_CONCEPT`, `layerSeparationPlan` phải ghi concept có proxy
  chỉ là provenance; clean master được tạo bằng edit/inpaint sau selection và
  cần `CLEAN_PLATE_PASS` trước khi tách layer;
- đánh đổi layout đang áp dụng.

## Phân tách artifact

Lưu hai artifact có vai trò khác nhau:

- `<option>-storyboard.json`: nguồn đầy đủ cho shot, prompt và phần trình bày;
- `<option>-preview-contract.json`: contract tối thiểu để kiểm SVG và render.

Preview contract là consumer của storyboard artifact, không phải nguồn thay thế.

## Composition card dành cho người dùng

Mỗi composition hoặc revision được trình duyệt phải có `userFacingCard` để bảo
đảm dữ liệu quan trọng được trình
bày ngay trong hội thoại, không chỉ tồn tại trong artifact nội bộ:

- `summary`: kết quả và đánh đổi trong một dòng;
- `sceneMeaning`;
- `selectedMoment`;
- `focusAndEyePath`;
- `staging`;
- `emotionRead`;
- `requiredEvidence`;
- `forbiddenReadings`;
- `continuityForbidden`;
- `layoutImpact`;
- `tradeoff`.

`userFacingCard` không tạo dữ kiện mới. Rút từng mục từ các field đầy đủ của
composition và viết bằng ngôn ngữ tự nhiên, tránh bắt người dùng đọc key kỹ thuật.
Không đặt `compositionPreview.previewStatus: READY` nếu composition mới chỉ có
preview contract mà chưa có storyboard artifact và `userFacingCard`.

`meaningPreservationCheck` phải kiểm tra cả hai chiều: phần giản lược không làm
mất quy mô, quan hệ, tính tập thể hoặc cảm xúc; phần biểu hiện trực tiếp không
làm mất sự tinh tế, tính tự nhiên hay khoảng trống cho người đọc. Focus rõ chưa
đủ để PASS.

Mỗi dependency nên dùng key ổn định từ context resolution thay vì chép lại văn
bản dài. `writesIfApproved` là khai báo tác động dự kiến, không phải quyền cập
nhật continuity ledger.

Với composition được đưa ra cho người dùng duyệt,
`compositionPreview.previewStatus` phải là `READY`, `pngPath` phải tồn tại và
preview phải được hiển thị. Mô tả chữ không thay thế cho PNG preview.
`debug-box` không thể có trạng thái `READY` cho cổng duyệt, dù file PNG tồn tại.
