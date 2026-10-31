#!/usr/bin/env python3
"""Filesystem regressions for exact, optional review reuse."""
import hashlib
import json
from pathlib import Path
import tempfile
import unittest

from writing_review_cache import review_cache, review_key


class ReviewCacheTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory(prefix="ccfa-review-")
        self.addCleanup(self.tmp.cleanup)
        self.root = Path(self.tmp.name).resolve()
        self.manuscript = self.root / "论文.md"
        self.manuscript.write_text("# Introduction\n科学问题与方法。\n", encoding="utf-8")
        self.source = self.root / "results.json"
        self.source.write_text('{"accuracy": 0.8}', encoding="utf-8")
        def digest(path):
            return hashlib.sha256(path.read_bytes()).hexdigest()
        self.packet = {"schema_version": 1, "manuscript": {"path": str(self.manuscript), "sha256": digest(self.manuscript)},
                       "targets": ["introduction"], "context": {"throughline": "One research question"},
                       "guidance": {"text": "Review the argument"},
                       "dependencies": [{"id": "results", "path": str(self.source),
                                         "sha256": digest(self.source), "used_by": ["introduction"]}]}
        self.cache = self.root / "review-cache.json"
        self.result = self.root / "review.md"
        self.result.write_text("检查引言论点与结果是否一致。\n", encoding="utf-8")
        self.coverage = {"kind": "full", "sections": ["introduction"]}

    def call(self, action, **kwargs):
        return review_cache(action, self.packet, self.cache, kwargs.pop("model", "actual-model"), **kwargs)

    def complete(self):
        self.call("begin")
        return self.call("complete", result_path=self.result, coverage=self.coverage)

    def test_exact_completed_result_reused_without_copying_report(self):
        self.complete()
        found = self.call("lookup")
        self.assertTrue(found["hit"])
        self.assertEqual(found["record"]["coverage"], self.coverage)
        self.assertNotIn("检查", self.cache.read_text(encoding="utf-8"))
        self.assertTrue(self.call("begin")["hit"])
        self.assertEqual(sorted(p.name for p in self.root.iterdir()),
                         sorted([self.manuscript.name, self.source.name, self.cache.name, self.result.name]))

    def test_pending_is_not_success_and_cannot_silently_retry(self):
        self.call("begin")
        self.assertFalse(self.call("lookup")["hit"])
        with self.assertRaisesRegex(ValueError, "pending"):
            self.call("begin")
        with self.assertRaisesRegex(ValueError, "call-stopped"):
            self.call("abandon")
        self.call("abandon", call_stopped=True)
        self.assertEqual(self.call("begin")["record"]["status"], "pending")

    def test_changed_model_parameters_or_prompt_not_reused(self):
        self.complete()
        self.assertFalse(self.call("lookup", model="different-model")["hit"])
        self.assertFalse(self.call("lookup", options={"rubric": "changed"})["hit"])
        self.packet["guidance"]["text"] = "Different review scope"
        self.assertFalse(self.call("lookup")["hit"])

    def test_changed_or_missing_result_not_reused(self):
        self.complete()
        self.result.write_text("User edited the report", encoding="utf-8")
        self.assertFalse(self.call("lookup")["hit"])
        self.result.unlink()
        self.assertFalse(self.call("lookup")["hit"])

    def test_unrelated_source_change_or_removal_keeps_scoped_review(self):
        appendix = self.root / "appendix.csv"
        appendix.write_text("count,2", encoding="utf-8")
        dependency = {"id": "appendix", "path": str(appendix),
                      "sha256": hashlib.sha256(appendix.read_bytes()).hexdigest(),
                      "used_by": ["appendix"]}
        self.packet["dependencies"].append(dependency)
        key = review_key(self.packet, "actual-model")
        self.complete()
        appendix.write_text("count,3", encoding="utf-8")
        self.assertTrue(self.call("lookup")["hit"])
        dependency["sha256"] = hashlib.sha256(appendix.read_bytes()).hexdigest()
        self.assertEqual(review_key(self.packet, "actual-model"), key)
        self.assertTrue(self.call("lookup")["hit"])
        appendix.unlink()
        self.assertTrue(self.call("lookup")["hit"])

    def test_unknown_dependency_scope_remains_conservative(self):
        self.packet["dependencies"][0]["used_by"] = []
        self.complete()
        self.source.write_text('{"accuracy": 0.5}', encoding="utf-8")
        with self.assertRaises(ValueError):
            self.call("lookup")

    def test_relative_active_source_refresh_changes_key_and_prevents_reuse(self):
        dependency = self.packet["dependencies"][0]
        dependency["path"] = self.source.name  # Resolved against manuscript, not caller CWD.
        key = review_key(self.packet, "actual-model")
        with self.assertRaisesRegex(ValueError, "overwrite"):
            review_cache("begin", self.packet, self.source, "actual-model")
        self.complete()
        self.source.write_text('{"accuracy": 0.4}', encoding="utf-8")
        dependency["sha256"] = hashlib.sha256(self.source.read_bytes()).hexdigest()
        self.assertNotEqual(review_key(self.packet, "actual-model"), key)
        self.assertFalse(self.call("lookup")["hit"])

    def test_changed_source_or_manuscript_blocks_completion(self):
        self.call("begin")
        self.source.write_text('{"accuracy": 0.9}', encoding="utf-8")
        with self.assertRaisesRegex(ValueError, "changed"):
            self.call("complete", result_path=self.result, coverage=self.coverage)
        self.assertEqual(json.loads(self.cache.read_text(encoding="utf-8"))["status"], "pending")
        # Reconciliation remains possible even after inputs changed.
        self.call("abandon", call_stopped=True)

    def test_partial_coverage_preserved_and_unknown_section_rejected(self):
        self.call("begin")
        with self.assertRaisesRegex(ValueError, "Coverage"):
            self.call("complete", result_path=self.result, coverage={"kind": "full", "sections": ["other"]})
        self.call("complete", result_path=self.result,
                  coverage={"kind": "excerpt", "sections": ["introduction"], "unexamined": "Full references"})
        self.assertEqual(self.call("lookup")["record"]["coverage"]["kind"], "excerpt")

    def test_empty_result_or_cache_result_alias_rejected(self):
        self.call("begin")
        self.result.write_text("", encoding="utf-8")
        with self.assertRaisesRegex(ValueError, "nonempty"):
            self.call("complete", result_path=self.result, coverage=self.coverage)
        with self.assertRaisesRegex(ValueError, "overwrite"):
            self.call("complete", result_path=self.cache, coverage=self.coverage)

    def test_refuses_existing_unrelated_json_and_input_paths(self):
        self.cache.write_text('{"important": true}', encoding="utf-8")
        with self.assertRaisesRegex(ValueError, "Not a writing-review"):
            self.call("begin")
        self.assertEqual(json.loads(self.cache.read_text(encoding="utf-8")), {"important": True})
        with self.assertRaisesRegex(ValueError, "overwrite"):
            review_cache("begin", self.packet, self.source, "actual-model")

    def test_lock_refusal_does_not_remove_other_owners_lock(self):
        lock = self.cache.with_name("." + self.cache.name + ".lock")
        lock.write_text("another owner", encoding="utf-8")
        with self.assertRaisesRegex(ValueError, "busy"):
            self.call("begin")
        self.assertEqual(lock.read_text(encoding="utf-8"), "another owner")

    def test_key_is_canonical_but_rejects_nonfinite_parameters(self):
        self.assertEqual(review_key(self.packet, "model", {"a": 1, "b": 2}),
                         review_key(self.packet, "model", {"b": 2, "a": 1}))
        with self.assertRaises(ValueError):
            review_key(self.packet, "model", {"temperature": float("nan")})


if __name__ == "__main__":
    unittest.main()
