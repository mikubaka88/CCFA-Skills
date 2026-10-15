#!/usr/bin/env python3
"""Behavioral regression cases for the read-only continuity checker."""

from __future__ import annotations

from copy import deepcopy
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

import continuity


def record() -> dict:
    return {
        "version": 1,
        "task_id": "paper-revision",
        "goal": {
            "revision": 1,
            "objective": "Revise the supplied paper without inventing results.",
            "source": "user:request-1",
            "constraints": ["Preserve verified measurements."],
            "acceptance": ["Requested sections revised; supplied measurements retained."],
        },
        "route": {"id": "revise", "summary": "Use the supplied draft and evidence."},
        "phase": "drafting",
        "mode": "normal",
        "next_action": "Revise the method section.",
    }


def change(kind: str, basis: str, **extra: str) -> dict:
    return {"kind": kind, "basis": basis, "reason": "Apply the current supported decision.",
            "evidence": ["user:request-2"], **extra}


def artifact(status: str = "verified") -> dict:
    return {"path": "paper/method.tex", "revision": "draft-1", "status": status,
            "evidence": ["review:method-draft-1"] if status == "verified" else []}


class TransitionTests(unittest.TestCase):
    def codes(self, current: object, previous: object = continuity._MISSING) -> set[str]:
        return {issue["code"] for issue in continuity.check_records(current, previous)}

    def test_minimal_record_and_ordinary_progress_need_no_change_log(self) -> None:
        previous = record()
        current = deepcopy(previous)
        current["phase"] = "checking"
        current["next_action"] = "Check supplied measurements in the edited section."
        self.assertEqual(self.codes(previous), set())
        self.assertEqual(self.codes(current, previous), set())

    def test_another_task_cannot_replace_this_task(self) -> None:
        previous = record()
        current = deepcopy(previous)
        current["task_id"] = "unrelated-project"
        self.assertEqual(self.codes(current, previous), {"task_mismatch"})

    def test_silent_goal_drift_and_route_record_do_not_authorize_new_goal(self) -> None:
        previous = record()
        current = deepcopy(previous)
        current["goal"]["objective"] = "Provide general advice instead of the requested revision."
        current["changes"] = [change("route", "new_evidence")]
        self.assertEqual(self.codes(current, previous), {"goal_revision", "goal_change"})

    def test_explicit_user_goal_change_and_corrected_intent_are_allowed(self) -> None:
        previous = record()
        for basis in ("user_instruction", "intent_correction"):
            with self.subTest(basis=basis):
                current = deepcopy(previous)
                current["goal"].update(revision=2, objective="Revise only the introduction.",
                                       source="user:request-2")
                current["changes"] = [change("goal", basis)]
                self.assertEqual(self.codes(current, previous), set())

    def test_changed_acceptance_requires_explicit_goal_revision(self) -> None:
        previous = record()
        current = deepcopy(previous)
        current["goal"]["acceptance"] = ["Return an outline instead of revised sections."]
        current["goal"]["revision"] = 2
        current["changes"] = [change("goal", "comparison")]
        self.assertEqual(self.codes(current, previous), {"goal_change"})

    def test_mistaken_acceptance_can_be_corrected_against_the_same_request(self) -> None:
        previous = record()
        current = deepcopy(previous)
        current["goal"]["revision"] = 2
        current["goal"]["acceptance"] = ["Revise the requested sections without requiring unrequested new experiments."]
        current["changes"] = [change("goal", "intent_correction")]
        self.assertEqual(self.codes(current, previous), set())
        current["changes"][0]["basis"] = "new_evidence"
        self.assertEqual(self.codes(current, previous), {"goal_change"})

    def test_revisions_do_not_go_backwards(self) -> None:
        previous = record()
        previous["goal"]["revision"] = 2
        current = record()
        self.assertEqual(self.codes(current, previous), {"goal_revision"})
        current["goal"]["revision"] = 3
        self.assertEqual(self.codes(current, previous), set())

    def test_evidence_based_route_change_does_not_need_a_new_goal(self) -> None:
        previous = record()
        current = deepcopy(previous)
        current["route"] = {"id": "reconcile-source", "summary": "Use the corrected source table."}
        self.assertEqual(self.codes(current, previous), {"route_change"})
        for basis in ("user_instruction", "intent_correction", "new_evidence", "verified_failure", "comparison"):
            with self.subTest(basis=basis):
                current["changes"] = [change("route", basis)]
                self.assertEqual(self.codes(current, previous), set())

    def test_one_declared_relevant_check_allows_recovery(self) -> None:
        for old_mode in ("focused", "reconciling"):
            with self.subTest(old_mode=old_mode):
                previous = record()
                previous["mode"] = old_mode
                current = record()
                self.assertEqual(self.codes(current, previous), {"recovery"})
                current["changes"] = [change("recovery", "recovery_check")]
                self.assertEqual(self.codes(current, previous), set())

    def test_focused_entry_and_initial_record_do_not_require_recovery(self) -> None:
        previous = record()
        current = deepcopy(previous)
        current["mode"] = "focused"
        self.assertEqual(self.codes(current, previous), set())
        self.assertEqual(self.codes(record()), set())

    def test_old_transition_declaration_cannot_be_replayed(self) -> None:
        previous = record()
        previous["changes"] = [change("route", "new_evidence")]
        current = deepcopy(previous)
        current["route"]["summary"] = "Apply a different source correction."
        self.assertEqual(self.codes(current, previous), {"route_change"})
        current["changes"][0]["evidence"] = ["source:corrected-table-v2"]
        self.assertEqual(self.codes(current, previous), set())

    def test_verified_artifacts_cannot_silently_disappear(self) -> None:
        previous = record()
        previous["artifacts"] = [artifact()]
        current = record()
        self.assertEqual(self.codes(current, previous), {"artifact_retirement"})
        current["changes"] = [change("artifact_retirement", "user_instruction", artifact="wrong.tex")]
        self.assertEqual(self.codes(current, previous), {"artifact_retirement"})
        current["changes"][0]["artifact"] = "paper/method.tex"
        self.assertEqual(self.codes(current, previous), set())

    def test_changed_artifact_can_be_reopened_for_validation(self) -> None:
        previous = record()
        previous["artifacts"] = [artifact()]
        current = deepcopy(previous)
        current["artifacts"][0].update(revision="draft-2", status="executed", evidence=[])
        self.assertEqual(self.codes(current, previous), set())

    def test_changed_verified_revision_needs_a_fresh_check_reference(self) -> None:
        previous = record()
        previous["artifacts"] = [artifact()]
        previous["artifacts"][0]["evidence"].append("review:measurements-draft-1")
        current = deepcopy(previous)
        current["artifacts"][0]["revision"] = "draft-2"
        for evidence in (previous["artifacts"][0]["evidence"],
                         list(reversed(previous["artifacts"][0]["evidence"])),
                         previous["artifacts"][0]["evidence"][:1]):
            with self.subTest(evidence=evidence):
                current["artifacts"][0]["evidence"] = evidence
                self.assertEqual(self.codes(current, previous), {"artifact_reverification"})
        current["artifacts"][0]["evidence"] = [*previous["artifacts"][0]["evidence"], "review:method-draft-2"]
        self.assertEqual(self.codes(current, previous), set())

    def test_changed_revision_may_reopen_without_erasing_prior_evidence(self) -> None:
        previous = record()
        previous["artifacts"] = [artifact()]
        for status in ("proposed", "executed"):
            with self.subTest(status=status):
                current = deepcopy(previous)
                current["artifacts"][0].update(revision="draft-2", status=status)
                self.assertEqual(self.codes(current, previous), set())

    def test_new_verified_artifact_can_declare_its_first_check(self) -> None:
        previous = record()
        current = deepcopy(previous)
        current["artifacts"] = [artifact()]
        self.assertEqual(self.codes(current, previous), set())

    def test_verification_is_a_recorded_reference_not_a_file_existence_test(self) -> None:
        current = record()
        current["artifacts"] = [artifact()]
        self.assertEqual(self.codes(current), set())
        current["artifacts"][0]["evidence"] = []
        self.assertEqual(self.codes(current), {"schema"})

    def test_malformed_shapes_and_boolean_integers_are_rejected(self) -> None:
        cases = [None, [], {**record(), "version": True}, {**record(), "artifacts": {}},
                 {**record(), "changes": ["done"]}, {**record(), "unknown": "value"}]
        bad_goal = record()
        bad_goal["goal"]["revision"] = True
        cases.append(bad_goal)
        empty_criteria = record()
        empty_criteria["goal"]["acceptance"] = []
        cases.append(empty_criteria)
        duplicate = record()
        duplicate["artifacts"] = [artifact(), artifact()]
        cases.append(duplicate)
        for current in cases:
            with self.subTest(current=current):
                self.assertIn("schema", self.codes(current))
        self.assertIn("schema", self.codes(record(), None))


class CommandTests(unittest.TestCase):
    def invoke(self, args: list[str], data: bytes | None = None) -> tuple[int, dict]:
        result = subprocess.run([sys.executable, "-B", str(Path(continuity.__file__)), "check", *args],
                                input=data, capture_output=True, check=False)
        self.assertEqual(result.stderr, b"")
        return result.returncode, json.loads(result.stdout.decode("utf-8"))

    def test_utf8_bom_chinese_paths_and_read_only_comparison(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            path = root / "任务状态.json"
            previous = record()
            previous["goal"]["objective"] = "根据原稿修改方法部分，保留已验证的结果。"
            raw = b"\xef\xbb\xbf" + json.dumps(previous, ensure_ascii=False).encode("utf-8")
            path.write_bytes(raw)
            current = deepcopy(previous)
            current["route"]["summary"] = "先核对更新后的中文原始记录。"
            current["changes"] = [change("route", "new_evidence")]
            before = sorted(root.iterdir())
            code, output = self.invoke(["-", "--previous", str(path)],
                                       json.dumps(current, ensure_ascii=False).encode("utf-8"))
            self.assertEqual(code, 0)
            self.assertEqual(output, {"ok": True, "scope": "recorded_consistency", "findings": []})
            self.assertEqual(path.read_bytes(), raw)
            self.assertEqual(sorted(root.iterdir()), before)

    def test_invalid_json_encoding_size_and_depth(self) -> None:
        bad_inputs = [b'{"version":1,"version":1}', b'{"goal":{"revision":1,"revision":2}}',
                      b'\xff', b'{', b'NaN', b'"\\ud800"', b' ' * (continuity.MAX_BYTES + 1),
                      b'[' * 40 + b'0' + b']' * 40]
        for data in bad_inputs:
            with self.subTest(data=data[:60]):
                code, output = self.invoke(["-"], data)
                self.assertEqual(code, 2)
                self.assertFalse(output["ok"])
                self.assertEqual(output["findings"][0]["code"], "input")

    def test_chinese_artifact_reference_survives_diagnostics(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "previous.json"
            previous = record()
            previous["artifacts"] = [{**artifact(), "path": "论文/方法.tex"}]
            path.write_text(json.dumps(previous, ensure_ascii=False), encoding="utf-8")
            code, output = self.invoke(["-", "--previous", str(path)], json.dumps(record()).encode("utf-8"))
            self.assertEqual(code, 1)
            self.assertIn("论文/方法.tex", output["findings"][0]["message"])

    def test_null_previous_is_invalid_instead_of_ignored(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "previous.json"
            path.write_text("null", encoding="utf-8")
            code, output = self.invoke(["-", "--previous", str(path)], json.dumps(record()).encode("utf-8"))
            self.assertEqual(code, 1)
            self.assertEqual(output["findings"][0]["path"], "$previous")

    def test_missing_input_returns_structured_read_error(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            code, output = self.invoke([str(Path(directory) / "missing.json")])
            self.assertEqual(code, 2)
            self.assertFalse(output["ok"])


if __name__ == "__main__":
    unittest.main()
