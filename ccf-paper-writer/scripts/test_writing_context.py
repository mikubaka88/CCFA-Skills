"""Actual-file checks for scoped writing context and dependency impact."""
from __future__ import annotations

import copy
import hashlib
import json
from pathlib import Path
import sys
import tempfile
import unittest
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).resolve().parent))
import manuscript_patch
import writing_context as context

class WritingContextTests(unittest.TestCase):
    def setUp(self):
        self.temporary = tempfile.TemporaryDirectory(prefix="ccfa-writing-context-")
        self.folder = Path(self.temporary.name)
        self.manuscript = self.folder / "中文论文.md"
        self.manuscript.write_text(
            "# Study\nThe shared scientific question.\n\n"
            "## Motivation\nThe previous section explains the missing relationship.\n\n"
            "## Method\n我们保留对象身份和观察时间。引用为 \\cite{source}，数值为 12.5%。\n\n"
            "## Results\nThe following section reports the observed result.\n\n"
            "## Appendix\nUnrelated appendix detail remains in the actual manuscript.\n",
            encoding="utf-8", newline="\n")
        self.exemplar = self.folder / "原文片段.md"
        self.exemplar.write_text("Source title\n第一行不是所选段落。\nThe selected explanation states its operation.\n它随后解释同一对象的依赖关系。\nUnused tail.\n", encoding="utf-8", newline="\n")
        self.other = self.folder / "结果表.csv"
        self.other.write_text("method,value\nUNRELATED_SOURCE_SENTINEL,0.8\n", encoding="utf-8", newline="\n")

    def tearDown(self):
        self.temporary.cleanup()

    def source(self, **updates):
        result = {"id": "source-paper", "path": str(self.exemplar), "kind": "exemplar", "used_by": ["method"], "start_line": 3, "end_line": 4}
        result.update(updates)
        return result

    def packet(self, **kwargs):
        return context.prepare_context(self.manuscript, ["method"], sources=[self.source()], **kwargs)

    def test_actual_parser_target_and_both_neighbors_are_preserved(self):
        packet = self.packet()
        self.assertEqual(packet["targets"], ["method"])
        inventory = manuscript_patch.inspect_manuscript(self.manuscript)
        actual = next(section["text"] for section in inventory["sections"] if section["id"] == "method")
        self.assertEqual(packet["context"]["targets"][0]["text"], actual)
        self.assertEqual({n["id"] for n in packet["context"]["neighbors"]}, {"motivation", "results"})
        self.assertNotIn("text", packet["sections"][0])
        self.assertNotIn("Unrelated appendix detail", json.dumps(packet["context"], ensure_ascii=False))

    def test_multiple_targets_are_not_duplicated_as_neighbors(self):
        packet = context.prepare_context(self.manuscript, ["method", "results"])
        self.assertEqual(len(packet["context"]["targets"]), 2)
        self.assertFalse({"method", "results"} & {n["id"] for n in packet["context"]["neighbors"]})
        self.assertEqual({n["id"] for n in packet["context"]["neighbors"]}, {"motivation", "appendix"})

    def test_explicit_original_lines_and_whole_file_identity(self):
        packet = self.packet()
        source = packet["context"]["sources"][0]
        self.assertEqual(source["text"], "The selected explanation states its operation.\n它随后解释同一对象的依赖关系。\n")
        self.assertEqual((source["start_line"], source["end_line"]), (3, 4))
        self.assertEqual(source["sha256"], hashlib.sha256(self.exemplar.read_bytes()).hexdigest())
        self.assertNotIn("第一行不是", source["text"])
        self.assertNotIn("Unused tail", source["text"])

    def test_irrelevant_source_is_not_prompt_content_but_remains_a_dependency(self):
        declaration = {"id": "result-table", "path": str(self.other), "kind": "result", "used_by": ["results", "fig:overview"]}
        packet = context.prepare_context(self.manuscript, ["method"], sources=[self.source(), declaration])
        self.assertEqual([s["id"] for s in packet["context"]["sources"]], ["source-paper"])
        self.assertEqual([d["id"] for d in packet["dependencies"]], ["source-paper", "result-table"])
        self.assertNotIn("UNRELATED_SOURCE_SENTINEL", json.dumps(packet["context"]))

    def test_scientific_brief_is_optional_and_is_not_invented(self):
        packet = self.packet()
        self.assertNotIn("message", packet["context"])
        self.assertNotIn("throughline", packet["context"])
        brief = {"message": "解释对象身份和时间如何共同组织查询。", "throughline": "长期查询需要历史状态。",
                 "terminology": {"belief": "normalized state distribution"}, "protected_literals": ["12.5%", "\\cite{source}"]}
        original = copy.deepcopy(brief)
        packet = self.packet(brief=brief)
        for key, value in brief.items():
            self.assertEqual(packet["context"][key], value)
        self.assertEqual(brief, original)
        with self.assertRaisesRegex(context.WritingContextError, "Unknown scientific"):
            self.packet(brief={"agent_mode": "checklist"})

    def test_inputs_and_source_files_are_not_modified(self):
        declarations = [self.source()]
        original = copy.deepcopy(declarations)
        before = {p.name: p.read_bytes() for p in self.folder.iterdir()}
        packet = context.prepare_context(self.manuscript, ["method"], sources=declarations)
        context.assess_impact(packet)
        self.assertEqual(declarations, original)
        self.assertEqual(before, {p.name: p.read_bytes() for p in self.folder.iterdir()})

    def test_long_neighbor_uses_the_adjacent_edge_with_explicit_omission(self):
        self.manuscript.write_text("## Prior\n" + "old material\n"*200 + "ADJACENT_END\n## Method\nTarget.\n## Next\nNEXT_START\n" + "later material\n"*200, encoding="utf-8", newline="\n")
        packet = context.prepare_context(self.manuscript, ["method"])
        prior, following = packet["context"]["neighbors"]
        self.assertTrue(prior["text"].endswith("ADJACENT_END\n"))
        self.assertTrue(following["text"].startswith("## Next\nNEXT_START"))
        self.assertTrue(prior["omitted"])
        self.assertTrue(following["omitted"])
        self.assertLessEqual(len(prior["text"]), context.NEIGHBOR_CHARS)

    def test_long_shared_neighbor_keeps_both_transitions_without_overlap(self):
        self.manuscript.write_text("## Method\nFirst target.\n## Results\nSHARED_START\n" +
                                   "middle material\n"*250 + "SHARED_END\n## Appendix\nSecond target.\n",
                                   encoding="utf-8", newline="\n")
        packet = context.prepare_context(self.manuscript, ["method", "appendix"])
        head, tail = packet["context"]["neighbors"]
        self.assertEqual([head["id"], tail["id"]], ["results", "results"])
        self.assertEqual([head["edge"], tail["edge"]], ["head", "tail"])
        self.assertIn("SHARED_START", head["text"])
        self.assertTrue(tail["text"].endswith("SHARED_END\n"))
        self.assertLessEqual(head["end"], tail["start"])
        self.assertEqual(head["adjacent_to"], [{"target": "method", "side": "next"}])
        self.assertEqual(tail["adjacent_to"], [{"target": "appendix", "side": "previous"}])

    def test_short_shared_neighbor_is_included_only_once(self):
        packet = context.prepare_context(self.manuscript, ["method", "appendix"])
        shared = [item for item in packet["context"]["neighbors"] if item["id"] == "results"]
        self.assertEqual(len(shared), 1)
        self.assertEqual(shared[0]["edge"], "full")
        self.assertEqual(len(shared[0]["adjacent_to"]), 2)

    def test_budget_cuts_only_optional_text_and_keeps_readback_positions(self):
        self.exemplar.write_text("line\n" + "这是给定来源中的原文关系。\n"*300, encoding="utf-8", newline="\n")
        declaration = self.source(start_line=2, end_line=301)
        brief = {"message": "原研究消息不能被裁掉。", "throughline": "共同主线。", "protected_literals": ["12.5%"]}
        full = context.prepare_context(self.manuscript, ["method"], brief=brief, sources=[declaration])
        budget = full["budget"]["used_chars"]-500
        limited = context.prepare_context(self.manuscript, ["method"], brief=brief, sources=[declaration], max_chars=budget)
        self.assertLessEqual(len(json.dumps(limited["context"], ensure_ascii=False)), budget)
        self.assertEqual(limited["budget"]["used_chars"], len(json.dumps(limited["context"], ensure_ascii=False)))
        self.assertEqual(limited["context"]["targets"], full["context"]["targets"])
        for key, value in brief.items():self.assertEqual(limited["context"][key], value)
        source = limited["context"]["sources"][0]
        self.assertTrue(source["omitted"])
        self.assertIn("start_line", source["omitted"][0])
        self.assertEqual(source["requested"], full["context"]["sources"][0]["requested"])

    def test_tiny_budget_refuses_instead_of_cutting_the_target_or_mainline(self):
        with self.assertRaisesRegex(context.WritingContextError, "complete targets"):
            self.packet(brief={"message": "重要论证。"*30}, max_chars=30)
        for budget in (True, 0, -1, 1.5):
            with self.assertRaises(context.WritingContextError):self.packet(max_chars=budget)

    def test_same_file_with_two_explicit_ids_preserves_separate_line_windows(self):
        packet = context.prepare_context(self.manuscript, ["method"], sources=[self.source(), self.source(id="other-window", start_line=1, end_line=1, used_by=["results"])])
        self.assertEqual(len(packet["dependencies"]), 2)
        self.assertEqual(len(packet["context"]["sources"]), 1)
        result = context.assess_impact(packet)
        self.assertEqual(result["changed_sources"], [])

    def test_same_source_is_read_once_per_prepare_and_impact_call(self):
        declarations = [self.source(), self.source(id="other-window", start_line=1, end_line=1, used_by=["results"])]
        original = Path.read_bytes
        reads = []

        def tracked_read(path):
            reads.append(path)
            return original(path)

        with patch.object(Path, "read_bytes", tracked_read):
            packet = context.prepare_context(self.manuscript, ["method"], sources=declarations)
        self.assertEqual(reads.count(self.exemplar), 1)
        self.assertEqual(packet["dependencies"][0]["sha256"], packet["dependencies"][1]["sha256"])
        self.exemplar.write_text("Changed actual source.\n", encoding="utf-8")
        reads.clear()
        with patch.object(Path, "read_bytes", tracked_read):
            impact = context.assess_impact(packet)
        self.assertEqual(reads.count(self.exemplar), 1)
        self.assertEqual(len(impact["changed_sources"]), 2)
        self.assertEqual(impact["affected_sections"], ["method", "results"])

    def test_source_change_maps_only_its_declared_sections_and_figures(self):
        dependency = {"id": "result-table", "path": str(self.other), "kind": "result", "used_by": ["results", "fig:overview", "table:main"]}
        packet = context.prepare_context(self.manuscript, ["method"], sources=[self.source(), dependency])
        self.other.write_text("method,value\nChanged,0.7\n", encoding="utf-8")
        impact = context.assess_impact(packet)
        self.assertEqual([s["id"] for s in impact["changed_sources"]], ["result-table"])
        self.assertEqual(impact["affected_sections"], ["results"])
        self.assertEqual(impact["affected_figures"], ["fig:overview"])
        self.assertEqual(impact["affected_tables"], ["table:main"])
        self.assertFalse(impact["scope_unknown"])
        self.assertEqual(impact["affected_targets"], [])
        self.assertIs(impact["manuscript_changed"], False)

    def test_missing_source_is_reported_without_editing_or_crashing(self):
        packet = self.packet()
        self.exemplar.unlink()
        impact = context.assess_impact(packet)
        self.assertEqual(impact["changed_sources"][0]["status"], "missing")
        self.assertEqual(impact["unknown_dependencies"], ["source-paper"])
        self.assertEqual(impact["affected_targets"], ["method"])

    def test_missing_manuscript_is_unknown_not_claimed_unchanged(self):
        packet = self.packet()
        self.manuscript.unlink()
        impact = context.assess_impact(packet)
        self.assertIsNone(impact["manuscript_changed"])
        self.assertEqual(impact["manuscript"]["status"], "missing")

    def test_changed_manuscript_localizes_the_actual_changed_section(self):
        packet = self.packet()
        text = self.manuscript.read_text(encoding="utf-8")
        self.manuscript.write_text(text.replace("following section reports", "following section now reports"), encoding="utf-8", newline="\n")
        impact = context.assess_impact(packet)
        self.assertTrue(impact["manuscript_changed"])
        self.assertEqual(impact["changed_sections"], ["results"])
        self.assertEqual(impact["affected_sections"], ["results"])
        self.assertEqual(impact["affected_targets"], [])

    def test_deleted_and_added_sections_are_identified(self):
        packet = self.packet()
        self.manuscript.write_text(self.manuscript.read_text(encoding="utf-8").replace("## Appendix", "## Supplement"), encoding="utf-8", newline="\n")
        impact = context.assess_impact(packet)
        self.assertEqual(impact["removed_sections"], ["appendix"])
        self.assertEqual(impact["added_sections"], ["supplement"])

    def test_unknown_dependency_identity_is_explicit(self):
        packet = self.packet()
        packet["dependencies"][0].pop("sha256")
        impact = context.assess_impact(packet)
        self.assertEqual(impact["changed_sources"][0]["status"], "unknown")
        self.assertEqual(impact["affected_targets"], ["method"])

    def test_manually_unmapped_changed_source_reports_unknown_scope(self):
        packet = self.packet()
        packet["dependencies"][0]["used_by"] = []
        self.exemplar.write_text("Changed source without a dependency map.\n", encoding="utf-8")
        impact = context.assess_impact(packet)
        self.assertEqual(impact["changed_sources"][0]["status"], "changed")
        self.assertEqual(impact["unknown_dependencies"], ["source-paper"])
        self.assertEqual(impact["scope_unknown_dependencies"], ["source-paper"])
        self.assertTrue(impact["scope_unknown"])
        self.assertEqual(impact["affected_sections"], [])

    def test_unknown_dependent_ids_are_not_pretended_to_be_figures(self):
        packet = context.prepare_context(self.manuscript, ["method"], sources=[self.source(used_by=["unmapped-artifact"])])
        self.exemplar.write_text("New source.\n", encoding="utf-8")
        impact = context.assess_impact(packet)
        self.assertEqual(impact["unmapped_dependents"], ["unmapped-artifact"])
        self.assertEqual(impact["affected_figures"], [])

    def test_strict_utf8_bom_and_crlf_source_positions(self):
        self.manuscript.write_bytes(b"\xef\xbb\xbf" + "## Method\r\n中文内容保持原换行。\r\n## Results\r\n结果。\r\n".encode("utf-8"))
        self.exemplar.write_bytes(b"\xef\xbb\xbf" + "首行。\r\n所选原文。\r\n末行。\r\n".encode("utf-8"))
        packet = context.prepare_context(self.manuscript, ["method"], sources=[self.source(start_line=2, end_line=2)])
        self.assertIn("\r\n", packet["context"]["targets"][0]["text"])
        self.assertEqual(packet["context"]["sources"][0]["text"], "所选原文。\r\n")
        self.assertNotIn("\ufeff", packet["context"]["targets"][0]["text"])

    def test_invalid_utf8_and_nonexistent_sources_are_rejected_on_prepare(self):
        self.exemplar.write_bytes(b"\xff")
        with self.assertRaisesRegex(context.WritingContextError, "UTF-8"):
            self.packet()
        self.exemplar.unlink()
        with self.assertRaises(context.WritingContextError):self.packet()

    def test_source_turning_invalid_utf8_is_reported_as_unreadable(self):
        packet = self.packet()
        self.exemplar.write_bytes(b"\xff")
        impact = context.assess_impact(packet)
        self.assertEqual(impact["changed_sources"][0]["status"], "unreadable")

    def test_invalid_ids_mappings_and_ranges_are_rejected(self):
        for target in (["absent"], ["method", "method"], "method", []):
            with self.assertRaises(context.WritingContextError):context.prepare_context(self.manuscript, target)
        invalid = [self.source(used_by=[]), self.source(start_line=0), self.source(end_line=1000), self.source(start_line=4, end_line=3)]
        invalid.append({"id": "missing-map", "path": str(self.exemplar), "kind": "exemplar"})
        for declaration in invalid:
            with self.assertRaises(context.WritingContextError):context.prepare_context(self.manuscript, ["method"], sources=[declaration])

    def test_racing_manuscript_inspection_is_not_accepted_as_current(self):
        inspected = manuscript_patch.inspect_manuscript(self.manuscript)
        self.manuscript.write_text(self.manuscript.read_text(encoding="utf-8")+"Changed.\n", encoding="utf-8")
        with patch.object(context, "_inspect_manuscript", return_value=inspected):
            with self.assertRaisesRegex(context.WritingContextError, "changed during"):
                context.prepare_context(self.manuscript, ["method"])

    def test_manuscript_cannot_be_its_own_source_dependency(self):
        with self.assertRaisesRegex(context.WritingContextError, "own source"):
            context.prepare_context(self.manuscript, ["method"], sources=[
                self.source(path=str(self.manuscript), start_line=1, end_line=2)])

    def test_prepared_packet_is_compatible_with_the_scoped_patch_api(self):
        packet = self.packet()
        result = manuscript_patch.apply_patch(packet, {"base_sha256": packet["manuscript"]["sha256"], "edits": [{"section_id": "method", "before": "对象身份和观察时间", "after": "对象身份及其观察时间"}]})
        self.assertTrue(result["changed"])
        self.assertEqual(result["changed_sections"], ["method"])
        self.assertEqual(context.assess_impact(packet)["changed_sections"], ["method"])


if __name__ == "__main__":
    unittest.main()
