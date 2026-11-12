---
name: comic-character-signature
description: Đề xuất, đối chiếu và soát nét riêng của nhân vật để tránh mặt chung chung, mặt người mẫu và nhân vật giống nhau; xuất chữ, không tạo ảnh. Chỉ dùng khi người dùng gọi đích danh skill này ($comic-character-signature hoặc /comic-character-signature) hoặc yêu cầu rõ dùng skill này; không tự kích hoạt trong Character Studio, TTPQ Comic hay workflow khác.
---

# Nét riêng nhân vật — dùng khi cần

Đọc [luật nét riêng nhân vật](references/character-distinctiveness.md) trước
khi làm. Skill chỉ xuất chữ: không tạo hoặc chỉnh ảnh, không sửa profile,
skill hay prompt của workflow khác khi người dùng chưa yêu cầu rõ.

Kết quả chỉ áp cho lượt gọi hiện tại. Workflow đang dùng (Character Studio,
TTPQ Comic…) vẫn theo contract và skill của nó; người dùng tự quyết định có
chèn kết quả vào prompt hay profile không.

## Chọn việc theo yêu cầu

Xác định việc từ câu gọi; nếu không rõ, hỏi một câu với bốn lựa chọn dưới đây.

1. **Đề xuất nét riêng**
   - **Đầu vào:** brief, vai trong truyện, ảnh gốc nếu có.
   - **Làm:** xếp mức tôn kính (mục 4); có ảnh gốc thì chỉ liệt kê nét thấy
     trong ảnh (mục 3); chỉ có brief thì đề xuất nét theo năm tầng và số nét
     tối thiểu theo vai (mục 5), ưu tiên nét kể đời người.
   - **Xuất:** danh sách nét, chia **Nét xa** và **Nét gần**, ghi trái/phải
     theo cơ thể nhân vật, mỗi nét kèm một dòng "kể gì".

2. **Đối chiếu cast**
   - **Đầu vào:** profile cần kiểm và các profile cùng nhóm người dùng chỉ ra,
     hoặc thư mục profile của workflow đang dùng. Chỉ đọc file `.md`; chỉ mở
     ảnh khi mô tả không đủ để so.
   - **Làm:** so theo 6 trục (chư Tăng theo 4 trục còn lại) và phép thử bóng
     đen (mục 6).
   - **Xuất:** bảng nhận diện mỗi nhân vật một dòng; các cặp khác nhau dưới
     3 trục kèm hướng tách cụ thể.

3. **Soát ảnh**
   - **Đầu vào:** ảnh profile, sheet hoặc outline người dùng chỉ định, cùng
     profile gốc của từng nhân vật xuất hiện.
   - **Làm:** xem ảnh thật, trả lời 5 câu soát và các mục soát thêm (mục 10).
     Không ghi đạt khi chưa xem ảnh.
   - **Xuất:** mỗi câu `Đạt` / `Chưa đạt` (người nào, nét nào, vùng nào) /
     `Không áp dụng`; đề xuất câu comment sửa để người dùng dán vào workflow.

4. **Viết đoạn nét riêng cho prompt**
   - **Đầu vào:** nhân vật, cỡ khung (xa, trung, cận), workflow sẽ dùng.
   - **Làm:** chọn nét hợp cỡ khung theo mục 9 và kho câu mẫu, dùng ngôn ngữ
     nét vẽ 2D; nhân vật có profile thì chỉ lấy nét có trong profile.
   - **Xuất:** đoạn tiếng Anh trọn trong một code block, kèm dòng AVOID bổ
     sung; ghi rõ đoạn này cần tương thích với quy tắc prompt của workflow
     đích (ví dụ TTPQ không mô tả lại identity của nhân vật có profile).

## Giới hạn

- Đức Phật và hình thiêng theo dung nghi; không đề xuất nét riêng kiểu người đời.
- Mức tôn kính chưa rõ (ví dụ Thái tử Tất Đạt Đa) thì hỏi người dùng, không
  tự xếp.
- Không tự thêm nét mà ảnh gốc không có; không xấu hóa, không biếm họa.
- Mọi đoạn tiếng Anh cho prompt theo style ttpq comic light, không dùng từ
  kéo về ảnh thật.
- Kết thúc bằng 1–2 bước tiếp theo khả thi, mỗi câu trả lời mẫu trong một
  code block riêng theo `AGENTS.md`.
