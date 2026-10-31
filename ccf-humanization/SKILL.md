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

## Required First Preflight

Apply this baseline before every CCFA skill and contributor, including research, review, retrieval, experiments, visuals, and maintenance. Then apply [ccf-common](../ccf-common/SKILL.md), once, without recursive re-entry. Reuse applicable active rules at handoffs; refresh rules that changed or were lost. Specialist skills retain ownership. This activation creates no report, warning file, editing pass, or separate agent.

## Family Baseline

- Communicate the actual question, scientific content, evidence, and decisions directly. Remove imagined objections, empty assurances, repetitive warnings, and process narration. Keep real criticism, meaningful uncertainty, scientific facts, source quotations, and mandatory checks. Do not adjust review scores to sound more agreeable.
- Use existing authorization and evidence. Ask only about an unresolved decision that changes the work; continue independent authorized parts. A checklist alone does not justify new experiments or a smaller research objective.
- In prose, ideas, and experiment plans, explain the object, operation, relationship, and intended or observed result. Labels such as `verifiable`, `feasible`, or their Chinese equivalents do not substitute for that explanation. Preserve them when they name a genuine technical property. Comparisons need real alternatives; qualifications need a specific factual or logical reason. A proposed mechanism remains a proposal without requiring completed experiments.
- Compose from the supplied science and the reader's path through it. Preserve conceptual, theoretical, and interpretive explanations as well as computations; do not force every paragraph into an operation list. Reviewer expectations and internal checks are not manuscript content.
- Preserve assumptions, negative findings, protocol facts, calibrated uncertainty, citations, equations, numbers, terminology, and disclosures. Negation and hedging can be scientifically necessary. Keep the author's sentence-final emphasis, synthesis, and broader significance; connect it to the paragraph and distinguish prospective implications from observed results.
- When execution becomes unreliable, narrow the next action while preserving the goal and evidence standard. Recover from actual artifacts through Common's continuity rules instead of adding cautionary prose or replacing the deliverable with an easier task.

## Apply Only Relevant Detail

| Current work | What to load or do |
| --- | --- |
| Family preflight or ordinary clear local edit | Apply the baseline above and continue with Common and the owner. No read-all policy pass. |
| Requested humanization or an actual defensive/unclear passage | Read the relevant sentence decisions, repairs, punctuation, or acceptance checks in [humanization-policy.md](references/humanization-policy.md). Recover the scientific message, repair the sentence relationships, then check wording. |
| Reported comparison or executable experiment change | Read [experiment-discipline.md](references/experiment-discipline.md) when method identity or protocol matters. A supplied method can be drafted without demanding new runs or checkpoints. |
| Full section or paper revision | Check the resulting argument once; run the writer's [prose checker](../ccf-paper-writer/scripts/check_prose_quality.py) when available. Inspect candidates in context, retain justified technical language, and rerun only changed or unresolved content. |
| Concrete unresolved scientific decision | Use the policy's warning contract for the dependent claim only; continue unaffected work. Ordinary accurate edits need no extra approval. |

Prose edits require an authorized writing task. Review-only work diagnoses without rewriting; non-prose work keeps the baseline without starting prose checks. Return the requested artifact in its original format, without a compulsory style report. Keep internal confirmation and version-gate status out of manuscript prose.

## Shared Contracts

Handoff mode remains **PARTIAL**, governed by the preserved metadata and Common's [handoff modes](../ccf-common/references/handoff-modes.md). Before file work, reuse canonical paths and one stable task directory, defaulting to `ccfa-workfiles/<purpose>/<artifact-id>/`; update current artifacts in place and preserve inputs. Apply [artifact-contracts.md](../ccf-common/references/artifact-contracts.md) for ownership, cleanup, and UTF-8/Chinese checks. Common resolves scope, prerequisites, and applicable preferences before specialist execution.
