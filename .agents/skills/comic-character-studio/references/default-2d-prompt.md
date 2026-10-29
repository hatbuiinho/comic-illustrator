# Prompt chuyển style mặc định — ttpq comic light

Cập nhật ngày 2026-10-29, thay toàn bộ khối rendering cũ.
Chỉ @ skill kèm ảnh gốc vẫn đủ khởi động chuyển style, không tự tạo sheet.

## Lắp prompt

1. Chép nguyên khối STYLE tại
   [định nghĩa độc lập](../../../../docs/style-ttpq-comic-light.md).
2. Thêm khối giữ nguồn dưới đây, điều chỉnh theo brief thực tế.
3. Chỉ khi có tu sĩ, đọc và bổ sung
   [màu y/cách quấn y](../../../../docs/monastic-robes.md), phân vai ref rõ.
4. Ghi điều cấm phù hợp ngay từ đầu; không dùng ref style/bảng trang sức cũ.

```text
Giữ identity theo ảnh/profile gốc: cấu trúc mặt, tuổi, biểu cảm, màu da,
ngũ quan, tóc/râu nếu có và tỷ lệ tự nhiên. Không tự trẻ hóa, lý tưởng hóa
quá mức, đổi hình hoặc màu môi, phóng mắt, thu mũi hay làm thon mặt.
Giữ thiết kế trang phục, phụ kiện, tư thế và bố cục theo yêu cầu tác vụ;
resolve quy chuẩn y riêng nếu có tu sĩ. Chỉ chuyển cách thể hiện sang
"ttpq comic light"; không lấy identity hoặc thiết kế từ output trước.
Chỉ áp dụng ràng buộc cho thành phần thực sự xuất hiện trong ảnh.
```

## QA và lưu

QA theo [qa-checklist.md](qa-checklist.md). Lưu prompt, input/vai trò, ngoại lệ và QA
có version theo contract studio. Chờ người dùng duyệt ảnh trước bước sheet;
chỉ lưu profile khi được chọn rõ theo workflow.
