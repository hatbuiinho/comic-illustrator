# Đức Phật — Thế Tôn

- Trạng thái: APPROVED — người dùng yêu cầu "trong folder local có thêm 3 ảnh profile của Phật, bạn hãy thêm vào ttpq comic" ngày 2026-11-12; mô tả ghi nhận trực tiếp từ ảnh, không phát triển thiết kế mới.
- Version mô tả: v002
- Tên trong prompt: the Buddha
- Ref prompt: ref-v001-di-dung.png
- Dòng prompt: very tall, about 10 heads tall, broad rounded shoulders; full round face, downcast half-closed eyes, black snail-shell curls with small ushnisha, very long earlobes, no halo
- Ảnh ref (cả ba cùng là chuẩn identity; chọn ảnh theo tư thế của cảnh, có thể đính kèm nhiều ảnh):
  - `ref-v001-ngoi-thien.png` — ngồi kiết già, tay thiền định; 4 góc: chính diện, sau lưng, nghiêng, 3/4 trước. Từ `local/Phật ngồi thiền.jpg`.
  - `ref-v001-thuyet-phap.png` — ngồi kiết già thuyết Pháp, tay phải giơ ngang ngực lòng bàn tay hướng ra, tay trái ngửa trên đùi; 4 góc: chính diện, 3/4 trước, nghiêng, 3/4 sau. Từ `local/Phật thuyết Pháp.jpg`.
  - `ref-v001-di-dung.png` — đứng/đi chân trần, hai tay ôm bình bát; 4 góc: 3/4 trước, sau lưng, nghiêng đang bước, nghiêng đứng. Từ `local/Phật đi, đứng.jpg`.
  - Cả ba: 2193×1274, chuyển từ jpg sang png, giữ nguyên pixel; ảnh không có chữ.
- Vai trò trong truyện: Đức Phật tại Jetavana; T53 xuất hiện ở S22, S24, S37 (xem `story/t53/bible.md`).

## Mô tả (tiếng Việt, để duyệt)

- **Tuổi, giới:** nam, trung niên trẻ; không có tuổi số.
- **Vóc dáng, tỉ lệ:** rất cao, khoảng 10 đầu (người thường trong truyện khoảng 7–7,5 đầu), nên đứng cạnh người khác thì cao vượt hẳn; đầy đặn cân đối, vai tròn rộng; dáng thẳng, an tĩnh; chân trần.
- **Khuôn mặt:** mặt tròn đầy, đường nét mềm; mày cong thanh; mắt dài hơi khép nhìn xuống, tròng mắt xanh nhạt; mũi thẳng; môi nhỏ, mỉm cười rất nhẹ; điểm bạch hào (chấm trắng nhỏ) giữa hai mày; dái tai rất dài, buông gần tới cằm.
- **Da:** sáng ấm, sắc đào nhạt.
- **Tóc/râu:** tóc đen xoăn ốc sát da đầu; nhục kế (búi tóc tròn nhỏ) trên đỉnh đầu; không râu.
- **Trang phục:** y một màu nâu đỏ đất, phủ kín hai vai, quấn nhiều vòng mềm quanh cổ thành nếp rủ tầng trước ngực; một tà y buông từ vai trái xuống dọc lưng; lớp dưới dài gần mắt cá, nếp rủ nhiều. Khi đi, mép y bay nhẹ phía sau.
- **Phụ kiện/trang sức, đạo cụ:** không trang sức. Bình bát tròn màu đồng chỉ khi đi khất thực hoặc theo cảnh.
- **Biểu cảm/thần thái mặc định:** tĩnh lặng, từ hòa, mắt nhìn xuống, nụ cười nhẹ.
- **Tư thế chuẩn:** ngồi kiết già (thiền định hoặc thuyết Pháp), đứng/đi ôm bát.

## Dấu hiệu bắt buộc

- Tóc xoăn ốc đen + nhục kế nhỏ trên đỉnh; dái tai rất dài; bạch hào giữa mày.
- Mặt tròn đầy, mắt khép hờ nhìn xuống, nụ cười rất nhẹ; không râu.
- Y nâu đỏ đất trơn phủ hai vai, quấn cổ nhiều nếp.

## Không được nhầm

- Không lẫn với tỳ kheo (Ananda, Moggallana…): Đức Phật có tóc xoăn ốc và nhục kế, không cạo trọc; tỳ kheo đầu cạo, không bạch hào.
- Không vẽ kiểu tượng: không da vàng kim, không hào quang, không tòa sen, không vương miện, không trang sức, trừ khi cảnh yêu cầu rõ.
- Không vẽ già, gầy hay khổ hạnh; không thêm râu.
- Ảnh ref có shading mềm kiểu painterly: chỉ lấy identity và màu cục bộ, vẽ theo style ttpq comic light thuần 2D. Màu y và cách quấn y theo ảnh ref của profile này, không áp `docs/monastic-robes.md`.

## Dòng nhận diện (tiếng Anh, ≤ 45 từ; chép vào prompt cạnh "Image N = <tên>")

```text
THE BUDDHA (Image <N>): serene, very tall man, about 10 heads tall, full round face, downcast half-closed eyes, faint smile, small white urna between brows, very long earlobes, tight black snail-shell curls with small ushnisha, no beard. Plain earth-reddish-brown robe covering both shoulders. No halo, gold skin, or jewelry.
```

## Lịch sử

| Version | Ngày | Thay đổi | Người duyệt |
| --- | --- | --- | --- |
| v001 | 2026-11-12 | Tiếp nhận 3 ảnh từ `local/` (ngồi thiền, thuyết Pháp, đi đứng), lưu 3 file `ref-v001-*.png` và ghi nhận diện | Người dùng chỉ định ảnh làm profile |
| v001 | 2026-11-13 | Màu y/cách quấn y theo ảnh ref của profile, bỏ dẫn chiếu `docs/monastic-robes.md` | Người dùng yêu cầu gỡ quy chuẩn y chung khỏi ttpq-comic |
| v002 | 2026-11-15 | Thêm chiều cao khoảng 10 đầu vào vóc dáng, Dòng prompt và dòng nhận diện | Người dùng: "Đức Phật cao 10 heads" |
