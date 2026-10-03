# Trạng thái delivery

Trạng thái hợp lệ:

- `storyboard-pending`
- `approved`
- `generating`
- `generated`
- `interrupted`
- `qa-passed`
- `approved-filed`
- `approved-filed-context-pending`

`qa-passed` chỉ dùng khi các delivery bắt buộc tồn tại và QA áp dụng đã PASS.
`approved-filed` chỉ dùng sau khi người dùng chọn rõ output, file đã được chuyển
vào `approved/`, mọi đường dẫn liên quan đã cập nhật và continuity event bắt
buộc đã được commit. `approved-filed-context-pending` dùng khi file/đường dẫn đã
hoàn tất nhưng ledger hoặc invalidation cần reconciliation; trạng thái này
không cho phép tuyên bố context downstream đã đồng bộ.
