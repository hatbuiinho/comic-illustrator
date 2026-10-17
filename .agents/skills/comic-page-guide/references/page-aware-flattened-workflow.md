# Workflow page-aware flattened artwork

Dùng cho page/spread mà shot được duyệt trước, sau đó layout chữ thật được đưa
vào ngay tại bước tạo hình để artwork và chữ hòa quyện. Delivery mặc định lưu
đúng ảnh được chọn; hậu kỳ cho InDesign chỉ chạy khi người dùng yêu cầu.

## Chuỗi bắt buộc

1. Đọc canvas, trim, gáy, safe zone, mask thật, fixed element, content, reading
   order và typography từ layout gốc. Khóa content/typography, không khóa vị trí
   text frame ban đầu.
2. `comic-shot-design` đưa 2–3 narrative direction bằng chữ, ưu tiên cảm nhận
   của người đọc, emotional thesis, khoảnh khắc, cách kể và đánh đổi. Không dựng
   shot preview, reflow preview hoặc layout proof ở bước này.
3. Sau khi người dùng chọn một direction, dựng phác chì ImageGen tối giản
   theo `comic-shot-design/references/pencil-composition-preview.md`; SVG chỉ
   khi người dùng chọn rõ. Composition preview thể
   hiện camera, cỡ cảnh, vị trí/tỷ lệ/crop tương đối, emotional anchor, eye path
   và lớp sâu trong `sceneExtentPlan` vừa đủ; preview toàn canvas bao gồm cả
   nền giấy/khoảng thở chủ ý, không bắt cảnh phủ spread.
4. Resolve contract. Nếu chữ production hoàn thiện ở InDesign và mục tiêu là để
   AI đồng thiết kế hình–chữ, dùng `BAKED_TEXT_PROXY_CONCEPT`: dựng text-burden
   proxy gần production và đưa proxy vào composition toàn trang. Nếu cần chữ
   thật trước generation, tiếp tục dùng `FINAL_TEXT_REFLOW`.
5. Chạy art-direction gate trên shot preview và reflow preview ở mức phác thảo:
   kiểm ý đồ cảm xúc, visual thesis, camera/staging, figure–ground, rhythm,
   eye path, page character và text capacity bằng dấu hiệu nhìn thấy. Không đòi
   nét, ánh sáng, chất liệu hoặc biểu cảm hoàn thiện như production; ghi rõ
   phần chưa kiểm chứng, không tự ghi PASS cho phần đó.
6. Người dùng xác nhận composition thì khóa `selectedPageComposition`: camera,
   shot size, staging, silhouette, relative placement/scale/crop, eye path và
   background depth.
7. Kế thừa proxy/reflow đã PASS; khóa text footprint, interaction edge, vùng
   glyph được phép sửa và recognition core không được đổi.
8. Với `BAKED_TEXT_PROXY_CONCEPT`, tạo `integratedTextConcept` từ composition có
   proxy; model được dùng proxy như element thị giác nhưng không được đổi shot,
   reading order hoặc text burden. Với contract khác, tạo candidate theo contract
   đó.
9. Chạy visual QA và layout art-direction QA trên toàn trang. Chữ sai không phải
   lỗi ở mode baked; footprint giả, proxy co nhỏ hoặc hình–chữ không hòa nhập là lỗi.
10. Khi người dùng chọn đích danh ảnh/concept và QA áp dụng đạt, ghi selection
    rồi dùng `comic-delivery` lưu đúng file đó vào `approved/`. Concept có proxy
    giữ vai trò `integratedTextConcept`, không được gọi là artwork sạch để in.
11. Đề xuất tùy chọn tách nhân vật/background bằng ImageGen hoặc hậu kỳ InDesign.
    Chỉ khi người dùng yêu cầu artwork sạch mới khóa artwork ngoài
    `proxyRemovalMask`, edit/inpaint concept để tạo `cleanArtworkMaster` và kiểm
    `CLEAN_PLATE_PASS`. Chỉ tạo `bg + mgfg + wrap + layout-preview` nếu họ yêu cầu
    bộ layer; không tạo lại master từ đầu.

## Invariant

- Áp mục **Phạm vi cảnh khác kích thước canvas** trong
  `../../comic-layout-qa/references/text-artwork-integration.md`. Khóa footprint
  cảnh cùng shot; generation/expand không tự mở rộng cảnh để lấp trang.

- Shot composition được tự do đề xuất trên toàn canvas nhưng chỉ được duyệt khi
  reflow chữ thật đã chứng minh capacity mà không đổi content/typography.
- Trước khi composition được xác nhận, reflow chữ thật chỉ chứng minh capacity
  cho composition của direction đã chọn. Sau xác nhận và trước generation mới
  art-direct contour/knockout/overlap cuối;
  bước này không được âm thầm đổi camera, staging hay tương quan nhân vật/cảnh.
- Typography thật được giữ ngoài deliverable artwork; chữ model sinh trong
  `integratedTextConcept` chỉ là proxy tạm. Concept được approved đúng vai trò;
  phải tháo proxy trước bàn giao artwork sạch hoặc bộ layer được yêu cầu.
- Recognition core, cử chỉ và đạo cụ kể chuyện phải nằm trong phần nhìn thấy ở
  candidate; không giao bước expand phát minh nội dung quan trọng.
- Clean-up/expand chỉ sửa vùng removal/repair đã khai báo và không được đổi pixel
  artwork được bảo vệ.
