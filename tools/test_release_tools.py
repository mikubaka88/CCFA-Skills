#!/usr/bin/env python3
"""Exercise real clean installs and conservative updates without network access."""
from __future__ import annotations

import copy
import json
from pathlib import Path
import stat
import subprocess
import sys
import tempfile
from types import SimpleNamespace
import unittest
from unittest.mock import patch
import zipfile

import build_release as builder
import install_release as installer
import release_support as support

ROOT = Path(__file__).resolve().parents[1]
SKILLS = sorted(p.name for p in ROOT.glob("ccf-*") if (p / "SKILL.md").is_file())
BUILD = ROOT / "ccfa-workfiles/skill-maintenance/release-012/build"


class ReleaseTests(unittest.TestCase):
    def setUp(self):
        BUILD.mkdir(parents=True, exist_ok=True)
        self.temp = tempfile.TemporaryDirectory(prefix="release-test-", dir=BUILD)
        self.directory = Path(self.temp.name).resolve()
        self.assertEqual(self.directory.parent, BUILD.resolve())
        self.repo = self.directory / "repository 中文"
        self.repo.mkdir()
        subprocess.run(["git", "init", "-q", str(self.repo)], check=True)
        subprocess.run(["git", "-C", str(self.repo), "config", "core.autocrlf", "false"], check=True)
        for skill in SKILLS:
            self.put(skill+"/SKILL.md", "# "+skill+"\n")
        for path, value in {
            ".codex-plugin/plugin.json": '{"version":"0.12.0"}',
            ".claude-plugin/plugin.json": '{"version":"0.12.0"}',
            "ccf-common/references/routing.md": "Shared routing",
            "ccf-paper-writer/references/exemplars/papers/original.md": "Attributable original text",
            "ccf-paper-writer/references/exemplar-style-analysis.md": "Original prose analysis",
            "ccf-paper-writer/references/exemplars/index.md": "Exemplar card index",
            "ccf-paper-writer/references/custom-format/default-user-format.md": "Optional user selection",
            "ccf-paper-writer/scripts/convert.py": "# legacy bridge\n",
            "ccf-paper-to-exemplar/scripts/convert.py": "# shared converter\n",
            "ccf-latex-templates/NeurIPS/template.tex": "Template retained",
            "ccf-latex-templates/CVPR/2027/main.tex": "Year-specific template retained",
            "ccf-latex-templates/CVPR/2027/template-source.json": '{"venue":"CVPR","year":2027}',
            "assets/visual-showcase/reference.svg": "<svg/>",
            "README.md": "Download documentation",
            "LICENSE": "Fixture license",
        }.items(): self.put(path, value)
        self.put(support.PAPERS+"original.pdf", b"%PDF-1.4 fixture\n")
        self.legacy_pdf = "ccf-paper-writer/paper_ref/旧版 paper.pdf"
        self.put(self.legacy_pdf, b"%PDF-1.4 legacy fixture\n")
        for file in ("install_release.py", "release_support.py"):
            self.put("tools/"+file, (ROOT / "tools" / file).read_bytes())
        subprocess.run(["git", "-C", str(self.repo), "add", "."], check=True)
        for path in ("ccfa-workfiles/private.txt", "output/private.txt", ".secrets/token.txt"):
            self.put(path, "not a release file")
            subprocess.run(["git", "-C", str(self.repo), "add", "-f", path], check=True)
        self.output = self.directory / "packages"
        self.make_release()
        self.target = self.directory / "installed skills 中文"

    def tearDown(self):
        # Only the new, checked task-owned temporary directory is removed.
        self.temp.cleanup()

    def put(self, name, value):
        path = self.repo / name
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_bytes(value if isinstance(value, bytes) else value.encode("utf-8"))

    def make_release(self, version="0.12.0"):
        for plugin in (".codex-plugin", ".claude-plugin"):
            self.put(plugin+"/plugin.json", json.dumps({"version": version}))
        self.reports = builder.build(self.repo, self.output)
        sources = {}
        for item in self.reports:
            with zipfile.ZipFile(self.output / item["file"]) as archive:
                archive.extractall(self.directory / ("extracted-"+version))
            sources[item["profile"]] = self.directory / ("extracted-"+version) / ("ccfa-skills-"+version+"-"+item["profile"])
        self.source, self.papers = sources["lean"], sources["papers"]

    def test_both_profiles_share_version_hash_manifest_and_exclude_private_paths(self):
        for source in (self.source, self.papers):
            _, manifest = support.load_release(source)
            self.assertEqual(manifest["version"], "0.12.0")
            self.assertEqual(manifest["skills"], SKILLS)
            self.assertFalse(any(not support.public_path(e["path"]) for e in manifest["files"]))
        self.assertFalse((self.source / (support.PAPERS+"original.pdf")).exists())
        self.assertTrue((self.source / (support.PAPERS+"original.md")).exists())
        self.assertTrue((self.papers / (support.PAPERS+"original.pdf")).exists())
        self.assertFalse((self.source / self.legacy_pdf).exists())
        self.assertTrue((self.papers / self.legacy_pdf).exists())
        self.assertTrue((self.source / "assets/visual-showcase/reference.svg").is_file())
        for report in self.reports:
            self.assertEqual(support.digest(self.output/report["file"]), report["sha256"])

    def test_clean_full_install_has_18_entries_resources_but_no_root_readme_or_pdf(self):
        result = installer.install(self.source, self.target)
        self.assertEqual(len(result["skills"]), 18)
        self.assertEqual(sorted(p.name for p in self.target.glob("ccf-*") if (p/"SKILL.md").exists()), SKILLS)
        for name in ("ccf-latex-templates/NeurIPS/template.tex", "ccf-latex-templates/CVPR/2027/main.tex", "ccf-latex-templates/CVPR/2027/template-source.json", "ccf-paper-to-exemplar/scripts/convert.py", "assets/visual-showcase/reference.svg"):
            self.assertTrue((self.target/name).is_file(), name)
        self.assertFalse((self.target/"README.md").exists())
        self.assertFalse((self.target/(support.PAPERS+"original.pdf")).exists())
        self.assertFalse((self.target/self.legacy_pdf).exists())

    def test_partial_install_completes_siblings_without_activating_their_skills(self):
        result = installer.install(self.source, self.target, ["ccf-paper-reviewer"])
        self.assertEqual(set(result["skills"]), support.REQUIRED | {"ccf-paper-reviewer"})
        for name in ("ccf-paper-writer/references/exemplars/papers/original.md", "ccf-paper-writer/scripts/convert.py", "ccf-paper-to-exemplar/scripts/convert.py"):
            self.assertTrue((self.target/name).is_file(), name)
        self.assertFalse((self.target/"ccf-paper-writer/SKILL.md").exists())
        self.assertFalse((self.target/"ccf-paper-to-exemplar/SKILL.md").exists())

    def test_each_individual_skill_has_resource_closure_without_extra_skill_activation(self):
        _, manifest = support.load_release(self.source)
        for skill in SKILLS:
            with self.subTest(skill=skill):
                skills, files = support.select_files(manifest, [skill])
                self.assertEqual(set(skills), support.REQUIRED | {skill})
                entries = {e["path"] for e in files}
                self.assertEqual({p.split("/")[0] for p in entries if p.endswith("/SKILL.md")}, set(skills))
                if skill in {"ccf-paper-writer", "ccf-project-scaffolder", "ccf-submission-checker"}:
                    self.assertTrue({"ccf-latex-templates/CVPR/2027/main.tex",
                                     "ccf-latex-templates/CVPR/2027/template-source.json"}.issubset(entries))
        installer.install(self.source, self.target, ["ccf-paper-to-exemplar"])
        for name in ("exemplar-style-analysis.md", "exemplars/index.md", "custom-format/default-user-format.md"):
            self.assertTrue((self.target/"ccf-paper-writer/references"/name).is_file(), name)
        self.assertFalse((self.target/"ccf-paper-writer/SKILL.md").exists())

    def test_default_build_excludes_untracked_files_and_records_source_identity(self):
        self.put("private-notes.md", "Untracked fixture, never a public release input")
        self.make_release()
        _, manifest = support.load_release(self.source)
        self.assertNotIn("private-notes.md", {e["path"] for e in manifest["files"]})
        self.assertEqual(manifest["source"], {"commit": None, "dirty": True, "file_selection": "tracked"})
        reports = builder.build(self.repo, self.output, tracked_only=False)
        with zipfile.ZipFile(self.output/reports[0]["file"]) as archive:
            self.assertTrue(any(name.endswith("/private-notes.md") for name in archive.namelist()))
            manifest = json.loads(archive.read("ccfa-skills-0.12.0-lean/"+support.MANIFEST))
            self.assertEqual(manifest["source"]["file_selection"], "tracked-and-untracked")

    def test_committed_build_records_commit_and_clean_worktree(self):
        subprocess.run(["git", "-C", str(self.repo), "add", "."], check=True)
        subprocess.run(["git", "-C", str(self.repo), "-c", "user.name=Fixture", "-c", "user.email=fixture@example.invalid",
                        "commit", "-qm", "fixture"], check=True)
        expected = subprocess.check_output(["git", "-C", str(self.repo), "rev-parse", "HEAD"], text=True).strip()
        self.make_release()
        _, manifest = support.load_release(self.source)
        self.assertEqual(manifest["source"], {"commit": expected, "dirty": False, "file_selection": "tracked"})

    def _interrupt_update(self, fresh=False):
        if not fresh:
            installer.install(self.source, self.target)
        for skill in ("ccf-common", "ccf-humanization"):
            self.put(skill+"/SKILL.md", "Updated "+skill+"\n")
        self.make_release("0.12.1")
        replace = installer.os.replace
        count = 0
        def interrupted(source, destination):
            nonlocal count
            if Path(destination).name == "SKILL.md":
                count += 1
                if count == 2:
                    raise OSError("Injected replacement failure")
            return replace(source, destination)
        with patch.object(installer.os, "replace", interrupted), self.assertRaisesRegex(OSError, "Injected"):
            installer.install(self.source, self.target)
        return support.read_json(self.target/support.RECEIPT)

    def test_interrupted_fresh_install_and_update_resume_from_durable_receipt(self):
        for fresh in (True, False):
            with self.subTest(fresh=fresh):
                self.target = self.directory/("fresh" if fresh else "update")
                pending = self._interrupt_update(fresh)
                self.assertIn("pending", pending)
                self.assertFalse((self.target/".ccfa-release-install.lock").exists())
                self.assertTrue(installer.install(self.source, self.target, dry_run=True)["resuming"])
                self.assertEqual(support.read_json(self.target/support.RECEIPT), pending)
                result = installer.install(self.source, self.target)
                self.assertTrue(result["resuming"])
                receipt = support.read_json(self.target/support.RECEIPT)
                self.assertNotIn("pending", receipt)
                self.assertEqual(receipt["version"], "0.12.1")
                self.assertTrue(all(support.digest(self.target/name) == entry["sha256"] for name, entry in receipt["files"].items()))
                self.assertFalse(list(self.target.rglob(".ccfa-install-*.tmp")))
                # Restore the original fixture so the next subcase is a real update.
                if fresh:
                    for skill in ("ccf-common", "ccf-humanization"):
                        self.put(skill+"/SKILL.md", "# "+skill+"\n")
                    self.make_release("0.12.0")

    def test_pending_update_preserves_intervening_user_edit_or_deletion(self):
        pending = self._interrupt_update()
        changed = self.target/"ccf-common/SKILL.md"
        changed.write_text("MY CONCURRENT EDIT", encoding="utf-8")
        with self.assertRaisesRegex(ValueError, "after an interrupted"):
            installer.install(self.source, self.target)
        self.assertEqual(changed.read_text(encoding="utf-8"), "MY CONCURRENT EDIT")
        self.assertEqual(support.read_json(self.target/support.RECEIPT), pending)
        changed.unlink()
        with self.assertRaisesRegex(ValueError, "after an interrupted"):
            installer.install(self.source, self.target)
        self.assertFalse(changed.exists())
        self.assertEqual(support.read_json(self.target/support.RECEIPT), pending)

    def test_pending_update_rejects_different_release_selection(self):
        pending = self._interrupt_update()
        with self.assertRaisesRegex(ValueError, "same release, skill selection"):
            installer.install(self.source, self.target, ["ccf-humanization"])
        self.assertEqual(support.read_json(self.target/support.RECEIPT), pending)

    def test_final_receipt_failure_is_resumable_after_all_files_were_replaced(self):
        installer.install(self.source, self.target)
        self.put("ccf-common/SKILL.md", "Updated common\n")
        self.make_release("0.12.1")
        write_receipt = installer._write_receipt
        def interrupted(target, value):
            if "pending" not in value:
                raise OSError("Injected final receipt failure")
            return write_receipt(target, value)
        with patch.object(installer, "_write_receipt", interrupted), self.assertRaisesRegex(OSError, "final receipt"):
            installer.install(self.source, self.target)
        result = installer.install(self.source, self.target)
        self.assertTrue(result["resuming"])
        self.assertEqual(result["updated_files"], 0)
        self.assertNotIn("pending", support.read_json(self.target/support.RECEIPT))

    def test_dry_run_creates_nothing_and_cli_works_from_the_extracted_package(self):
        result = subprocess.run([sys.executable, "-B", str(self.source/"tools/install_release.py"), "--source", str(self.source),
            "--target", str(self.target), "--skill", "ccf-paper-writer", "--dry-run"], capture_output=True, text=True, encoding="utf-8")
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertTrue(json.loads(result.stdout)["dry_run"])
        self.assertFalse(self.target.exists())

    def test_optional_papers_can_be_added_later_or_with_the_lean_install(self):
        with self.assertRaisesRegex(ValueError, "matching lean"):
            installer.install(self.papers, self.target)
        installer.install(self.source, self.target, ["ccf-paper-writer"])
        installer.install(self.papers, self.target)
        self.assertEqual((self.target/(support.PAPERS+"original.pdf")).read_bytes(), b"%PDF-1.4 fixture\n")
        self.assertEqual((self.target/self.legacy_pdf).read_bytes(), b"%PDF-1.4 legacy fixture\n")
        other = self.directory/"second installation"
        installer.install(self.source, other, ["ccf-paper-writer"], papers=self.papers)
        self.assertTrue((other/(support.PAPERS+"original.pdf")).is_file())
        self.assertTrue((other/self.legacy_pdf).is_file())

    def test_updates_replace_only_unchanged_managed_files_and_keep_extra_user_files(self):
        installer.install(self.source, self.target, ["ccf-paper-writer"])
        extra = self.target/"ccf-paper-writer/personal.txt"; extra.write_text("KEEP", encoding="utf-8")
        prefs = self.target/".ccfa/preferences.json"; prefs.parent.mkdir(); prefs.write_text('{"version":1}', encoding="utf-8")
        self.put("ccf-paper-writer/SKILL.md", "Updated writer\n")
        self.make_release("0.12.1")
        installer.install(self.source, self.target, ["ccf-paper-writer"])
        self.assertEqual((self.target/"ccf-paper-writer/SKILL.md").read_text(encoding="utf-8"), "Updated writer\n")
        self.assertEqual(extra.read_text(encoding="utf-8"), "KEEP")
        self.assertEqual(prefs.read_text(encoding="utf-8"), '{"version":1}')

    def test_retired_files_follow_selected_resource_closure_and_preserve_papers_and_extras(self):
        name = "ccf-paper-writer/references/exemplar-style-analysis.md"
        installer.install(self.source, self.target, papers=self.papers)
        extra = self.target / "ccf-paper-writer/references/personal.md"
        extra.write_text("KEEP", encoding="utf-8")
        (self.repo / name).unlink()
        self.make_release("0.12.1")
        # An unrelated partial update does not retire the writer's files.
        installer.install(self.source, self.target, ["ccf-humanization"])
        self.assertTrue((self.target / name).is_file())
        # Reviewer selects writer references as resources, without its skill.
        preview = installer.install(self.source, self.target, ["ccf-paper-reviewer"], dry_run=True)
        self.assertEqual(preview["retired_paths"], [name])
        self.assertTrue((self.target / name).is_file())
        result = installer.install(self.source, self.target, ["ccf-paper-reviewer"])
        self.assertEqual(result["retired_files"], 1)
        self.assertFalse((self.target / name).exists())
        self.assertNotIn(name, support.read_json(self.target / support.RECEIPT)["files"])
        self.assertEqual(extra.read_text(encoding="utf-8"), "KEEP")
        self.assertTrue((self.target / (support.PAPERS + "original.pdf")).is_file())
        self.assertTrue((self.target / self.legacy_pdf).is_file())

    def test_personal_edit_to_retired_file_rejects_update_before_any_mutation(self):
        name = "ccf-paper-writer/references/exemplar-style-analysis.md"
        installer.install(self.source, self.target)
        (self.target / name).write_text("PERSONAL", encoding="utf-8")
        (self.repo / name).unlink()
        self.put("ccf-common/SKILL.md", "New common")
        self.make_release("0.12.1")
        receipt = (self.target / support.RECEIPT).read_bytes()
        common = (self.target / "ccf-common/SKILL.md").read_bytes()
        with self.assertRaisesRegex(ValueError, "personal edit to a retired file"):
            installer.install(self.source, self.target)
        self.assertEqual((self.target / name).read_text(encoding="utf-8"), "PERSONAL")
        self.assertEqual((self.target / support.RECEIPT).read_bytes(), receipt)
        self.assertEqual((self.target / "ccf-common/SKILL.md").read_bytes(), common)

    def test_retirement_resumes_after_receipt_failure_and_preserves_intervening_edit(self):
        name = "ccf-paper-writer/references/exemplar-style-analysis.md"
        installer.install(self.source, self.target)
        (self.repo / name).unlink()
        self.make_release("0.12.1")
        write_receipt = installer._write_receipt
        def interrupted(target, value):
            if "pending" not in value:
                raise OSError("Injected retirement receipt failure")
            return write_receipt(target, value)
        with patch.object(installer, "_write_receipt", interrupted), self.assertRaisesRegex(OSError, "retirement receipt"):
            installer.install(self.source, self.target)
        self.assertFalse((self.target / name).exists())
        (self.target / name).write_text("NEW PERSONAL EDIT", encoding="utf-8")
        with self.assertRaisesRegex(ValueError, "personal edit to a retired file"):
            installer.install(self.source, self.target)
        (self.target / name).unlink()
        result = installer.install(self.source, self.target)
        self.assertTrue(result["resuming"])
        self.assertEqual(result["retired_files"], 0)
        receipt = support.read_json(self.target / support.RECEIPT)
        self.assertNotIn("pending", receipt)
        self.assertNotIn(name, receipt["files"])

    def test_personal_edit_or_unmanaged_collision_rejects_the_entire_preflight(self):
        installer.install(self.source, self.target)
        target = self.target/"ccf-paper-writer/SKILL.md"; target.write_text("MY EDIT", encoding="utf-8")
        before = (self.target/support.RECEIPT).read_bytes()
        with self.assertRaisesRegex(ValueError, "personal or unmanaged"):
            installer.install(self.source, self.target)
        self.assertEqual(target.read_text(encoding="utf-8"), "MY EDIT")
        self.assertEqual((self.target/support.RECEIPT).read_bytes(), before)
        other = self.directory/"unmanaged"; (other/"ccf-common").mkdir(parents=True)
        (other/"ccf-common/SKILL.md").write_text("PERSONAL", encoding="utf-8")
        with self.assertRaises(ValueError): installer.install(self.source, other)
        self.assertFalse((other/support.RECEIPT).exists())

    def test_corrupt_file_or_manifest_is_rejected_before_target_creation(self):
        target = self.source/"ccf-common/SKILL.md"; original=target.read_bytes(); target.write_bytes(b"tampered")
        with self.assertRaisesRegex(ValueError, "manifest"): installer.install(self.source, self.target)
        self.assertFalse(self.target.exists()); target.write_bytes(original)
        path = self.source/support.MANIFEST
        value = support.read_json(path); value["files"][0]["sha256"]="bad"
        path.write_text(json.dumps(value), encoding="utf-8")
        with self.assertRaises(ValueError): installer.install(self.source, self.target)
        self.assertFalse(self.target.exists())

    def test_missing_sibling_resource_and_mismatched_papers_are_rejected(self):
        path=self.source/support.MANIFEST; original=support.read_json(path)
        manifest=copy.deepcopy(original)
        manifest["files"]=[e for e in manifest["files"] if not e["path"].startswith("ccf-paper-to-exemplar/scripts/")]
        path.write_text(json.dumps(manifest),encoding="utf-8")
        with self.assertRaisesRegex(ValueError,"required sibling"):
            installer.install(self.source,self.target,["ccf-paper-reviewer"])
        self.assertFalse(self.target.exists())
        path.write_text(json.dumps(original),encoding="utf-8")
        paper_path=self.papers/support.MANIFEST; paper=support.read_json(paper_path)
        paper.update(version="0.12.1",release_id="ccfa-skills-0.12.1")
        paper_path.write_text(json.dumps(paper),encoding="utf-8")
        with self.assertRaisesRegex(ValueError,"must match"):
            installer.install(self.source,self.target,papers=self.papers)
        self.assertFalse(self.target.exists())

    def test_path_traversal_case_aliases_and_symbolic_links_are_rejected(self):
        for value in ("../outside", "/absolute", "C:/outside", "a\\..\\outside", "a/./b", "a/NUL.txt", "a//b"):
            with self.subTest(path=value), self.assertRaises(ValueError): support.relative_path(value)
        path=self.source/support.MANIFEST; manifest=support.read_json(path)
        alias=copy.deepcopy(manifest["files"][0]);alias["path"]=alias["path"].upper();manifest["files"].append(alias)
        path.write_text(json.dumps(manifest),encoding="utf-8")
        with self.assertRaises(ValueError): installer.install(self.source,self.target)
        actual=Path.lstat
        link=self.source/"ccf-common/SKILL.md"
        def simulated(candidate,*args,**kwargs):
            return SimpleNamespace(st_mode=stat.S_IFLNK,st_file_attributes=0) if candidate==link else actual(candidate,*args,**kwargs)
        with patch.object(Path,"lstat",simulated),self.assertRaisesRegex(ValueError,"Symlinks"):
            support.no_links(link)


if __name__ == "__main__": unittest.main()
