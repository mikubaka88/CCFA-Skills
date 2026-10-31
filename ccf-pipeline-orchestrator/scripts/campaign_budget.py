"""Opt-in shared experiment allowances; no model calls or execution service."""

import contextlib
import datetime as dt
import json
import math
import os
from pathlib import Path
import uuid


class CampaignError(ValueError):
    pass


def _finite(value):
    try:
        return type(value) in (int, float) and math.isfinite(value) and value >= 0
    except OverflowError:
        return False


def _plain(path):
    path = Path(os.path.abspath(path))
    for part in (path, *path.parents):
        if part.is_symlink() or (hasattr(part, "is_junction") and part.is_junction()):
            raise CampaignError("Campaign paths cannot pass through links/junctions")
    return path


def _now():
    return dt.datetime.now(dt.timezone.utc).isoformat()


def _final_binding_valid(value):
    return (isinstance(value, dict) and set(value) == {"candidate_id", "candidate_hash", "protocol_hash"}
            and all(isinstance(value[name], str) and bool(value[name]) for name in value)
            and len(value["candidate_hash"]) == len(value["protocol_hash"]) == 64)


@contextlib.contextmanager
def _lock(path):
    path = _plain(path)
    lock = _plain(path.with_name(path.name + ".lock"))
    with lock.open("a+b") as stream:
        stream.seek(0, 2)
        if stream.tell() == 0:
            stream.write(b"\0")
            stream.flush()
        stream.seek(0)
        try:
            if os.name == "nt":
                import msvcrt
                msvcrt.locking(stream.fileno(), msvcrt.LK_NBLCK, 1)
            else:
                import fcntl
                fcntl.flock(stream.fileno(), fcntl.LOCK_EX | fcntl.LOCK_NB)
        except OSError as exc:
            raise CampaignError("Shared campaign budget is busy; retry after its current transaction") from exc
        try:
            yield path
        finally:
            stream.seek(0)
            if os.name == "nt":
                msvcrt.locking(stream.fileno(), msvcrt.LK_UNLCK, 1)
            else:
                fcntl.flock(stream.fileno(), fcntl.LOCK_UN)


def _pairs(items):
    result = {}
    for key, value in items:
        if key in result:
            raise CampaignError("Duplicate campaign JSON key")
        result[key] = value
    return result


def _load(path, campaign_id, project):
    path = _plain(path)
    try:
        if not path.is_file() or path.stat().st_nlink != 1:
            raise CampaignError("Campaign record must be a regular unshared file")
        data = json.loads(path.read_text(encoding="utf-8-sig"), object_pairs_hook=_pairs,
                          parse_constant=lambda _: (_ for _ in ()).throw(CampaignError("Nonfinite campaign JSON")))
        valid = (data["schema_version"] == 1 and type(data["schema_version"]) is int
                 and data["id"] == campaign_id and Path(data["project"]) == project
                 and type(data["budgets"]["max_attempts"]) is int and data["budgets"]["max_attempts"] > 0
                 and _finite(data["budgets"]["max_seconds"]) and data["budgets"]["max_seconds"] > 0
                 and isinstance(data["reservations"], dict) and isinstance(data["task_sets"], dict))
        if not valid:
            raise CampaignError("Campaign identity or budget schema does not match")
        for item in data["reservations"].values():
            if (not isinstance(item, dict) or item["status"] not in ("reserved", "settled", "unknown")
                    or not _finite(item["reserved_seconds"]) or not _finite(item.get("charge_seconds", 0))):
                raise CampaignError("Invalid shared reservation")
        for identity, item in data["task_sets"].items():
            if (not isinstance(identity, str) or not identity or not isinstance(item, dict)
                    or item.get("role") not in ("development", "selection", "final")
                    or not isinstance(item.get("content_hash"), str) or len(item["content_hash"]) != 64
                    or not isinstance(item.get("workdirs"), list) or any(not isinstance(v, str) for v in item["workdirs"])):
                raise CampaignError("Invalid shared task-set identity")
        # Older records did not track whether a final score had already been
        # viewed. Never turn that missing history into a fresh held-out use.
        if "final_uses" not in data:
            data["final_uses"] = {
                item["content_hash"]: {"status": "legacy_unknown", "binding": None}
                for item in data["task_sets"].values() if item["role"] == "final"
            }
        if not isinstance(data["final_uses"], dict):
            raise CampaignError("Invalid shared final-use record")
        for identity, item in data["final_uses"].items():
            if (not isinstance(identity, str) or len(identity) != 64 or not isinstance(item, dict)
                    or item.get("status") not in ("reserved", "completed", "retryable", "unknown", "legacy_unknown")
                    or (item.get("status") != "legacy_unknown" and (
                        not _final_binding_valid(item.get("binding"))
                        or not isinstance(item.get("reservation"), str)
                        or not item["reservation"]))):
                raise CampaignError("Invalid shared final-use identity")
        return data
    except (OSError, UnicodeError, ValueError, KeyError, TypeError) as exc:
        if isinstance(exc, CampaignError):
            raise
        raise CampaignError(f"Cannot load shared campaign budget: {exc}") from exc


def _save(path, value):
    temporary = path.with_name(f".{path.name}.{uuid.uuid4().hex}.tmp")
    try:
        with temporary.open("xb") as stream:
            stream.write((json.dumps(value, ensure_ascii=False, sort_keys=True, allow_nan=False) + "\n").encode("utf-8"))
            stream.flush()
            os.fsync(stream.fileno())
        os.replace(temporary, path)
    finally:
        temporary.unlink(missing_ok=True)


def initialize(path, project, campaign_id, max_attempts, max_seconds):
    project = Path(project).resolve(strict=True)
    path = _plain(path)
    if (not path.is_relative_to(project) or path == project or not isinstance(campaign_id, str) or not campaign_id.strip()
            or type(max_attempts) is not int or max_attempts < 1 or not _finite(max_seconds) or max_seconds <= 0):
        raise CampaignError("Campaign requires a project-local record, nonempty ID and positive finite budgets")
    path.parent.mkdir(parents=True, exist_ok=True)
    with _lock(path):
        if path.exists():
            raise CampaignError("Campaign already exists; reuse its remaining budget, never reinitialize")
        data = {"schema_version": 1, "id": campaign_id, "project": str(project),
                "budgets": {"max_attempts": max_attempts, "max_seconds": max_seconds},
                "reservations": {}, "task_sets": {}, "final_uses": {}, "model_tokens": None, "created_at": _now()}
        _save(path, data)
        return _summary(data)


def _summary(data):
    items = list(data["reservations"].values())
    charged = sum(item.get("charge_seconds", 0) for item in items)
    reserved = sum(item["reserved_seconds"] for item in items if item["status"] == "reserved")
    result = {"id": data["id"], "attempts_used": len(items),
            "attempts_remaining": max(0, data["budgets"]["max_attempts"] - len(items)),
            "execution_seconds_charged": charged, "execution_seconds_reserved": reserved,
            "execution_seconds_remaining": max(0, data["budgets"]["max_seconds"] - charged - reserved),
            "duration_unknown": any(item["status"] == "unknown" for item in items),
            "model_tokens": None,
            "meter_scope": "shared foreground-command seconds; model usage and host preparation are not measured"}
    if data.get("final_uses"):
        result["final_task_uses"] = [
            {"task_content_hash": content, "status": usage["status"], "reservation": usage.get("reservation"),
             "candidate_id": (usage.get("binding") or {}).get("candidate_id")}
            for content, usage in sorted(data["final_uses"].items())
        ]
    return result


def status(path, campaign_id, project):
    return _summary(_load(path, campaign_id, project))


def register(path, campaign_id, project, workdir, evaluation=None, validate_only=False):
    """Bind task-set roles to this campaign without consuming execution budget."""
    with _lock(path):
        data = _load(path, campaign_id, project)
        if evaluation:
            identity, role = evaluation["task_set_id"], evaluation["split_role"]
            content_hash = evaluation["task_content_hash"]
            previous = data["task_sets"].get(identity)
            if previous and ((previous["role"] == "final") != (role == "final")):
                raise CampaignError("A final task set cannot be reused for development/selection, or vice versa")
            same_content = [(name, item) for name, item in data["task_sets"].items()
                            if item.get("content_hash") == content_hash]
            if role == "final" and any(item["role"] != "final" for _, item in same_content):
                raise CampaignError("Final task content was already used for development/selection; renaming cannot restore held-out status")
            prior_final = {name for name, item in same_content if item["role"] == "final"}
            reuse = evaluation.get("reused_final")
            relative = str(workdir.relative_to(project)).replace("\\", "/")
            final_use = data["final_uses"].get(content_hash) if role == "final" else None
            if final_use:
                if final_use["status"] == "legacy_unknown":
                    raise CampaignError("Legacy final-task use is unknown; reconcile its prior records or use a new final set / explicit non-final reuse")
                if evaluation["frozen_candidate"]["candidate_id"] != final_use["binding"]["candidate_id"]:
                    raise CampaignError("Final task content is already bound to a frozen candidate and protocol in this campaign; use a new final set or explicit non-final reuse")
                if final_use["status"] != "retryable" and (not previous or relative not in previous["workdirs"]):
                    raise CampaignError("Final task content is already used or reserved in this campaign; report its existing result without rerunning in another directory")
            if role != "final" and prior_final:
                if not reuse or reuse["task_set_id"] not in prior_final or not reuse["reason"].strip():
                    raise CampaignError("Reusing final task content requires explicit reused_final identity/reason and a new non-final label")
            if reuse and reuse["task_set_id"] not in prior_final:
                raise CampaignError("reused_final must reference matching final task content in this campaign")
            if not previous:
                data["task_sets"][identity] = {"role": role, "workdirs": [], "content_hash": content_hash,
                                                "held_out": role == "final", "reused_final": reuse}
                previous = data["task_sets"][identity]
            elif previous.get("content_hash") != content_hash:
                raise CampaignError("A task_set_id is already bound to different task content")
            if relative not in previous["workdirs"]:
                previous["workdirs"].append(relative)
        if not validate_only:
            _save(path, data)


def reserve(path, campaign_id, project, key, requested_seconds, workdir, run_id, final_use=None):
    if final_use is not None and (not isinstance(final_use, dict)
            or set(final_use) != {"task_content_hash", "candidate_id", "candidate_hash", "protocol_hash"}
            or not isinstance(final_use.get("task_content_hash"), str) or len(final_use["task_content_hash"]) != 64
            or not _final_binding_valid({name: value for name, value in final_use.items() if name != "task_content_hash"})):
        raise CampaignError("Final reservation requires task-content, frozen-candidate and protocol identities")
    with _lock(path):
        data = _load(path, campaign_id, project)
        if key in data["reservations"]:
            raise CampaignError("This shared run ID was already reserved; reconcile its recorded attempt instead of rerunning")
        summary = _summary(data)
        if summary["attempts_remaining"] < 1 or summary["execution_seconds_remaining"] <= 0:
            raise CampaignError("Shared campaign attempt or execution-time budget is exhausted")
        if final_use:
            content_hash = final_use["task_content_hash"]
            binding = {name: final_use[name] for name in ("candidate_id", "candidate_hash", "protocol_hash")}
            previous = data["final_uses"].get(content_hash)
            if previous:
                if previous["status"] == "legacy_unknown":
                    raise CampaignError("Legacy final-task use is unknown; reconcile its prior records or use a new final set / explicit non-final reuse")
                if previous["binding"] != binding:
                    raise CampaignError("Final task content is already bound to a frozen candidate and protocol in this campaign; use a new final set or explicit non-final reuse")
                if previous["status"] != "retryable":
                    raise CampaignError("Final task content is already used or reserved in this campaign; report its existing result without rerunning in another directory")
            data["final_uses"][content_hash] = {
                "binding": binding, "status": "reserved", "reservation": key, "reserved_at": _now(),
            }
        seconds = min(requested_seconds, summary["execution_seconds_remaining"])
        data["reservations"][key] = {"status": "reserved", "reserved_seconds": seconds,
                                     "workdir": str(workdir.relative_to(project)).replace("\\", "/"),
                                     "run_id": run_id, "created_at": _now()}
        if final_use:
            data["reservations"][key]["final_content_hash"] = final_use["task_content_hash"]
        _save(path, data)
        return seconds


def settle(path, campaign_id, project, key, seconds=None, outcome=None):
    with _lock(path):
        data = _load(path, campaign_id, project)
        item = data["reservations"].get(key)
        if item is None:
            raise CampaignError("Missing shared reservation; preserve the experiment for reconciliation")
        if item["status"] != "reserved":
            if seconds is None:
                # A durable measured/zero-start settlement is stronger than a
                # caller's later uncertainty; never replace it with a guess.
                return _summary(data)
            if seconds is not None and item["status"] == "settled" and item["charge_seconds"] == seconds:
                return _summary(data)
            raise CampaignError("Shared budget settlement is immutable")
        if seconds is None:
            charged = sum(other.get("charge_seconds", 0) for other in data["reservations"].values())
            item.update(status="unknown", charge_seconds=max(0, data["budgets"]["max_seconds"] - charged),
                        note="Unknown duration closes the campaign's remaining allowance; not measured runtime")
        else:
            if not _finite(seconds):
                raise CampaignError("Shared settlement requires nonnegative finite elapsed seconds")
            item.update(status="settled", charge_seconds=seconds)
        item["settled_at"] = _now()
        if item.get("final_content_hash"):
            usage = data["final_uses"][item["final_content_hash"]]
            if usage.get("reservation") != key:
                raise CampaignError("Final-use reservation changed before settlement; reconcile shared records")
            # A failed command can retry only its unchanged candidate/protocol.
            # A score already produced, or an unknown execution, closes use.
            usage.update(status="unknown" if seconds is None or outcome is None else
                         "completed" if outcome == "ok" else "retryable",
                         outcome=outcome, settled_at=item["settled_at"])
        _save(path, data)
        return _summary(data)
