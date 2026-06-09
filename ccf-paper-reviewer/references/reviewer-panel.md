# Reviewer Panel

Use independent reviewer perspectives before writing the AC/meta-review. Do not let one perspective contaminate another before synthesis.

Do not force reviewers to disagree, praise, or reject. Each reviewer must ground its stance in manuscript evidence, supplied artifacts, or searched sources. If the evidence is insufficient, say `insufficient evidence` and name the missing artifact or check.

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

For detailed paragraph or LaTeX review, use the writing-review references under `references/writing-review/`.

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
Evidence basis:
Fatal concern if any:
Score-change condition:
```

## Synthesis Rule

The final stance must be consistent with the strongest unresolved concern. Do not average away a fatal flaw.

## Additional Full-Review Roles

Use these roles in every full review unless the paper type makes a role genuinely irrelevant. Each reviewer must produce an independent score or score tendency before aggregation.

### Domain Application Reviewer

Checks whether the method, claim, and evaluation align with the target domain practice.

- Does the assumption match real-world deployment constraints?
- Is the experimental setup representative of practical use?
- Does the paper miss an important practical constraint that every practitioner would flag?
- Score axis: practical/domain validity (1-5).

### Evidence/Ablation Reviewer

Checks whether the empirical evaluation is rigorous and decisive.

- Are comparisons fair, multi-axis, and reproducible?
- Do ablations isolate the claimed mechanism?
- Are results robust to hyperparameters? Do confidence intervals or repeated runs cover favorable and unfavorable settings when relevant?
- Are percentage gains or bar charts used where statistical significance is meaningful?
- Score axis: experimental rigor (1-5).

### Reproducibility Reviewer

Checks whether today someone could reproduce, understand, and trust the results without the authors.

- Are all necessary model details and training hyperparameters shared?
- Is the code available? Is there documentation for non-obvious implementation choices?
- Are datasets accessible, and is the pre-processing reproducible?
- Are seeds fixed or made available?
- Score axis: reproducibility completeness (1-5).

### Novice Advocate Reviewer

Reviews from the perspective of a new-to-the-conference researcher. Checks for clarity of material, figures, data, and narrative flow.

- Is each paragraph a clear, succinct argument?
- Are figures interpretable without the caption? Do appendix/supplementary figures make intuitive sense?
- Does the abstract correctly summarize what the paper actually does and finds?
- Does the introduction provide a realistic roadmap for the paper?
- In the experiments section, does each result paragraph begin with an orienting sentence before the data?
- Score axis: accessibility (1-5).

## Panel Synthesis

After independent reviewer blocks, include:

```text
Agreement:
Disagreement:
Decisive positive axis:
Decisive negative axis:
Unresolved evidence:
AC stance:
```
