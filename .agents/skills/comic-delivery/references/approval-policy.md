# Chính sách duyệt

- Chọn output không thay thế QA; nó chuyển master sang
  `SELECTED_FOR_LAYOUT` để chuẩn bị bộ layer InDesign.
- Không tự chọn active output khi có variant hoặc trade-off.
- Chỉ một lệnh xác nhận rõ cho output cụ thể mới cho phép chuyển file.
- Không chuyển variant chưa chọn.
- Không tách layer cho variant chưa chọn. Không trộn layer khác version hoặc
  sửa nội dung master trong bước hậu kỳ.
- Không ghi đè file đã duyệt.
- Báo output active, trạng thái QA, override và lỗi còn lại ảnh hưởng page.
- Chỉ chuyển cả bộ asset vào `approved/` sau khi `bg + mgfg` khớp master, wrap
  path hợp lệ và clean layout preview xác nhận nhân vật không đè chữ.
- Chỉ commit continuity event có source fact hoặc xác nhận người dùng đủ rõ;
  `writesIfApproved` tự nó không phải bằng chứng.
- Nếu file đã approved nhưng ledger chưa đồng bộ, giữ file và ghi
  `approved-filed-context-pending`; không tuyên bố context downstream hoàn tất.
