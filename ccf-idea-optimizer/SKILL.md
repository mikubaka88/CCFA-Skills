---
name: ccf-idea-optimizer
description: "Develop and optimize rough CCF research ideas into problems, insights, mechanisms, and evidence plans. Use for 优化idea, 具象化idea, 找方向, 方向探索, and rescue routes without requested scoring. Explicit numeric scoring/ranking belongs to ccf-idea-reviewer; manuscript edits belong to ccf-paper-writer."
metadata:
  ccf_skill_controls:
    handoff_question_mode: partial
    respect_session_denylists: true
    protect_idea_scope_in_writing: true
    private_material_safety: moderate
    shared_controls: ../ccf-common/references/
---

# CCF Idea Optimizer

## Invocation Controls

**CCFA Handoff Mode: PARTIAL (Recommended).** Follow `metadata.ccf_skill_controls.handoff_question_mode`, `../ccf-common/references/handoff-modes.md`, and `../ccf-common/references/task-modes.md`. Complete requested idea development and necessary public-safe grounding under existing authorization. Do not load scoring, writing, or full experiment-design workflows unless their deliverables are requested or needed.

## Core Rule

Turn a rough direction into a concrete problem, grounded gap, causal insight, mechanism, and falsifiable evidence plan. Distinguish source-backed observations from inferred opportunities. Do not invent prior work, results, reviewer sentiment, or novelty. Related work should clarify differentiation; an unsearched or crowded direction is uncertain, not automatically dead.

Preserve the user's theme and constraints. Vary framing or mechanism within the authorized development scope, and explain consequential changes. A useful idea has a coherent reason the intervention should change an observable result; a list of familiar modules is insufficient.

## Modes

- Exploratory: develop rough seeds, find directions, and rescue promising ingredients before judging readiness.
- Quick: repair one local mechanism or give a concise idea card.
- Standard: ground a mature direction and produce a handoff-ready research plan.

## Workflow

1. Extract the user's decision, field, stage, resources, timeline, and available sources. Infer routine details and mark unknowns. Load `references/idea-intake.md` only for messy or incomplete inputs; do not restart intake when the conversation already supplies them.
2. When venue fit matters, use `../ccf-common/references/ccf-a-venue-map.md` and the relevant `references/venue-idea-adapters.md` passage. An unspecified venue can use a labeled generic CCF-A lens.
3. Ground timeliness and closest work when needed for the request. Use `../ccf-common/references/privacy-and-evidence.md` before browsing; search public-safe terms. Use `ccf-literature-monitor` for recent-paper watch and `ccf-literature-searcher` for deeper retrieval. Honor no-browsing requests and label unsearched novelty accurately.
4. When sources are available, use `references/literature-grounded-evolution.md` to retain compact evidence cards, mechanism primitives, protocol anchors, and unresolved relations. Keep source locations rather than loading whole abstracts repeatedly. Trace borrowed ideas and inferred gaps separately.
5. For an underdetermined direction, use `references/frontier-ideation.md` to generate meaningfully different candidates. Three to five is a starting range, not a quota; one well-specified idea needs targeted improvement, not a forced tournament. Keep meaningful lineage and operations such as refine, combine, transfer, invert, or instrument internally.
6. Use `references/problem-method-blueprint.md` to connect problem, root challenge, insight, mechanism, assumptions, and expected observation. Check incompatible data assumptions, objectives, or resources. Keep the strongest route and a genuinely different fallback when useful.
7. Challenge the route against the closest-overlap concern and its weakest evidence link. Revise only for a material weakness; do not repeat self-critique that merely paraphrases the idea. Development selection can be internal; numeric ranking belongs to an explicitly requested `ccf-idea-reviewer` task.
8. Use `references/experiment-design.md` to outline the minimum convincing evidence for the central claim: compatible datasets, baselines, metrics, and discriminating tests. A full execution protocol belongs to `ccf-experiment-designer` when requested. Planned results remain predictions to test, not evidence.
9. Return the developed idea in the user's requested shape. For a weak seed, distinguish current weakness from development potential and identify a concrete rescue or reformulation before recommending abandonment. If a required decision remains open, explain the exact evidence needed and finish the independent parts.

## Output Contract

Return an idea card, options, mechanism blueprint, or roadmap as requested. A standard plan contains the problem, source-backed gap, insight, method, contribution type, evidence plan, closest-work difference, material assumptions, and next decision. Include candidate alternatives only when developed and useful. Keep branch bookkeeping, reviewer simulation, and generic checklist status out of publication prose.

Do not switch to scoring, full review, or manuscript writing merely because the idea could benefit from it. If the user requests a combined workflow, use each deliverable's owner without another authorization round.

## References

- `references/idea-intake.md`: normalize incomplete or multiple seeds.
- `references/frontier-ideation.md`, `references/literature-grounded-evolution.md`: diverse development and source-grounded evolution.
- `references/problem-method-blueprint.md`: problem-to-mechanism reasoning.
- `references/venue-idea-adapters.md`: applicable venue priorities.
- `references/experiment-design.md`: minimum discriminating evidence.
- `references/research-taste.md`: explicit questions about research quality, elegance, and timeliness.
- `references/source-notes.md`: source provenance and current-policy checks.

For file outputs, follow `../ccf-common/references/artifact-contracts.md`: resolve existing project paths first, keep generated working files under one stable task/artifact directory, and update canonical files in place. Load this shared policy only when files are written and it is not already in context.
