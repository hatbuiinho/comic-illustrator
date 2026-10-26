---
name: comic-image-playground
description: Tạo hoặc chỉnh ảnh tự do trong Image Playground theo style dự án và profile được mention; dùng cho concept, poster, thử pose/cảnh độc lập với minh họa tập/page.
---

# Image Playground

Đọc và áp dụng [contract studio](../../../docs/studio-contract.md).

- Nhận yêu cầu ảnh, profile/reference được chỉ định và tỷ lệ khung nếu có.
  Không bắt có nhân vật/profile cho ảnh phong cảnh hoặc vật thể; nhân vật mới
  có thể theo brief, nhưng phát triển profile chính thức dùng Character Studio.
- Resolve từng reference và ghi vai trò; nhiều profile phải giữ identity riêng,
  không trộn mặt, tóc, trang phục hoặc dấu nhận diện giữa các nhân vật.
- Brief đủ rõ thì viết prompt và tạo ngay. Không bắt chọn direction hay duyệt
  storyboard. Suy luận vừa đủ chi tiết chưa nêu, không tự thêm sự kiện canon.
- Khi sửa, nêu delta và các phần giữ nguyên; xem lại ảnh đích cùng profile gốc.
  Tạo version mới trong Playground, kể cả khi ảnh đích xuất phát từ một tập.
- Khi chuyển ảnh gốc sang style dự án và cần giữ chi tiết, đọc
  [chuyển style giữ nguồn](references/source-faithful-restyling.md). Áp dụng
  khóa mảng theo nguồn và phân vai ref; có trang sức thì dùng phương án giảm
  bóng đã tạm chốt trong reference, không lấy thiết kế từ bảng vật liệu.
- Copy output của lượt (ảnh tạo, crop nguồn) vào
  `studios/playground/outputs/<request-id>/` theo contract; chỉ trình người
  dùng bản trong thư mục đó. Ảnh so sánh QA không cần lưu.
- Bàn giao ảnh cùng kết quả kiểm style/identity ngắn gọn. Ảnh Playground không
  tự trở thành character profile, canon, master hoặc asset đã duyệt của tập.
