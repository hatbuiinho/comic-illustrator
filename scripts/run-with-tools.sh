#!/usr/bin/env bash
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_ROOT="$(cd "$SCRIPT_DIR/.." && pwd)"

"$SCRIPT_DIR/bootstrap-macos.sh"

eval "$(brew shellenv)"
export PATH="$PROJECT_ROOT/.venv/bin:$(brew --prefix)/bin:$(brew --prefix)/sbin:$PATH"

if [[ "${1:-}" == "--" ]]; then
  shift
fi

if [[ "$#" -eq 0 ]]; then
  echo "Toolchain đã sẵn sàng. Không có lệnh cần chạy."
  exit 0
fi

exec "$@"
