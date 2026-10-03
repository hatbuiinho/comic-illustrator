# Schema storyboard tối thiểu

Mỗi option gồm:

- `optionId`;
- `sceneMeaning`;
- `readerExperience`: điều cần hiểu, cảm nhận và bằng chứng;
- `shotThesis`: moment, viewpoint, focus, out-of-frame;
- `cinematicIntent`;
- `populationPlan`: trong cảnh, trong khung, cần đọc rõ, vai trò nhóm;
- `compositionStrategy`;
- `spatialDepthPlan`;
- `emotionLock`;
- `criticalAnatomy`: các bộ phận cơ thể mang focus, cảm xúc, cử chỉ, tương tác
  hoặc chiếm diện tích lớn; mỗi mục ghi `subject`, `bodyPart`, `intendedPose` và
  `mustRead`. Bộ phận thuộc `explicitRequired` và giữ ý nghĩa kể chuyện phải
  được khai báo tại đây;
- `profileReferences`;
- `continuityDependencies`:
  - `reads`: các fact/lock mà option dựa vào;
  - `writesIfApproved`: thay đổi chỉ có thể ghi sau delivery/xác nhận phù hợp;
  - `mustNotChange`: trạng thái hình không được vô tình thay đổi;
  - `forbidden`: chi tiết tương lai hoặc trạng thái sai không được xuất hiện;
- `locationAnchors` khi áp dụng;
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
- `compositionPreview`:
  - `pngPath`: đường dẫn tới PNG riêng của option;
  - `semanticSvgPath`: SVG semantic nguồn do Codex dựng theo shot;
  - `debugPngPath`: overlay geometry riêng, không phải preview lựa chọn;
  - `renderMode`: `semantic-svg` cho preview chính; `custom-vector` khi cảnh cần
    SVG đặc thù; `debug-box` không hợp lệ ở cổng lựa chọn;
  - `actors`: actor ID, profile reference, palette lấy từ profile và semantic
    parts bắt buộc (`head`, `torso`, `gesture` mặc định);
  - `requiredLocationAnchors` và `requiredInteractions`;
  - `layoutBasis`: frame/mask/aspect ratio dùng để dựng preview;
  - `legend`: các nhãn hoặc ký hiệu cần để đọc sơ đồ;
  - `previewStatus`: `READY`, `BLOCKED` hoặc `NOT_APPLICABLE`;
- đánh đổi layout đang áp dụng.

## Phân tách artifact

Lưu hai artifact có vai trò khác nhau:

- `<option>-storyboard.json`: nguồn đầy đủ cho shot, prompt và phần trình bày;
- `<option>-preview-contract.json`: contract tối thiểu để kiểm SVG và render.

Preview contract là consumer của storyboard artifact, không phải nguồn thay thế.

## Composition card dành cho người dùng

Mỗi option phải có `userFacingCard` để bảo đảm dữ liệu quan trọng được trình
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
option và viết bằng ngôn ngữ tự nhiên, tránh bắt người dùng đọc key kỹ thuật.
Không đặt `compositionPreview.previewStatus: READY` nếu option mới chỉ có
preview contract mà chưa có storyboard artifact và `userFacingCard`.

`meaningPreservationCheck` phải kiểm tra cả hai chiều: phần giản lược không làm
mất quy mô, quan hệ, tính tập thể hoặc cảm xúc; phần biểu hiện trực tiếp không
làm mất sự tinh tế, tính tự nhiên hay khoảng trống cho người đọc. Focus rõ chưa
đủ để PASS.

Mỗi dependency nên dùng key ổn định từ context resolution thay vì chép lại văn
bản dài. `writesIfApproved` là khai báo tác động dự kiến, không phải quyền cập
nhật continuity ledger.

Với option được đưa ra cho người dùng chọn, `compositionPreview.previewStatus`
phải là `READY`, `pngPath` phải tồn tại và preview phải được hiển thị. Mô tả chữ
không thay thế cho PNG preview. `debug-box` không thể có trạng thái `READY` cho
cổng lựa chọn, dù file PNG tồn tại.
