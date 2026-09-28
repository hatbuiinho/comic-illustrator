---
name: comic-production
description: Điều phối quy trình minh họa truyện tranh nhiều giai đoạn từ đọc nguồn đến bàn giao. Dùng khi người dùng yêu cầu làm hoàn chỉnh một page, frame hoặc chuỗi shot; không dùng cho một tác vụ độc lập đã nêu rõ.
---

# Điều phối sản xuất truyện tranh

Xác định deliverable và chỉ thực hiện các giai đoạn cần thiết. Yêu cầu trực tiếp
mới nhất của người dùng luôn được ưu tiên hơn mặc định của workflow.

## Routing

1. Đọc và kiểm chứng nguồn: dùng `comic-source-reader`.
2. Thiết kế shot/storyboard: dùng `comic-shot-design`.
3. Viết prompt: dùng `comic-prompt-writer`.
4. Tạo, chỉnh hoặc tạo variant ảnh: dùng `comic-image-production`.
5. Kiểm tra nội dung nhìn thấy: dùng `comic-visual-qa`.
6. Kiểm tra ảnh trong layout: chỉ dùng `comic-layout-qa` khi deliverable gắn
   với layout hoặc người dùng yêu cầu.
7. Chuyển bản đã duyệt vào `approved/`: dùng `comic-delivery`.

Không chạy lại giai đoạn đã được người dùng chốt nếu đầu vào của giai đoạn đó
không thay đổi. Không tự biến một tác vụ độc lập thành toàn bộ pipeline.

## Trạng thái kiểm tra

Mỗi kiểm tra điều kiện phải là một trong ba trạng thái:

- `REQUIRED`: áp dụng và có thể làm deliverable FAIL.
- `NOT_APPLICABLE`: không liên quan đến loại deliverable.
- `SKIPPED_BY_USER`: người dùng chủ động bỏ qua; ghi lý do và phạm vi, không
  tính là FAIL.

Nếu người dùng không nêu phạm vi override, chỉ áp dụng cho deliverable hiện tại.

## Điểm dừng

Chỉ yêu cầu quyết định khi lựa chọn làm thay đổi đáng kể nội dung, composition
hoặc output active. Khi có 2–3 lựa chọn thực tế, trình bày thành danh sách đánh
số ngắn. Không chuyển file sang `approved/` nếu chưa có xác nhận rõ.
