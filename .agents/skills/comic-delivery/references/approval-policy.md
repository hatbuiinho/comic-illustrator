# Chính sách duyệt

- Chọn output không thay thế QA; nó xác định hình sẽ bàn giao. Có thể giữ
  trạng thái `SELECTED_FOR_LAYOUT` cho tương thích, nhưng không suy từ trạng
  thái này ra yêu cầu hay quyền tự tách layer.
- Không tự chọn active output khi có variant hoặc trade-off.
- Chỉ một lệnh xác nhận rõ cho output cụ thể mới cho phép chuyển file.
- Không chuyển variant chưa chọn.
- Chỉ tách layer khi người dùng yêu cầu rõ, sau khi chọn đúng nguồn. Không trộn layer khác version hoặc
  sửa nội dung master trong bước hậu kỳ.
- Không ghi đè file đã duyệt.
- Báo output active, trạng thái QA, override và lỗi còn lại ảnh hưởng page.
- Delivery ảnh đơn không đòi bộ layer, clean plate, alpha hoặc wrap. Nếu người
  dùng yêu cầu bộ layer, chỉ chuyển cả bộ asset vào `approved/` sau khi `bg + mgfg` khớp master, wrap
  path hợp lệ và clean layout preview xác nhận nhân vật không đè chữ.
- Chỉ commit continuity event có source fact hoặc xác nhận người dùng đủ rõ;
  `writesIfApproved` tự nó không phải bằng chứng.
- Nếu file đã approved nhưng ledger chưa đồng bộ, giữ file và ghi
  `approved-filed-context-pending`; không tuyên bố context downstream hoàn tất.

Quyết định workflow của người dùng ngày 2026-10-14: `SKIPPED_BY_USER` đối với
quy tắc cũ tự tách sau selection. Mặc định mới là lưu hình đã chọn, rồi đề xuất
tác vụ bổ sung tùy nhu cầu; không tự áp lại quy tắc tách bắt buộc.
