---
name: ccf-humanization
description: "Required first preflight before every CCFA skill, including research, review, retrieval, experiments, visuals, and maintenance. Keep reasoning and communication direct, remove empty defensive framing, and preserve evidence and uncertainty. Also use for 去防御性 and 论文人性化. Apply prose edits only within the authorized task; specialist skills retain ownership."
metadata:
  ccf_skill_controls:
    handoff_question_mode: partial
    respect_session_denylists: true
    protect_idea_scope_in_writing: true
    private_material_safety: moderate
    shared_controls: ../ccf-common/references/
---

# CCF Humanization

## Family File Contract

Before writing, resolve the canonical output and one stable working directory per task/artifact. Reuse explicit or established task paths; otherwise use project-root `ccfa-workfiles/<purpose>/<artifact-id>/`, with `source/`, `assets/`, `cache/`, and `build/` only as needed. Update current files in place; do not scatter intermediates or create iteration copies. Preserve inputs and required evidence; clean only verified disposable files created by this task. Use UTF-8 text I/O and check Chinese text after saving or rendering. For file work, apply [artifact-contracts.md](../ccf-common/references/artifact-contracts.md) and reuse the same paths across skill transitions.

## Collaboration Contract

This is the first required family preflight. Apply the baseline below, then activate [ccf-common](../ccf-common/SKILL.md) before specialist work. The two preflights bootstrap once without recursively re-entering each other; reuse applicable rules across contributors.

Keep one integrating owner and actively use other skills to resolve missing prerequisites or check material findings. Reuse applicable evidence; do not skip necessary groundwork to save tokens. Before finalizing, integrate contributions and verify affected results. Follow the conditional [cooperation routes](../ccf-common/references/routing.md); avoid unrelated stages and duplicate reports.

## Invocation Controls

**CCFA Handoff Mode: PARTIAL (Recommended).** Follow `metadata.ccf_skill_controls.handoff_question_mode`, `../ccf-common/references/handoff-modes.md`, and `../ccf-common/references/task-modes.md`.

Activate this first for every CCFA task and contributor, including planning, retrieval, review, auditing, rendering, scaffolding, and maintenance. Apply the family baseline below before `ccf-common` and specialist execution. Reuse an already loaded, applicable baseline at handoffs; refresh changed or lost rules. Prose editing and experiment checks depend on the actual task, but baseline activation is universal. Specialist skills retain ownership and explicit user/host constraints still apply.

## Family Baseline

Read and apply this entry's baseline before specialist work. Communicate the concrete task, evidence, and decisions directly; avoid imagined objections, empty assurances, repetitive warnings, and unnecessary process narration. Preserve real risks, critical review findings, uncertainty, scientific facts, source quotations, and mandatory checks. Do not turn critical assessment into praise or change scores to sound less defensive. Review-only tasks diagnose without rewriting; non-prose tasks apply these rules without inventing a prose-edit pass. Enable only relevant detailed modes below. This preflight creates no report, warning file, or separate agent by default.

## Core Rule

Write the scientific argument directly: problem, insight, mechanism, evidence, and supported implication. Remove authorial self-defense, imagined reviewer objections, apologetic novelty positioning, denial-led statements, empty assurances, stacked hedging, repeated scope disclaimers, and obligatory cautionary endings. Replace a defensive sentence with its scientific payload or delete it if it adds none.

Humanization preserves rigor: retain meaningful uncertainty, actual assumptions, negative results, protocol facts, citations, equations, numbers, terminology, and required disclosures. Do not turn `suggests` into `proves`, omit a known failure, or hide a real comparison limitation. Do not treat isolated words such as `only`, `not`, or `may` as errors.

Keep method confirmation and version-gate status internal. Describe the actual method and relevant configuration naturally. Use supplied specifications for method drafting, cited evidence for prior work, and verified full configurations for reported comparisons; do not require new experiments just to edit supported prose.

## Modes

- `family-preflight`: always apply the baseline before any CCFA specialist; no manuscript or experiment artifact is required.
- `manuscript-humanization`: revise defensive prose while preserving scientific content and source format.
- `experiment-humanization`: apply the same prose standard to final experiment descriptions and tables; preserve full-method comparisons and labeled ablations.
- `warning-only`: identify a concrete unresolved scientific decision without modifying its dependent artifact.

## Workflow

For `family-preflight`, apply the baseline, ensure `ccf-common` is active, and continue the requested specialist task. The following editing workflow applies only when the task includes relevant prose or experiment artifacts; do not run it merely to complete the universal preflight.

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
