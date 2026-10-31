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
            "ccf-paper-writer/scripts/convert.py": "# legacy bridge\n",
            "ccf-paper-to-exemplar/scripts/convert.py": "# shared converter\n",
            "ccf-latex-templates/NeurIPS/template.tex": "Template retained",
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
        for name in ("ccf-latex-templates/NeurIPS/template.tex", "ccf-paper-to-exemplar/scripts/convert.py", "assets/visual-showcase/reference.svg"):
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
