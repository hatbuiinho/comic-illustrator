# Crop ref màu y v002

- Ngày: 2026-10-23. Người dùng yêu cầu crop chỉ chứa vải, giữ nguyên mẫu màu y đã chọn.
- Nguồn: `mau-y-chuan-v001.png` (1920 × 1200); provenance tại `mau-y-chuan-v001.md`.
- Output: `mau-y-chuan-crop-v002.png` (200 × 380).
- Phương pháp: Pillow crop hộp `(530, 350, 730, 730)`, gốc tọa độ trên trái; phải/dưới không bao gồm. Không resize, chỉnh màu, lọc hoặc sinh lại bằng model.
- Vai trò: chỉ màu y, không lấy thiết kế/cách quấn/hình học bóng/rendering. Không phải chuẩn màu mới.
- Kiểm trực tiếp: chỉ vải và nét nếp vải, không mặt/da/chữ/nền. Đạt cho ref màu y.
- v001 là crop thử còn da, đã loại khỏi asset cuối; chưa dùng tạo ảnh.
