# Preview composition bằng SVG semantic

Preview chính là SVG do Codex dựng riêng theo shot, dùng silhouette, pose,
interaction, background và bảng màu lấy từ profile đúng tập. Script chỉ kiểm
contract và rasterize; không thay cảnh bằng bounding box.

## Hai lớp output

- `<option>-composition.png`: preview semantic để người dùng lựa chọn.
- `<option>-debug.png`: geometry, label, safe zone, spine và recognition box.

Debug-box không được dùng thay preview chính.

## Marker bắt buộc

Root SVG có `data-preview-type="semantic-composition"`. Mỗi actor dùng group
`data-role="actor"`, `data-actor-id` và `data-profile-ref`. Các phần đủ để đọc
pose có `data-owner` cùng `data-part="head|torso|gesture"`. Location và
interaction bắt buộc dùng `data-location-anchor` và `data-interaction`.

Palette trong composition contract lấy từ profile gốc đã đọc. Dùng màu để nhận
biết nhanh, không sao chép preview thành identity reference và không cho nhân
vật khác mượn palette đặc trưng.

## Routing

1. Codex viết semantic SVG phù hợp riêng với option.
2. Chạy `scripts/render-composition-preview.js <svg> <contract.json> [png]`.
3. Nếu quality gate báo `SEMANTIC_RENDER_INSUFFICIENT`, bổ sung SVG; không hạ
   xuống debug-box.
4. Chỉ chạy `render-composition-debug.js` khi cần kiểm geometry nội bộ.
