#!/usr/bin/env python3
"""Deterministic continuity artifact validation, hashing and state updates."""

from __future__ import annotations

import argparse
import copy
import hashlib
import json
import os
import sys
import tempfile
from pathlib import Path

import yaml

PROVENANCE = {"sourceFact", "userConfirmed", "assistantInference"}
STATUSES = {"CURRENT", "STALE", "CONFLICT"}


def load_data(path: Path):
    with path.open("r", encoding="utf-8") as handle:
        if path.suffix.lower() == ".json":
            return json.load(handle)
        return yaml.safe_load(handle)


def dump_data(path: Path, data):
    path.parent.mkdir(parents=True, exist_ok=True)
    suffix = path.suffix.lower()
    fd, tmp_name = tempfile.mkstemp(prefix=f".{path.name}.", dir=path.parent)
    try:
        with os.fdopen(fd, "w", encoding="utf-8") as handle:
            if suffix == ".json":
                json.dump(data, handle, ensure_ascii=False, indent=2)
                handle.write("\n")
            else:
                yaml.safe_dump(data, handle, allow_unicode=True, sort_keys=False)
        os.replace(tmp_name, path)
    except Exception:
        try:
            os.unlink(tmp_name)
        except FileNotFoundError:
            pass
        raise


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(block)
    return f"sha256:{digest.hexdigest()}"


def relative_target(base: Path, raw: str) -> Path:
    target = (base / raw).resolve()
    if not target.is_relative_to(base.resolve()):
        raise ValueError(f"Đường dẫn vượt namespace: {raw}")
    return target


def episode_root(artifact: Path) -> Path:
    start = artifact.parent.resolve()
    for candidate in (start, *start.parents):
        if (candidate / "episode.json").exists():
            return candidate
    return start


def artifact_kind(data) -> str:
    explicit = data.get("artifactType") if isinstance(data, dict) else None
    if explicit:
        return explicit
    if isinstance(data, dict) and "events" in data:
        return "continuity-ledger"
    if isinstance(data, dict) and ("stage" in data or "pendingQuestion" in data):
        return "page-state"
    if isinstance(data, dict) and ("continuityIn" in data or "continuityOut" in data):
        return "scene-packet"
    return "episode-canon"


def validate(path: Path, data) -> list[str]:
    errors: list[str] = []
    if not isinstance(data, dict):
        return ["Artifact phải là object/map."]
    for key in ("schemaVersion", "scope"):
        if key not in data:
            errors.append(f"Thiếu trường bắt buộc: {key}.")
    status = data.get("status")
    if status is not None and status not in STATUSES:
        errors.append(f"status không hợp lệ: {status}.")
    base = episode_root(path)
    dependencies = data.get("generatedFrom", [])
    if dependencies is not None and not isinstance(dependencies, list):
        errors.append("generatedFrom phải là danh sách.")
    for index, dependency in enumerate(dependencies or []):
        if not isinstance(dependency, dict) or not dependency.get("path"):
            errors.append(f"generatedFrom[{index}] thiếu path.")
            continue
        raw = dependency["path"]
        if Path(raw).is_absolute():
            errors.append(f"generatedFrom[{index}] phải dùng đường dẫn tương đối.")
            continue
        try:
            target = relative_target(base, raw)
            if not target.exists():
                errors.append(f"Dependency không tồn tại: {raw}.")
        except ValueError as error:
            errors.append(str(error))
    for index, fact in enumerate(data.get("facts", []) or []):
        if not isinstance(fact, dict):
            errors.append(f"facts[{index}] phải là object.")
            continue
        if not fact.get("key"):
            errors.append(f"facts[{index}] thiếu key.")
        provenance = fact.get("provenance")
        if provenance not in PROVENANCE:
            errors.append(f"facts[{index}] provenance không hợp lệ: {provenance}.")
        if not fact.get("evidence"):
            errors.append(f"facts[{index}] thiếu evidence.")
    kind = artifact_kind(data)
    if kind == "continuity-ledger":
        seen = set()
        for index, event in enumerate(data.get("events", []) or []):
            event_id = event.get("eventId") if isinstance(event, dict) else None
            if not event_id:
                errors.append(f"events[{index}] thiếu eventId.")
            elif event_id in seen:
                errors.append(f"eventId bị trùng: {event_id}.")
            seen.add(event_id)
            if isinstance(event, dict) and event.get("provenance") == "assistantInference":
                errors.append(f"Event {event_id or index} không được dùng assistantInference.")
            if isinstance(event, dict) and event.get("status") not in {"CONFIRMED", "REVOKED"}:
                errors.append(f"Event {event_id or index} có status không hợp lệ.")
    if kind == "page-state" and data.get("stage") not in {
        None, "scope", "source", "composition", "production", "visual_qa",
        "layout_qa", "delivery", "complete"
    }:
        errors.append(f"stage không hợp lệ: {data.get('stage')}.")
    return errors


def freshness(path: Path, data):
    stale = []
    for dependency in data.get("generatedFrom", []) or []:
        raw = dependency.get("path")
        expected = dependency.get("fingerprint")
        if not raw or not expected:
            continue
        try:
            target = relative_target(episode_root(path), raw)
        except ValueError as error:
            stale.append({"path": raw, "reason": str(error)})
            continue
        if not target.exists():
            stale.append({"path": raw, "reason": "MISSING"})
            continue
        actual = sha256(target)
        if actual != expected:
            stale.append({"path": raw, "reason": "FINGERPRINT_CHANGED", "expected": expected, "actual": actual})
    return stale


def cmd_validate(args):
    path = Path(args.artifact).resolve()
    data = load_data(path)
    errors = validate(path, data)
    stale = freshness(path, data) if isinstance(data, dict) else []
    result = {"artifact": str(path), "kind": artifact_kind(data), "valid": not errors, "errors": errors, "staleDependencies": stale}
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 1 if errors else 0


def cmd_fingerprint(args):
    root = Path(args.root).resolve() if args.root else Path.cwd().resolve()
    entries = []
    for raw in args.sources:
        source = Path(raw).resolve()
        if not source.exists() or not source.is_file():
            raise FileNotFoundError(raw)
        try:
            display = source.relative_to(root).as_posix()
        except ValueError:
            display = str(source)
        entries.append({"path": display, "fingerprint": sha256(source), "size": source.stat().st_size})
    print(json.dumps(entries, ensure_ascii=False, indent=2))
    return 0


def cmd_check_stale(args):
    path = Path(args.artifact).resolve()
    data = load_data(path)
    stale = freshness(path, data)
    print(json.dumps({"status": "STALE" if stale else "CURRENT", "staleDependencies": stale}, ensure_ascii=False, indent=2))
    return 1 if stale else 0


def cmd_invalidate(args):
    path = Path(args.artifact).resolve()
    data = load_data(path)
    stale = freshness(path, data)
    if args.reason:
        stale.append({"path": None, "reason": args.reason})
    if stale:
        data["status"] = "STALE"
        existing = data.setdefault("staleReasons", [])
        for item in stale:
            if item not in existing:
                existing.append(item)
        if args.write:
            dump_data(path, data)
    print(json.dumps({"artifact": str(path), "status": data.get("status", "CURRENT"), "staleReasons": stale, "written": bool(args.write and stale)}, ensure_ascii=False, indent=2))
    return 0


def cmd_invalidate_dependents(args):
    episode = Path(args.episode).resolve()
    changed = Path(args.changed_source).resolve()
    candidates = list(episode.glob("**/*.json")) + list(episode.glob("**/*.yaml")) + list(episode.glob("**/*.yml"))
    artifacts = {}
    for path in candidates:
        try:
            data = load_data(path)
        except (OSError, ValueError, yaml.YAMLError, json.JSONDecodeError):
            continue
        if isinstance(data, dict) and isinstance(data.get("generatedFrom"), list):
            artifacts[path.resolve()] = data
    stale_paths = {changed}
    affected = []
    made_progress = True
    while made_progress:
        made_progress = False
        for path, data in artifacts.items():
            if path in stale_paths:
                continue
            for dependency in data.get("generatedFrom", []):
                raw = dependency.get("path") if isinstance(dependency, dict) else None
                if not raw:
                    continue
                try:
                    target = relative_target(episode_root(path), raw)
                except ValueError:
                    continue
                if target in stale_paths:
                    stale_paths.add(path)
                    affected.append({"artifact": str(path.relative_to(episode)), "dependency": str(target)})
                    if args.write:
                        data["status"] = "STALE"
                        reason = {"path": raw, "reason": "DEPENDENCY_INVALIDATED"}
                        if reason not in data.setdefault("staleReasons", []):
                            data["staleReasons"].append(reason)
                        dump_data(path, data)
                    made_progress = True
                    break
    print(json.dumps({"changedSource": str(changed), "affected": affected, "written": args.write}, ensure_ascii=False, indent=2))
    return 0


def cmd_commit_event(args):
    ledger_path = Path(args.ledger).resolve()
    event_path = Path(args.event).resolve()
    ledger = load_data(ledger_path)
    event = load_data(event_path)
    if event.get("provenance") == "assistantInference":
        raise ValueError("Không được commit assistantInference vào continuity ledger.")
    if event.get("provenance") not in {"sourceFact", "userConfirmed"}:
        raise ValueError("Event phải có provenance sourceFact hoặc userConfirmed.")
    for field in ("eventId", "effectiveAfter", "changes", "evidence"):
        if not event.get(field):
            raise ValueError(f"Event thiếu {field}.")
    event["status"] = event.get("status", "CONFIRMED")
    existing = {item.get("eventId") for item in ledger.get("events", [])}
    if event["eventId"] in existing:
        raise ValueError(f"eventId đã tồn tại: {event['eventId']}.")
    updated = copy.deepcopy(ledger)
    updated.setdefault("events", []).append(event)
    errors = validate(ledger_path, updated)
    if errors:
        raise ValueError("; ".join(errors))
    if args.write:
        dump_data(ledger_path, updated)
    print(json.dumps({"status": "READY" if not args.write else "COMMITTED", "eventId": event["eventId"], "ledger": str(ledger_path)}, ensure_ascii=False, indent=2))
    return 0


def cmd_resolve(args):
    episode = Path(args.episode).resolve()
    candidates = []
    if args.page_state:
        candidates.append(Path(args.page_state).resolve())
    else:
        page_pattern = f"page-{int(args.page):03d}" if args.page else None
        if page_pattern:
            candidates.extend(episode.glob(f"**/{page_pattern}/page-state.y*ml"))
            candidates.extend(episode.glob(f"**/{page_pattern}/page-state.json"))
    candidates.extend(sorted((episode / "continuity" / "scenes").glob("*.y*ml")) if (episode / "continuity" / "scenes").exists() else [])
    candidates.extend([episode / "continuity" / "ledger.yaml", episode / "continuity" / "ledger.json", episode / "continuity" / "episode-canon.yaml", episode / "continuity" / "episode-canon.json"])
    artifacts = []
    stale_all = []
    for path in candidates:
        if not path.exists() or path in [Path(item["path"]) for item in artifacts]:
            continue
        data = load_data(path)
        stale = freshness(path, data)
        stale_all.extend({"artifact": str(path), **item} for item in stale)
        artifacts.append({"path": str(path), "kind": artifact_kind(data), "status": "STALE" if stale else data.get("status", "CURRENT")})
    status = "STALE" if stale_all else ("COMPLETE" if artifacts else "NEEDS_SOURCE_EXPANSION")
    print(json.dumps({"target": {"episode": episode.name, "part": args.part, "page": args.page, "frame": args.frame}, "status": status, "artifacts": artifacts, "staleArtifacts": stale_all}, ensure_ascii=False, indent=2))
    return 0


def parser():
    root = argparse.ArgumentParser(description=__doc__)
    sub = root.add_subparsers(dest="command", required=True)
    validate_parser = sub.add_parser("validate")
    validate_parser.add_argument("artifact")
    validate_parser.set_defaults(func=cmd_validate)
    fingerprint_parser = sub.add_parser("fingerprint")
    fingerprint_parser.add_argument("sources", nargs="+")
    fingerprint_parser.add_argument("--root")
    fingerprint_parser.set_defaults(func=cmd_fingerprint)
    stale_parser = sub.add_parser("check-stale")
    stale_parser.add_argument("artifact")
    stale_parser.set_defaults(func=cmd_check_stale)
    invalidate_parser = sub.add_parser("invalidate")
    invalidate_parser.add_argument("artifact")
    invalidate_parser.add_argument("--reason")
    invalidate_parser.add_argument("--write", action="store_true")
    invalidate_parser.set_defaults(func=cmd_invalidate)
    tree_parser = sub.add_parser("invalidate-dependents")
    tree_parser.add_argument("episode")
    tree_parser.add_argument("changed_source")
    tree_parser.add_argument("--write", action="store_true")
    tree_parser.set_defaults(func=cmd_invalidate_dependents)
    commit_parser = sub.add_parser("commit-event")
    commit_parser.add_argument("ledger")
    commit_parser.add_argument("event")
    commit_parser.add_argument("--write", action="store_true")
    commit_parser.set_defaults(func=cmd_commit_event)
    resolve_parser = sub.add_parser("resolve")
    resolve_parser.add_argument("episode")
    resolve_parser.add_argument("--part")
    resolve_parser.add_argument("--page", type=int)
    resolve_parser.add_argument("--frame")
    resolve_parser.add_argument("--page-state")
    resolve_parser.set_defaults(func=cmd_resolve)
    return root


def main():
    try:
        args = parser().parse_args()
        return args.func(args)
    except (OSError, ValueError, yaml.YAMLError, json.JSONDecodeError) as error:
        print(f"ERROR: {error}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
