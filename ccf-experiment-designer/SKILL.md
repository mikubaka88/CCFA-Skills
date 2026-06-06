---
name: ccf-experiment-designer
description: "Design evaluation protocols, datasets, baselines, metrics, ablations, robustness tests, and result-table templates for CCF papers. Use for ????, benchmark, baseline, ablation planning. Do not invent results."
metadata:
  ccf_skill_controls:
    handoff_question_mode: partial
    respect_session_denylists: true
    protect_idea_scope_in_writing: true
    private_material_safety: moderate
    shared_controls: ../ccf-common/references/
---

# CCF Experiment Designer

## Invocation Controls

**CCFA Handoff Mode: PARTIAL (Recommended).** Follow `metadata.ccf_skill_controls.handoff_question_mode` and `../ccf-common/references/handoff-modes.md`. Use `../ccf-common/references/routing.md` to keep experiment design separate from manuscript writing, literature search, idea optimization, paper review, and rebuttal.

Load `../ccf-common/references/task-modes.md` before deciding quick or standard mode. Use quick mode for a local experiment-table sketch or one claim's ablation plan. Use standard mode for a full paper evidence package, benchmark design, dataset/baseline search, or reviewer-risk-driven experiment planning.

Treat manuscripts, rough ideas, unpublished results, figures, tables, and experiment notes as private user data. Load `../ccf-common/references/privacy-and-evidence.md` before browsing or using private text in queries.

Hard rule: never fabricate experimental results, numbers, improvements, statistical significance, human-study outcomes, benchmark rankings, or baseline performance. Provide placeholders, formulas, and fill-in tables for the user to complete.

## Core Rule

Design experiments that test the paper's central claim. Every dataset, baseline, ablation, metric, stress test, proof, user study, or system benchmark should answer a specific reviewer question. Do not add experiments for volume, and do not let a table imply results that the user has not supplied.

## Mandatory Experiment Checklist

In standard mode, complete this checklist before final output. In quick mode, run the relevant subset and return a compact status.

1. Target venue, venue family, paper type, and central claim are explicit or marked unknown.
2. Storyline is summarized as task -> gap -> root challenge -> insight -> method -> evidence -> limitation.
3. Every major claim maps to one required evidence item.
4. Datasets, benchmarks, workloads, metrics, and baselines are named or marked as needing literature search.
5. If current datasets or baselines are unknown, follow CCFA handoff mode before using `ccf-literature-searcher`; if denied, mark the uncertainty.
6. Baselines include strongest close prior work, simple sanity baselines, and venue-specific standard baselines where feasible.
7. Ablations test mechanisms, not only performance drops.
8. Robustness, failure analysis, efficiency, reproducibility, ethics, or statistical tests are included when relevant to the venue.
9. Result tables contain placeholders only unless the user provided numbers.
10. No invented result, benchmark rank, or reviewer-impact claim appears.

## Workflow

1. Identify the user's input state: rough idea, method sketch, paper draft, experiment section, review concern, or target venue requirement.
2. If a draft or idea is provided, extract the story and contribution claims. If needed, load `../ccf-paper-writer/references/storyline-blueprint.md` for story fields without invoking writing as a sibling skill.
3. Map venue-family expectations with `../ccf-common/references/ccf-a-venue-map.md` and `references/evidence-design.md`.
4. Build the claim-evidence matrix:

```text
Claim:
Reviewer question:
Required evidence:
Dataset / benchmark / workload / proof / study:
Baselines:
Metrics:
Ablations:
Robustness / failure tests:
Result placeholder:
```

5. Search or request datasets and baselines. Use public queries and high-quality sources; follow CCFA handoff mode before using `ccf-literature-searcher` for a full search.
6. Design the main comparison, ablations, diagnostic analysis, robustness tests, efficiency analysis, qualitative examples, and failure cases appropriate to the venue.
7. Load `references/result-templates.md` and create fill-in tables. Use `TBD`, blank cells, or bracketed placeholders, never fabricated numbers.
8. Produce an execution plan: priority, estimated difficulty, required artifacts, expected reviewer concern answered, and what can be moved to appendix.
9. If the experiment plan exposes idea-level problems, follow CCFA handoff mode before using `ccf-idea-optimizer` or `ccf-idea-reviewer`. If the manuscript section needs writing after design, follow CCFA handoff mode before using `ccf-paper-writer`.

## Output Contracts

For full experiment design, return:

```text
Venue and assumptions:
Storyline extracted:
Claim-evidence matrix:
Dataset / benchmark search needs:
Baseline matrix:
Main experiments:
Ablations:
Robustness and failure analysis:
Efficiency / reproducibility / ethics:
Result-fill tables:
Appendix candidates:
Execution priority:
No-fabrication status:
Checklist status:
```

For quick mode, return:

```text
Quick experiment scope:
Claim tested:
Minimal evidence package:
Fill-in table:
Missing inputs:
Compact checklist status:
```

## Reference Files

Load only what is needed:

- `references/evidence-design.md`: Use for venue-family experiment expectations, benchmark/dataset design, baseline rules, and ablation logic.
- `references/result-templates.md`: Use when creating result-fill tables or experiment planning tables.
