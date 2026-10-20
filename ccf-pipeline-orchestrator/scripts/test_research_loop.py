#!/usr/bin/env python3
"""Executable integration tests in isolated temporary projects; no model calls."""

import importlib.util
import json
import os
from pathlib import Path
import subprocess
import sys
import tempfile
import time
import unittest


SCRIPT = Path(__file__).with_name("research_loop.py")
SPEC = importlib.util.spec_from_file_location("research_loop", SCRIPT)
LOOP = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(LOOP)

EVALUATOR = """\
import json
from pathlib import Path
import sys
import time

metrics = Path(sys.argv[1])
config = json.loads(Path("candidate.json").read_text(encoding="utf-8"))
with Path("calls.log").open("a", encoding="utf-8") as log:
    log.write(config["kind"] + "\\n")
print("actual evaluator stdout", flush=True)
print("actual evaluator stderr", file=sys.stderr, flush=True)
kind = config["kind"]
if kind == "crash":
    sys.exit(7)
if kind == "timeout":
    time.sleep(20)
if kind == "wait":
    Path("started.flag").write_text("ready", encoding="utf-8")
    time.sleep(0.4)
if kind == "tamper":
    Path("evaluator.py").write_text("# changed evaluator", encoding="utf-8")
if kind == "mutate":
    Path("candidate.json").write_text('{"external": true}', encoding="utf-8")
if kind == "nan":
    metrics.write_text('{"score": NaN}', encoding="utf-8")
elif kind == "bool":
    metrics.write_text('{"score": true}', encoding="utf-8")
elif kind == "infinity":
    metrics.write_text('{"score": 1e999}', encoding="utf-8")
elif kind == "huge_integer":
    metrics.write_text('{"score": ' + "9" * 1000 + '}', encoding="utf-8")
elif kind == "duplicate":
    metrics.write_text('{"score": 1, "score": 99}', encoding="utf-8")
elif kind == "malformed":
    metrics.write_text("not json", encoding="utf-8")
else:
    data = json.loads(Path("data.json").read_text(encoding="utf-8"))
    metrics.write_text(json.dumps({"score": config["value"] + data["offset"]}), encoding="utf-8")
"""


class ResearchLoopTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory(prefix="ccfa-research-loop-")
        self.addCleanup(self.temp.cleanup)
        self.project = Path(self.temp.name)
        self.workdir = self.project / "ccfa-workfiles" / "experiments" / "mechanism-check"
        (self.project / "evaluator.py").write_text(EVALUATOR, encoding="utf-8")
        (self.project / "data.json").write_text('{"offset": 0}', encoding="utf-8")
        (self.project / "unmanaged.txt").write_text("existing uncommitted user work\n", encoding="utf-8")
        self.edit("normal", 10)
        self.original = (self.project / "candidate.json").read_bytes()
        self.contract = {
            "objective": "Improve the specified mechanism's measured score",
            "constraints": ["Preserve the fixed data and evaluator"],
            "scientific_value": "Test the supplied mechanism; score gains alone do not establish novelty",
            "editable_files": ["candidate.json", "optional.py"],
            "evaluator_files": ["evaluator.py"],
            "data_files": ["data.json"],
            "command": [sys.executable, "evaluator.py", "{metrics}"],
            "metric": {"name": "score", "direction": "max", "min_delta": 0.5},
            "budgets": {"max_attempts": 30, "max_seconds": 30, "timeout_seconds": 2},
        }
        self.contract_path = self.project / "contract-source.json"
        self.init()

    def init(self, workdir=None):
        # BOM compatibility covers contracts produced by common Windows editors.
        self.contract_path.write_text(json.dumps(self.contract, ensure_ascii=False), encoding="utf-8-sig")
        return LOOP.initialize(self.project, workdir or self.workdir, self.contract_path)

    def edit(self, kind, value=10):
        (self.project / "candidate.json").write_text(json.dumps({"kind": kind, "value": value}), encoding="utf-8")

    def calls(self):
        path = self.project / "calls.log"
        return path.read_text(encoding="utf-8").splitlines() if path.exists() else []

    def baseline(self):
        result = LOOP.run(self.workdir, "baseline")["attempt"]
        self.assertEqual(result["status"], "kept")
        self.assertEqual(result["metric"], 10)
        return result

    def test_good_bad_and_parent_identity(self):
        baseline = self.baseline()
        self.edit("normal", 12)
        good = LOOP.run(self.workdir, "mechanism-a", "Change the scoring mechanism")["attempt"]
        self.assertTrue(good["eligible"])
        self.assertEqual(good["parent"], "baseline")
        self.assertNotEqual(good["candidate_id"], baseline["candidate_id"])
        kept = LOOP.decide(self.workdir, "mechanism-a", "keep", "The specified mechanism improves the frozen measure")["attempt"]
        self.assertEqual(kept["status"], "kept")
        kept_bytes = (self.project / "candidate.json").read_bytes()
        self.edit("normal", 11)
        (self.project / "optional.py").write_text("candidate-only file\n", encoding="utf-8")
        bad = LOOP.run(self.workdir, "mechanism-b", "A competing update")["attempt"]
        self.assertFalse(bad["eligible"])
        with self.assertRaisesRegex(LOOP.LoopError, "frozen min_delta"):
            LOOP.decide(self.workdir, "mechanism-b", "keep", "Wanted this to win")
        LOOP.decide(self.workdir, "mechanism-b", "discard", "The candidate reduces the measured score")
        self.assertEqual((self.project / "candidate.json").read_bytes(), kept_bytes)
        self.assertFalse((self.project / "optional.py").exists())
        self.assertEqual((self.project / "unmanaged.txt").read_text(encoding="utf-8"), "existing uncommitted user work\n")
        state = LOOP.status(self.workdir)
        self.assertEqual(state["best"]["id"], "mechanism-a")
        self.assertEqual(state["best"]["hypothesis"], "Change the scoring mechanism")
        # A valid but worse measurement must survive compact context too,
        # not only runtime failures such as crashes.
        self.assertEqual(state["recent_decisions"][-1]["id"], "mechanism-b")
        self.assertEqual(state["recent_decisions"][-1]["decision"], "discard")
        self.assertEqual(state["recent_decisions"][-1]["reason"], "The candidate reduces the measured score")
        self.assertEqual(state["budget"]["attempts_used"], 3)
        self.assertIn("not measured", state["budget"]["meter_scope"])
        self.assertTrue((self.workdir / "attempts" / "mechanism-a" / "stdout.log").read_bytes())
        self.assertTrue((self.workdir / "attempts" / "mechanism-a" / "stderr.log").read_bytes())

    def test_crash_timeout_invalid_metrics_preserve_baseline(self):
        self.baseline()
        for kind in ("crash", "timeout", "nan", "bool", "infinity", "huge_integer", "duplicate", "malformed"):
            with self.subTest(kind=kind):
                self.edit(kind, 100)
                result = LOOP.run(self.workdir, kind, "Test a distinct failure")["attempt"]
                expected = kind if kind in ("crash", "timeout") else "invalid_metric"
                self.assertEqual(result["outcome"], expected)
                self.assertEqual(result["status"], "discarded")
                self.assertEqual((self.project / "candidate.json").read_bytes(), self.original)
                self.assertEqual(LOOP.status(self.workdir)["best"]["id"], "baseline")
        self.assertEqual(len(self.calls()), 9)

    def test_frozen_evaluator_and_data_changes_are_not_overwritten(self):
        self.baseline()
        self.edit("normal", 15)
        evaluator = self.project / "evaluator.py"
        evaluator.write_text("# user's new evaluator", encoding="utf-8")
        with self.assertRaisesRegex(LOOP.LoopError, "evaluator/data changed"):
            LOOP.run(self.workdir, "changed-evaluator", "An experiment with a changed evaluator")
        self.assertEqual(len(self.calls()), 1)
        self.assertEqual(evaluator.read_text(encoding="utf-8"), "# user's new evaluator")
        self.assertIn("integrity_error", (self.workdir / "events.jsonl").read_text(encoding="utf-8"))
        evaluator.write_text(EVALUATOR, encoding="utf-8")
        (self.project / "data.json").write_text('{"offset": 100}', encoding="utf-8")
        with self.assertRaises(LOOP.LoopError):
            LOOP.run(self.workdir, "changed-data", "Changed data cannot be compared")
        self.assertEqual(LOOP.status(self.workdir)["best"]["metric"], 10)
        (self.project / "data.json").write_text('{"offset": 0}', encoding="utf-8")
        self.edit("tamper", 100)
        result = LOOP.run(self.workdir, "during-run-tamper", "Evaluator integrity must also hold after execution")["attempt"]
        self.assertEqual(result["outcome"], "integrity_error")
        self.assertEqual(result["status"], "discarded")
        self.assertEqual(evaluator.read_text(encoding="utf-8"), "# changed evaluator")
        self.assertEqual((self.project / "candidate.json").read_bytes(), self.original)
        self.assertEqual(LOOP.status(self.workdir)["best"]["metric"], 10)

    def test_command_tampering_and_concurrent_edit_preservation(self):
        self.baseline()
        self.edit("mutate", 15)
        result = LOOP.run(self.workdir, "source-mutation", "Evaluator must not modify its inputs")["attempt"]
        self.assertEqual(result["outcome"], "integrity_error")
        self.assertEqual(result["status"], "rollback_conflict")
        self.assertEqual((self.project / "candidate.json").read_text(encoding="utf-8"), '{"external": true}')
        self.assertEqual(LOOP.status(self.workdir)["best"]["id"], "baseline")
        # Owner reconciles to the submitted candidate, then a discard is safe.
        self.edit("mutate", 15)
        LOOP.decide(self.workdir, "source-mutation", "discard", "External edit reconciled")
        self.edit("normal", 20)
        LOOP.run(self.workdir, "good", "Test a higher score")
        self.edit("normal", 21)
        with self.assertRaisesRegex(LOOP.LoopError, "changed after evaluation"):
            LOOP.decide(self.workdir, "good", "keep", "Must not keep unmeasured work")
        conflict = LOOP.decide(self.workdir, "good", "discard", "Preserve concurrent user work")["attempt"]
        self.assertEqual(conflict["status"], "rollback_conflict")
        self.assertEqual(json.loads((self.project / "candidate.json").read_text(encoding="utf-8"))["value"], 21)

    def test_resume_does_not_repeat_subprocess_or_decision(self):
        self.baseline()
        replay = LOOP.run(self.workdir, "baseline")
        self.assertTrue(replay["already_recorded"])
        self.assertEqual(len(self.calls()), 1)
        self.edit("normal", 13)
        LOOP.run(self.workdir, "new-candidate", "A measurable change")
        with self.assertRaisesRegex(LOOP.LoopError, "pending run"):
            LOOP.run(self.workdir, "another", "Do not skip the decision")
        # A fresh interpreter exercises on-disk recovery rather than in-memory state.
        command = [sys.executable, str(SCRIPT), "run", "--workdir", str(self.workdir), "--id", "new-candidate"]
        output = subprocess.run(command, capture_output=True, text=True, encoding="utf-8", check=True, timeout=5)
        self.assertTrue(json.loads(output.stdout)["already_recorded"])
        self.assertEqual(len(self.calls()), 2)
        LOOP.decide(self.workdir, "new-candidate", "discard", "No scientific value for this route")
        LOOP.decide(self.workdir, "new-candidate", "discard", "Repeat the same completed decision")
        self.assertEqual(len(self.calls()), 2)

    def test_process_interruption_has_explicit_recovery_without_reexecution(self):
        self.contract["budgets"].update(max_seconds=0.5, timeout_seconds=0.15)
        self.workdir = self.workdir.parent / "supervision-lost"
        self.init()
        self.baseline()
        self.edit("wait", 15)
        controller = subprocess.Popen(
            [sys.executable, str(SCRIPT), "run", "--workdir", str(self.workdir), "--id", "interrupted", "--hypothesis", "An interrupted evaluation"],
            stdout=subprocess.PIPE, stderr=subprocess.PIPE,
        )
        self.addCleanup(lambda: controller.kill() if controller.poll() is None else None)
        deadline = time.monotonic() + 5
        while not (self.project / "started.flag").exists() and time.monotonic() < deadline:
            time.sleep(0.01)
        self.assertTrue((self.project / "started.flag").exists())
        controller.kill()
        controller.communicate(timeout=5)
        # The evaluator exits itself; recovery never assumes parent death killed it.
        time.sleep(0.6)
        before = len(self.calls())
        replay = LOOP.run(self.workdir, "interrupted")
        self.assertEqual(replay["attempt"]["status"], "running")
        with self.assertRaisesRegex(LOOP.LoopError, "confirm-stopped"):
            LOOP.recover(self.workdir, "interrupted", "Controller terminated")
        result = LOOP.recover(self.workdir, "interrupted", "Checked that evaluator exited", True)["attempt"]
        self.assertEqual(result["outcome"], "interrupted")
        self.assertTrue(result["duration_unknown"])
        self.assertIsNone(result["elapsed_seconds"])
        self.assertIn("not measured runtime", result["budget_note"])
        self.assertEqual(len(self.calls()), before)
        self.assertEqual((self.project / "candidate.json").read_bytes(), self.original)
        status = LOOP.status(self.workdir)
        self.assertEqual(status["best"]["id"], "baseline")
        self.assertEqual(status["budget"]["execution_seconds_remaining"], 0)
        self.assertTrue(status["budget"]["duration_unknown"])
        self.edit("normal", 20)
        with self.assertRaisesRegex(LOOP.LoopError, "budget is exhausted"):
            LOOP.run(self.workdir, "after-unknown-duration", "Cannot reuse unmeasured remaining budget")
        self.assertEqual(len(self.calls()), before)

    def test_threshold_direction_budget_and_invalid_contracts(self):
        self.baseline()
        self.edit("normal", 10.5)
        result = LOOP.run(self.workdir, "within-noise", "Threshold boundary")["attempt"]
        self.assertFalse(result["eligible"])
        LOOP.decide(self.workdir, "within-noise", "discard", "Does not exceed the frozen noise threshold")
        self.contract["metric"]["direction"] = "min"
        self.contract["budgets"]["max_attempts"] = 2
        other = self.project / "ccfa-workfiles" / "experiments" / "minimize"
        self.init(other)
        LOOP.run(other, "baseline")
        self.edit("normal", 8)
        self.assertTrue(LOOP.run(other, "lower", "Lower is better under the frozen measure")["attempt"]["eligible"])
        LOOP.decide(other, "lower", "keep", "The measured cost decreased")
        self.edit("normal", 7)
        with self.assertRaisesRegex(LOOP.LoopError, "budget is exhausted"):
            LOOP.run(other, "over-budget", "Must not execute")
        for key, value in (("max_attempts", True), ("max_seconds", float("nan")), ("timeout_seconds", float("inf"))):
            raw = json.loads(json.dumps(self.contract))
            raw["budgets"][key] = value
            with self.assertRaises(LOOP.LoopError):
                LOOP._contract(raw)
        self.assertEqual(len(self.calls()), 4)

    def test_baseline_must_be_original_dirty_snapshot_and_failed_baseline_can_retry(self):
        self.edit("normal", 11)
        with self.assertRaisesRegex(LOOP.LoopError, "before editing"):
            LOOP.run(self.workdir, "premature")
        self.assertEqual(self.calls(), [])
        # A separate initialized dirty state is a valid baseline, never git HEAD.
        self.edit("crash", 17)
        other = self.project / "ccfa-workfiles" / "experiments" / "failed-baseline"
        self.init(other)
        result = LOOP.run(other, "baseline")["attempt"]
        self.assertEqual(result["outcome"], "crash")
        self.assertIsNone(LOOP.status(other)["best"])
        self.assertEqual(LOOP.run(other, "retry")["attempt"]["outcome"], "crash")
        self.assertEqual(self.calls(), ["crash", "crash"])

    def test_total_execution_budget_and_contract_hash_are_enforced(self):
        self.edit("timeout")
        self.contract["budgets"].update(max_seconds=0.2, timeout_seconds=2)
        other = self.project / "ccfa-workfiles" / "experiments" / "short-budget"
        self.init(other)
        result = LOOP.run(other, "baseline")["attempt"]
        self.assertEqual(result["outcome"], "timeout")
        self.assertAlmostEqual(result["reserved_seconds"], 0.2)
        self.assertGreaterEqual(result["elapsed_seconds"], 0.2)
        with self.assertRaisesRegex(LOOP.LoopError, "budget is exhausted"):
            LOOP.run(other, "cannot-retry")
        self.assertEqual(self.calls(), ["timeout"])
        # Contract changes cannot silently reset the experiment or relax limits.
        frozen = LOOP._json(self.workdir / "contract.json")
        frozen["objective"] = "Different objective"
        LOOP._write_json(self.workdir / "contract.json", frozen)
        with self.assertRaisesRegex(LOOP.LoopError, "Frozen contract changed"):
            LOOP.run(self.workdir, "switched-objective")
        self.assertIn("integrity_error", (self.workdir / "events.jsonl").read_text(encoding="utf-8"))

    def test_raw_metric_evidence_must_match_before_keep(self):
        self.baseline()
        self.edit("normal", 20)
        result = LOOP.run(self.workdir, "good-metric", "An improved candidate")["attempt"]
        metrics_path = self.workdir / result["metrics"]
        actual = metrics_path.read_bytes()
        metrics_path.write_text('{"score": 999}', encoding="utf-8")
        with self.assertRaisesRegex(LOOP.LoopError, "Raw metrics evidence changed"):
            LOOP.decide(self.workdir, "good-metric", "keep", "An edited evidence file must not pass")
        self.assertEqual(metrics_path.read_text(encoding="utf-8"), '{"score": 999}')
        self.assertEqual(LOOP.status(self.workdir)["best"]["id"], "baseline")
        metrics_path.unlink()
        with self.assertRaisesRegex(LOOP.LoopError, "Raw metrics evidence changed"):
            LOOP.decide(self.workdir, "good-metric", "keep", "Missing evidence must not pass")
        metrics_path.write_bytes(actual)
        self.assertEqual(LOOP.decide(self.workdir, "good-metric", "keep", "Original raw evidence restored")["attempt"]["status"], "kept")

    def test_large_integer_metric_preserves_single_count_improvement(self):
        self.edit("normal", 2**53)
        other = self.project / "ccfa-workfiles" / "experiments" / "integer-count"
        self.init(other)
        baseline = LOOP.run(other, "baseline")["attempt"]
        self.assertIsInstance(baseline["metric"], int)
        self.edit("normal", 2**53 + 1)
        candidate = LOOP.run(other, "one-more", "Improve the exact count by one")["attempt"]
        self.assertEqual(candidate["metric"], 2**53 + 1)
        self.assertEqual(candidate["improvement"], 1)
        self.assertTrue(candidate["eligible"])
        self.assertEqual(LOOP.decide(other, "one-more", "keep", "One measured count exceeds the fixed threshold")["attempt"]["status"], "kept")

    def test_input_file_hardlink_alias_is_rejected(self):
        alias = self.project / "alias.json"
        try:
            os.link(self.project / "candidate.json", alias)
        except OSError as exc:
            self.skipTest(f"Hardlinks unavailable: {exc}")
        self.contract["data_files"].append("alias.json")
        other = self.project / "ccfa-workfiles" / "experiments" / "hardlink-alias"
        with self.assertRaisesRegex(LOOP.LoopError, "different files"):
            self.init(other)
        self.assertFalse(other.exists())

    @unittest.skipUnless(os.name == "nt", "Windows case alias regression")
    def test_windows_case_alias_is_rejected(self):
        self.contract["data_files"].append("CANDIDATE.JSON")
        other = self.project / "ccfa-workfiles" / "experiments" / "case-alias"
        with self.assertRaisesRegex(LOOP.LoopError, "different files"):
            self.init(other)
        self.assertFalse(other.exists())

    def test_lock_serializes_writers_and_status_reads_live_run(self):
        self.baseline()
        with LOOP._lock(self.workdir):
            response = subprocess.run(
                [sys.executable, str(SCRIPT), "run", "--workdir", str(self.workdir), "--id", "blocked"],
                capture_output=True, text=True, encoding="utf-8", timeout=5,
            )
            self.assertEqual(response.returncode, 2)
            self.assertIn("Another process owns", response.stdout)
            self.assertEqual(LOOP.status(self.workdir)["best"]["id"], "baseline")
        self.assertEqual(len(self.calls()), 1)


if __name__ == "__main__":
    unittest.main(verbosity=2)
