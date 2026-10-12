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
thái này cho phép tách `bg + mgfg + wrap` nhưng chưa cho phép chuyển vào
`approved/`. `layer-package-ready` chỉ dùng khi bộ layer đồng phiên bản đã qua
QA kỹ thuật và bản ghép khớp master.
`approved-filed` chỉ dùng sau khi người dùng chọn rõ output, file đã được chuyển
vào `approved/`, mọi đường dẫn liên quan đã cập nhật và continuity event bắt
buộc đã được commit. `approved-filed-context-pending` dùng khi file/đường dẫn đã
hoàn tất nhưng ledger hoặc invalidation cần reconciliation; trạng thái này
không cho phép tuyên bố context downstream đã đồng bộ.
