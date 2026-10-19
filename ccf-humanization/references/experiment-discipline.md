# Experiment Discipline

## Confirmed Publication Method Gate

For methods reported as executed experiments or baseline comparisons, verify the actual full configuration against supplied records or inspectable sources. Do not run this gate for ordinary prose edits, conceptual explanations, or raw experiment planning. Use the supplied specification for a proposed method and label its evaluation as planned; a cited method is grounded in its paper and does not require a local checkpoint. Record only applicable fields internally:

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

Only `confirmed` methods may enter publication artifacts as completed full-method comparisons. Keep `provisional` and `simplified` development substitutes out of those claims; explicitly planned studies and clearly labeled ablations remain valid. Development substitutes include toy, debug, mocked, or altered runs used in place of the intended protocol, including unapproved reductions in budget, layers, resolution, training, or data.

For an authorized, scientifically defined budget comparison, minimal system, synthetic setting, or controlled mechanism study, verify the actual specified protocol and report that study for the question it answers. A smaller system can be the intended scientific object; it must not be presented as another method's full configuration or as evidence for an untested setting. A debug run does not become scientific evidence merely by changing its label: its design, controls, records, and interpretation must support the stated question.

The `confirmed` label is internal metadata. Do not copy `confirmed`, `approved`, `publication-ready`, gate status, confirmation source, or similar engineering language into manuscript prose, captions, or table labels. Once the gate passes, name the method and report only scientifically relevant configuration details. For example, write `Transformer Base with six encoder and six decoder layers`, not `the confirmed full Transformer Base version`.

If compute or availability prevents the confirmed version from running, do not silently substitute a simplified version. Keep that comparison unresolved and identify the needed method or evidence. Continue supported writing and planning. Ask only if the remaining choice changes the claim or protocol and is not already authorized.

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

- every reported full-method comparison is `confirmed`; proposed designs, cited methods, and ablations use their appropriate evidence basis;
- table values map to the confirmed configuration and dataset split;
- development substitutes are not presented as the intended full method; legitimate controlled or minimal-system studies use their actual protocol and scoped interpretation;
- smoke tests are absent from the evidence narrative unless the paper studies testing itself;
- necessary ablations are labeled as ablations rather than alternate main methods;
- a known label or configuration-description error is corrected from supplied records within the authorized edit, without changing measured values; an unresolved identity mismatch remains an affected-claim warning, not an invented correction or a reason to stop unrelated work;
- manuscript prose and display labels describe the method naturally without exposing internal confirmation or publication-readiness status.
