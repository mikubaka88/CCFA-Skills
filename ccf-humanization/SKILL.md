---
name: ccf-humanization
description: "Remove defensive academic prose while preserving evidence, uncertainty, and source format. Use for 去防御性, 论文人性化, apologetic framing, imagined reviewer objections, and repetitive caveats. A writing sidecar; never the primary research owner. Do not auto-run for raw planning, review, retrieval, audit, or visual rendering without prose."
metadata:
  ccf_skill_controls:
    handoff_question_mode: partial
    respect_session_denylists: true
    protect_idea_scope_in_writing: true
    private_material_safety: moderate
    shared_controls: ../ccf-common/references/
---

# CCF Humanization

## Invocation Controls

**CCFA Handoff Mode: PARTIAL (Recommended).** Follow `metadata.ccf_skill_controls.handoff_question_mode`, `../ccf-common/references/handoff-modes.md`, and `../ccf-common/references/task-modes.md`.

Use this as the highest-priority preflight for manuscript prose, including explicitly requested humanization. In a combined writing task, the writer remains the primary owner. Do not auto-load for raw experiment planning, retrieval, review, auditing, routing, or visual rendering without publication prose. Follow user intent and existing authorization; a style preflight does not open a new research stage.

## Core Rule

Write the scientific argument directly: problem, insight, mechanism, evidence, and supported implication. Remove authorial self-defense, imagined reviewer objections, apologetic novelty positioning, denial-led statements, empty assurances, stacked hedging, repeated scope disclaimers, and obligatory cautionary endings. Replace a defensive sentence with its scientific payload or delete it if it adds none.

Humanization preserves rigor: retain meaningful uncertainty, actual assumptions, negative results, protocol facts, citations, equations, numbers, terminology, and required disclosures. Do not turn `suggests` into `proves`, omit a known failure, or hide a real comparison limitation. Do not treat isolated words such as `only`, `not`, or `may` as errors.

Keep method confirmation and version-gate status internal. Describe the actual method and relevant configuration naturally. Use supplied specifications for method drafting, cited evidence for prior work, and verified full configurations for reported comparisons; do not require new experiments just to edit supported prose.

## Modes

- `manuscript-humanization`: revise defensive prose while preserving scientific content and source format.
- `experiment-humanization`: apply the same prose standard to final experiment descriptions and tables; preserve full-method comparisons and labeled ablations.
- `warning-only`: identify a concrete unresolved scientific decision without modifying its dependent artifact.

## Workflow

1. Identify the requested artifact, existing authorization, and whether the input is prose, a proposed design, or reported results. Read `references/humanization-policy.md` for the sentence decisions and bilingual repair examples.
2. Recover each paragraph's scientific message. State the observation, operation, assumption, or inference directly. Delete empty self-defense instead of moving it into a warning block.
3. Remove repeated caveats across sections. Express scope where it changes interpretation; do not require every abstract, paragraph, caption, or conclusion to end with a limitation.
4. Preserve material facts and calibrated uncertainty in the authorized edit. If a decision requires new evidence or a research-scope change, isolate that decision and continue unaffected work. Do not edit a source file merely to encode a warning.
5. For actual publication comparisons or executable experiment changes, load `references/experiment-discipline.md`. Preserve a verified identity and full configuration in the internal gate; keep legitimate ablations clearly labeled. Run this step only when the task needs it.
6. Apply the existing punctuation and terminology preferences after the scientific argument is sound. For full sections or papers, run `../ccf-paper-writer/scripts/check_prose_quality.py` when available and inspect its candidate locations in context. Do not rewrite correct scientific language merely to clear a heuristic warning.
7. Read the final prose once. Check that rhetorical caution has not been replaced by hype, factual omission, or a different scientific claim. Rerun a check only for changed text or an unresolved finding.
8. Return the requested artifact in its original format. When acting as a sidecar, return ownership to the content skill; do not append a process report to ordinary prose.

## Warning Contract

Use only for a concrete decision that cannot be resolved from supplied evidence and existing authorization:

```text
CCF Humanization Warning: not inserted into artifacts
Affected claim / file / experiment:
Evidence gap and material consequence:
Decision needed:
Materiality: advisory / blocking
File changes made for this warning: none
```

`blocking` applies to the dependent claim or change, not the entire task. Style choices, already documented limitations, and accurate local claim narrowing are ordinary authorized edits.

## References

- `references/humanization-policy.md`: direct scientific voice, sentence/paragraph repair, bilingual examples, material facts, warning-only decisions, punctuation, and checksum policy.
- `references/experiment-discipline.md`: full-method comparisons, supplied specifications, ablations, and proportionate smoke checks.

For file outputs, follow `../ccf-common/references/artifact-contracts.md`: resolve existing project paths first, keep generated working files under one stable task/artifact directory, and update canonical files in place. Load this shared policy only when files are written and it is not already in context.
