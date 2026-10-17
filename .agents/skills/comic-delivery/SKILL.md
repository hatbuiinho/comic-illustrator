---
name: comic-delivery
description: Hoàn tất và lưu bản minh họa truyện tranh đã được QA và người dùng chọn, gồm version, approved và cập nhật đường dẫn. Chỉ dùng sau xác nhận rõ; không dùng để tự chọn output.
---

# Bàn giao output

Đọc [status-model.md](references/status-model.md) và
[approval-policy.md](references/approval-policy.md).

Mặc định delivery chỉ chuyển đúng hình đã được người dùng chọn vào `approved/`
và cập nhật đường dẫn. Không tự tạo thêm ảnh, tách nhân vật/background, tách
layer, expand, tháo proxy hoặc tạo wrap. Việc chọn master hay nói “bàn giao”
không tự cấp phép những tác vụ bổ sung đó.

Chỉ thực hiện khi:

- output bắt buộc tồn tại;
- visual QA bắt buộc đã PASS;
- layout QA đã PASS, hoặc là `NOT_APPLICABLE`, hoặc các check liên quan được
  người dùng ghi rõ `SKIPPED_BY_USER`;
- người dùng đã chọn đúng output khi có variant.
- chỉ khi người dùng đã yêu cầu rõ InDesign layer package: master ở
  `SELECTED_FOR_LAYOUT`, bộ `master + bg + mgfg + wrap + layout-preview` cùng
  version đã tồn tại và layout QA kỹ thuật đã PASS.
- với `BAKED_TEXT_PROXY_CONCEPT`, được lưu đúng concept đã chọn vào `approved/`
  với vai trò `integratedTextConcept`, ghi rõ chưa phải artwork sạch để in.
  Chỉ khi người dùng yêu cầu artwork sạch hoặc bộ layer mới cần
  `cleanArtworkMaster` đạt `CLEAN_PLATE_PASS`; không tự tháo proxy.

Trước khi thay đổi file, chạy `scripts/validate-delivery.js <delivery.json>` và
`scripts/execute-delivery.js <delivery.json>` để xem dry-run. Chỉ thêm
`--execute` sau khi plan khớp đúng output, approved directory và các path update.

Chuyển file đã chọn từ `outputs/` sang `approved/` trong đúng page/tập; chỉ
chuyển toàn bộ layer package khi người dùng đã yêu cầu và bộ đó qua QA áp dụng.
Giữ tên version; nếu một đích tồn tại, dừng và tạo version
mới, không ghi đè. Cập nhật mọi manifest và đường dẫn tiêu thụ. Không để hai bộ
khác version cùng đóng vai trò nguồn chuẩn.

Sau khi file và đường dẫn đã cập nhật thành công, gọi
`comic-continuity-manager` ở chế độ `COMMIT_EVENT` cho các thay đổi đã được
nguồn hoặc người dùng xác nhận. Dùng `writesIfApproved` làm danh sách ứng viên
để kiểm tra, không coi nó là bằng chứng tự đủ. Sau đó chạy `INVALIDATE` để đánh
dấu đúng artifact downstream phụ thuộc event/revision đã đổi.

Nếu cập nhật ledger thất bại, không hoàn tác hoặc xóa file approved đã bàn giao;
ghi trạng thái delivery là cần reconciliation và báo chính xác phần context còn
chưa đồng bộ. Dùng `scripts/reconcile-delivery.js <receipt.json>` để thử hoàn
tất phần còn thiếu; không tự tạo event để làm cho workflow có vẻ hoàn tất.

## Đề xuất làm thêm sau bàn giao

Sau khi lưu hình thành công, đưa 2–3 đề xuất có ích cho đúng ảnh, ví dụ tách
nhân vật chính thành PNG alpha bằng ImageGen, tạo background clean plate bằng
ImageGen, hoặc chuẩn bị bộ layer/đường wrap cho InDesign. Mỗi đề xuất nêu ngắn
kết quả và đánh đổi; ImageGen có thể tái tạo nét, đổi tỷ lệ hoặc vị trí, không
hứa giữ nguyên từng pixel. Dùng follow-up tùy chọn hoặc câu trả lời copy đầy đủ
theo quy tắc project. Không biến đề xuất thành cổng bắt buộc và không chạy
cho tới khi người dùng yêu cầu rõ. Output bổ sung nằm trong `outputs/`, có
version và QA riêng; không tự thay hình đã approved.
