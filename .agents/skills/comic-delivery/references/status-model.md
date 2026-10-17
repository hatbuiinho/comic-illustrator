# Trạng thái delivery

Trạng thái hợp lệ:

- `storyboard-pending`
- `approved`
- `generating`
- `generated`
- `interrupted`
- `qa-passed`
- `selected-for-layout`
- `layer-package-ready`
- `approved-filed`
- `approved-filed-context-pending`

`qa-passed` chỉ dùng khi master đã qua QA sáng tạo áp dụng.
`selected-for-layout` chỉ dùng sau khi người dùng chọn đích danh master; trạng
thái này xác định nguồn được chọn; không tự cấp phép tách `bg + mgfg + wrap`.
Ảnh đơn đã qua QA áp dụng được chuyển thẳng sang delivery, không cần
`layer-package-ready`. Trạng thái `layer-package-ready` chỉ áp dụng khi người
dùng yêu cầu bộ layer và bộ đồng phiên bản đã qua QA kỹ thuật, bản ghép khớp master.
`approved-filed` chỉ dùng sau khi người dùng chọn rõ output, file đã được chuyển
vào `approved/`, mọi đường dẫn liên quan đã cập nhật và continuity event bắt
buộc đã được commit. `approved-filed-context-pending` dùng khi file/đường dẫn đã
hoàn tất nhưng ledger hoặc invalidation cần reconciliation; trạng thái này
không cho phép tuyên bố context downstream đã đồng bộ.
