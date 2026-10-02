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
- `profileReferences`;
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
  - `layoutBasis`: frame/mask/aspect ratio dùng để dựng preview;
  - `legend`: các nhãn hoặc ký hiệu cần để đọc sơ đồ;
  - `previewStatus`: `READY`, `BLOCKED` hoặc `NOT_APPLICABLE`;
- đánh đổi layout đang áp dụng.

`meaningPreservationCheck` phải kiểm tra cả hai chiều: phần giản lược không làm
mất quy mô, quan hệ, tính tập thể hoặc cảm xúc; phần biểu hiện trực tiếp không
làm mất sự tinh tế, tính tự nhiên hay khoảng trống cho người đọc. Focus rõ chưa
đủ để PASS.

Với option được đưa ra cho người dùng chọn, `compositionPreview.previewStatus`
phải là `READY`, `pngPath` phải tồn tại và preview phải được hiển thị. Mô tả chữ
không thay thế cho PNG preview.
