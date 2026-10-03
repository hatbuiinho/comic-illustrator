#!/usr/bin/env bash
set -euo pipefail

CHECK_ONLY=0
FORCE_REFRESH=0

for arg in "$@"; do
  case "$arg" in
    --check-only) CHECK_ONLY=1 ;;
    --force-refresh) FORCE_REFRESH=1 ;;
    *) echo "Tham số không hỗ trợ: $arg" >&2; exit 2 ;;
  esac
done

if [[ "$(uname -s)" != "Darwin" ]]; then
  echo "Script này chỉ dùng cho macOS." >&2
  exit 1
fi

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_ROOT="$(cd "$SCRIPT_DIR/.." && pwd)"
MANIFEST_PATH="$PROJECT_ROOT/.tools/macos-tools.json"
STATE_PATH="$PROJECT_ROOT/.tools/state.macos.json"
REQUIREMENTS_PATH="$PROJECT_ROOT/requirements-tools.txt"
VENV_PATH="$PROJECT_ROOT/.venv"
VENV_PYTHON="$VENV_PATH/bin/python"

if ! command -v brew >/dev/null 2>&1; then
  if [[ "$CHECK_ONLY" -eq 1 ]]; then
    echo "Thiếu Homebrew. Chạy lại không có --check-only để cài tự động." >&2
    exit 1
  fi

  echo "[INSTALL] Homebrew"
  echo "macOS có thể yêu cầu mật khẩu quản trị trong bước này."
  /bin/bash -c "$(/usr/bin/curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

  if [[ -x /opt/homebrew/bin/brew ]]; then
    export PATH="/opt/homebrew/bin:$PATH"
  elif [[ -x /usr/local/bin/brew ]]; then
    export PATH="/usr/local/bin:$PATH"
  fi

  if ! command -v brew >/dev/null 2>&1; then
    echo "Đã chạy installer nhưng vẫn chưa tìm thấy Homebrew." >&2
    exit 1
  fi
fi

eval "$(brew shellenv)"

if [[ ! -f "$MANIFEST_PATH" ]]; then
  echo "Không tìm thấy manifest: $MANIFEST_PATH" >&2
  exit 1
fi

# Python 3.12 được bootstrapped trước vì chính nó dùng để đọc manifest JSON
# mà không phụ thuộc jq hoặc runtime không còn được macOS cài sẵn.
if ! brew list --formula python@3.12 >/dev/null 2>&1; then
  if [[ "$CHECK_ONLY" -eq 1 ]]; then
    echo "Thiếu Python 3.12 (python@3.12). Chạy lại không có --check-only để cài." >&2
    exit 1
  fi
  echo "[INSTALL] Python 3.12"
  brew install python@3.12
fi
export PATH="$(brew --prefix python@3.12)/bin:$PATH"

mapfile_compat() {
  python3.12 - "$MANIFEST_PATH" <<'PY'
import json
import sys

with open(sys.argv[1], encoding="utf-8") as handle:
    manifest = json.load(handle)

for tool in manifest["homebrew"]:
    print("\t".join((tool["name"], tool["formula"], ",".join(tool["commands"]))))
PY
}

while IFS=$'\t' read -r name formula commands_csv; do
  missing=0
  IFS=',' read -r -a commands <<< "$commands_csv"
  for command_name in "${commands[@]}"; do
    if ! command -v "$command_name" >/dev/null 2>&1; then
      missing=1
      break
    fi
  done

  if [[ "$missing" -eq 0 ]]; then
    echo "[OK] $name"
    continue
  fi

  if [[ "$CHECK_ONLY" -eq 1 ]]; then
    echo "Thiếu $name ($formula). Chạy lại không có --check-only để cài." >&2
    exit 1
  fi

  echo "[INSTALL] $name"
  if brew list --formula "$formula" >/dev/null 2>&1; then
    brew link --overwrite "$formula" >/dev/null 2>&1 || true
  else
    brew install "$formula"
  fi
  eval "$(brew shellenv)"
done < <(mapfile_compat)

PYTHON312="$(command -v python3.12 || true)"
if [[ -z "$PYTHON312" ]]; then
  echo "Sau bootstrap vẫn thiếu python3.12." >&2
  exit 1
fi

if [[ ! -x "$VENV_PYTHON" ]]; then
  if [[ "$CHECK_ONLY" -eq 1 ]]; then
    echo "Thiếu môi trường Python .venv. Chạy lại không có --check-only để tạo." >&2
    exit 1
  fi
  echo "[CREATE] .venv"
  "$PYTHON312" -m venv "$VENV_PATH"
fi

requirements_hash="$(shasum -a 256 "$REQUIREMENTS_PATH" | awk '{print $1}')"
manifest_hash="$(shasum -a 256 "$MANIFEST_PATH" | awk '{print $1}')"
previous_hash=""
if [[ -f "$STATE_PATH" ]]; then
  previous_hash="$($VENV_PYTHON - "$STATE_PATH" <<'PY' 2>/dev/null || true
import json
import sys
try:
    with open(sys.argv[1], encoding="utf-8") as handle:
        print(json.load(handle).get("requirementsSha256", ""))
except Exception:
    pass
PY
)"
fi

python_ready=0
if [[ "$FORCE_REFRESH" -eq 0 && "$previous_hash" == "$requirements_hash" ]]; then
  if "$VENV_PYTHON" -c "import yaml, PIL, pdfplumber, pypdf, reportlab" >/dev/null 2>&1; then
    python_ready=1
  fi
fi

if [[ "$python_ready" -eq 0 ]]; then
  if [[ "$CHECK_ONLY" -eq 1 ]]; then
    echo "Python requirements chưa đồng bộ. Chạy lại không có --check-only để cài." >&2
    exit 1
  fi
  echo "[SYNC] Python requirements"
  "$VENV_PYTHON" -m pip install --upgrade pip
  "$VENV_PYTHON" -m pip install --requirement "$REQUIREMENTS_PATH"
fi

export PATH="$VENV_PATH/bin:$(brew --prefix)/bin:$(brew --prefix)/sbin:$PATH"
required_commands=(git node rg pdfinfo pdftotext pdftoppm rsvg-convert python3)
for command_name in "${required_commands[@]}"; do
  if ! command -v "$command_name" >/dev/null 2>&1; then
    echo "Sau bootstrap vẫn thiếu command bắt buộc: $command_name" >&2
    exit 1
  fi
done

"$VENV_PYTHON" - "$STATE_PATH" "$manifest_hash" "$requirements_hash" "${required_commands[@]}" <<'PY'
import datetime
import json
import os
import platform
import shutil
import subprocess
import sys

state_path, manifest_hash, requirements_hash, *commands = sys.argv[1:]
command_state = {}
for name in commands:
    path = shutil.which(name)
    try:
        result = subprocess.run([path, "--version"], capture_output=True, text=True, timeout=10)
        version = (result.stdout or result.stderr).splitlines()[0].strip()
    except Exception:
        version = "installed"
    command_state[name] = {"path": path, "version": version}

state = {
    "schemaVersion": 1,
    "checkedAt": datetime.datetime.now(datetime.timezone.utc).astimezone().isoformat(),
    "machine": platform.node(),
    "manifestSha256": manifest_hash,
    "requirementsSha256": requirements_hash,
    "venvPython": sys.executable,
    "commands": command_state,
}
with open(state_path, "w", encoding="utf-8") as handle:
    json.dump(state, handle, ensure_ascii=False, indent=2)
    handle.write("\n")
PY

echo "[READY] Toolchain đã sẵn sàng. State: $STATE_PATH"
