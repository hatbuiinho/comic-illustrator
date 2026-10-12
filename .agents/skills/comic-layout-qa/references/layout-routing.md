# Routing layout QA

- Full spread hoặc artwork linh hoạt qua hai trang: text/subject exclusion,
  print-safe và spine mặc định `REQUIRED`; frame/ratio chỉ `REQUIRED` khi có
  hard frame hoặc mask thật.
- Trang đơn: spine mặc định `NOT_APPLICABLE`; kiểm text/subject exclusion và
  print-safe. Brief region không tạo frame check.
- Hình chen nằm trong một trang: spine `NOT_APPLICABLE` trừ khi frame thật sự
  chạm vùng đóng sách.
- Concept art, profile, style test hoặc ảnh chưa gắn layout: toàn bộ layout QA
  `NOT_APPLICABLE`.
- Bộ layer InDesign chỉ kiểm sau `SELECTED_FOR_LAYOUT`; trước đó layer QA là
  `NOT_APPLICABLE`.
- Page không có `briefRegion` và hard frame: dùng
  `GENERATION_LAYOUT_INTEGRATION`; resolve contract trong
  `text-artwork-integration.md`. `FINAL_TEXT_REFLOW` chạy proof chữ thật;
  `TEXT_PROXY_INTEGRATION` chạy production proxy và hoãn exact capacity,
  `typographyIntegrity`, `textIntegrity` sang InDesign;
  `BAKED_TEXT_PROXY_CONCEPT` dùng proxy bake trong concept để AI đồng thiết kế
  hình–chữ, rồi bắt buộc clean-plate gate trước bộ layer InDesign.

Yêu cầu mới nhất của người dùng có thể chuyển một check thành
`SKIPPED_BY_USER`. Ghi lý do và phạm vi. Nếu không nêu phạm vi, chỉ áp dụng cho
deliverable hiện tại.
