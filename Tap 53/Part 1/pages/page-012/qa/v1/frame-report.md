# Layout frame QA report

- Manifest: `/workspace/Tap 53/Part 1/pages/page-012/manifest.json`
- Kết quả: **FAIL**
- Fail: 1; Warning: 1; Pass: 3

## Fail

- **part1-spread12-punna-sanitation-request/H1/nalini-face-and-gaze** — Chi tiết quan trọng nằm ngoài frame/mask.

## Warning

- **part1-spread12-punna-sanitation-request/H1** — Chưa có optionAlignment; không được coi frame mới là brief đã được người dùng chốt.

## Pass

- **part1-spread12-punna-sanitation-request/printTrimLock** — Trim x 1.049% · y 1.478%; critical-safe x 2.797% · y 3.941%.
- **part1-spread12-punna-sanitation-request/layoutQa** — Đã dùng layout gốc có text làm nền overlay: storyboards/page12-layout-source.png.
- **part1-spread12-punna-sanitation-request/H1** — Tỷ lệ contentFrame khớp frame (0.03% lệch).

## Overlay

- part1-spread12-punna-sanitation-request: `/workspace/Tap 53/Part 1/pages/page-012/qa/v1/part1-spread12-punna-sanitation-request-overlay.svg` (source layout: `storyboards/page12-layout-source.png`)
