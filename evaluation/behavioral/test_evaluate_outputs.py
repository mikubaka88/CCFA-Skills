"""Outcome-anchor validation must never masquerade as semantic scoring."""
import unittest
from evaluate_outputs import check_outputs


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


if __name__ == "__main__":
    unittest.main()
