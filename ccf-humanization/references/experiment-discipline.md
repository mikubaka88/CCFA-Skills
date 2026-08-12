# Experiment Discipline

## Confirmed Publication Method Gate

Every method appearing in manuscript prose, final result tables, captions, or claimed comparisons must be a confirmed full version. Record the gate internally:

```text
Display name:
Implementation source:
Release/revision:
Full configuration:
Dataset and split:
Checkpoint/model identity:
Confirmation source:
Status: confirmed / provisional / simplified
```

Only `confirmed` methods may enter publication artifacts. Keep `provisional` and `simplified` variants in development notes. This includes toy, approximate, proxy, reduced-budget, debug, fewer-layer, lower-resolution, shortened-training, subset-only, mocked, emulated, and otherwise altered variants.

The `confirmed` label is internal metadata. Do not copy `confirmed`, `approved`, `publication-ready`, gate status, confirmation source, or similar engineering language into manuscript prose, captions, or table labels. Once the gate passes, name the method and report only scientifically relevant configuration details. For example, write `Transformer Base with six encoder and six decoder layers`, not `the confirmed full Transformer Base version`.

If compute or availability prevents the confirmed version from running, do not silently substitute a simplified version. Return a blocking warning and ask the user to choose among obtaining the confirmed version, changing the claim, postponing the comparison, or explicitly redesigning the experiment outside the manuscript.

An ablation is not a simplified substitute when it is clearly labeled, starts from the confirmed full method, changes exactly the intended component, and is reported only as an ablation rather than as the main method or baseline.

## Smoke-Test Scope

Smoke tests are engineering checks, not paper evidence. Retain a smoke test only when all conditions hold:

1. It exercises a changed or newly connected path.
2. It can catch a realistic initialization, import, configuration, dataflow, or execution failure.
3. Its signal is not already provided by another retained smoke test.
4. It is cheaper than the substantive validation it precedes.
5. Its pass/fail outcome changes the next action.

Use the smallest effective set, typically one test per distinct critical path. Remove repeated invocations with the same coverage, ceremonial "can run" checks after the same path already passed, and speculative tests for cases excluded by the method or data contract.

Do not:

- repeat smoke tests across equivalent configurations;
- add a smoke test for every helper function;
- present smoke success as accuracy, robustness, reproducibility, or benchmark evidence;
- replace full experiments with a quick, toy, reduced, proxy, or debug run;
- describe simplified smoke configurations as the paper's method.

## Experiment-to-Paper Gate

Before publication-facing output, verify:

- every named method is `confirmed`;
- table values map to the confirmed configuration and dataset split;
- simplified development runs are absent from manuscript claims and final tables;
- smoke tests are absent from the evidence narrative unless the paper studies testing itself;
- necessary ablations are labeled as ablations rather than alternate main methods;
- any unresolved version mismatch is reported as a warning with no automatic file change;
- manuscript prose and display labels describe the method naturally without exposing internal confirmation or publication-readiness status.
