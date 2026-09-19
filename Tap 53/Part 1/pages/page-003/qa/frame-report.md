# Layout frame QA report

- Manifest: `/workspace/Tap 53/Part 1/scripts/layout_frames.json`
- Kết quả: **FAIL**
- Fail: 13; Warning: 6; Pass: 49

## Fail

- **part1-spread01-chapter1-opening/page001-chapter1-opening-dawn/optionAlignment** — Chưa có xác nhận userConfirmed: true cho Option-to-manifest QA.
- **part1-spread06-option1-shared-meal/rest-meal** — Không tìm thấy output: ../pages/page-006/outputs/part1-spread06-option1-shared-meal-v1.png
- **part1-spread06-option2-water-cup/rest-meal** — Không tìm thấy output: ../pages/page-006/outputs/part1-spread06-option2-water-cup-v1.png
- **part1-spread10-option2-nalini-realization/nalini-realization** — Không tìm thấy output: ../pages/page-010/outputs/part1-spread10-option2-nalini-realization-v1.png
- **part1-spread10-option3-stone-vow/stone-vow** — Không tìm thấy output: ../pages/page-010/outputs/part1-spread10-option3-stone-vow-v1.png
- **part1-spread23-restart-option2-calm-and-disorientation/h1-calm-moggallana** — Không tìm thấy output: ../pages/page-023/outputs/part1-page23-restart-option2-h1-calm-moggallana-v1.png
- **part1-spread23-restart-option2-calm-and-disorientation/h2-disoriented-ascetic** — Không tìm thấy output: ../pages/page-023/outputs/part1-page23-restart-option2-h2-disoriented-ascetic-v1.png
- **part1-spread24-option1-circle-and-extinguished-lamp/h1-silent-ascetic-circle** — Không tìm thấy output: ../pages/page-024/outputs/part1-page24-option1-h1-silent-ascetic-circle-v2.png
- **part1-spread24-option1-circle-and-extinguished-lamp/h2-extinguished-oil-lamp** — Không tìm thấy output: ../pages/page-024/outputs/part1-page24-option1-h2-extinguished-oil-lamp-v1.png
- **part1-spread24-option1-fist-and-extinguished-lamp/h1-fist-silences-circle** — Không tìm thấy output: ../pages/page-024/outputs/part1-page24-option1-h1-fist-silences-circle-v1.png
- **part1-spread24-option1-fist-and-extinguished-lamp/h2-wind-extinguishes-lamp** — Không tìm thấy output: ../pages/page-024/outputs/part1-page24-option1-h2-wind-extinguishes-lamp-v1.png
- **part1-spread24-reprocess-optionA/h1-optionA-fist-silences-circle** — Không tìm thấy output: ../pages/page-024/outputs/part1-page24-reprocess-optionA-h1-fist-silences-circle-v1.png
- **part1-spread24-reprocess-optionA/h2-optionA-wind-extinguishes-lamp** — Không tìm thấy output: ../pages/page-024/outputs/part1-page24-reprocess-optionA-h2-wind-extinguishes-lamp-v1.png

## Warning

- **part1-spread01-chapter1-opening/page001-chapter1-opening-dawn** — Chưa có output; overlay chỉ hiển thị frame và guide.
- **part1-spread15-chapter1-ending/page15-chapter1-ending-hero** — Chưa có optionAlignment; không được coi frame mới là brief đã được người dùng chốt.
- **part1-spread06-option1-shared-meal/rest-meal** — Chưa có optionAlignment; không được coi frame mới là brief đã được người dùng chốt.
- **part1-spread06-option2-water-cup/rest-meal** — Chưa có optionAlignment; không được coi frame mới là brief đã được người dùng chốt.
- **part1-spread10-option2-nalini-realization/nalini-realization** — Chưa có optionAlignment; không được coi frame mới là brief đã được người dùng chốt.
- **part1-spread10-option3-stone-vow/stone-vow** — Chưa có optionAlignment; không được coi frame mới là brief đã được người dùng chốt.

## Pass

- **part1-spread01-chapter1-opening/printTrimLock** — Trim x 1.049% · y 1.478%; critical-safe x 2.797% · y 3.941%.
- **part1-spread01-chapter1-opening/layoutQa** — Đã dùng layout gốc có text làm nền overlay: ../pages/page-001/storyboards/page001-layout-source.png.
- **part1-spread15-chapter1-ending/printTrimLock** — Trim x 1.049% · y 1.478%; critical-safe x 2.797% · y 3.941%.
- **part1-spread15-chapter1-ending/layoutQa** — Đã dùng layout gốc có text làm nền overlay: ../tmp/pdf_all/p15.png.
- **part1-spread15-chapter1-ending/page15-chapter1-ending-hero** — Tỷ lệ output khớp frame (0.15% lệch).
- **part1-spread06-option1-shared-meal/printTrimLock** — Trim x 1.049% · y 1.478%; critical-safe x 2.797% · y 3.941%.
- **part1-spread06-option1-shared-meal/layoutQa** — Đã dùng layout gốc có text làm nền overlay: ../../../tmp/pdf_pages/page_06_hi.png.
- **part1-spread06-option2-water-cup/printTrimLock** — Trim x 1.049% · y 1.478%; critical-safe x 2.797% · y 3.941%.
- **part1-spread06-option2-water-cup/layoutQa** — Đã dùng layout gốc có text làm nền overlay: ../../../tmp/pdf_pages/page_06_hi.png.
- **part1-spread10-option2-nalini-realization/printTrimLock** — Trim x 1.049% · y 1.478%; critical-safe x 2.797% · y 3.941%.
- **part1-spread10-option2-nalini-realization/layoutQa** — Đã dùng layout gốc có text làm nền overlay: ../../../tmp/pdf_pages/page_10_hi.png.
- **part1-spread10-option3-stone-vow/printTrimLock** — Trim x 1.049% · y 1.478%; critical-safe x 2.797% · y 3.941%.
- **part1-spread10-option3-stone-vow/layoutQa** — Đã dùng layout gốc có text làm nền overlay: ../../../tmp/pdf_pages/page_10_hi.png.
- **part1-spread23-restart-option1-club-and-empty-hand/printTrimLock** — Trim x 1.049% · y 1.478%; critical-safe x 2.797% · y 3.941%.
- **part1-spread23-restart-option1-club-and-empty-hand/layoutQa** — Đã dùng layout gốc có text làm nền overlay: ../../../tmp/pdf_pages/page_23.png.
- **part1-spread23-restart-option1-club-and-empty-hand/h1-suspended-strike/optionAlignment** — Option page23-ambush-optionA-h1 đã được người dùng xác nhận.
- **part1-spread23-restart-option1-club-and-empty-hand/h1-suspended-strike** — Tỷ lệ output khớp frame (0.01% lệch).
- **part1-spread23-restart-option1-club-and-empty-hand/h2-ravine-wake/optionAlignment** — Option page23-ambush-optionA-h2 đã được người dùng xác nhận.
- **part1-spread23-restart-option1-club-and-empty-hand/h2-ravine-wake** — Tỷ lệ output khớp frame (0.01% lệch).
- **part1-spread23-restart-option2-calm-and-disorientation/printTrimLock** — Trim x 1.049% · y 1.478%; critical-safe x 2.797% · y 3.941%.
- **part1-spread23-restart-option2-calm-and-disorientation/layoutQa** — Đã dùng layout gốc có text làm nền overlay: ../../../tmp/pdf_pages/page_23.png.
- **part1-spread23-restart-option2-calm-and-disorientation/h1-calm-moggallana/optionAlignment** — Option page23-restart-option2-calm-and-disorientation-h1 đã được người dùng xác nhận.
- **part1-spread23-restart-option2-calm-and-disorientation/h2-disoriented-ascetic/optionAlignment** — Option page23-restart-option2-calm-and-disorientation-h2 đã được người dùng xác nhận.
- **part1-spread24-option1-circle-and-extinguished-lamp/printTrimLock** — Trim x 1.049% · y 1.478%; critical-safe x 2.797% · y 3.941%.
- **part1-spread24-option1-circle-and-extinguished-lamp/layoutQa** — Đã dùng layout gốc có text làm nền overlay: ../../../tmp/pdf_pages/page_24.png.
- **part1-spread24-option1-circle-and-extinguished-lamp/h1-silent-ascetic-circle/optionAlignment** — Option page24-option1-circle-and-extinguished-lamp-h1 đã được người dùng xác nhận.
- **part1-spread24-option1-circle-and-extinguished-lamp/h2-extinguished-oil-lamp/optionAlignment** — Option page24-option1-circle-and-extinguished-lamp-h2 đã được người dùng xác nhận.
- **part1-spread24-option1-fist-and-extinguished-lamp/printTrimLock** — Trim x 1.049% · y 1.478%; critical-safe x 2.797% · y 3.941%.
- **part1-spread24-option1-fist-and-extinguished-lamp/layoutQa** — Đã dùng layout gốc có text làm nền overlay: ../../../tmp/pdf_pages/page_24.png.
- **part1-spread24-option1-fist-and-extinguished-lamp/h1-fist-silences-circle/optionAlignment** — Option page24-option1-fist-silences-circle-h1 đã được người dùng xác nhận.
- **part1-spread24-option1-fist-and-extinguished-lamp/h2-wind-extinguishes-lamp/optionAlignment** — Option page24-option1-fist-silences-circle-h2 đã được người dùng xác nhận.
- **part1-spread24-reprocess-optionA/printTrimLock** — Trim x 1.049% · y 1.478%; critical-safe x 2.797% · y 3.941%.
- **part1-spread24-reprocess-optionA/layoutQa** — Đã dùng layout gốc có text làm nền overlay: ../../../tmp/pdf_pages/page_24.png.
- **part1-spread24-reprocess-optionA/h1-optionA-fist-silences-circle/optionAlignment** — Option page24-reprocess-optionA-h1 đã được người dùng xác nhận.
- **part1-spread24-reprocess-optionA/h2-optionA-wind-extinguishes-lamp/optionAlignment** — Option page24-reprocess-optionA-h2 đã được người dùng xác nhận.
- **part1-spread10-restart-option1-visakha-stone-gesture/printTrimLock** — Trim x 1.049% · y 1.478%; critical-safe x 2.797% · y 3.941%.
- **part1-spread10-restart-option1-visakha-stone-gesture/layoutQa** — Đã dùng layout gốc có text làm nền overlay: ../../../tmp/pdf_pages/page_10_hi.png.
- **part1-spread10-restart-option1-visakha-stone-gesture/h1-visakha-stone-gesture/optionAlignment** — Option page10-option1-visakha-stone-gesture đã được người dùng xác nhận.
- **part1-spread10-restart-option1-visakha-stone-gesture/h1-visakha-stone-gesture** — Tỷ lệ output khớp frame (0.01% lệch).
- **part1-spread05-community-worksite-restart-v9/printTrimLock** — Trim x 1.049% · y 1.478%; critical-safe x 2.797% · y 3.941%.
- **part1-spread05-community-worksite-restart-v9/layoutQa** — Đã dùng layout gốc có text làm nền overlay: ../tmp/page-005-source/layout.png.
- **part1-spread05-community-worksite-restart-v9/page05-community-worksite-strip/optionAlignment** — Option page05-restart-option4-visakha-chap-tay-cam-ta-expanded đã được người dùng xác nhận.
- **part1-spread05-community-worksite-restart-v9/page05-community-worksite-strip** — Tỷ lệ contentFrame khớp frame (0.01% lệch).
- **part1-page003-nalini-volunteers/printTrimLock** — Trim x 1.049% · y 1.478%; critical-safe x 2.797% · y 3.941%.
- **part1-page003-nalini-volunteers/layoutQa** — Đã dùng layout gốc có text làm nền overlay: ../pages/page-003/storyboards/page003-layout-source.png.
- **part1-page003-nalini-volunteers/h1-nalini-holds-elder-hand/optionAlignment** — Option page003-reprocess-option3-nguoi-cho-ngoai-khung đã được người dùng xác nhận.
- **part1-page003-nalini-volunteers/h1-nalini-holds-elder-hand** — Tỷ lệ contentFrame khớp frame (0.65% lệch).
- **part1-page003-nalini-volunteers/h2-nalini-warmed-by-volunteers/optionAlignment** — Option page003-reprocess-option3-nguoi-cho-ngoai-khung đã được người dùng xác nhận.
- **part1-page003-nalini-volunteers/h2-nalini-warmed-by-volunteers** — Tỷ lệ contentFrame khớp frame (0.65% lệch).

## Overlay

- part1-spread01-chapter1-opening: `/workspace/Tap 53/Part 1/pages/page-003/qa/part1-spread01-chapter1-opening-overlay.svg` (source layout: `../pages/page-001/storyboards/page001-layout-source.png`)
- part1-spread15-chapter1-ending: `/workspace/Tap 53/Part 1/pages/page-003/qa/part1-spread15-chapter1-ending-overlay.svg` (source layout: `../tmp/pdf_all/p15.png`)
- part1-spread06-option1-shared-meal: `/workspace/Tap 53/Part 1/pages/page-003/qa/part1-spread06-option1-shared-meal-overlay.svg` (source layout: `../../../tmp/pdf_pages/page_06_hi.png`)
- part1-spread06-option2-water-cup: `/workspace/Tap 53/Part 1/pages/page-003/qa/part1-spread06-option2-water-cup-overlay.svg` (source layout: `../../../tmp/pdf_pages/page_06_hi.png`)
- part1-spread10-option2-nalini-realization: `/workspace/Tap 53/Part 1/pages/page-003/qa/part1-spread10-option2-nalini-realization-overlay.svg` (source layout: `../../../tmp/pdf_pages/page_10_hi.png`)
- part1-spread10-option3-stone-vow: `/workspace/Tap 53/Part 1/pages/page-003/qa/part1-spread10-option3-stone-vow-overlay.svg` (source layout: `../../../tmp/pdf_pages/page_10_hi.png`)
- part1-spread23-restart-option1-club-and-empty-hand: `/workspace/Tap 53/Part 1/pages/page-003/qa/part1-spread23-restart-option1-club-and-empty-hand-overlay.svg` (source layout: `../../../tmp/pdf_pages/page_23.png`)
- part1-spread23-restart-option2-calm-and-disorientation: `/workspace/Tap 53/Part 1/pages/page-003/qa/part1-spread23-restart-option2-calm-and-disorientation-overlay.svg` (source layout: `../../../tmp/pdf_pages/page_23.png`)
- part1-spread24-option1-circle-and-extinguished-lamp: `/workspace/Tap 53/Part 1/pages/page-003/qa/part1-spread24-option1-circle-and-extinguished-lamp-overlay.svg` (source layout: `../../../tmp/pdf_pages/page_24.png`)
- part1-spread24-option1-fist-and-extinguished-lamp: `/workspace/Tap 53/Part 1/pages/page-003/qa/part1-spread24-option1-fist-and-extinguished-lamp-overlay.svg` (source layout: `../../../tmp/pdf_pages/page_24.png`)
- part1-spread24-reprocess-optionA: `/workspace/Tap 53/Part 1/pages/page-003/qa/part1-spread24-reprocess-optionA-overlay.svg` (source layout: `../../../tmp/pdf_pages/page_24.png`)
- part1-spread10-restart-option1-visakha-stone-gesture: `/workspace/Tap 53/Part 1/pages/page-003/qa/part1-spread10-restart-option1-visakha-stone-gesture-overlay.svg` (source layout: `../../../tmp/pdf_pages/page_10_hi.png`)
- part1-spread05-community-worksite-restart-v9: `/workspace/Tap 53/Part 1/pages/page-003/qa/part1-spread05-community-worksite-restart-v9-overlay.svg` (source layout: `../tmp/page-005-source/layout.png`)
- part1-page003-nalini-volunteers: `/workspace/Tap 53/Part 1/pages/page-003/qa/part1-page003-nalini-volunteers-overlay.svg` (source layout: `../pages/page-003/storyboards/page003-layout-source.png`)
