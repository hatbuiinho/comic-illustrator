---
name: comic-delivery
description: Hoàn tất và lưu bản minh họa truyện tranh đã được QA và người dùng chọn, gồm version, approved và cập nhật đường dẫn. Chỉ dùng sau xác nhận rõ; không dùng để tự chọn output.
---

# Bàn giao output

Đọc [status-model.md](references/status-model.md) và
[approval-policy.md](references/approval-policy.md).

Chỉ thực hiện khi:

- output bắt buộc tồn tại;
- visual QA bắt buộc đã PASS;
- layout QA đã PASS, hoặc là `NOT_APPLICABLE`, hoặc các check liên quan được
  người dùng ghi rõ `SKIPPED_BY_USER`;
- người dùng đã chọn đúng output khi có variant.
- nếu deliverable dùng InDesign layer package: master ở
  `SELECTED_FOR_LAYOUT`, bộ `master + bg + mgfg + wrap + layout-preview` cùng
  version đã tồn tại và layout QA kỹ thuật đã PASS.
- nếu contract là `BAKED_TEXT_PROXY_CONCEPT`: `integratedTextConcept` chỉ được
  lưu làm provenance; `cleanArtworkMaster` phải đạt `CLEAN_PLATE_PASS` và bộ
  layer không được chứa glyph proxy trước khi chuyển vào `approved/`.

Trước khi thay đổi file, chạy `scripts/validate-delivery.js <delivery.json>` và
`scripts/execute-delivery.js <delivery.json>` để xem dry-run. Chỉ thêm
`--execute` sau khi plan khớp đúng output, approved directory và các path update.

Chuyển file đã chọn hoặc toàn bộ layer package từ `outputs/` sang `approved/`
trong đúng page/tập. Giữ tên version; nếu một đích tồn tại, dừng và tạo version
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
