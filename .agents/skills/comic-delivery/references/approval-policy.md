# Chính sách duyệt

- Chọn output không thay thế QA.
- Không tự chọn active output khi có variant hoặc trade-off.
- Chỉ một lệnh xác nhận rõ cho output cụ thể mới cho phép chuyển file.
- Không chuyển variant chưa chọn.
- Không ghi đè file đã duyệt.
- Báo output active, trạng thái QA, override và lỗi còn lại ảnh hưởng page.
- Chỉ commit continuity event có source fact hoặc xác nhận người dùng đủ rõ;
  `writesIfApproved` tự nó không phải bằng chứng.
- Nếu file đã approved nhưng ledger chưa đồng bộ, giữ file và ghi
  `approved-filed-context-pending`; không tuyên bố context downstream hoàn tất.
