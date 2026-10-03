# Prompt contract

Prompt nên mô tả theo thứ tự:

1. Loại ảnh và tỷ lệ/canvas mục tiêu. Nếu layout dùng mask tròn, oval hoặc hình
   bất quy tắc, phải ghi rõ output vẫn là canvas chữ nhật đầy đủ, background
   phủ kín bốn góc; không alpha, cutout, viền/vignette hay crop sẵn theo mask.
   Mask chỉ là guide bố cục và được áp ở bước dàn trang.
2. Khoảnh khắc, cảm xúc hoặc quan hệ ưu tiên, focus, camera và điểm nhìn.
3. Nhân vật, hành động, quan hệ, population plan và điều người đọc được phép tự
   suy ra.
4. Profile reference cùng dấu hiệu phải giữ.
5. Background, thời điểm và location anchors.
6. Bố cục, eye path, negative space và intentional crop.
7. Ngôn ngữ thuần 2D.
8. Các chi tiết bắt buộc và cách đọc sai cần tránh.
9. Negative constraints thực sự áp dụng.

Nếu prompt dùng để chỉnh ảnh, nêu rõ phần giữ nguyên và phần cần thay đổi. Không
dùng output cũ làm chuẩn identity thay cho profile gốc.

Giữ nguyên phân cấp `emotionalPriority`, `explicitRequired`, `implicitReadable`
và `optionalSupport` từ storyboard. Chỉ mô tả trực diện những gì thực sự cần
nhìn rõ để bảo toàn ý nghĩa. Với thông tin có thể suy ra, dùng một số tín hiệu
tối thiểu từ nhịp, hướng, tư thế, phản ứng, chồng lớp hoặc ngữ cảnh; không biến
chúng thành checklist hình thể.

Negative constraints không được loại bỏ sự mơ hồ có chủ ý hoặc buộc mọi yếu tố
phải rõ ngang nhau. Nếu prompt dẫn đến hành động phô diễn, tạo dáng giải thích
hoặc quá nhiều điểm cạnh tranh thị giác, phải giảm chi tiết trước khi sản xuất.
