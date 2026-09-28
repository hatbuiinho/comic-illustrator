# Manifest layout QA

Tọa độ `x`, `y`, `width`, `height` chuẩn hóa 0..1 theo spread.

```json
{
  "defaults": {
    "ratioTolerance": 0.015,
    "printTrim": {
      "trimPercent": { "x": 0.0104895, "y": 0.0147783 },
      "criticalSafePercent": { "x": 0.027972, "y": 0.0394089 }
    },
    "checks": {
      "frame": "REQUIRED",
      "ratio": "REQUIRED",
      "textReserve": "REQUIRED",
      "printSafe": "REQUIRED",
      "spine": "REQUIRED"
    }
  },
  "overrides": {
    "spine": {
      "status": "SKIPPED_BY_USER",
      "reason": "Người dùng yêu cầu không cần tránh gáy",
      "scope": "deliverable hiện tại"
    }
  },
  "spreads": []
}
```

Mỗi spread cần `id`, `canvas`, `pageImage`, `frames`. Mỗi frame có `id`, `box`,
`shape`, `output`, `textReserve`, `spine`, `critical`; có thể override `checks`.
`contentFrame` là vùng output ánh xạ vào frame xanh khi canvas mở rộng.

Trạng thái hợp lệ: `REQUIRED`, `NOT_APPLICABLE`, `SKIPPED_BY_USER`.
