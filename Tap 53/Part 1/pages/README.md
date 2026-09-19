# Page packages

Mỗi page là một đơn vị xử lý độc lập. `layout.json` chỉ chứa frame của page;
`options/<optionId>/manifest.json` chỉ chứa storyboard, prompt, lock và delivery
của option đó. Context page khác bị chặn mặc định.

Từ Part 1, chạy QA riêng một page bằng:

```bash
node ../../scripts/run-page-qa.js pages/page-010
```

Các page hiện đã được gom: `page-006`, `page-010`, `page-023`, `page-024`.
Manifest cũ ở `scripts/layout_frames.json` chỉ là index tương thích ngược.
