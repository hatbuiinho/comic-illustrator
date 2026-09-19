# Gói xử lý trang — Part 2

Mỗi page là một đơn vị xử lý độc lập. Khi bắt đầu một spread, tạo thư mục
`page-XXX/` tại đây; `layout.json` chứa frame của page, còn
`options/<optionId>/manifest.json` chứa storyboard, prompt, các lock và thông
tin bàn giao của phương án đó.

PDF dàn trang gốc của Part 2 được lưu tại:
`Tap 53/Part 2/layouts/Tập 53_Chương 5_Chánh Nghiêm_Phước Thịnh_đàn trang demo_07.09.pdf`.

Không dùng context của page khác nếu chưa có `continuityInput` được ghi rõ trong
manifest của page hiện tại.
