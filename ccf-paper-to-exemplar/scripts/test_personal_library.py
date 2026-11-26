"""Exercise usable personal-card registration, reuse and invalidation."""
from __future__ import annotations

import json
import contextlib
import io
import os
from pathlib import Path
import tempfile
import sys
import unittest
from unittest.mock import patch

import convert
import personal_library as library


CARD = """# 机制与动机范例
Source: A supplied paper, accepted version, Section 1 paragraph 2.

## Introduction Moves
Source observation: the passage derives a computational consequence from the stated dependency.

## Reusable Techniques
Adaptation advice: explain the actual dependency before its consequence.

## Do-Not-Copy Boundary
Use the target work's own mechanism and findings.
"""


class PersonalLibraryTests(unittest.TestCase):
    def setUp(self):
        self.temporary = tempfile.TemporaryDirectory(prefix="ccfa-personal-exemplars-")
        self.addCleanup(self.temporary.cleanup)
        self.root = Path(self.temporary.name)
        self.project = self.root / "项目"
        self.project.mkdir()
        self.card = self.root / "动机卡片.md"
        self.source = self.root / "原始论文.md"
        self.card.write_text(CARD, encoding="utf-8")
        self.source.write_text("Original operation—dependency—and its consequence. 中文原文。", encoding="utf-8")
        self.environment = patch.dict(os.environ, {"CODEX_HOME": str(self.root / "codex-home")})
        self.environment.start()
        self.addCleanup(self.environment.stop)

    def register(self, **changes):
        values = {"key": "paper-a-motivation", "card": self.card, "source": self.source,
                  "source_id": "paper-a", "source_version": "accepted", "locations": ["Section 1 paragraph 2"],
                  "functions": ["motivation"], "coverage": "passage", "project": self.project}
        values.update(changes)
        return library.register(**values)

    def test_project_registration_keeps_original_files_and_source_locations(self):
        before = {p: p.read_bytes() for p in (self.card, self.source)}
        result = self.register()
        self.assertEqual(result["action"], "registered")
        self.assertEqual(result["entry"]["source"]["version"], "accepted")
        self.assertEqual(result["entry"]["source"]["locations"], ["Section 1 paragraph 2"])
        self.assertEqual(result["entry"]["coverage"], "passage")
        self.assertEqual({p: p.read_bytes() for p in before}, before)
        self.assertEqual([p.name for p in (self.project / ".ccfa/exemplars").iterdir()], ["library.json"])
        self.assertFalse((self.root / "codex-home").exists())

    def test_unfinished_and_empty_cards_cannot_enter_library(self):
        for content in (CARD + "\n[ANALYZE] remaining source observation\n",
                        CARD.replace("Adaptation advice: explain the actual dependency before its consequence.", ""),
                        CARD.replace("Source observation: the passage derives a computational consequence from the stated dependency.", "")):
            self.card.write_text(content, encoding="utf-8")
            with self.assertRaises(library.LibraryError):
                self.register()
            self.assertFalse((self.project / ".ccfa").exists())

    def test_missing_explicit_scope_and_card_as_original_are_rejected(self):
        with self.assertRaises(library.LibraryError):
            self.register(project=None)
        with self.assertRaises(library.LibraryError):
            self.register(source=self.card)

    def test_repeat_registration_is_noop_and_version_update_has_one_entry(self):
        first = self.register()
        with patch.object(library, "_publish", side_effect=AssertionError("unchanged registration rewrote library")):
            self.assertEqual(self.register()["action"], "unchanged")
        updated = self.register(source_version="arXiv v2")
        self.assertEqual(updated["action"], "updated")
        saved = json.loads(Path(first["library"]).read_text(encoding="utf-8"))
        self.assertEqual(list(saved["entries"]), ["paper-a-motivation"])
        self.assertEqual(saved["entries"]["paper-a-motivation"]["source"]["version"], "arXiv v2")

    def test_same_id_does_not_silently_replace_another_paper(self):
        first = self.register()
        original = Path(first["library"]).read_bytes()
        with self.assertRaises(library.LibraryError):
            self.register(source_id="different-paper")
        self.assertEqual(Path(first["library"]).read_bytes(), original)
        self.assertEqual(self.register(source_id="different-paper", replace_source=True)["action"], "updated")

    def test_query_reads_metadata_without_loading_card_or_original(self):
        self.register()
        actual_read = Path.read_text

        def metadata_only(path, *args, **kwargs):
            if path in (self.card, self.source):
                raise AssertionError("query loaded paper or card contents")
            return actual_read(path, *args, **kwargs)

        with patch.object(Path, "read_text", metadata_only), patch.object(Path, "read_bytes", side_effect=AssertionError("query read full file bytes")):
            result = library.query(project=self.project, functions=["motivation"])
        self.assertEqual(result["total_matches"], 1)
        self.assertEqual(result["matches"][0]["source"]["path"], str(self.source.resolve()))
        self.assertNotIn("text", result["matches"][0])
        self.assertEqual(library.query(project=self.project, functions=["evidence"])["matches"], [])

    def test_changed_or_missing_original_invalidates_prior_analysis(self):
        self.register()
        self.source.write_text("Changed original source and a different explanation.", encoding="utf-8")
        result = library.query(project=self.project, text="motivation")
        self.assertEqual(result["matches"], [])
        self.assertEqual(result["unavailable"][0]["reason"], "source changed")
        stale = result["unavailable"][0]
        self.assertFalse(stale["analysis_current"])
        self.assertEqual(stale["library"], str(library.library_path(project=self.project)))
        self.assertEqual(stale["card"]["path"], str(self.card.resolve()))
        self.assertEqual(stale["source"], {"path": str(self.source.resolve()), "id": "paper-a", "version": "accepted",
                                          "locations": ["Section 1 paragraph 2"]})
        self.register(source_version="rechecked")
        self.assertEqual(library.query(project=self.project)["total_matches"], 1)
        self.card.unlink()
        self.assertEqual(library.query(project=self.project)["unavailable"][0]["reason"], "card missing")

    def test_project_entry_shadows_personal_entry_and_empty_query_writes_nothing(self):
        self.assertEqual(library.query(project=self.project)["matches"], [])
        self.assertFalse((self.project / ".ccfa").exists())
        self.assertFalse((self.root / "codex-home").exists())
        self.register(project=None, scope="user", title="Personal entry")
        self.register(title="Project entry")
        self.assertEqual(library.query(project=self.project)["matches"][0]["title"], "Project entry")
        self.assertEqual(library.query()["matches"][0]["title"], "Personal entry")

    def test_failed_publish_preserves_the_previous_library_and_cleans_scratch(self):
        first = self.register()
        path = Path(first["library"])
        original = path.read_bytes()
        with patch.object(library.os, "replace", side_effect=OSError("simulated interrupted publication")):
            with self.assertRaises(OSError):
                self.register(source_version="changed")
        self.assertEqual(path.read_bytes(), original)
        self.assertEqual([p.name for p in path.parent.iterdir()], ["library.json"])

    def test_scoped_skeleton_and_original_punctuation_are_preserved(self):
        skeleton = convert.make_card({"title": "Paper", "venue": "ICLR"}, ["introduction", "introduction"])
        self.assertIn("## Introduction Moves", skeleton)
        self.assertEqual(skeleton.count("## Introduction Moves"), 1)
        self.assertNotIn("## Abstract Moves", skeleton)
        self.assertNotIn("## Evidence Moves", skeleton)
        self.assertIn("[ANALYZE]", skeleton)
        self.assertEqual(convert.clean_text("Original—explanation–condition. 中文破折号。"), "Original—explanation–condition. 中文破折号。")

    def test_whole_paper_registration_retains_all_eight_analysis_sections(self):
        with self.assertRaises(library.LibraryError):
            self.register(coverage="paper")
        whole = CARD
        for heading in ("Story Pattern", "Abstract Moves", "Method Moves", "Evidence Moves", "Citation Patterns"):
            whole += "\n## " + heading + "\nSource observation: the inspected section supplies the relevant explanation.\n"
        self.card.write_text(whole, encoding="utf-8")
        self.assertEqual(self.register(coverage="paper")["entry"]["coverage"], "paper")
        skeleton = convert.make_card({"title": "Paper"})
        for heading in ("Story Pattern", "Abstract Moves", "Introduction Moves", "Method Moves", "Evidence Moves", "Citation Patterns", "Reusable Techniques", "Do-Not-Copy Boundary"):
            self.assertIn("## " + heading, skeleton)

    def test_explicit_default_selection_prioritizes_only_matching_tasks(self):
        self.register(key="a-other", functions=["motivation"])
        self.register(key="z-preferred", functions=["motivation"])
        self.register(key="evidence-only", functions=["evidence"])
        library.set_defaults(keys=["z-preferred", "evidence-only"], project=self.project)
        result = library.query(project=self.project, functions=["motivation"])
        self.assertEqual([entry["id"] for entry in result["matches"]], ["z-preferred", "a-other"])
        self.assertTrue(result["matches"][0]["is_default"])
        self.assertEqual(result["defaults_scope"], "project")
        self.assertEqual(library.query(project=self.project, text="does-not-match")["matches"], [])

    def test_default_inheritance_override_clear_and_restore(self):
        self.register(project=None, scope="user", key="personal")
        self.register(key="project")
        library.set_defaults(keys=["personal"], scope="user")
        self.assertEqual(library.query(project=self.project)["defaults_scope"], "user")
        self.assertEqual(library.query(project=self.project)["matches"][0]["id"], "personal")
        library.set_defaults(keys=["project"], project=self.project)
        self.assertEqual(library.query(project=self.project)["matches"][0]["id"], "project")
        self.assertEqual(library.query()["matches"][0]["id"], "personal")
        library.set_defaults(keys=[], project=self.project)
        self.assertFalse(any(entry["is_default"] for entry in library.query(project=self.project)["matches"]))
        library.set_defaults(project=self.project, inherit=True)
        self.assertEqual(library.query(project=self.project)["defaults_scope"], "user")

    def test_registration_preserves_defaults_and_preferences(self):
        first = self.register()
        library.set_defaults(keys=["paper-a-motivation"], project=self.project)
        self.register(key="new-card")
        self.register(source_version="rechecked")
        saved = json.loads(Path(first["library"]).read_text(encoding="utf-8"))
        self.assertEqual(saved["defaults"], ["paper-a-motivation"])
        self.assertFalse((self.project / ".ccfa/preferences.json").exists())
        self.assertFalse((self.root / "codex-home").exists())

    def test_unregistered_or_stale_default_does_not_change_previous_selection(self):
        result = self.register()
        library.set_defaults(keys=["paper-a-motivation"], project=self.project)
        path = Path(result["library"])
        original = path.read_bytes()
        with self.assertRaises(library.LibraryError):
            library.set_defaults(keys=["unknown-id"], project=self.project)
        self.assertEqual(path.read_bytes(), original)
        self.source.write_text("Changed original.", encoding="utf-8")
        with self.assertRaises(library.LibraryError):
            library.set_defaults(keys=["paper-a-motivation"], project=self.project)
        self.assertEqual(path.read_bytes(), original)
        self.assertEqual(library.query(project=self.project)["matches"], [])

    def test_legacy_converter_flags_preserve_completed_card_and_full_text(self):
        pdf = self.root / "来源论文.pdf"
        pdf.write_bytes(b"fixture; extraction is supplied by the test")
        cards, cache = self.root / "cards", self.root / "cache"
        cards.mkdir()
        existing = cards / "来源论文.md"
        existing.write_text(CARD, encoding="utf-8")
        source = "## Page 1\n\nAbstract\nOriginal—explanation–condition. 中文原文。\n\n## Page 2\n\nMethod and proof."
        argv = ["convert.py", str(pdf), "--output-dir", str(cards), "--full-text", "--full-text-dir", str(cache), "--set-default"]
        output = io.StringIO()
        with patch.object(sys, "argv", argv), patch.object(convert, "_check_pymupdf", return_value=None), patch.object(convert, "extract_text", return_value=source), contextlib.redirect_stdout(output):
            self.assertEqual(convert.main(), 0)
        self.assertEqual(existing.read_text(encoding="utf-8"), CARD)
        extracted = (cache / "来源论文.full.md").read_text(encoding="utf-8")
        self.assertIn("## Page 1", extracted)
        self.assertIn("## Page 2", extracted)
        self.assertIn("Original—explanation–condition. 中文原文。", extracted)
        self.assertIn("set-default --project", output.getvalue())
        self.assertFalse((self.project / ".ccfa").exists())


if __name__ == "__main__":
    unittest.main()
