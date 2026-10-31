"""Filesystem regression tests for bounded manuscript patches (stdlib only)."""

import copy
import hashlib
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch as mock_patch

import manuscript_patch as mp


class ManuscriptPatchTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory(prefix="ccfa-manuscript-")
        self.addCleanup(self.tmp.cleanup)
        self.root = Path(self.tmp.name).resolve()
        self.path = self.root / "论文.md"

    def write(self, text, suffix=".md", bom=False):
        self.path = self.root / ("论文" + suffix)
        data = text.encode("utf-8")
        self.path.write_bytes((mp._BOM if bom else b"") + data)
        return mp.inspect_manuscript(self.path)

    def packet(self, targets=None, dependencies=None):
        inventory = mp.inspect_manuscript(self.path)
        return {"schema_version": 1,
                "manuscript": {"path": str(self.path), "sha256": inventory["sha256"]},
                "targets": targets or [inventory["sections"][0]["id"]],
                "sections": inventory["sections"], "dependencies": dependencies or []}

    def apply(self, packet, *edits):
        return mp.apply_patch(packet, {"base_sha256": packet["manuscript"]["sha256"], "edits": list(edits)})

    def rejected(self, packet, edits, pattern=None):
        before = self.path.read_bytes()
        files = set(self.root.iterdir())
        with self.assertRaisesRegex(mp.ManuscriptPatchError, pattern or ".*"):
            self.apply(packet, *edits)
        self.assertEqual(self.path.read_bytes(), before)
        self.assertEqual(set(self.root.iterdir()), files)

    def test_chinese_bom_crlf_roundtrip_and_unchanged_bytes(self):
        text = "前言。\r\n# 方法\r\n我们建模关系。\r\n# 结论\r\n保留这一段。\r\n"
        inventory = self.write(text, bom=True)
        self.assertEqual([entry["id"] for entry in inventory["sections"]], ["preamble", "方法", "结论"])
        self.assertEqual(inventory["path"], str(self.path))
        for entry in inventory["sections"]:
            self.assertEqual(text[entry["start"]:entry["end"]], entry["text"])
        packet = self.packet(["方法"])
        result = self.apply(packet, {"section_id": "方法", "before": "我们建模关系。", "after": "我们建模变量之间的关系。"})
        expected = mp._BOM + text.replace("我们建模关系。", "我们建模变量之间的关系。").encode("utf-8")
        self.assertEqual(self.path.read_bytes(), expected)
        self.assertEqual(result["after_sha256"], hashlib.sha256(expected).hexdigest())
        self.assertEqual(result["before_sha256"], packet["manuscript"]["sha256"])
        self.assertEqual(result["changed_sections"], ["方法"])
        self.assertTrue(result["changed"])
        self.assertEqual(set(self.root.iterdir()), {self.path})

    def test_markdown_fences_atx_setext_and_duplicate_ids(self):
        text = "# Intro\nA.\n```python\n# fake\nFake\n---\n```\n## Intro\nB.\n~~~~\n# fake too\n~~~\n~~~~\nMethod\n======\nC.\n# Intro-2\nD.\n"
        inventory = self.write(text)
        self.assertEqual([entry["id"] for entry in inventory["sections"]], ["intro", "intro-2", "method", "intro-2-2"])
        self.assertEqual(inventory["sections"][1]["heading"], "Intro")
        self.assertEqual(inventory["sections"][2]["text"], "Method\n======\nC.\n")
        self.assertEqual("".join(entry["text"] for entry in inventory["sections"]), text)

    def test_latex_preamble_nested_title_and_ignored_comments_verbatim(self):
        text = ("\\documentclass{article}\n% \\section{Fake}\n\\begin{document}\n"
                "\\chapter*{Intro}\nA.\n\\section[Short {x}]{Method {and} \\textbf{detail}}\n"
                "\\begin{verbatim}\n\\section{Ignored}\n\\end{verbatim}\n"
                "\\verb|\\section{also ignored}|\n"
                "\\subsection{Analysis}\n真实内容。 % \\chapter{Fake}\n\\end{document}\n")
        inventory = self.write(text, ".tex", bom=True)
        self.assertEqual([entry["heading"] for entry in inventory["sections"]], ["", "Intro", r"Method {and} \textbf{detail}", "Analysis"])
        self.assertEqual(inventory["sections"][0]["id"], "preamble")
        target = inventory["sections"][-1]["id"]
        result = self.apply(self.packet([target]), {"section_id": target, "before": "真实内容。", "after": "关系来自联合建模。"})
        self.assertEqual(result["changed_sections"], [target])
        self.assertIn("关系来自联合建模。", self.path.read_bytes().decode("utf-8-sig"))

    def test_body_only_and_empty_documents(self):
        inventory = self.write("正文，没有标题。\n")
        self.assertEqual(inventory["sections"], [{"id": "body", "heading": "", "start": 0, "end": 9, "text": "正文，没有标题。\n"}])
        inventory = self.write("")
        self.assertEqual(inventory["sections"][0]["start"], 0)
        self.assertEqual(inventory["sections"][0]["end"], 0)

    def test_stale_packet_and_mismatched_patch_base(self):
        self.write("# Main\nOriginal.\n")
        packet = self.packet()
        self.path.write_bytes(b"# Main\nNew external version.\n")
        self.rejected(packet, [{"section_id": "main", "before": "Original.", "after": "New."}], "manuscript changed")
        current = self.packet()
        before = self.path.read_bytes()
        with self.assertRaisesRegex(mp.ManuscriptPatchError, "patch base"):
            mp.apply_patch(current, {"base_sha256": "0" * 64, "edits": []})
        self.assertEqual(self.path.read_bytes(), before)

    def test_unauthorized_cross_section_empty_and_ambiguous_matches(self):
        self.write("# One\naaa\n# Two\nbeta\n")
        packet = self.packet(["one"])
        cases = [
            {"section_id": "two", "before": "beta", "after": "new"},
            {"section_id": "one", "before": "aaa\n# Two", "after": "new"},
            {"section_id": "one", "before": "", "after": "new"},
            {"section_id": "one", "before": "aa", "after": "new"},
        ]
        for edit in cases:
            with self.subTest(edit=edit):
                self.rejected(packet, [edit])

    def test_overlap_rejected_and_nonoverlapping_original_offsets_applied(self):
        self.write("# Main\nabcdef\n")
        packet = self.packet()
        self.rejected(packet, [
            {"section_id": "main", "before": "abc", "after": "x"},
            {"section_id": "main", "before": "bcd", "after": "y"},
        ], "overlapping")
        result = self.apply(packet,
            {"section_id": "main", "before": "ab", "after": "longer"},
            {"section_id": "main", "before": "ef", "after": "short"})
        self.assertEqual(self.path.read_bytes(), b"# Main\nlongercdshort\n")
        self.assertEqual(result["changed_sections"], ["main"])

    def test_same_text_in_other_section_is_untouched(self):
        self.write("# One\ncommon\n# Two\ncommon\n")
        self.apply(self.packet(["one"]), {"section_id": "one", "before": "common", "after": "first only"})
        self.assertEqual(self.path.read_bytes(), b"# One\nfirst only\n# Two\ncommon\n")

    def test_dependency_changes_missing_files_and_relative_paths(self):
        self.write("# Main\nOriginal.\n")
        dependency = self.root / "table.csv"
        dependency.write_bytes(b"x,y\n1,2\n")
        entry = {"id": "table", "path": dependency.name, "sha256": hashlib.sha256(dependency.read_bytes()).hexdigest(), "used_by": ["main", "figure-1"]}
        packet = self.packet(dependencies=[entry])
        edit = {"section_id": "main", "before": "Original.", "after": "Updated."}
        dependency.write_bytes(b"x,y\n3,4\n")
        self.rejected(packet, [edit], "dependency changed")
        dependency.unlink()
        self.rejected(packet, [edit], "regular file")
        dependency.write_bytes(b"x,y\n1,2\n")
        self.assertTrue(self.apply(packet, edit)["changed"])

    def test_partial_inventory_validated_but_not_trusted_for_scope(self):
        self.write("# One\nalpha\n# Two\nbeta\n")
        packet = self.packet(["two"])
        packet["sections"] = [packet["sections"][1]]
        self.apply(packet, {"section_id": "two", "before": "beta", "after": "new"})
        packet = self.packet(["one"])
        packet["sections"][0]["end"] += 1
        self.rejected(packet, [], "stale inventory")

    def test_multiple_source_windows_can_share_dependency_file(self):
        self.write("# Main\nOriginal.\n")
        source = self.root / "source.md"
        source.write_bytes(b"source text")
        digest = hashlib.sha256(source.read_bytes()).hexdigest()
        dependencies = [
            {"id": "window-1", "path": str(source), "sha256": digest, "used_by": ["main"]},
            {"id": "window-2", "path": source.name, "sha256": digest, "used_by": ["main"]},
        ]
        packet = self.packet(dependencies=dependencies)
        self.assertEqual(len(mp._dependencies(packet, self.path)), 1)
        self.apply(packet)
        packet["dependencies"][1]["sha256"] = "0" * 64
        self.rejected(packet, [], "inconsistent hashes")

    def test_dependency_scope_limits_hash_checks_and_unknown_scope_still_gates(self):
        self.write("# One\nalpha\n# Two\nbeta\n")
        source = self.root / "other-section.md"
        source.write_bytes(b"old source")
        digest = hashlib.sha256(source.read_bytes()).hexdigest()
        dependency = {"id": "other-source", "path": str(source), "sha256": digest, "used_by": ["two"]}
        packet = self.packet(["one"], [dependency])
        source.write_bytes(b"updated other section source")
        result = self.apply(packet, {"section_id": "one", "before": "alpha", "after": "new alpha"})
        self.assertEqual(result["changed_sections"], ["one"])
        for used_by in (["one"], []):
            dependency["used_by"] = used_by
            packet = self.packet(["one"], [dependency])
            with self.subTest(used_by=used_by):
                self.rejected(packet, [], "dependency changed")

    def test_shared_dependency_any_relevant_window_gates_hash(self):
        self.write("# One\nalpha\n# Two\nbeta\n")
        source = self.root / "shared-source.md"
        source.write_bytes(b"old")
        digest = hashlib.sha256(source.read_bytes()).hexdigest()
        dependencies = [
            {"id": "unrelated-window", "path": str(source), "sha256": digest, "used_by": ["two"]},
            {"id": "relevant-window", "path": str(source), "sha256": digest, "used_by": ["one"]},
        ]
        packet = self.packet(["one"], dependencies)
        source.write_bytes(b"new")
        self.rejected(packet, [], "dependency changed")

    def test_deleted_unrelated_source_does_not_block_target_patch(self):
        self.write("# One\nalpha\n# Two\nbeta\n")
        source = self.root / "other-section.md"
        source.write_bytes(b"source for section two")
        dependency = {"id": "other-source", "path": str(source), "sha256": hashlib.sha256(source.read_bytes()).hexdigest(), "used_by": ["two"]}
        packet = self.packet(["one"], [dependency])
        source.unlink()
        self.assertTrue(self.apply(packet, {"section_id": "one", "before": "alpha", "after": "updated alpha"})["changed"])
        dependency["used_by"] = []
        self.rejected(self.packet(["one"], [dependency]), [], "regular file")

    def test_readonly_review_packet_cannot_apply_patch_or_noop(self):
        self.write("# Main\nOriginal.\n")
        packet = self.packet()
        packet["operation"] = "review"
        for edits in ([], [{"section_id": "main", "before": "Original.", "after": "Changed."}]):
            with self.subTest(edits=edits):
                self.rejected(packet, edits, "read-only")
        packet["operation"] = "write"
        self.assertFalse(self.apply(packet)["changed"])
        packet["operation"] = "unknown"
        self.rejected(packet, [], "operation")

    def test_existing_lock_is_preserved(self):
        self.write("# Main\nOriginal.\n")
        lock = self.path.with_name(f".{self.path.name}.ccfa-patch.lock")
        lock.write_bytes(b"other owner")
        self.rejected(self.packet(), [], "locked")
        self.assertEqual(lock.read_bytes(), b"other owner")

    def test_noops_do_not_replace_file(self):
        self.write("# Main\r\nOriginal.\r\n", bom=True)
        packet = self.packet()
        for edits in ([], [{"section_id": "main", "before": "Original.", "after": "Original."}]):
            with self.subTest(edits=edits), mock_patch.object(mp.os, "replace") as replace:
                result = self.apply(packet, *edits)
                self.assertFalse(result["changed"])
                self.assertEqual(result["changed_sections"], [])
                self.assertEqual(result["before_sha256"], result["after_sha256"])
                replace.assert_not_called()
        self.assertEqual(set(self.root.iterdir()), {self.path})

    def test_replace_failure_cleans_owned_temp_and_lock(self):
        self.write("# Main\nOriginal.\n")
        original = self.path.read_bytes()
        with mock_patch.object(mp.os, "replace", side_effect=OSError("simulated failed replace")):
            with self.assertRaises(OSError):
                self.apply(self.packet(), {"section_id": "main", "before": "Original.", "after": "Changed."})
        self.assertEqual(self.path.read_bytes(), original)
        self.assertEqual(set(self.root.iterdir()), {self.path})

    def test_dependency_rechecked_before_replace(self):
        self.write("# Main\nOriginal.\n")
        dependency = self.root / "results.csv"
        dependency.write_bytes(b"old")
        entry = {"id": "results", "path": str(dependency), "sha256": hashlib.sha256(b"old").hexdigest(), "used_by": ["main"]}
        packet = self.packet(dependencies=[entry])
        check = mp._check_dependencies
        calls = 0

        def alter_after_first(dependencies):
            nonlocal calls
            check(dependencies)
            calls += 1
            if calls == 1:
                dependency.write_bytes(b"new")

        with mock_patch.object(mp, "_check_dependencies", side_effect=alter_after_first):
            self.rejected(packet, [{"section_id": "main", "before": "Original.", "after": "Changed."}], "dependency changed")
        self.assertEqual(calls, 1)

    def test_unknown_format_invalid_utf8_and_invalid_latex(self):
        self.path = self.root / "notes.txt"
        self.path.write_bytes(b"# Main\ntext")
        with self.assertRaisesRegex(mp.ManuscriptPatchError, "supported manuscript"):
            mp.inspect_manuscript(self.path)
        self.path = self.root / "broken.md"
        self.path.write_bytes(b"\xff\xfe")
        with self.assertRaisesRegex(mp.ManuscriptPatchError, "strict UTF-8"):
            mp.inspect_manuscript(self.path)
        for text in (r"\section{Unclosed", r"\section\dynamic", "\\begin{verbatim}\ntext", r"\newcommand{\dynamic}{\section{Generated}}"):
            self.path = self.root / "broken.tex"
            self.path.write_text(text, encoding="utf-8")
            with self.subTest(text=text), self.assertRaises(mp.ManuscriptPatchError):
                mp.inspect_manuscript(self.path)

    def test_symlink_manuscript_and_dependency_rejected(self):
        self.write("# Main\nOriginal.\n")
        link = self.root / "linked.md"
        try:
            link.symlink_to(self.path)
        except (OSError, NotImplementedError):
            self.skipTest("symlinks unavailable for this user")
        with self.assertRaisesRegex(mp.ManuscriptPatchError, "symbolic links"):
            mp.inspect_manuscript(link)
        packet = self.packet(dependencies=[{"id": "linked", "path": str(link), "sha256": hashlib.sha256(self.path.read_bytes()).hexdigest(), "used_by": ["main"]}])
        self.rejected(packet, [], "symbolic links")

    def test_symlink_detection_without_platform_privileges(self):
        self.write("# Main\nOriginal.\n")
        original_is_symlink = Path.is_symlink

        def marked(path):
            return path == self.path or original_is_symlink(path)

        with mock_patch.object(Path, "is_symlink", marked):
            with self.assertRaisesRegex(mp.ManuscriptPatchError, "symbolic links"):
                mp.inspect_manuscript(self.path)

    def test_external_manuscript_change_before_replace_is_preserved(self):
        self.write("# Main\nOriginal.\n")
        packet = self.packet()
        original_check = mp._check_dependencies
        calls = 0

        def mutate(dependencies):
            nonlocal calls
            original_check(dependencies)
            calls += 1
            if calls == 1:
                self.path.write_bytes(b"# Main\nExternal writer.\n")

        with mock_patch.object(mp, "_check_dependencies", side_effect=mutate):
            with self.assertRaisesRegex(mp.ManuscriptPatchError, "changed while"):
                self.apply(packet, {"section_id": "main", "before": "Original.", "after": "Changed."})
        self.assertEqual(self.path.read_bytes(), b"# Main\nExternal writer.\n")
        self.assertEqual(set(self.root.iterdir()), {self.path})

    def test_explicit_schema_errors(self):
        self.write("# Main\ntext\n")
        packet = self.packet()
        cases = [("schema_version", True), ("targets", []), ("targets", ["missing"]), ("targets", ["main", "main"]), ("dependencies", [{}])]
        for key, value in cases:
            candidate = copy.deepcopy(packet)
            candidate[key] = value
            with self.subTest(key=key, value=value):
                self.rejected(candidate, [])


if __name__ == "__main__":
    unittest.main()
