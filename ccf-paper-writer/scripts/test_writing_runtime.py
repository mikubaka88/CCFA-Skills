#!/usr/bin/env python3
"""End-to-end CLI checks with real UTF-8 files and no model calls."""
import json
import os
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest


SCRIPT = Path(__file__).with_name("writing_runtime.py").resolve()


class WritingRuntimeTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory(prefix="ccfa-writing-cli-")
        self.addCleanup(self.tmp.cleanup)
        self.root = Path(self.tmp.name).resolve()
        self.paper = self.root / "论文.md"
        self.paper.write_bytes(b"\xef\xbb\xbf" + (
            "# Motivation\r\n空间平均丢失了局部差异。\r\n"
            "# Method\r\n模型保留分组特征。\r\n"
            "# Results\r\nThe grouped model reaches 82.0% accuracy.\r\n"
            "# Discussion\r\n局部差异与性能变化相联系。\r\n").encode("utf-8"))
        self.data = self.root / "实测.json"
        self.write(self.data, {"baseline": 79.0, "grouped": 82.0})
        self.brief = self.root / "brief.json"
        self.write(self.brief, {"message": "Explain the accuracy difference.",
                               "throughline": "Retaining local distinctions changes downstream behavior."})
        self.sources = self.root / "sources.json"
        self.write(self.sources, [{"id": "observed", "path": self.data.name,
                                   "kind": "measurement", "used_by": ["results", "figure:main"]}])
        self.packet = self.root / "writing-packet.json"

    def write(self, path, obj):
        path.write_text(json.dumps(obj, ensure_ascii=False), encoding="utf-8")

    def cli(self, *args, ok=True):
        result = subprocess.run([sys.executable, "-X", "utf8", str(SCRIPT), *map(str, args)],
                                cwd=self.root, capture_output=True, text=True, encoding="utf-8", timeout=15,
                                env={**os.environ, "CODEX_HOME": str(self.root / "codex-home")})
        if ok:
            self.assertEqual(result.returncode, 0, result.stderr)
            return json.loads(result.stdout)
        self.assertEqual(result.returncode, 2, result.stdout + result.stderr)
        self.assertIn("error", json.loads(result.stderr))
        return result

    def prepare(self, mode="results"):
        self.cli("prepare", "--manuscript", self.paper, "--target", "results", "--brief", self.brief,
                 "--sources", self.sources, "--mode", mode, "--output", self.packet)
        return json.loads(self.packet.read_text(encoding="utf-8"))

    def test_inspect_returns_navigation_not_full_text(self):
        result = self.cli("inspect", "--manuscript", self.paper)
        self.assertEqual([s["id"] for s in result["sections"]], ["motivation", "method", "results", "discussion"])
        self.assertTrue(all("text" not in s for s in result["sections"]))

    def test_selected_prompt_neighbors_mainline_and_located_source(self):
        packet = self.prepare()
        self.assertEqual(packet["guidance"]["mode"], "results")
        self.assertIn("sample units", packet["guidance"]["text"])
        self.assertNotIn("<!-- prompt:", packet["guidance"]["text"])
        self.assertNotIn("Organize the authorized passage", packet["guidance"]["text"])
        self.assertIn("Retaining local distinctions", json.dumps(packet["context"], ensure_ascii=False))
        self.assertIn("模型保留分组特征", json.dumps(packet["context"], ensure_ascii=False))
        self.assertIn("局部差异与性能变化", json.dumps(packet["context"], ensure_ascii=False))
        self.assertTrue(any(d["path"] == str(self.data) for d in packet["dependencies"]))
        self.assertEqual(packet["patch_schema"]["base_sha256"], packet["manuscript"]["sha256"])

    def test_safe_patch_preserves_other_sections_bom_and_crlf(self):
        packet = self.prepare()
        old = self.paper.read_bytes()
        patch = self.root / "patch.json"
        before = "The grouped model reaches 82.0% accuracy."
        after = "Retaining grouped features raises accuracy from 79.0% to 82.0%."
        self.write(patch, {"base_sha256": packet["manuscript"]["sha256"],
                           "edits": [{"section_id": "results", "before": before, "after": after}]})
        result = self.cli("apply", "--packet", self.packet, "--patch", patch)
        self.assertEqual(result["changed_sections"], ["results"])
        self.assertEqual(self.paper.read_bytes(), old.replace(before.encode(), after.encode()))
        self.cli("apply", "--packet", self.packet, "--patch", patch, ok=False)

    def test_readonly_consistency_packet_cannot_apply_patch(self):
        packet = self.prepare("consistency")
        self.assertEqual(packet["operation"], "review")
        self.assertNotIn("patch_schema", packet)
        patch = self.root / "patch.json"
        self.write(patch, {"base_sha256": packet["manuscript"]["sha256"], "edits": []})
        self.cli("apply", "--packet", self.packet, "--patch", patch, ok=False)

    def test_source_change_blocks_edit_and_reports_section_figure_impact(self):
        packet = self.prepare()
        self.write(self.data, {"baseline": 79.0, "grouped": 81.0})
        impact = self.cli("impact", "--packet", self.packet)
        serialized = json.dumps(impact)
        self.assertIn("observed", serialized)
        self.assertIn("figure:main", serialized)
        self.assertIn("results", serialized)
        patch = self.root / "patch.json"
        self.write(patch, {"base_sha256": packet["manuscript"]["sha256"], "edits": []})
        self.cli("apply", "--packet", self.packet, "--patch", patch, ok=False)

    def test_packet_update_in_place_and_refuse_overwriting_inputs(self):
        self.prepare()
        self.prepare("draft")
        self.assertEqual(len(list(self.root.glob("writing-packet*.json"))), 1)
        unrelated = self.root / "user.json"
        self.write(unrelated, {"keep": True})
        self.cli("prepare", "--manuscript", self.paper, "--target", "results", "--output", unrelated, ok=False)
        self.assertEqual(json.loads(unrelated.read_text()), {"keep": True})
        self.cli("prepare", "--manuscript", self.paper, "--target", "results", "--output", self.paper, ok=False)
        self.assertFalse(list(self.root.glob(".*.tmp")))

    def test_all_modes_and_reserved_source_ids(self):
        for mode in ["draft", "related-work", "results", "consistency"]:
            self.assertEqual(self.prepare(mode)["guidance"]["mode"], mode)
        declarations = json.loads(self.sources.read_text(encoding="utf-8"))
        declarations[0]["id"] = "ccfa-writing-brief"
        self.write(self.sources, declarations)
        self.cli("prepare", "--manuscript", self.paper, "--target", "results", "--sources", self.sources, ok=False)

    def test_pending_mode_resolves_project_and_explicit_override_without_context_change(self):
        off = self.prepare()
        project_file = self.root / ".ccfa" / "preferences.json"
        project_file.parent.mkdir()
        self.write(project_file, {"version": 1, "preferences": {"results_pending_draft": "on"}})
        project_before = project_file.read_bytes()
        on = self.cli("prepare", "--manuscript", self.paper, "--target", "results",
                      "--brief", self.brief, "--sources", self.sources, "--mode", "results",
                      "--project", self.root)
        self.assertEqual(on["context"], off["context"])
        self.assertEqual(on["draft_policy"]["results_pending"], "on")
        self.assertTrue(on["draft_policy"]["alignment_required"])
        self.assertFalse(on["draft_policy"]["fabricated_observations_allowed"])
        self.assertIn("[[PENDING:claim-id]]", on["guidance"]["text"])
        explicit = self.cli("prepare", "--manuscript", self.paper, "--target", "results",
                            "--project", self.root, "--results-pending", "off")
        self.assertEqual(explicit["draft_policy"]["results_pending"], "off")
        self.assertNotIn("deliberately enabled", explicit["guidance"]["text"])
        self.assertEqual(project_file.read_bytes(), project_before)
        self.assertFalse((self.root / "codex-home").exists())

    def test_pending_review_is_readonly_and_legacy_user_file_stays_sparse(self):
        user_file = self.root / "codex-home" / "ccfa" / "preferences.json"
        user_file.parent.mkdir(parents=True)
        self.write(user_file, {"version": 1, "preferences": {"reference_style_search": "off"}})
        before = user_file.read_bytes()
        off = self.prepare()
        self.assertEqual(off["draft_policy"]["results_pending"], "off")
        self.assertEqual(user_file.read_bytes(), before)
        on = self.cli("prepare", "--manuscript", self.paper, "--target", "results",
                      "--mode", "consistency", "--results-pending", "on")
        self.assertEqual(on["operation"], "review")
        self.assertNotIn("patch_schema", on)
        self.assertIn("assess only", on["guidance"]["text"])

    def test_review_cache_cli_lifecycle_does_not_submit_any_request(self):
        self.prepare("consistency")
        cache = self.root / "review-cache.json"
        common = ["--packet", self.packet, "--cache", cache, "--model", "actual-test-runtime"]
        result = self.cli("review-cache", "begin", *common)
        self.assertEqual(result["record"]["status"], "pending")
        self.assertFalse(self.cli("review-cache", "lookup", *common)["hit"])
        self.cli("review-cache", "begin", *common, ok=False)
        review = self.root / "review.md"
        review.write_text("Inspected results only; terminology is consistent.\n", encoding="utf-8")
        coverage = self.root / "coverage.json"
        self.write(coverage, {"kind": "excerpt", "sections": ["results"], "unexamined": ["method appendix"]})
        self.cli("review-cache", "complete", *common, "--result", review, "--coverage", coverage)
        self.assertTrue(self.cli("review-cache", "lookup", *common)["hit"])
        self.cli("review-cache", "begin", *common, "--cache", self.packet, ok=False)


if __name__ == "__main__":
    unittest.main()
