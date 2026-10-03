# Hình chen

Mỗi hình chen là một shot riêng. Kiểm mask, tỷ lệ, text reserve và khả năng đọc
ở kích thước layout. Spine chỉ áp dụng nếu frame thật sự giao vùng đóng sách.
Intentional crop được phép khi vẫn giữ nghĩa, anatomy và recognition core.

Với mask tròn, oval hoặc hình bất quy tắc, raw output phải là ảnh chữ nhật
full-bleed và được kiểm riêng trước khi áp mask. FAIL nếu canvas/alpha đã cắt
theo mask, các góc bị rỗng/trắng, hoặc ảnh có viền/vignette mô phỏng mask.
Overlay đã mask không được dùng để chứng minh raw output đạt check này.
