# Reviewer Panel

Use independent reviewer perspectives before writing the AC/meta-review. Do not let one perspective contaminate another before synthesis.

## Required Reviewers

### Best-Justified Reviewer

Finds the strongest defensible accept case.

Checks:

- clearest contribution,
- strongest evidence,
- community value,
- what a sympathetic expert would defend.

### Critical Reviewer

Finds the strongest reject case.

Checks:

- fatal novelty collapse,
- unsupported central claim,
- invalid method or evaluation,
- missing decisive comparison,
- venue mismatch.

### Method / Soundness Reviewer

Checks:

- assumptions,
- algorithm/proof/system/study validity,
- mechanism clarity,
- correctness of causal claims,
- failure modes.

### Evidence / Experiment Reviewer

Checks:

- baselines,
- ablations,
- datasets/benchmarks,
- metrics,
- robustness,
- statistical rigor,
- reproducibility details.

### Novelty / Positioning Reviewer

Checks:

- closest prior art,
- missing related work,
- whether the novelty delta is real,
- whether comparisons are fair and current.

### Writing / Clarity Reviewer

Checks only clarity as it affects scientific review:

- contribution recoverability,
- figure/table interpretability,
- claim-evidence visibility,
- terminology stability.

For detailed paragraph or LaTeX review, hand off to `ccf-paper-reviewer`.

### Ethics / Reproducibility Reviewer

Checks:

- responsible research,
- data licensing and human subjects,
- privacy/bias/misuse risks,
- artifacts and auditability,
- limitation honesty.

### AC / Meta-Reviewer

Synthesizes:

- reviewer consensus,
- reviewer disagreement,
- decisive accept/reject axis,
- likely discussion outcome,
- author questions that could change the decision.

## Per-Reviewer Format

```text
Reviewer:
Expertise:
Likely score:
Confidence:
Main positive signal:
Main negative signal:
Fatal concern if any:
Score-change condition:
```

## Synthesis Rule

The final stance must be consistent with the strongest unresolved concern. Do not average away a fatal flaw.
