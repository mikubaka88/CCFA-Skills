#!/usr/bin/env python3
"""Build a lean runtime and an optional full-PDF pack from public Git candidates."""
from __future__ import annotations

import argparse
import hashlib
import json
import os
from pathlib import Path
import subprocess
import sys
import tempfile
import zipfile

from release_support import MANIFEST, digest, is_paper_pdf, no_links, public_path, read_json


def build(root, output, tracked_only=True):
    root = no_links(root).resolve()
    output = no_links(output).resolve()
    codex = read_json(root / ".codex-plugin/plugin.json")["version"]
    if codex != read_json(root / ".claude-plugin/plugin.json")["version"]:
        raise ValueError("Plugin release versions disagree")
    command = ["git", "-C", str(root), "ls-files", "-c", "-z"]
    if not tracked_only:
        command += ["-o", "--exclude-standard"]
    names = subprocess.check_output(command).decode("utf-8").split("\0")
    head = subprocess.run(["git", "-C", str(root), "rev-parse", "--verify", "HEAD"],
                          capture_output=True, text=True, encoding="utf-8")
    source_identity = {
        "commit": head.stdout.strip() if head.returncode == 0 else None,
        "dirty": bool(subprocess.check_output(["git", "-C", str(root), "status", "--porcelain", "--untracked-files=normal"])),
        "file_selection": "tracked" if tracked_only else "tracked-and-untracked",
    }
    files = []
    for name in sorted(set(names)-{""}):
        if not public_path(name):
            continue
        path = no_links(root / name)
        if path.is_file():
            files.append(name)
    skills = sorted(name.split("/")[0] for name in files if name.startswith("ccf-") and name.count("/") == 1 and name.endswith("/SKILL.md"))
    if len(skills) != 18:
        raise ValueError("A family release must include all 18 current skill entries")
    output.mkdir(parents=True, exist_ok=True)
    reports = []
    for profile in ("lean", "papers"):
        controls = {"tools/install_release.py", "tools/release_support.py", "LICENSE"}
        chosen = [name for name in files if (is_paper_pdf(name) == (profile == "papers"))
                  or (profile == "papers" and name in controls)]
        entries = [{"path": name, "sha256": digest(root / name), "bytes": (root / name).stat().st_size} for name in chosen]
        manifest = {"schema_version": 1, "release_id": "ccfa-skills-"+codex, "version": codex,
                    "profile": profile, "skills": skills, "files": entries, "source": source_identity}
        base = "ccfa-skills-"+codex+"-"+profile
        target = output / (base+".zip")
        fd, temporary = tempfile.mkstemp(prefix=".ccfa-release-", suffix=".zip", dir=output)
        os.close(fd)
        try:
            with zipfile.ZipFile(temporary, "w", compression=zipfile.ZIP_DEFLATED, compresslevel=6) as archive:
                for entry in entries:
                    path = no_links(root / entry["path"])
                    measured = hashlib.sha256(); size = 0
                    with path.open("rb") as inp, archive.open(base+"/"+entry["path"], "w") as out:
                        for block in iter(lambda: inp.read(1024*1024), b""):
                            out.write(block); measured.update(block); size += len(block)
                    if measured.hexdigest() != entry["sha256"] or size != entry["bytes"]:
                        raise ValueError("Source changed while packaging: "+entry["path"])
                archive.writestr(base+"/"+MANIFEST, json.dumps(manifest, ensure_ascii=False, indent=2)+"\n")
            os.replace(temporary, target)
        finally:
            Path(temporary).unlink(missing_ok=True)
        reports.append({"profile": profile, "file": target.name, "sha256": digest(target), "zip_bytes": target.stat().st_size,
                        "unpacked_bytes": sum(e["bytes"] for e in entries), "files": len(entries), "version": codex})
    (output / "SHA256SUMS").write_text("".join(r["sha256"]+"  "+r["file"]+"\n" for r in reports), encoding="utf-8")
    (output / "release-size-report.json").write_text(json.dumps(reports, indent=2)+"\n", encoding="utf-8")
    return reports


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1])
    parser.add_argument("--out", type=Path, default=Path("ccfa-workfiles/skill-maintenance/release-012/build"))
    selection = parser.add_mutually_exclusive_group()
    selection.add_argument("--tracked-only", dest="tracked_only", action="store_true", default=True,
                           help="Package indexed paths only (default); bytes come from the working tree")
    selection.add_argument("--include-untracked", dest="tracked_only", action="store_false",
                           help="Development only: also package non-ignored untracked files")
    args = parser.parse_args()
    try:
        print(json.dumps(build(args.root, args.out, args.tracked_only), indent=2))
    except (OSError, ValueError, KeyError, subprocess.CalledProcessError) as exc:
        parser.error(str(exc))


if __name__ == "__main__":
    for stream in (sys.stdout, sys.stderr):
        if hasattr(stream, "reconfigure"): stream.reconfigure(encoding="utf-8", errors="strict")
    main()
