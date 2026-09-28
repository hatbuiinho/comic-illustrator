# Trạng thái delivery

Trạng thái hợp lệ:

- `storyboard-pending`
- `approved`
- `generating`
- `generated`
- `interrupted`
- `qa-passed`
- `approved-filed`

`qa-passed` chỉ dùng khi các delivery bắt buộc tồn tại và QA áp dụng đã PASS.
`approved-filed` chỉ dùng sau khi người dùng chọn rõ output, file đã được chuyển
vào `approved/` và mọi đường dẫn liên quan đã cập nhật.
