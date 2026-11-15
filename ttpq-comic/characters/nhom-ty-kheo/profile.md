# Nhóm/đoàn tỳ kheo

- Trạng thái: APPROVED — người dùng yêu cầu "thêm 2 profile của nhóm/đoàn Tỳ Kheo ở trong folder local, dùng cho trường hợp nhóm Tỳ Kheo nhiều vị" ngày 2026-11-12; mô tả ghi nhận trực tiếp từ ảnh, không phát triển thiết kế mới.
- Version mô tả: v002
- Tên trong prompt: the monks
- Ref prompt: ref-v002-nhom-chinh-dien.png
- Dòng prompt: bhikkhus of mixed ages, each face distinct, shaved heads, plain deep earth-brown robes over both shoulders
- Ảnh ref (cả hai cùng là chuẩn của nhóm; chọn theo cảnh, có thể đính kèm cả hai):
  - `ref-v002-nhom-chinh-dien.png` — 6 vị đứng chụm chính diện, nhiều lứa tuổi, 3 vị ôm bát. Dùng cho nhóm đứng/ngồi, cận và trung cảnh. Từ `local/Nhóm Tỳ Kheo đã chỉnh màu.png`, 1024×1536.
  - `ref-v002-doan-di.png` — đoàn khoảng 18 vị đi một hàng chân trần, nhìn 3/4 nghiêng, xa dần về phải; một sa di nhỏ đi thứ hai; nhiều vị mang bát trong túi y bên hông. Dùng cho đoàn khất thực, đoàn đi đường, toàn cảnh. Từ `local/Đoàn Tỳ Kheo đã chỉnh màu y.png`, 1774×887.
  - Cả hai: chép nguyên file png, giữ nguyên pixel; ảnh không có chữ.- Vai trò trong truyện: tỳ kheo không tên, xuất hiện theo nhóm nhiều vị — ví dụ T53: ~20 tỳ kheo khất thực, thọ thực (S11–S14); 60 tỳ kheo về từ Matika (S24).
- Đây là profile nhóm: giữ tạo hình và trang phục nhất quán; số lượng, tuổi, hành động và đạo cụ theo chữ của cảnh. Các khuôn mặt trong ảnh là vai quần chúng, không gán tên riêng.

## Mô tả (tiếng Việt, để duyệt)

- **Tuổi, giới:** nam, trộn nhiều lứa tuổi: thanh niên, trung niên, cao tuổi (mặt nhăn, mày điểm bạc); có thể có sa di thiếu niên/trẻ nhỏ như ảnh đoàn đi.
- **Vóc dáng:** thể trạng bình thường, khác nhau từng người (gầy, đầy đặn, thấp, cao); dáng đứng thẳng, đi thong thả; chân trần.
- **Khuôn mặt:** mỗi vị một nét riêng (mặt tròn, mặt vuông, mặt dài; mày rậm hoặc thưa); thần thái hiền, mỉm cười nhẹ hoặc trầm tĩnh.
- **Da:** sáng ấm đến nâu nhạt.
- **Tóc/râu:** đầu cạo sạch, không râu.
- **Trang phục:** y một màu nâu đất trầm (ngả đỏ nhẹ, không đỏ gạch), trơn, không viền; đắp kín hai vai, quấn vòng mềm quanh cổ; một tà dọc buông từ vai trái xuống ngực; lớp dưới dài tới bắp chân – mắt cá, nếp rủ dọc.
- **Đạo cụ:** bình bát tròn màu nâu sẫm, ôm trước bụng bằng hai tay hoặc đựng trong túi y đeo bên hông. Không trang sức.
- **Thần thái chung:** an tĩnh, khiêm nhường, đồng điệu như một tập thể.

## Dấu hiệu bắt buộc

- Đầu cạo, không râu, chân trần; y nâu đất trầm trơn phủ hai vai, tà dọc vai trái.
- Trộn tuổi và nét mặt khác nhau, không nhân bản cùng một khuôn mặt.
- Bình bát nâu sẫm trơn khi khất thực.

## Không được nhầm

- Không lẫn với Đức Phật (`duc-phat`): tỳ kheo đầu cạo, không tóc xoăn ốc, không nhục kế, không bạch hào, dái tai bình thường.
- Không lẫn với tỳ kheo có profile riêng (Ananda, Moggallana, Godatta…): khi các vị này có mặt, đính kèm profile riêng và không để vị nào trong nhóm mượn dấu hiệu của họ (vd. dái tai dài, mặt trẻ thon của Ananda).
- Không y cam sáng hiện đại, không y vàng nghệ, không đỏ gạch tươi, không viền/hoa văn; màu y và cách quấn y theo ảnh ref của profile này, không áp `docs/monastic-robes.md`.
- Sa di chỉ đưa vào khi cảnh có; mặc định nhóm là tỳ kheo trưởng thành.
- Trạng thái theo cảnh được mô tả thêm bằng chữ, ví dụ 60 tỳ kheo về từ Matika: y sờn bạc, mặt sạm nắng (bible S24).
- Ảnh đoàn đi chỉ cho tạo hình; bố cục, hướng đi và số lượng theo layout của spread.

## Dòng nhận diện (tiếng Anh, ≤ 45 từ; chép vào prompt cạnh "Image N = <tên>")

```text
MONK GROUP (Image <N>): unnamed bhikkhus of mixed ages, each face distinct, shaved heads, no beards, barefoot, calm gentle expressions. Plain deep earth-brown robes covering both shoulders; dark-brown alms bowls held or slung at the hip. No orange, saffron or brick-red robes.
```

## Lịch sử

| Version | Ngày | Thay đổi | Người duyệt |
| --- | --- | --- | --- |
| v002 | 2026-11-12 | Tiếp nhận 2 ảnh đã chỉnh màu y (nâu đất trầm) từ `local/`, lưu `ref-v002-*.png` và ghi nhận diện; bỏ bản v001 theo yêu cầu | Người dùng chỉ định ảnh làm profile |
| v002 | 2026-11-13 | Màu y/cách quấn y theo ảnh ref của profile, bỏ dẫn chiếu `docs/monastic-robes.md` | Người dùng yêu cầu gỡ quy chuẩn y chung khỏi ttpq-comic |
