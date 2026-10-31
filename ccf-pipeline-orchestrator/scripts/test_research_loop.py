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
from unittest.mock import patch


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
if kind in ("wait", "hold"):
    Path("started.flag").write_text("ready", encoding="utf-8")
    time.sleep(20 if kind == "hold" else 0.4)
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
    measurements = {"score": config["value"] + data["offset"]}
    measurements.update(config.get("extra_metrics", {}))
    metrics.write_text(json.dumps(measurements), encoding="utf-8")
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

    def fail_process_cache_once(self, run_id):
        """Fail after the process-start event commits, with a real child alive."""
        original = LOOP._write_json
        failed = False

        def write(path, value):
            nonlocal failed
            attempt = value.get("attempts", {}).get(run_id, {})
            if path.name == "state.json" and attempt.get("pid") and not failed:
                failed = True
                deadline = time.monotonic() + 5
                while not (self.project / "started.flag").exists() and time.monotonic() < deadline:
                    time.sleep(0.01)
                self.assertTrue((self.project / "started.flag").exists())
                raise OSError("Injected process-start cache write failure")
            return original(path, value)

        return patch.object(LOOP, "_write_json", side_effect=write)

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
        with self.assertRaisesRegex(LOOP.LoopError, "frozen selection rule"):
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
        self.assertEqual(state["recent_decisions"][-1]["outcome"], "ok")
        self.assertEqual(state["recent_decisions"][-1]["metrics"], bad["metrics"])
        self.assertEqual(state["recent_decisions"][-1]["snapshot"], bad["snapshot"])
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

    def test_recorded_run_reuse_checks_frozen_inputs_without_reexecution(self):
        self.baseline()
        original = (self.project / "evaluator.py").read_bytes()
        (self.project / "evaluator.py").write_text("# stale evaluator", encoding="utf-8")
        with self.assertRaisesRegex(LOOP.LoopError, "Frozen evaluator/data changed"):
            LOOP.run(self.workdir, "baseline")
        self.assertEqual(len(self.calls()), 1)
        self.assertEqual(LOOP.status(self.workdir)["budget"]["attempts_used"], 1)
        (self.project / "evaluator.py").write_bytes(original)
        self.assertTrue(LOOP.run(self.workdir, "baseline")["already_recorded"])
        self.assertEqual(len(self.calls()), 1)

    def test_historical_recorded_run_reuse_checks_its_own_evidence(self):
        original = self.baseline()
        self.edit("normal", 15)
        LOOP.run(self.workdir, "better", "Test the revised mechanism")
        LOOP.decide(self.workdir, "better", "keep", "Measured improvement under the unchanged protocol")
        metrics = self.workdir / original["metrics"]
        saved = metrics.read_bytes()
        metrics.write_text('{"score": 999}', encoding="utf-8")
        # The current best remains valid, so checking only it would miss this.
        self.assertEqual(LOOP.status(self.workdir)["integrity"], "ok")
        with self.assertRaisesRegex(LOOP.LoopError, "Raw metrics evidence changed.*baseline"):
            LOOP.run(self.workdir, "baseline")
        with self.assertRaisesRegex(LOOP.LoopError, "Raw metrics evidence changed.*baseline"):
            LOOP.decide(self.workdir, "baseline", "keep", "Repeat the recorded decision")
        metrics.write_bytes(saved)
        LOOP.note(self.workdir, "baseline", "invalid_comparison", "The earlier interpretation is disputed",
                  "Inspect the original protocol", [original["metrics"]])
        with self.assertRaisesRegex(LOOP.LoopError, "Recorded evaluation was marked invalid"):
            LOOP.run(self.workdir, "baseline")
        with self.assertRaisesRegex(LOOP.LoopError, "Recorded evaluation was marked invalid"):
            LOOP.decide(self.workdir, "baseline", "keep", "Repeat the recorded decision")
        self.assertEqual(len(self.calls()), 2)
        self.assertEqual(LOOP.status(self.workdir)["budget"]["attempts_used"], 2)

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

    def test_controller_io_failure_stops_child_before_rollback(self):
        self.baseline()
        self.edit("hold", 15)
        stopped = []
        original_stop = LOOP._stop

        def stop(process):
            stopped.append(process)
            return original_stop(process)

        with self.fail_process_cache_once("cache-error"), patch.object(LOOP, "_stop", side_effect=stop):
            result = LOOP.run(self.workdir, "cache-error", "Exercise a controller write failure")["attempt"]
        self.assertEqual(len(stopped), 1)
        self.assertIsNotNone(stopped[0].poll())
        self.assertEqual(result["outcome"], "controller_error")
        self.assertIn("Controller I/O failed", result["error"])
        self.assertEqual(result["status"], "discarded")
        self.assertGreater(result["elapsed_seconds"], 0)
        self.assertFalse((self.workdir / result["metrics"]).exists())
        self.assertEqual((self.project / "candidate.json").read_bytes(), self.original)
        state = LOOP.status(self.workdir)
        self.assertIsNone(state["pending"])
        self.assertEqual(state["best"]["id"], "baseline")
        self.assertFalse(state["budget"]["duration_unknown"])
        self.assertEqual(state["recent_failures"][-1]["outcome"], "controller_error")
        self.assertTrue(LOOP.run(self.workdir, "cache-error")["already_recorded"])
        self.assertEqual(self.calls(), ["normal", "hold"])

    def test_controller_io_failure_with_unconfirmed_stop_preserves_pending(self):
        self.baseline()
        charged_before = LOOP.status(self.workdir)["budget"]["execution_seconds_charged"]
        self.edit("hold", 15)
        submitted = (self.project / "candidate.json").read_bytes()
        children = []
        original_stop = LOOP._stop

        def unconfirmed_stop(process):
            children.append(process)
            self.addCleanup(lambda: original_stop(process) if process.poll() is None else None)
            raise LOOP.LoopError("Injected termination confirmation failure")

        with self.fail_process_cache_once("unconfirmed"), patch.object(LOOP, "_stop", side_effect=unconfirmed_stop):
            with self.assertRaisesRegex(LOOP.LoopError, "termination is unconfirmed; pending run retained"):
                LOOP.run(self.workdir, "unconfirmed", "Exercise loss of process supervision")
        self.assertEqual(len(children), 1)
        self.assertIsNone(children[0].poll())
        state = LOOP.status(self.workdir)
        self.assertEqual(state["pending"]["id"], "unconfirmed")
        self.assertEqual(state["pending"]["status"], "running")
        self.assertEqual(state["budget"]["execution_seconds_charged"], charged_before)
        self.assertEqual((self.project / "candidate.json").read_bytes(), submitted)
        self.assertTrue(LOOP.run(self.workdir, "unconfirmed")["already_recorded"])
        self.assertEqual(self.calls(), ["normal", "hold"])
        with self.assertRaisesRegex(LOOP.LoopError, "pending run"):
            LOOP.run(self.workdir, "must-not-start", "Do not overlap the live evaluator")
        original_stop(children[0])
        recovered = LOOP.recover(self.workdir, "unconfirmed", "Confirmed the evaluator has stopped", True)["attempt"]
        self.assertEqual(recovered["status"], "discarded")
        self.assertIsNone(recovered["elapsed_seconds"])
        self.assertTrue(recovered["duration_unknown"])
        self.assertEqual((self.project / "candidate.json").read_bytes(), self.original)
        self.assertEqual(LOOP.status(self.workdir)["budget"]["execution_seconds_remaining"], 0)

    @unittest.skipUnless(os.name == "nt", "Windows process-tree termination regression")
    def test_timeout_with_failed_tree_termination_requires_explicit_recovery(self):
        self.baseline()
        self.edit("hold", 15)
        submitted = (self.project / "candidate.json").read_bytes()
        children = []
        original_stop = LOOP._stop

        def stop(process):
            children.append(process)
            self.addCleanup(lambda: process.kill() if process.poll() is None else None)
            return original_stop(process)

        # The real foreground evaluator times out; the injected OS tool failure
        # cannot confirm that its workers stopped even after the parent is killed.
        failed_taskkill = subprocess.CompletedProcess(["taskkill"], 5, b"", b"access denied")
        with patch.object(LOOP.subprocess, "run", return_value=failed_taskkill), patch.object(LOOP, "_stop", side_effect=stop):
            with self.assertRaisesRegex(LOOP.LoopError, "process-tree termination is unconfirmed"):
                LOOP.run(self.workdir, "tree-unconfirmed", "Exercise failed process-tree termination")
        self.assertEqual(len(children), 1)
        self.assertIsNotNone(children[0].poll())
        self.assertEqual((self.project / "candidate.json").read_bytes(), submitted)
        state = LOOP.status(self.workdir)
        self.assertEqual(state["pending"]["status"], "running")
        self.assertIn("inspect process", state["next_action"])
        # A second integrity issue must not hide the still-needed process check.
        (self.project / "evaluator.py").write_text("# external evaluator change", encoding="utf-8")
        state = LOOP.status(self.workdir)
        self.assertIn("inspect process", state["next_action"])
        self.assertIn("resolve recorded protocol", state["next_action"])
        (self.project / "evaluator.py").write_text(EVALUATOR, encoding="utf-8")
        recovered = LOOP.recover(self.workdir, "tree-unconfirmed", "Confirmed the controlled evaluator and all workers stopped", True)["attempt"]
        self.assertEqual(recovered["status"], "discarded")
        self.assertTrue(recovered["duration_unknown"])
        self.assertEqual((self.project / "candidate.json").read_bytes(), self.original)
        self.assertEqual(LOOP.status(self.workdir)["budget"]["execution_seconds_remaining"], 0)
        self.assertEqual(self.calls(), ["normal", "hold"])

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

    def test_retained_baseline_evidence_is_required_for_run_and_keep(self):
        baseline = self.baseline()
        metrics_path = self.workdir / baseline["metrics"]
        original = metrics_path.read_bytes()
        self.edit("normal", 20)
        metrics_path.write_text('{"score": 999}', encoding="utf-8")
        with self.assertRaisesRegex(LOOP.LoopError, "Raw metrics evidence changed.*baseline"):
            LOOP.run(self.workdir, "blocked-comparison", "A comparison needs the retained baseline evidence")
        self.assertEqual(self.calls(), ["normal"])
        self.assertEqual(LOOP.status(self.workdir)["budget"]["attempts_used"], 1)
        self.assertIn("Raw metrics evidence changed", LOOP.status(self.workdir)["integrity"])
        metrics_path.write_bytes(original)
        LOOP.run(self.workdir, "candidate", "Test a measured improvement")
        metrics_path.unlink()
        with self.assertRaisesRegex(LOOP.LoopError, "Raw metrics evidence changed.*baseline"):
            LOOP.decide(self.workdir, "candidate", "keep", "Both sides of the comparison need evidence")
        self.assertEqual(LOOP.status(self.workdir)["best"]["id"], "baseline")
        metrics_path.write_bytes(original)
        self.assertEqual(LOOP.decide(self.workdir, "candidate", "keep", "Original comparison evidence restored")["attempt"]["status"], "kept")

    def test_evaluated_transaction_recovery_preserves_known_cost_and_evidence(self):
        self.baseline()
        self.edit("normal", 20)
        original_write = LOOP._write_json
        failed = False

        def fail_after_run_finished(path, value):
            nonlocal failed
            attempt = value.get("attempts", {}).get("evaluated", {})
            if path.name == "state.json" and attempt.get("status") == "evaluated" and not failed:
                failed = True
                raise OSError("Injected cache failure after completed evaluation")
            return original_write(path, value)

        with patch.object(LOOP, "_write_json", side_effect=fail_after_run_finished):
            with self.assertRaisesRegex(OSError, "completed evaluation"):
                LOOP.run(self.workdir, "evaluated", "Keep completed execution distinct from an unfinished decision")
        before = LOOP.status(self.workdir)
        self.assertEqual(before["pending"]["status"], "evaluated")
        self.assertIn("recover the unfinished transaction", before["next_action"])
        charged = before["budget"]["execution_seconds_charged"]
        result = LOOP.recover(self.workdir, "evaluated", "Confirmed the evaluator exited and inspected the complete metrics", True)["attempt"]
        self.assertEqual(result["status"], "discarded")
        self.assertEqual(result["outcome"], "ok")
        self.assertEqual(result["metric"], 20)
        self.assertTrue((self.workdir / result["metrics"]).exists())
        self.assertEqual(LOOP.status(self.workdir)["budget"]["execution_seconds_charged"], charged)
        self.assertFalse(LOOP.status(self.workdir)["budget"]["duration_unknown"])
        self.assertEqual((self.project / "candidate.json").read_bytes(), self.original)
        self.assertEqual(self.calls(), ["normal", "normal"])

    def test_repeated_valid_candidate_records_prior_evidence_without_blocking_replication(self):
        self.baseline()
        self.edit("normal", 9)
        first = LOOP.run(self.workdir, "negative", "Test an alternative mechanism")["attempt"]
        self.assertEqual(first["previous_evaluations"], [])
        LOOP.decide(self.workdir, "negative", "discard", "The valid measurement does not improve the baseline")
        self.edit("normal", 9)
        repeat = LOOP.run(self.workdir, "negative-repeat", "Repeat the fixed protocol to assess measurement variability")["attempt"]
        self.assertEqual(repeat["previous_evaluations"], ["negative"])
        self.assertFalse(repeat["eligible"])
        self.assertEqual(repeat["outcome"], "ok")
        self.assertEqual(LOOP.status(self.workdir)["budget"]["attempts_used"], 3)
        self.assertEqual(len(self.calls()), 3)

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



    def metrics_candidate(self, value=10, **extra):
        (self.project / "candidate.json").write_text(json.dumps({
            "kind": "normal", "value": value, "extra_metrics": extra}), encoding="utf-8")

    def test_metric_guards_block_scalar_gaming_but_preserve_negative_result(self):
        self.contract["metric_guards"] = [{"name": "accuracy", "min": .8}]
        self.metrics_candidate(10, accuracy=.9)
        work = self.project / "guarded"
        self.init(work)
        LOOP.run(work, "baseline")
        self.metrics_candidate(20, accuracy=.5)
        attempt = LOOP.run(work, "constant", "Constant prediction improves the scalar")["attempt"]
        self.assertEqual(attempt["outcome"], "ok")
        self.assertFalse(attempt["eligible"])
        self.assertEqual(attempt["guard_failures"], ["accuracy"])
        with self.assertRaises(LOOP.LoopError):
            LOOP.decide(work, "constant", "keep", "Scalar is larger")
        LOOP.note(work, "constant", "negative_result", "Accuracy falls below the fixed floor",
                  "Restore useful predictions", [attempt["metrics"]])
        LOOP.decide(work, "constant", "discard", "Fails the accuracy requirement")
        self.assertEqual(LOOP.status(work)["best"]["id"], "baseline")

    def test_missing_guard_measurement_cannot_establish_baseline(self):
        self.contract["metric_guards"] = [{"name": "accuracy", "min": .8}]
        work = self.project / "missing"
        self.init(work)
        attempt = LOOP.run(work, "baseline")["attempt"]
        self.assertEqual(attempt["outcome"], "invalid_metric")
        self.assertIsNone(LOOP.status(work)["best"])

    def test_tie_breaker_allows_simplification_without_cumulative_quality_drift(self):
        self.contract["tie_breaker"] = {
            "name": "cost", "direction": "min", "min_delta": 0, "max_primary_loss": 1}
        self.metrics_candidate(10, cost=10)
        work = self.project / "cost-aware"
        self.init(work)
        LOOP.run(work, "baseline")
        self.metrics_candidate(10, cost=8)
        self.assertTrue(LOOP.run(work, "simpler", "Same quality with less cost")["attempt"]["eligible"])
        LOOP.decide(work, "simpler", "keep", "Quality retained and cost reduced")
        self.metrics_candidate(9, cost=6)
        self.assertTrue(LOOP.run(work, "trade", "Use the agreed quality tolerance")["attempt"]["eligible"])
        LOOP.decide(work, "trade", "keep", "Within the frozen tolerance")
        self.metrics_candidate(8, cost=4)
        attempt = LOOP.run(work, "drift", "A further one-point loss")["attempt"]
        self.assertFalse(attempt["eligible"])
        with self.assertRaises(LOOP.LoopError):
            LOOP.decide(work, "drift", "keep", "Only one lower than last time")

    def test_optional_selection_contract_rejects_ambiguous_bounds(self):
        import copy
        bad = [
            {"metric_guards": [{"name": "accuracy", "min": True}]},
            {"metric_guards": [{"name": "accuracy", "min": 2, "max": 1}]},
            {"metric_guards": [{"name": "accuracy", "min": 0}, {"name": "accuracy", "max": 1}]},
            {"tie_breaker": {"name": "score", "direction": "min", "min_delta": 0, "max_primary_loss": 0}},
            {"tie_breaker": {"name": "cost", "direction": "min", "min_delta": 0, "max_primary_loss": -1}},
        ]
        for extension in bad:
            with self.subTest(extension=extension), self.assertRaises(LOOP.LoopError):
                LOOP._contract(dict(copy.deepcopy(self.contract), **extension))

    def test_observation_survives_resume_without_rewriting_measurement_or_budget(self):
        self.baseline()
        self.edit("normal", 9)
        attempt = LOOP.run(self.workdir, "sparse", "稀疏记忆 removes needed history")["attempt"]
        LOOP.decide(self.workdir, "sparse", "discard", "Prediction did not improve")
        before = LOOP.status(self.workdir)
        raw = (self.workdir / attempt["metrics"]).read_bytes()
        LOOP.note(self.workdir, "sparse", "negative_result", "稀疏记忆 loses useful context",
                  "Test selective retrieval", [attempt["metrics"]])
        result = LOOP.context(self.workdir, "稀疏记忆", 1)
        self.assertEqual(result["related_attempts"][0]["id"], "sparse")
        self.assertEqual(result["related_attempts"][0]["observation"]["origin"], "host_interpretation")
        self.assertEqual(result["related_attempts"][0]["evidence_issues"], [])
        self.assertEqual(result["budget"], before["budget"])
        self.assertEqual((self.workdir / attempt["metrics"]).read_bytes(), raw)
        self.assertEqual(len(self.calls()), 2)
        events_before = (self.workdir / "events.jsonl").read_bytes()
        self.assertTrue(LOOP.note(self.workdir, "sparse", "negative_result",
                        "稀疏记忆 loses useful context", "Test selective retrieval",
                        [attempt["metrics"]])["already_recorded"])
        self.assertEqual((self.workdir / "events.jsonl").read_bytes(), events_before)
        cp = subprocess.run([sys.executable, str(SCRIPT), "context", "--workdir",
                             str(self.workdir), "--query", "稀疏记忆", "--limit", "1"],
                            capture_output=True, text=True, encoding="utf-8")
        self.assertEqual(cp.returncode, 0, cp.stdout + cp.stderr)
        self.assertEqual(json.loads(cp.stdout)["related_attempts"][0]["metric"], 9)

    def test_failed_execution_is_not_negative_science_and_evidence_must_exist(self):
        self.baseline()
        self.edit("crash")
        attempt = LOOP.run(self.workdir, "broken", "A broken implementation")["attempt"]
        with self.assertRaisesRegex(LOOP.LoopError, "not a scientific result"):
            LOOP.note(self.workdir, "broken", "negative_result", "Hypothesis fails",
                      "Change theory", [attempt["stderr"]])
        with self.assertRaises(LOOP.LoopError):
            LOOP.note(self.workdir, "broken", "implementation_error", "Exit 7",
                      "Fix implementation", ["../unmanaged.txt"])
        LOOP.note(self.workdir, "broken", "implementation_error", "Exit 7",
                  "Fix implementation", [attempt["stderr"]])
        (self.workdir / attempt["stderr"]).write_text("changed later", encoding="utf-8")
        result = LOOP.context(self.workdir, "broken")
        self.assertTrue(result["related_attempts"][0]["evidence_issues"])

    def test_invalid_baseline_interpretation_prevents_further_comparisons(self):
        attempt = self.baseline()
        LOOP.note(self.workdir, "baseline", "invalid_comparison", "Observed split mismatch",
                  "Establish a corrected protocol", [attempt["metrics"]])
        self.assertIn("marked invalid", LOOP.status(self.workdir)["integrity"])
        self.edit("normal", 12)
        with self.assertRaisesRegex(LOOP.LoopError, "marked invalid"):
            LOOP.run(self.workdir, "candidate", "Continue with invalid baseline")
        self.assertEqual(len(self.calls()), 1)



    def test_invalidation_requires_explicit_correction_and_includes_environment(self):
        attempt = self.baseline()
        invalid = LOOP.note(self.workdir, "baseline", "environment_error",
                            "The environment record needs reinspection", "Inspect configuration",
                            [attempt["metrics"]])["attempt"]["invalidated_by"]
        self.assertIn("marked invalid", LOOP.status(self.workdir)["integrity"])
        LOOP.note(self.workdir, "baseline", "supports_prediction", "A positive interpretation",
                  "Continue", [attempt["metrics"]])
        self.assertIn("marked invalid", LOOP.status(self.workdir)["integrity"])
        with self.assertRaises(LOOP.LoopError):
            LOOP.note(self.workdir, "baseline", "supports_prediction",
                      "Correction after reinspection", "Continue", [attempt["metrics"]], corrects=invalid + 1)
        LOOP.note(self.workdir, "baseline", "supports_prediction",
                  "Reinspection found the earlier environment classification mistaken; the recorded result applies",
                  "Continue under the unchanged protocol", [attempt["metrics"]], corrects=invalid)
        self.assertEqual(LOOP.status(self.workdir)["integrity"], "ok")
        self.assertEqual(len(self.calls()), 1)

    def test_historical_primary_anchor_evidence_is_checked(self):
        self.contract["tie_breaker"] = {
            "name": "cost", "direction": "min", "min_delta": 0, "max_primary_loss": 1}
        self.metrics_candidate(10, cost=10)
        work = self.project / "anchor-check"
        self.init(work)
        original = LOOP.run(work, "baseline")["attempt"]
        self.metrics_candidate(9, cost=8)
        LOOP.run(work, "cheaper", "Use the frozen tolerance")
        LOOP.decide(work, "cheaper", "keep", "Cost improved within allowance")
        (work / original["metrics"]).write_text('{"score":99,"cost":10}', encoding="utf-8")
        self.metrics_candidate(9, cost=7)
        with self.assertRaisesRegex(LOOP.LoopError, "Raw metrics"):
            LOOP.run(work, "next", "Another cheaper candidate")
        self.assertEqual(len(self.calls()), 2)

    def test_context_uses_one_event_snapshot(self):
        import copy
        self.baseline()
        original = LOOP._load(self.workdir)
        later = copy.deepcopy(original)
        later["seq"] += 1
        later["attempt_count"] += 1
        later["attempts"]["later"] = dict(later["attempts"]["baseline"], id="later")
        with patch.object(LOOP, "_load", side_effect=[original, later]) as load:
            result = LOOP.context(self.workdir, limit=20)
        self.assertEqual(load.call_count, 1)
        self.assertEqual(result["event_seq"], original["seq"])
        self.assertEqual(result["budget"]["attempts_used"], 1)
        self.assertEqual([item["id"] for item in result["related_attempts"]], ["baseline"])

    def test_explicit_incumbent_replication_records_noise_without_promotion(self):
        evaluator = EVALUATOR.replace('config["value"] + data["offset"]', 'config["value"] + data["offset"] + time.monotonic()')
        (self.project / "evaluator.py").write_text(evaluator, encoding="utf-8")
        work = self.project / "replication"
        self.init(work)
        original = LOOP.run(work, "baseline")["attempt"]
        repeated = LOOP.replicate(work, "repeat", "best", "Measure the incumbent again under the fixed protocol")["attempt"]
        self.assertEqual(repeated["status"], "reported")
        self.assertEqual(repeated["kind"], "replication")
        self.assertEqual(repeated["candidate_id"], original["candidate_id"])
        self.assertEqual(repeated["measurement_parent"], "baseline")
        self.assertGreater(repeated["metric"], original["metric"])
        self.assertEqual(LOOP.status(work)["best"]["metric"], original["metric"])
        self.assertEqual(LOOP.status(work)["budget"]["attempts_used"], 2)
        raw = json.loads((work / repeated["metrics"]).read_text(encoding="utf-8"))
        self.assertEqual(raw["score"], repeated["metric"])
        with self.assertRaisesRegex(LOOP.LoopError, "report-only"):
            LOOP.decide(work, "repeat", "keep", "A single high sample must not replace the incumbent")
        with self.assertRaisesRegex(LOOP.LoopError, "unchanged"):
            LOOP.run(work, "ordinary-repeat", "No explicit replication")
        with self.assertRaisesRegex(LOOP.LoopError, "reason"):
            LOOP.replicate(work, "no-reason", "baseline", "")

    def test_replication_of_prior_discarded_candidate_restores_incumbent(self):
        self.baseline()
        self.edit("normal", 9)
        measured = LOOP.run(self.workdir, "old", "Alternative mechanism")["attempt"]
        LOOP.decide(self.workdir, "old", "discard", "Negative measured result")
        with self.assertRaisesRegex(LOOP.LoopError, "identical"):
            LOOP.replicate(self.workdir, "wrong-bytes", "old", "Repeat prior measurement")
        self.edit("normal", 9)
        repeated = LOOP.replicate(self.workdir, "old-repeat", "old", "Check variability of the negative result")["attempt"]
        self.assertEqual(repeated["candidate_id"], measured["candidate_id"])
        self.assertEqual(repeated["status"], "reported")
        self.assertEqual((self.project / "candidate.json").read_bytes(), self.original)
        self.assertEqual(LOOP.status(self.workdir)["best"]["id"], "baseline")

    def test_literal_dependency_preflight_and_explicit_protected_files(self):
        (self.project / "helper.json").write_text('{"offset":0}', encoding="utf-8")
        evaluator = EVALUATOR.replace('data["offset"]', 'json.loads(Path("helper.json").read_text(encoding="utf-8"))["offset"]')
        (self.project / "evaluator.py").write_text(evaluator, encoding="utf-8")
        with self.assertRaisesRegex(LOOP.LoopError, "helper.json"):
            self.init(self.project / "missing-input")
        self.contract["protected_files"] = ["helper.json"]
        work = self.project / "closed-input"
        self.init(work)
        LOOP.run(work, "baseline")
        (self.project / "helper.json").write_text('{"offset":100}', encoding="utf-8")
        self.edit("normal", 11)
        with self.assertRaisesRegex(LOOP.LoopError, "Frozen evaluator/data"):
            LOOP.run(work, "changed-helper", "One-point candidate improvement")
        self.assertEqual(len(self.calls()), 1)

    def test_local_import_preflight_reports_and_can_be_declared(self):
        (self.project / "local_helper.py").write_text("OFFSET=0\n", encoding="utf-8")
        evaluator = "from local_helper import OFFSET\n" + EVALUATOR
        (self.project / "evaluator.py").write_text(evaluator, encoding="utf-8")
        with self.assertRaisesRegex(LOOP.LoopError, "local_helper.py"):
            self.init(self.project / "missing-import")
        self.contract["dependency_preflight"] = "report"
        report_work = self.project / "reported-import"
        result = self.init(report_work)
        self.assertEqual(result["declared_integrity"]["dependency_preflight"]["unlisted_local_inputs"][0]["path"], "local_helper.py")
        self.contract["protected_files"] = ["local_helper.py"]
        self.contract["dependency_preflight"] = "strict"
        self.init(self.project / "declared-import")

    def test_selected_environment_identity_is_checked(self):
        self.contract["environment"] = {"variables": ["CCFA_TEST_COMPARE_ID"]}
        work = self.project / "environment-check"
        with patch.dict(os.environ, {"CCFA_TEST_COMPARE_ID": "first"}):
            self.init(work)
            LOOP.run(work, "baseline")
        with patch.dict(os.environ, {"CCFA_TEST_COMPARE_ID": "changed"}):
            self.assertIn("environment identity changed", LOOP.status(work)["integrity"])
            with self.assertRaisesRegex(LOOP.LoopError, "environment identity changed"):
                LOOP.replicate(work, "repeat", "best", "Environment changed")
        state = LOOP._load(work)
        self.assertNotEqual(state["environment_identity"]["variables"]["CCFA_TEST_COMPARE_ID"], "first")

    def test_fast_status_and_context_skip_hashes_but_run_still_checks(self):
        self.baseline()
        with patch.object(LOOP, "_manifest", side_effect=AssertionError("data should not be rehashed")), \
                patch.object(LOOP, "_metric_evidence", side_effect=AssertionError("metrics should not be rehashed")):
            status = LOOP.status(self.workdir, fast=True)
            recall = LOOP.context(self.workdir, limit=1, fast=True)
        self.assertEqual(status["integrity"], "not_rechecked")
        self.assertIn("checked_at", status["last_verified"])
        self.assertFalse(recall["related_attempts"][0]["evidence_rechecked"])
        (self.project / "data.json").write_text('{"offset":999}', encoding="utf-8")
        self.assertEqual(LOOP.status(self.workdir, fast=True)["integrity"], "not_rechecked")
        with self.assertRaisesRegex(LOOP.LoopError, "Frozen evaluator/data"):
            LOOP.replicate(self.workdir, "stale-fast", "best", "A fast read does not authorize execution")
        cp = subprocess.run([sys.executable, str(SCRIPT), "status", "--workdir", str(self.workdir), "--fast"], capture_output=True, text=True, encoding="utf-8", timeout=5)
        self.assertEqual(cp.returncode, 0)
        self.assertFalse(json.loads(cp.stdout)["verification"]["rechecked"])

    def shared(self, attempts=3, seconds=5):
        record = self.project / "ccfa-workfiles" / "campaign" / "source" / "budget.json"
        LOOP.CAMPAIGN.initialize(record, self.project, "shared-research", attempts, seconds)
        self.contract["campaign"] = {"id": "shared-research", "record": record.relative_to(self.project).as_posix()}
        return record

    def test_nonempty_init_does_not_register_a_shared_task_set(self):
        record = self.shared()
        self.contract["evaluation"] = {"split_role": "selection", "task_set_id": "unused-selection"}
        occupied = self.project / "occupied"
        occupied.mkdir()
        (occupied / "user-notes.md").write_text("Keep this input", encoding="utf-8")
        before = record.read_bytes()
        with self.assertRaisesRegex(LOOP.LoopError, "not empty"):
            self.init(occupied)
        self.assertEqual(record.read_bytes(), before)
        self.assertEqual((occupied / "user-notes.md").read_text(encoding="utf-8"), "Keep this input")
        self.assertEqual(self.calls(), [])

    def test_snapshot_failure_leaves_campaign_registration_unchanged(self):
        record = self.shared()
        self.contract["evaluation"] = {"split_role": "selection", "task_set_id": "snapshot-not-created"}
        before = record.read_bytes()
        with patch.object(LOOP, "_snapshot", side_effect=OSError("Injected snapshot failure")):
            with self.assertRaisesRegex(OSError, "snapshot failure"):
                self.init(self.project / "failed-snapshot")
        self.assertEqual(record.read_bytes(), before)
        self.assertEqual(self.calls(), [])

    def test_committed_initialization_recovers_missing_shared_registration(self):
        record = self.shared()
        self.contract["evaluation"] = {"split_role": "selection", "task_set_id": "recover-init"}
        work = self.project / "recover-initial-registration"
        original = LOOP._write_json

        def fail_cache(path, value):
            if path.name == "state.json":
                raise OSError("Injected initialization cache failure")
            return original(path, value)

        with patch.object(LOOP, "_write_json", side_effect=fail_cache):
            with self.assertRaisesRegex(OSError, "initialization cache"):
                self.init(work)
        self.assertEqual(json.loads(record.read_text(encoding="utf-8"))["task_sets"], {})
        self.assertEqual(LOOP.status(work)["budget"]["attempts_used"], 0)
        result = LOOP.run(work, "baseline")["attempt"]
        self.assertEqual(result["status"], "kept")
        registered = json.loads(record.read_text(encoding="utf-8"))["task_sets"]["recover-init"]
        self.assertEqual(registered["workdirs"], [work.name])
        self.assertEqual(len(self.calls()), 1)

    def test_shared_registration_save_failure_can_resume_initialized_record(self):
        record = self.shared()
        self.contract["evaluation"] = {"split_role": "selection", "task_set_id": "recover-save"}
        work = self.project / "recover-registration-save"
        before = record.read_bytes()
        with patch.object(LOOP.CAMPAIGN, "_save", side_effect=OSError("Injected registration save failure")):
            with self.assertRaisesRegex(OSError, "registration save"):
                self.init(work)
        self.assertEqual(record.read_bytes(), before)
        self.assertEqual(LOOP.status(work)["budget"]["attempts_used"], 0)
        LOOP.run(work, "baseline")
        self.assertIn("recover-save", json.loads(record.read_text(encoding="utf-8"))["task_sets"])
        self.assertEqual(len(self.calls()), 1)

    def test_shared_attempt_budget_survives_contract_and_branch_changes(self):
        self.shared(attempts=1)
        first, second = self.project / "branch-one", self.project / "branch-two"
        self.init(first)
        LOOP.run(first, "baseline")
        self.contract["scientific_value"] = "A changed protocol cannot reset campaign allowance"
        self.init(second)
        with self.assertRaisesRegex(LOOP.LoopError, "Shared campaign.*exhausted"):
            LOOP.run(second, "baseline")
        self.assertFalse((second / "attempts" / "baseline").exists())
        result = LOOP.status(second)["campaign_budget"]
        self.assertEqual(result["attempts_used"], 1)
        self.assertIsNone(result["model_tokens"])

    def test_shared_reservations_are_atomic_and_pending_time_is_not_reused(self):
        record = self.shared(attempts=3, seconds=2)
        work = self.project / "branch"
        self.init(work)
        binding = (record, "shared-research", self.project)
        with LOOP.CAMPAIGN._lock(record):
            with self.assertRaises(LOOP.CAMPAIGN.CampaignError):
                LOOP.CAMPAIGN.reserve(*binding, "other:pending", 2, work, "pending")
        LOOP.CAMPAIGN.reserve(*binding, "other:pending", 2, work, "pending")
        with self.assertRaisesRegex(LOOP.LoopError, "Shared campaign.*exhausted"):
            LOOP.run(work, "baseline")
        LOOP.CAMPAIGN.settle(*binding, "other:pending", 0.0)
        LOOP.run(work, "baseline")
        result = LOOP.status(work)["campaign_budget"]
        self.assertEqual(result["attempts_used"], 2)
        self.assertEqual(result["execution_seconds_reserved"], 0)
        self.assertGreater(result["execution_seconds_charged"], 0)
        LOOP.run(work, "baseline")
        self.assertEqual(LOOP.status(work)["campaign_budget"]["attempts_used"], 2)
        with self.assertRaisesRegex(LOOP.CAMPAIGN.CampaignError, "already exists"):
            LOOP.CAMPAIGN.initialize(record, self.project, "shared-research", 999, 999)

    def test_shared_unknown_duration_closes_remaining_campaign_without_replay(self):
        record = self.shared(attempts=5, seconds=10)
        work = self.project / "interrupted-shared"
        self.init(work)
        LOOP.run(work, "baseline")
        self.edit("wait", 20)
        controller = subprocess.Popen([sys.executable, str(SCRIPT), "run", "--workdir", str(work), "--id", "interrupted", "--hypothesis", "Interrupted shared run"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        self.addCleanup(lambda: controller.kill() if controller.poll() is None else None)
        deadline = time.monotonic() + 5
        while not (self.project / "started.flag").exists() and time.monotonic() < deadline:
            time.sleep(0.01)
        self.assertTrue((self.project / "started.flag").exists())
        controller.kill(); controller.communicate(timeout=5)
        time.sleep(0.6)
        before = len(self.calls())
        LOOP.recover(work, "interrupted", "Confirmed foreground process and workers exited", True)
        result = LOOP.status(work)["campaign_budget"]
        self.assertTrue(result["duration_unknown"])
        self.assertEqual(result["execution_seconds_remaining"], 0)
        self.assertEqual(len(self.calls()), before)
        other = self.project / "after-interruption"
        self.init(other)
        with self.assertRaisesRegex(LOOP.LoopError, "Shared campaign.*exhausted"):
            LOOP.run(other, "baseline")

    def test_orphan_reservation_recovery_preserves_inputs_and_never_replays(self):
        record = self.shared(attempts=3, seconds=5)
        work = self.project / "orphan-reservation"
        self.init(work)
        key = LOOP._reservation_key(self.project, work, "lost-before-event")
        LOOP.CAMPAIGN.reserve(record, "shared-research", self.project, key, 1, work, "lost-before-event")
        with self.assertRaisesRegex(LOOP.LoopError, "already reserved"):
            LOOP.run(work, "lost-before-event")
        with self.assertRaisesRegex(LOOP.LoopError, "confirm-stopped"):
            LOOP.recover_reservation(work, "lost-before-event", "Inspect workers first")
        result = LOOP.recover_reservation(work, "lost-before-event", "Checked that no related process or worker remains", True)
        self.assertFalse(result["replayed"])
        self.assertTrue(result["campaign_budget"]["duration_unknown"])
        self.assertEqual(result["campaign_budget"]["execution_seconds_remaining"], 0)
        self.assertEqual(self.calls(), [])
        self.assertEqual((self.project / "candidate.json").read_bytes(), self.original)

    def test_shared_settlement_recovers_completed_event_after_cache_failure(self):
        self.shared(attempts=3)
        work = self.project / "shared-cache-recovery"
        self.init(work)
        LOOP.run(work, "baseline")
        self.edit("normal", 20)
        original_write = LOOP._write_json
        failed = False

        def fail_cache(path, value):
            nonlocal failed
            attempt = value.get("attempts", {}).get("complete", {})
            if path.name == "state.json" and attempt.get("status") == "evaluated" and not failed:
                failed = True
                raise OSError("Injected shared completed-event cache failure")
            return original_write(path, value)

        with patch.object(LOOP, "_write_json", side_effect=fail_cache):
            with self.assertRaisesRegex(OSError, "completed-event"):
                LOOP.run(work, "complete", "Known measured duration survives cache failure")
        before = len(self.calls())
        recovered = LOOP.recover(work, "complete", "Confirmed completed measurement and stopped workers", True)["attempt"]
        budget = LOOP.status(work)["campaign_budget"]
        self.assertEqual(recovered["outcome"], "ok")
        self.assertFalse(budget["duration_unknown"])
        self.assertEqual(budget["execution_seconds_reserved"], 0)
        self.assertEqual(len(self.calls()), before)

    def selection_and_final(self, final_samples=1):
        self.contract["evaluation"] = {"split_role": "selection", "task_set_id": "selection-v1"}
        selection = self.project / "selection-stage"
        self.init(selection)
        selected = LOOP.run(selection, "selected")["attempt"]
        (self.project / "final-data.json").write_text('{"offset":1}', encoding="utf-8")
        evaluator = EVALUATOR.replace('Path("data.json")', 'Path("final-data.json")')
        if final_samples > 1:
            evaluator = evaluator.replace(
                'measurements = {"score": config["value"] + data["offset"]}',
                f'samples = [config["value"] + data["offset"] for _ in range({final_samples})]\n'
                '    measurements = {"score": sum(samples) / len(samples), "sample_count": len(samples)}')
        (self.project / "final-evaluator.py").write_text(evaluator, encoding="utf-8")
        self.contract["data_files"] = ["final-data.json"]
        self.contract["evaluator_files"] = ["final-evaluator.py"]
        self.contract["command"] = [sys.executable, "final-evaluator.py", "{metrics}"]
        self.contract["evaluation"] = {"split_role": "final", "task_set_id": "final-v1",
                                       "frozen_candidate": {"workdir": selection.relative_to(self.project).as_posix(), "candidate_id": selected["candidate_id"]}}
        final = self.project / "final-stage"
        self.init(final)
        return selection, final, selected

    def test_final_only_reports_frozen_selection_candidate_and_closes(self):
        selection, final, selected = self.selection_and_final()
        result = LOOP.run(final, "held-out")["attempt"]
        self.assertEqual(result["kind"], "final")
        self.assertEqual(result["status"], "reported")
        self.assertFalse(result["eligible"])
        status = LOOP.status(final)
        self.assertIsNone(status["best"])
        self.assertEqual(status["finalized"], "held-out")
        self.assertEqual(result["evaluation"]["frozen_candidate"]["candidate_id"], selected["candidate_id"])
        for action in ("keep", "discard"):
            with self.assertRaisesRegex(LOOP.LoopError, "report-only"):
                LOOP.decide(final, "held-out", action, "Final cannot be used for selection")
        with self.assertRaisesRegex(LOOP.LoopError, "already completed"):
            LOOP.run(final, "again", "Do not tune on the final score")
        self.assertTrue((final / result["metrics"]).is_file())

    def test_campaign_final_cannot_run_again_under_another_directory_or_label(self):
        record = self.shared(attempts=8)
        _, final, _ = self.selection_and_final()
        LOOP.run(final, "report")
        before = len(self.calls())
        usage_before = LOOP.status(final)["campaign_budget"]["attempts_used"]
        self.contract["evaluation"]["task_set_id"] = "renamed-final"
        other = self.project / "second-final-directory"
        with self.assertRaisesRegex(LOOP.LoopError, "already used or reserved"):
            self.init(other)
        self.assertEqual(len(self.calls()), before)
        self.assertEqual(LOOP.status(final)["campaign_budget"]["attempts_used"], usage_before)
        self.assertFalse(other.exists())
        usage = json.loads(record.read_text(encoding="utf-8"))["final_uses"]
        self.assertEqual(len(usage), 1)
        self.assertEqual(next(iter(usage.values()))["status"], "completed")

    def test_campaign_final_rejects_new_candidate_after_seeing_final_result(self):
        self.shared(attempts=8)
        selection, final, _ = self.selection_and_final()
        LOOP.run(final, "first-final")
        self.edit("normal", 20)
        LOOP.run(selection, "new-mechanism", "A new selection candidate")
        selected = LOOP.decide(selection, "new-mechanism", "keep", "Selection improved")["attempt"]
        self.contract["evaluation"]["frozen_candidate"]["candidate_id"] = selected["candidate_id"]
        other = self.project / "new-candidate-on-used-final"
        before = len(self.calls())
        with self.assertRaisesRegex(LOOP.LoopError, "already bound to a frozen candidate"):
            self.init(other)
        self.assertEqual(len(self.calls()), before)

    def test_campaign_final_reservation_blocks_concurrent_final_directories(self):
        record = self.shared(attempts=8)
        _, final, _ = self.selection_and_final()
        other = self.project / "concurrent-final"
        self.init(other)
        state = LOOP._load(final)
        contract = LOOP._contract(LOOP._json(final / "contract.json"))
        identity = LOOP._final_use(contract, state, state["initial"]["manifest"])
        LOOP.CAMPAIGN.reserve(record, "shared-research", self.project, "pending-final", 1, final, "pending", identity)
        before = len(self.calls())
        with self.assertRaisesRegex(LOOP.LoopError, "already used or reserved"):
            LOOP.run(other, "parallel-final")
        self.assertEqual(len(self.calls()), before)

    def test_campaign_final_failed_command_can_retry_unchanged_protocol(self):
        self.shared(attempts=8)
        _, final, _ = self.selection_and_final()
        with patch.object(LOOP.subprocess, "Popen", side_effect=OSError("Transient process start failure")):
            failed = LOOP.run(final, "failed-launch")["attempt"]
        self.assertEqual(failed["outcome"], "crash")
        result = LOOP.run(final, "unchanged-retry")["attempt"]
        self.assertEqual(result["status"], "reported")
        self.assertEqual(result["metric"], 11)

    def test_campaign_final_completed_event_recovers_report_without_replaying(self):
        self.shared(attempts=8)
        _, final, _ = self.selection_and_final()
        original = LOOP._write_json

        def fail_finished_cache(path, value):
            if path.name == "state.json" and value.get("attempts", {}).get("finished", {}).get("status") == "evaluated":
                raise OSError("Injected final finished-event cache failure")
            return original(path, value)

        with patch.object(LOOP, "_write_json", side_effect=fail_finished_cache):
            with self.assertRaisesRegex(OSError, "final finished-event"):
                LOOP.run(final, "finished")
        before = len(self.calls())
        metrics = final / "attempts" / "finished" / "metrics.json"
        raw = metrics.read_bytes()
        metrics.write_text('{"score":999}', encoding="utf-8")
        with self.assertRaisesRegex(LOOP.LoopError, "Raw metrics"):
            LOOP.recover(final, "finished", "Inspect retained metrics before reporting", True)
        self.assertIsNotNone(LOOP.status(final)["pending"])
        metrics.write_bytes(raw)
        result = LOOP.recover(final, "finished", "Checked completed evaluator and retained metrics", True)["attempt"]
        self.assertEqual(result["status"], "reported")
        self.assertEqual(result["decision"], "report")
        self.assertFalse(result["eligible"])
        status = LOOP.status(final)
        self.assertEqual(status["finalized"], "finished")
        self.assertEqual(status["campaign_budget"]["final_task_uses"][0]["status"], "completed")
        self.assertEqual(len(self.calls()), before)

    def test_campaign_final_repeat_measurements_stay_inside_frozen_evaluator(self):
        self.shared(attempts=8)
        _, final, _ = self.selection_and_final(final_samples=3)
        # The fixed command may aggregate repeats; controller enforces one use
        # of that command, not a limit on its internal sample count.
        result = LOOP.run(final, "frozen-repeat-protocol")["attempt"]
        self.assertEqual(result["status"], "reported")
        self.assertEqual(json.loads((final / result["metrics"]).read_text(encoding="utf-8"))["sample_count"], 3)
        with self.assertRaisesRegex(LOOP.LoopError, "already completed"):
            LOOP.replicate(final, "adaptive-extra", result["id"], "Additional score-dependent sample")

    def test_campaign_final_rejects_changed_protocol_on_identical_final_tasks(self):
        self.shared(attempts=8)
        _, final, _ = self.selection_and_final()
        with patch.object(LOOP.subprocess, "Popen", side_effect=OSError("Transient process start failure")):
            LOOP.run(final, "first-protocol")
        path = self.project / "final-evaluator.py"
        path.write_text(path.read_text(encoding="utf-8") + "\n# changed evaluation protocol\n", encoding="utf-8")
        other = self.project / "changed-final-protocol"
        self.init(other)
        before = len(self.calls())
        with self.assertRaisesRegex(LOOP.LoopError, "already bound to a frozen candidate and protocol"):
            LOOP.run(other, "new-protocol")
        self.assertEqual(len(self.calls()), before)

    def test_legacy_campaign_final_history_is_not_treated_as_unused(self):
        record = self.shared(attempts=8)
        _, final, _ = self.selection_and_final()
        LOOP.run(final, "legacy-report")
        data = json.loads(record.read_text(encoding="utf-8"))
        del data["final_uses"]
        record.write_text(json.dumps(data), encoding="utf-8")
        other = self.project / "legacy-history-reuse"
        before = len(self.calls())
        with self.assertRaisesRegex(LOOP.LoopError, "Legacy final-task use is unknown"):
            self.init(other)
        self.assertEqual(len(self.calls()), before)

    def test_final_rejects_changed_candidate_and_reused_task_identity(self):
        selection, final, _ = self.selection_and_final()
        self.edit("normal", 99)
        with self.assertRaisesRegex(LOOP.LoopError, "frozen"):
            LOOP.run(final, "adapted", "Must not tune on held-out tasks")
        self.edit("normal", 10)
        self.contract["evaluation"]["task_set_id"] = "selection-v1"
        with self.assertRaisesRegex(LOOP.LoopError, "distinct task-set"):
            self.init(self.project / "not-held-out")

    def test_final_keeps_its_explicit_frozen_identity_if_selection_later_advances(self):
        selection, final, frozen = self.selection_and_final()
        self.edit("normal", 20)
        LOOP.run(selection, "later-selection", "A later selection comparison")
        LOOP.decide(selection, "later-selection", "keep", "Selection measured the later candidate")
        self.edit("normal", 10)
        reported = LOOP.run(final, "frozen-report")["attempt"]
        self.assertEqual(reported["candidate_id"], frozen["candidate_id"])
        self.assertEqual(reported["status"], "reported")

    def test_campaign_rejects_final_to_selection_relabel_without_new_identity(self):
        self.shared(attempts=5)
        _, final, _ = self.selection_and_final()
        LOOP.run(final, "report")
        self.contract["evaluation"] = {"split_role": "selection", "task_set_id": "final-v1"}
        with self.assertRaisesRegex(LOOP.LoopError, "final task set cannot be reused"):
            self.init(self.project / "leaking-selection")
        self.contract["evaluation"]["task_set_id"] = "renamed-final-v1"
        with self.assertRaisesRegex(LOOP.LoopError, "Reusing final task content"):
            self.init(self.project / "renamed-leaking-selection")
        self.contract["evaluation"]["reused_final"] = {"task_set_id": "final-v1", "reason": "User explicitly chooses to reuse these tasks for development; they are no longer held out"}
        self.init(self.project / "explicitly-reused-final")

    def test_final_cannot_be_claimed_by_renaming_identical_task_bytes(self):
        self.contract["evaluation"] = {"split_role": "selection", "task_set_id": "selection-v1"}
        selection = self.project / "same-task-selection"
        self.init(selection)
        selected = LOOP.run(selection, "selected")["attempt"]
        self.contract["evaluation"] = {"split_role": "final", "task_set_id": "different-label",
                                       "frozen_candidate": {"workdir": selection.name, "candidate_id": selected["candidate_id"]}}
        with self.assertRaisesRegex(LOOP.LoopError, "content matches selection"):
            self.init(self.project / "not-held-out-by-label")


if __name__ == "__main__":
    unittest.main(verbosity=2)
