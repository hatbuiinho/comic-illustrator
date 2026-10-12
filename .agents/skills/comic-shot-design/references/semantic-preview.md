# Preview composition bằng SVG semantic

Đây là phương pháp mặc định cho phác thảo composition. Giữ SVG làm source chỉnh
sửa được và render PNG để review. Không dùng công cụ tạo ảnh ở bước này trừ khi
người dùng yêu cầu rõ; ngoại lệ được ghi `SKIPPED_BY_USER` cho deliverable hiện tại.

Preview SVG do agent dựng riêng theo shot, dùng silhouette, pose,
interaction, background và bảng màu lấy từ profile đúng tập. Script chỉ kiểm
contract và rasterize; không thay cảnh bằng bounding box.

Tổ chức actor, bộ phận pose, bối cảnh và vùng chữ thành group riêng; dùng tham số
hoặc transform cho vị trí, tỷ lệ và xoay. Khi phản hồi yêu cầu sửa, chỉnh source
hiện có rồi render version mới. Đổi camera cần sửa cả hướng mặt/thân, tỷ lệ
trước–sau và tín hiệu phối cảnh liên quan, không chỉ dịch các hình trên trang.

Mức hoàn thiện là nét phác và mảng giản lược. Không cần shading, texture hoặc
chi tiết production. Review những quyết định nhìn thấy được; ghi rõ tín hiệu
biểu cảm chưa kiểm chứng được để kiểm tiếp ở production. Duyệt SVG không khóa
contour thô và không đồng nghĩa duyệt chất lượng artwork cuối.

## Hai lớp output

- `<option>-composition.png`: preview semantic của direction đã chọn để người
  dùng duyệt composition.
- `<option>-debug.png`: geometry, label, safe zone, spine và recognition box.

Debug-box không được dùng thay preview chính.

Với chủ thể bị cắt, preview toàn trang phải cho thấy chủ thể đi qua mép trang
hoặc khung/mask inset thật, hay tiếp tục sau vật che nhìn thấy, theo
[crop-read-contract.md](crop-read-contract.md). Không dùng footprint cảnh hoặc
biên hòa giấy làm biên camera tưởng tượng giữa trang.
Không chỉ cắt polygon thân rồi đặt lên đất. Review cách đọc crop trước trình
duyệt; contour thô của SVG không phải khuôn phải sao chép khi render artwork.

## Marker bắt buộc

Root SVG có `data-preview-type="semantic-composition"`. Mỗi actor dùng group
`data-role="actor"`, `data-actor-id` và `data-profile-ref`. Các phần đủ để đọc
pose có `data-owner` cùng `data-part="head|torso|gesture"`. Location và
interaction bắt buộc dùng `data-location-anchor` và `data-interaction`.

Palette trong composition contract lấy từ profile gốc đã đọc. Dùng màu để nhận
biết nhanh, không sao chép preview thành identity reference và không cho nhân
vật khác mượn palette đặc trưng.

Khi direction phụ thuộc diễn xuất, mỗi actor thêm semantic part `gaze`,
`hand-gesture` và `posture` hoặc marker tương đương đủ nhìn thấy. Preview phải có
crop đọc được cụm mặt–tay–quan hệ, không chỉ thumbnail toàn spread. Contract ghi
`intendedRead` và `forbiddenReads`; renderer thành công không tự tạo
`PERFORMANCE_READ_PASS`, vẫn phải review bằng mắt cách pose thực sự được đọc.

## Routing

1. Sau khi narrative direction đã được chọn, agent viết semantic SVG phù hợp
   riêng với composition đang đề xuất.
2. Chạy `scripts/render-composition-preview.js <svg> <contract.json> [png]`.
3. Nếu quality gate báo `SEMANTIC_RENDER_INSUFFICIENT`, bổ sung SVG; không hạ
   xuống debug-box.
4. Chỉ chạy `render-composition-debug.js` khi cần kiểm geometry nội bộ.
