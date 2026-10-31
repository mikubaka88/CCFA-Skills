"""Outcome-anchor validation must never masquerade as semantic scoring."""
import unittest
import json
from pathlib import Path
from evaluate_outputs import check_outputs, model_requests


class OutputChecks(unittest.TestCase):
    def setUp(self):
        self.suite = {"tasks": [{"id": "numeric", "invariants": {"contains": ["42.1%", "47.3%", "citation-key"]}},
                                {"id": "concept", "invariants": {"contains": []}}]}
        self.answers = {"numeric": "Accuracy changes from 42.1% to 47.3% [citation-key].", "concept": "A coherent different mechanism."}

    def test_valid_anchors_do_not_invent_quality_score(self):
        result = check_outputs(self.suite, self.answers)
        self.assertTrue(result["factual_anchor_checks_pass"])
        self.assertIsNone(result["quality_score"])
        self.assertTrue(all(row["semantic_assessment_required"] for row in result["checks"]))

    def test_changed_value_fails_even_if_prose_is_fluent(self):
        self.answers["numeric"] = self.answers["numeric"].replace("47.3%", "49.3%")
        result = check_outputs(self.suite, self.answers)
        self.assertFalse(result["factual_anchor_checks_pass"])
        self.assertEqual(result["checks"][0]["missing_factual_anchors"], ["47.3%"])

    def test_missing_extra_and_empty_task_outputs_rejected(self):
        variants = [{"numeric": "text"}, {**self.answers, "unknown": "extra"}, {**self.answers, "concept": ""}]
        for output in variants:
            with self.assertRaises(ValueError):
                check_outputs(self.suite, output)

    def test_legitimate_output_variation_has_no_style_penalty(self):
        self.answers["concept"] = "Under the exact-model assumption, this suggests a different explanation."
        self.assertTrue(check_outputs(self.suite, self.answers)["factual_anchor_checks_pass"])

    def test_alternative_technical_spellings_are_anchors_not_a_style_template(self):
        self.suite["tasks"][1]["invariants"]["contains_any"] = [["finite-state", "finite state"], ["b_t", "bₜ"]]
        self.answers["concept"] = "The finite state assumption defines bₜ."
        self.assertTrue(check_outputs(self.suite, self.answers)["factual_anchor_checks_pass"])
        self.answers["concept"] = "The finite state assumption defines a distribution."
        result = check_outputs(self.suite, self.answers)
        self.assertFalse(result["factual_anchor_checks_pass"])
        self.assertEqual(result["checks"][1]["missing_anchor_alternatives"], [["b_t", "bₜ"]])

    def test_semantically_reversed_results_can_pass_anchors_but_remain_ungraded(self):
        self.suite["tasks"][0]["outcome_checks"] = ["Are baseline and method attributed correctly?"]
        self.suite["tasks"][0]["invariants"]["forbids_fabricated_results"] = True
        self.answers["numeric"] = "Baseline reaches 47.3% and our method reaches 42.1% [citation-key]."
        result = check_outputs(self.suite, self.answers)
        self.assertTrue(result["factual_anchor_checks_pass"])
        self.assertIsNone(result["quality_score"])
        row = result["checks"][0]
        self.assertTrue(row["semantic_assessment_required"])
        self.assertIn("Are baseline and method attributed correctly?", row["semantic_outcomes_to_check"])
        self.assertEqual(len(row["semantic_outcomes_to_check"]), 2)

    def test_preparation_omits_grading_fields_and_retains_raw_task_inputs(self):
        suite = {"execution": "No browsing; use supplied content.", "tasks": [{
            "id": "revision", "owner": "ccf-paper-writer", "request": "Update the manuscript.",
            "materials": {"abstract": "Raw source text"},
            "conversation": [{"role": "user", "content": "Original goal"}],
            "invariants": {"contains": ["hidden-anchor"]},
            "outcome_checks": ["hidden-outcome"], "quality_question": "hidden-rubric"}]}
        prepared = model_requests(suite)["revision"]
        self.assertEqual(set(prepared), {"execution", "owner", "request", "materials", "conversation"})
        self.assertEqual(prepared["materials"], suite["tasks"][0]["materials"])
        self.assertNotIn("hidden-", json.dumps(prepared))

    def test_duplicate_ids_and_malformed_anchor_groups_rejected(self):
        bad = [
            {"tasks": [self.suite["tasks"][0], self.suite["tasks"][0]]},
            {"tasks": [{"id": "concept", "invariants": {"contains_any": ["word"]}}]},
            {"tasks": [{"id": "concept", "invariants": {"contains_any": [[]]}}]},
            {"tasks": [{"id": "concept", "outcome_checks": "wrong"}]}
        ]
        for suite in bad:
            with self.subTest(suite=suite), self.assertRaises(ValueError):
                check_outputs(suite, {"concept": "answer"})

    def test_original_suite_and_archived_outputs_remain_compatible(self):
        directory = Path(__file__).parent
        suite = json.loads((directory / "tasks.json").read_text(encoding="utf-8"))
        archive = json.loads((directory / "results/0.12.0-smoke.json").read_text(encoding="utf-8"))
        self.assertEqual(len(suite["tasks"]), 4)
        for answers in archive["outputs"].values():
            self.assertTrue(check_outputs(suite, answers)["factual_anchor_checks_pass"])

    def test_integration_suite_has_distinct_unscored_outcome_checks(self):
        directory = Path(__file__).parent
        suite = json.loads((directory / "tasks-integration.json").read_text(encoding="utf-8"))
        prepared = model_requests(suite)
        self.assertEqual(len(prepared), 5)
        self.assertTrue(all(len(task.get("outcome_checks", [])) >= 3 for task in suite["tasks"]))
        self.assertIn("manuscript-method-change", prepared)
        self.assertIn("continue-after-context-drift", prepared)
        self.assertIn("limited-budget-codebase-choice", prepared)


if __name__ == "__main__":
    unittest.main()
