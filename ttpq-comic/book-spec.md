# Book spec

Giá trị đo từ layout mẫu (InDesign, Minion Pro). Mỗi spread luôn đọc lại bằng
`read-layout.py`; số đo trong `layout.json` của spread được ưu tiên hơn bảng này.

## Khổ

| Mục | Giá trị |
| --- | --- |
| Spread | 810.71 × 575.43 pt (tỉ lệ 1.409), 2 trang 405.35 pt |
| Gáy | x = 405.35 pt |
| Khối chữ trang trái | x 48–346 pt, bắt đầu y ≈ 66 pt |
| Khối chữ trang phải | x 468–765 pt, bắt đầu y ≈ 66 pt |
| Số trang | Minion Pro 13 pt, y ≈ 545 pt, ở lề ngoài (trái x ≈ 48 pt, phải x ≈ 763 pt) |

## Chữ

| Mục | Giá trị |
| --- | --- |
| Font thân bài | Minion Pro Regular, 12 pt |
| Leading | 17 pt |
| Đoạn | Thụt dòng đầu ~20 pt; lời thoại bắt đầu bằng "- " thụt ~6 pt; cách đoạn ~6 pt |
| Căn lề | Justify, dòng cuối đoạn căn trái |
| Màu | Đen/nâu rất đậm |

## Canvas ChatGPT Image

ChatGPT Image tạo 1536×1024 (ngang), 1024×1536 (dọc) hoặc 1024×1024.

- **Mode spread:** canvas 1536×1024. Spread chiếm 1443 px giữa; dư 47 px mỗi bên
  là bleed chỉ có nền, sẽ cắt sau. Gáy tại x = 768 px. Chữ 12 pt ≈ 21 px,
  leading 17 pt ≈ 30 px (tỉ lệ 1024/575.43).
- **Mode frame:** canvas theo tỉ lệ vùng của Hình (xem SKILL), chọn khổ gần nhất
  trong ba khổ trên; quy đổi cỡ chữ theo cùng tỉ lệ pt → px của vùng đó.

## Quy tắc chữ ôm hình

Chữ trong ảnh ChatGPT/Codex chỉ để tham khảo dàn trang; chữ in cuối cùng dàn
trong InDesign theo cùng quy tắc này.

- **Giữ nguyên:** nội dung, thứ tự đoạn, font, cỡ, leading, ngôn ngữ từng trang
  (VI trái, EN phải). Không tóm tắt, không thêm chữ.
- **Được đổi:** độ dài từng dòng và đường biên khối chữ để ôm theo đường viền
  tranh (reflow). Tổng số dòng có thể tăng/giảm khoảng ±15% so với layout.
- **Vị trí:** chữ nằm trong trang của nó, cách gáy ≥ 30 pt, giữ lề trên và lề
  ngoài như layout; không tràn sang trang kia.
- **Nền dưới chữ:** vùng yên, sáng, ít chi tiết (trời, tường, nền đất, sương nhạt
  của phối cảnh xa). Không đặt chữ đè lên mặt, tay, hành động chính.
- **Không** khung chữ, hộp nền, bóng chữ, bong bóng thoại, chú thích.
- **Dòng tối thiểu:** không dòng nào ngắn hơn ~35% độ rộng cột gốc (trừ dòng cuối
  đoạn); không ngắt tạo một từ đứng riêng ở dòng cuối đoạn.
