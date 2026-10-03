#!/usr/bin/env python3
"""Audit reusable comic workflow artifacts without modifying the project."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path

import yaml


def load(path):
    with path.open("r", encoding="utf-8") as handle:
        return json.load(handle) if path.suffix == ".json" else yaml.safe_load(handle)


def main():
    if len(sys.argv) == 2 and sys.argv[1] in {"-h", "--help"}:
        print("Usage: python3 audit-project.py <episode-directory>")
        return 0
    if len(sys.argv) != 2:
        print("Usage: python3 audit-project.py <episode-directory>", file=sys.stderr)
        return 2
    episode = Path(sys.argv[1]).resolve()
    if not episode.is_dir():
        print("ERROR: episode-directory không tồn tại.", file=sys.stderr)
        return 2
    context_cli = Path(__file__).with_name("comic-context.py")
    errors = []
    warnings = []
    context_files = []
    for pattern in ("continuity/**/*.yaml", "continuity/**/*.yml", "continuity/**/*.json", "**/page-state.yaml", "**/page-state.yml", "**/page-state.json"):
        context_files.extend(episode.glob(pattern))
    for path in sorted(set(context_files)):
        result = subprocess.run([sys.executable, str(context_cli), "validate", str(path)], capture_output=True, text=True)
        if result.returncode:
            errors.append({"artifact": str(path.relative_to(episode)), "detail": result.stdout.strip() or result.stderr.strip()})
        stale = subprocess.run([sys.executable, str(context_cli), "check-stale", str(path)], capture_output=True, text=True)
        if stale.returncode == 1:
            warnings.append({"artifact": str(path.relative_to(episode)), "detail": "STALE"})
    empty_outputs = [str(path.relative_to(episode)) for path in episode.glob("**/outputs/*") if path.is_file() and path.stat().st_size == 0]
    for item in empty_outputs:
        warnings.append({"artifact": item, "detail": "Reservation/output rỗng."})
    result = {"episode": episode.name, "status": "FAIL" if errors else "PASS", "contextArtifacts": len(set(context_files)), "errors": errors, "warnings": warnings}
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 1 if errors else 0


if __name__ == "__main__":
    raise SystemExit(main())
