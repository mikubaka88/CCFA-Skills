#!/usr/bin/env python3
"""Real-file request checks; no model endpoint is called by this suite."""
import json
import copy
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest
from unittest.mock import patch

import prepare_expert_review as expert


class ExpertRequestTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory(prefix="ccfa-expert-")
        self.addCleanup(self.tmp.cleanup)
        self.root = Path(self.tmp.name).resolve()
        self.paper = self.root / "中文论文.md"
        self.paper.write_bytes(b"\xef\xbb\xbf" + "# Method\r\n保留原始对象。\\cite{paper}\r\n# Results\r\nAccuracy: 82.0%.\r\n".encode())
        self.supplement = self.root / "补充.md"
        self.supplement.write_text("# Proof\nThe actual supporting argument.\n", encoding="utf-8")
        self.criteria = self.root / "criteria.md"
        self.criteria.write_text("Assess correctness and significance.\n", encoding="utf-8")
        self.ready_args = {"independent_review": "on", "available_models": ["gpt-6-astra"], "context_isolation": True}

    def request(self, **changes):
        return expert.prepare_expert_review(self.paper, **{**self.ready_args, **changes})

    def prepared_for_reuse(self, **changes):
        return self.request(runtime="test-host/1", effort="ultra", options={}, **changes)

    def completed_fixture(self, prepared):
        """Declared test evidence only; this suite never executes a model."""
        request = prepared["request"]
        return {"status": "complete", "executed": True, "fingerprint": prepared["fingerprint"],
                "response": "Fixture specialist response with located findings.",
                "execution": {"model": request["model"], "fresh_context": True,
                              **copy.deepcopy(request["execution_spec"]),
                              "policies": [{"id": p["id"], "sha256": p["sha256"]} for p in request["policies"]]},
                "coverage": [{"path": d["path"], "sha256": d["sha256"], "complete": True} for d in request["documents"]]}

    def test_off_does_not_even_read_manuscript(self):
        with patch.object(expert, "_source") as source:
            result = expert.prepare_expert_review("absent.md")
        self.assertEqual(result["status"], "disabled")
        source.assert_not_called()
        self.assertFalse(result["executed"])

    def test_explicit_request_overrides_off_for_task_only(self):
        result = self.request(independent_review="off", explicit_expert=True)
        self.assertEqual(result["status"], "ready")
        self.assertTrue(result["primary_review_continues"])
        self.assertFalse(result["executed"])

    def test_auto_requires_actual_trigger_and_reason(self):
        for changes in [{}, {"reason": "A concrete unresolved issue"}, {"trigger": "unresolved-judgment"}]:
            self.assertEqual(self.request(independent_review="auto", **changes)["status"], "needs_trigger")
        for trigger in expert.TRIGGERS:
            self.assertEqual(self.request(independent_review="auto", trigger=trigger,
                                          reason="An independent reading can change the result.")["status"], "ready")

    def test_writing_does_not_automatically_expand_scientific_scope(self):
        self.assertEqual(self.request(mode="writing")["status"], "not_applicable")
        result = self.request(mode="writing", explicit_expert=True)
        self.assertEqual(result["status"], "ready")
        self.assertIn("Writing and argument only", result["request"]["task"]["scope"])

    def test_concept_routes_to_idea_owner_without_reading_paper(self):
        with patch.object(expert, "_source") as source:
            result = self.request(mode="concept", explicit_expert=True)
        self.assertEqual(result["owner"], "ccf-idea-reviewer")
        self.assertEqual(result["status"], "not_applicable")
        source.assert_not_called()

    def test_real_context_isolation_is_required(self):
        result = self.request(context_isolation=False)
        self.assertEqual(result["status"], "unavailable")
        self.assertNotIn("request", result)

    def test_model_must_be_gpt6_and_actually_declared_available(self):
        for models in [[], ["other-model"], ["gpt-5.6-sol"]]:
            self.assertEqual(self.request(available_models=models)["status"], "unavailable")
        result = self.request(available_models=["gpt-6-astra"], model="gpt-6-sol")
        self.assertEqual(result["status"], "unavailable")
        self.assertNotIn("request", result)

    def test_preserves_explicit_model_or_host_preference_order(self):
        models = ["gpt-6-sol", "gpt-6-astra"]
        self.assertEqual(self.request(available_models=models)["request"]["model"], "gpt-6-sol")
        self.assertEqual(self.request(available_models=models, model="gpt-6-astra")["request"]["model"], "gpt-6-astra")

    def test_three_languages_select_only_one_short_prompt(self):
        for language in expert.LANGUAGES:
            result = self.request(language=language)
            guidance = result["request"]["guidance"]
            self.assertEqual(guidance["language"], language)
            self.assertNotIn("<!-- prompt:", guidance["text"])
            self.assertNotIn("## Integrate Once", guidance["text"])
            self.assertTrue(guidance["text"].strip())

    def test_actual_utf8_bom_crlf_citations_and_complete_text_preserved(self):
        result = self.request()
        document = result["request"]["documents"][0]
        self.assertIn("保留原始对象。\\cite{paper}\r\n", document["text"])
        self.assertEqual(document["text"], self.paper.read_bytes().decode("utf-8-sig"))
        self.assertEqual(document["coverage"], "complete supplied text file")

    def test_only_scientific_inputs_not_leading_reason_passed(self):
        result = self.request(independent_review="auto", trigger="unresolved-judgment",
                              reason="LEAD_VERDICT_SENTINEL: reject because of X", supplements=[self.supplement],
                              criteria=self.criteria, venue="Supplied venue criteria")
        serialized = json.dumps(result["request"], ensure_ascii=False)
        self.assertNotIn("LEAD_VERDICT_SENTINEL", serialized)
        self.assertNotIn("independent_review", result["request"])
        self.assertEqual([s["role"] for s in result["request"]["documents"]], ["manuscript", "supplement", "venue-criteria"])

    def test_request_fingerprint_changes_with_source_phase_or_model(self):
        first = self.request()["fingerprint"]
        self.assertEqual(first, self.request()["fingerprint"])
        self.assertNotEqual(first, self.request(phase="results-pending")["fingerprint"])
        self.assertNotEqual(first, self.request(available_models=["gpt-6-sol"])["fingerprint"])
        self.paper.write_text("Changed manuscript", encoding="utf-8")
        self.assertNotEqual(first, self.request()["fingerprint"])

    def test_neutral_question_scope_constraints_and_actual_focus_reach_reader(self):
        result = self.request(review_question="Does the update preserve object identity?",
                              scope="Inspect the supplied method only.", constraints=["No numerical scores."],
                              exclusions=["New experiment design"],
                              focus_locations=[{"path": self.paper, "anchor": "Method", "start_line": 1, "end_line": 2}],
                              reason="LEAD_REJECT_SENTINEL")
        task = result["request"]["task"]
        self.assertEqual(task["review_question"], "Does the update preserve object identity?")
        self.assertEqual(task["requested_scope"], "Inspect the supplied method only.")
        self.assertEqual(task["constraints"], ["No numerical scores."])
        self.assertEqual(task["exclusions"], ["New experiment design"])
        self.assertEqual(task["focus_locations"][0]["sha256"], result["request"]["documents"][0]["sha256"])
        self.assertNotIn("LEAD_REJECT_SENTINEL", json.dumps(result))

    def test_fingerprint_tracks_actual_neutral_task_and_not_leading_reason(self):
        baseline = self.request()["fingerprint"]
        variants = [dict(review_question="Inspect the mechanism."), dict(scope="Only the method."),
                    dict(constraints=["No scores."]), dict(exclusions=["Experiments"]),
                    dict(focus_locations=[{"path": self.paper, "start_line": 1, "end_line": 2}])]
        for variant in variants:
            self.assertNotEqual(baseline, self.request(**variant)["fingerprint"])
        self.assertEqual(baseline, self.request(reason="Lead wants a different verdict.")["fingerprint"])

    def test_effective_runtime_effort_and_options_change_identity(self):
        baseline = self.prepared_for_reuse()["fingerprint"]
        for change in [dict(runtime="test-host/2"), dict(effort="high"), dict(options={"max_output_tokens": 1000})]:
            args = dict(runtime="test-host/1", effort="ultra", options={})
            args.update(change)
            self.assertNotEqual(baseline, self.request(**args)["fingerprint"])
        self.assertFalse(self.request()["reuse_identity_complete"])
        self.assertTrue(self.prepared_for_reuse()["reuse_identity_complete"])
        self.assertFalse(self.prepared_for_reuse()["executed"])

    def test_other_language_and_explanation_changes_do_not_invalidate_selected_prompt(self):
        path = self.root / "prompts.md"
        original = expert.PROMPT_PATH.read_text(encoding="utf-8")
        path.write_text(original, encoding="utf-8")
        with patch.object(expert, "PROMPT_PATH", path):
            baseline = self.request(language="en")["fingerprint"]
            changed = original.replace("<!-- prompt:zh-CN -->", "<!-- prompt:zh-CN -->\nDifferent Chinese-only instruction.")
            path.write_text(changed + "\nDocumentation changed only.\n", encoding="utf-8")
            self.assertEqual(baseline, self.request(language="en")["fingerprint"])
            path.write_text(changed.replace("<!-- prompt:en -->", "<!-- prompt:en -->\nInspect the specified question."), encoding="utf-8")
            self.assertNotEqual(baseline, self.request(language="en")["fingerprint"])

    def test_required_and_additional_applied_policy_versions_are_bound(self):
        family = self.root / "family"
        for name in ("ccf-humanization", "ccf-common"):
            policy = family / name / "SKILL.md"
            policy.parent.mkdir(parents=True)
            policy.write_text("Fixture baseline for " + name, encoding="utf-8")
        with patch.object(expert, "FAMILY_ROOT", family):
            first = self.request(policy_files=[self.criteria])
            self.assertEqual([p["id"] for p in first["request"]["policies"]], ["ccf-humanization", "ccf-common", "additional-policy-1"])
            policy.write_text("Changed shared baseline.", encoding="utf-8")
            self.assertNotEqual(first["fingerprint"], self.request(policy_files=[self.criteria])["fingerprint"])
            second = self.request(policy_files=[self.criteria])["fingerprint"]
            self.criteria.write_text("Changed additional applied instruction.", encoding="utf-8")
            self.assertNotEqual(second, self.request(policy_files=[self.criteria])["fingerprint"])

    def test_matching_completed_actual_execution_and_coverage_can_be_reused(self):
        prepared = self.prepared_for_reuse()
        completed = self.completed_fixture(prepared)
        before = copy.deepcopy(completed)
        self.assertTrue(expert.assess_review_reuse(prepared, completed)["reusable"])
        self.assertEqual(completed, before)

    def test_missing_actual_execution_or_changed_effort_cannot_be_reused(self):
        prepared = self.prepared_for_reuse()
        completed = self.completed_fixture(prepared)
        variants = []
        for key, value in [("runtime", "different-host"), ("effort", "high"), ("options", {"different": True}),
                           ("model", "gpt-6-sol"), ("fresh_context", False), ("policies", [])]:
            item = copy.deepcopy(completed)
            item["execution"][key] = value
            variants.append(item)
        for key, value in [("status", "pending"), ("executed", False), ("response", ""), ("coverage", [])]:
            item = copy.deepcopy(completed)
            item[key] = value
            variants.append(item)
        for item in variants:
            self.assertFalse(expert.assess_review_reuse(prepared, item)["reusable"])
        unspecified = self.request()
        self.assertFalse(expert.assess_review_reuse(unspecified, self.completed_fixture(unspecified))["reusable"])

    def test_partial_coverage_requires_the_actual_requested_locations(self):
        prepared = self.prepared_for_reuse(focus_locations=[{"path": self.paper, "start_line": 1, "end_line": 2}])
        completed = self.completed_fixture(prepared)
        completed["coverage"][0]["complete"] = False
        self.assertFalse(expert.assess_review_reuse(prepared, completed)["reusable"])
        completed["coverage"][0]["locations"] = prepared["request"]["task"]["focus_locations"]
        self.assertTrue(expert.assess_review_reuse(prepared, completed)["reusable"])
        completed["coverage"][0]["locations"] = "not an inspected-location list"
        self.assertFalse(expert.assess_review_reuse(prepared, completed)["reusable"])

    def test_old_preparation_cannot_reuse_after_current_source_changes(self):
        prepared = self.prepared_for_reuse()
        completed = self.completed_fixture(prepared)
        self.paper.write_text("Current revised manuscript.", encoding="utf-8")
        self.assertFalse(expert.assess_review_reuse(prepared, completed)["reusable"])
        for invalid in [{}, {"status": "ready", "request": {}}, None]:
            self.assertFalse(expert.assess_review_reuse(invalid, completed)["reusable"])

    def test_invalid_focus_and_nonfinite_or_untyped_options_refused(self):
        invalid = [[{"path": self.supplement, "anchor": "Proof"}],
                   [{"path": self.paper}], [{"path": self.paper, "start_line": 0, "end_line": 2}],
                   [{"path": self.paper, "start_line": 1, "end_line": 999}]]
        for locations in invalid:
            with self.assertRaises(ValueError):
                self.request(focus_locations=locations)
        for options in [[], {"temperature": float("nan")}]:
            with self.assertRaises(ValueError):
                self.request(options=options)

    def test_cli_neutral_scope_options_and_readonly_reuse_entry(self):
        script = Path(expert.__file__).resolve()
        prepared = self.prepared_for_reuse(review_question="Inspect the method.")
        record = self.root / "completed.json"
        record.write_text(json.dumps(self.completed_fixture(prepared)), encoding="utf-8")
        process = subprocess.run([sys.executable, "-B", "-X", "utf8", str(script), "--manuscript", str(self.paper),
                                  "--independent-review", "on", "--available-model", "gpt-6-astra", "--context-isolation",
                                  "--review-question", "Inspect the method.", "--runtime", "test-host/1", "--effort", "ultra",
                                  "--options-json", "{}", "--reuse-record", str(record)],
                                 cwd=self.root, capture_output=True, text=True, encoding="utf-8", timeout=10)
        self.assertEqual(process.returncode, 0, process.stderr)
        self.assertTrue(json.loads(process.stdout)["reuse_check"]["reusable"])

    def test_character_limit_refuses_whole_request_instead_of_truncating(self):
        ready = self.request()
        exact = ready["input_characters"]
        self.assertEqual(self.request(max_input_chars=exact)["status"], "ready")
        too_small = self.request(max_input_chars=exact-1)
        self.assertEqual(too_small["status"], "unavailable")
        self.assertNotIn("request", too_small)

    def test_duplicate_sources_binary_and_empty_inputs_rejected(self):
        with self.assertRaisesRegex(ValueError, "duplicate"):
            self.request(supplements=[self.paper])
        self.supplement.write_bytes(b"%PDF-\xff")
        with self.assertRaises(UnicodeError):
            self.request(supplements=[self.supplement])
        self.supplement.write_bytes(b"")
        with self.assertRaisesRegex(ValueError, "Empty"):
            self.request(supplements=[self.supplement])

    def test_helper_does_not_write_reports_or_preferences(self):
        before = {p.name: p.read_bytes() for p in self.root.iterdir()}
        self.request(supplements=[self.supplement], criteria=self.criteria)
        self.assertEqual(before, {p.name: p.read_bytes() for p in self.root.iterdir()})

    def test_cli_default_off_ready_and_invalid_input(self):
        script = Path(expert.__file__).resolve()
        def call(*args):
            return subprocess.run([sys.executable, "-B", "-X", "utf8", str(script), *map(str, args)],
                                  cwd=self.root, capture_output=True, text=True, encoding="utf-8", timeout=10)
        off = call("--manuscript", "nonexistent.md")
        self.assertEqual(json.loads(off.stdout)["status"], "disabled")
        ready = call("--manuscript", self.paper, "--explicit-expert", "--available-model", "gpt-6-astra", "--context-isolation")
        self.assertEqual(ready.returncode, 0, ready.stderr)
        self.assertEqual(json.loads(ready.stdout)["status"], "ready")
        bad = call("--manuscript", "absent.md", "--explicit-expert", "--available-model", "gpt-6-astra", "--context-isolation")
        self.assertEqual(bad.returncode, 2)
        self.assertIn("error", json.loads(bad.stderr))


if __name__ == "__main__":
    unittest.main()
