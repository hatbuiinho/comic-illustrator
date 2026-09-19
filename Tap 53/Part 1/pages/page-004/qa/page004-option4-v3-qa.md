# Trang 4 — QA output phương án 4, v3

## Output và nguồn kiểm

- Output: `Tap 53/Part 1/pages/page-004/outputs/part1-page004-option4-community-work-v3-flat-horizon.png`.
- Layout nguồn: `Tap 53/Part 1/pages/page-004/storyboards/page004-layout-source.png`.
- Overlay: `Tap 53/Part 1/pages/page-004/qa/page004-option4-v3-layout-overlay.png`.
- Bố cục đã duyệt: `Tap 53/Part 1/pages/page-004/storyboards/page004-option4-confirmed-composition-v2.png`.
- Profile gốc được đọc lại ngay trước lượt sửa nền: `Tap 53/characters/thợ phụ.png`.
- Khóa ý nghĩa/cảm xúc: `Tap 53/Part 1/pages/page-004/storyboards/page004-emotional-flow-v1.md`.

## Layout QA — PASS

Tỷ lệ output là 1997 / 787 = 2,53748; khung nguồn là 2,53346; sai số khoảng 0,16%, trong dung sai 1,5%. Overlay dùng chính raster layout gốc có chữ. Artwork phủ khung dưới hoàn toàn, không hở mép. Dải gáy giữa nằm trên nền đất thấp tương phản; không cắt mặt, tay, thúng, gánh, búa, gỗ hoặc hành động chính. Chữ ở nửa trên không bị ảnh che.

Nhóm gom chính, gánh chính và người đổ đất nằm trong vùng xanh lá an toàn. Người phụ ở mép và nền đất/cây là phần có thể xén; không là bằng chứng duy nhất cho cảnh.

## Style QA — PASS

Line art rõ và nhất quán; mảng màu phẳng; bóng cel cứng, tiết chế. Nhân vật và nền cùng ngôn ngữ 2D. Không thấy blur, DOF, bokeh, volumetric light, bloom, lens flare, CGI hoặc texture ảnh thật. Nắng sáng được diễn đạt bằng bầu trời và bóng ngắn đồ họa, không thành hiệu ứng render.

## Location QA — PASS

Đọc được bãi công trường rộng với hố móng dở, đất đào/vùng san và rìa cây. Bản v2 đã fail vì có dải đồi xa; v3 đã thay toàn bộ bằng đường chân trời bằng phẳng, cây thưa và nền đất khô. Không có nước, núi, đồi, tinh xá hoàn thiện, tường/mái/cột lớn, xe ngựa hoặc nhân vật thuộc cảnh sau.

## Storyboard và visual delta QA — PASS có điều kiện chọn output

- Quy mô: nhiều lớp tổ lao động còn đọc được khi nhìn trong layout; hố, tổ phụ và công trường tiếp tục qua mép ảnh. Không cần đếm từng người để hiểu quy mô lớn.
- Nhịp công việc: đào → gom → gánh → đổ đất ở vùng trũng khô đọc được từ trái sang phải.
- Highlight: nắng sáng hiện qua bóng ngắn; các tương tác làm việc và nét mặt tự nhiên tạo không khí cười nói; nhóm trung cảnh có một người giáng búa và một người giữ gỗ, nên tiếng búa đục có nguyên nhân thị giác.
- Trẻ em vừa nhặt đá vừa quét dọn, tách khỏi tải nặng.
- Profile: những thợ nam chính giữ gương mặt Nam Á, khăn quấn/tóc/râu, y phục quấn và dáng lao động tương thích profile gốc. Phụ nữ/trẻ phân biệt nhận dạng; không thấy nhân bản lộ rõ, tay/chân thừa hoặc tỷ lệ đầu–thân sai.
- Bản v3 chỉnh riêng nền xa từ v2, giữ bố cục, hành động, profile và phong cách. Profile gốc được truyền lại cùng edit target trong chính lượt sửa; output v2 chỉ đóng vai trò target/composition, không là identity source.

Trạng thái kỹ thuật: `qa-passed`. Chưa chuyển vào `approved/` vì người dùng chưa chọn rõ output cuối.

```text
Chọn output: part1-page004-option4-community-work-v3-flat-horizon.png
```

```text
Chỉnh output: part1-page004-option4-community-work-v3-flat-horizon.png — giữ bố cục và quy mô; sửa <nội dung cụ thể>
```
