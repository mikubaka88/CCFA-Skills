---
name: ccf-idea-optimizer
description: "Develop and optimize rough CCF research ideas into problems, insights, mechanisms, and evidence plans. Use for 优化idea, 具象化idea, 找方向, 方向探索, and rescue routes when development is the requested deliverable. Judging whether an idea is worthwhile, novel, or coherent belongs to ccf-idea-reviewer even without scores; manuscript edits belong to ccf-paper-writer."
metadata:
  ccf_skill_controls:
    handoff_question_mode: partial
    respect_session_denylists: true
    protect_idea_scope_in_writing: true
    private_material_safety: moderate
    shared_controls: ../ccf-common/references/
---

# CCF Idea Optimizer

## Family File Contract

Before file work, reuse canonical paths and one task/artifact working directory; default to project-root `ccfa-workfiles/<purpose>/<artifact-id>/`. Update in place, preserve inputs, and use UTF-8 with Chinese-text checks. Apply [artifact-contracts.md](../ccf-common/references/artifact-contracts.md) for naming, ownership, and task-created cleanup; handoffs inherit these paths.

## Collaboration Contract

Before specialist execution, read and apply [ccf-humanization](../ccf-humanization/SKILL.md) first, then [ccf-common](../ccf-common/SKILL.md). At every handoff, reuse their applicable active rules or refresh missing/changed ones. Both preflights are required even without prose; detailed editing, experiment, and maintenance modes run only when relevant.

Integrate necessary specialist contributions under one owner; reuse valid prerequisites and verify affected results. Follow the [cooperation routes](../ccf-common/references/routing.md) without duplicate reports.

## Invocation Controls

**CCFA Handoff Mode: PARTIAL (Recommended).** Follow `metadata.ccf_skill_controls.handoff_question_mode`, `../ccf-common/references/handoff-modes.md`, and `../ccf-common/references/task-modes.md`. Complete requested idea development and necessary public-safe grounding under existing authorization. Do not load scoring, writing, or full experiment-design workflows unless their deliverables are requested or needed.

## Core Rule

Turn a rough direction into a concrete problem, grounded gap, causal insight, mechanism, and falsifiable evidence plan. Distinguish source-backed observations from inferred opportunities. Do not invent prior work, results, reviewer sentiment, or novelty. Related work should clarify differentiation; an unsearched or crowded direction is uncertain, not automatically dead.

Preserve the user's theme and constraints. Vary framing or mechanism within the authorized development scope, and explain consequential changes. A useful idea has a coherent reason the intervention should change an observable result; a list of familiar modules is insufficient.

Requested innovation authorizes distinct candidate mechanisms even with optional route comparison off. Keep the research question stable while exploring; preserve a selected mechanism during execution unless a material reason reopens it. Use Common's progress test to stop repeated critique or search that adds no decision-relevant information.

## Modes

- Exploratory: develop rough seeds, find directions, and rescue promising ingredients before judging readiness.
- Quick: repair one local mechanism or give a concise idea card.
- Standard: ground a mature direction and produce a handoff-ready research plan.

## Workflow

1. Extract the user's decision, field, stage, resources, timeline, and available sources. Infer routine details and mark unknowns. Load `references/idea-intake.md` only for messy or incomplete inputs; do not restart intake when the conversation already supplies them.
2. When venue fit matters, use `../ccf-common/references/ccf-a-venue-map.md` and the relevant `references/venue-idea-adapters.md` passage. An unspecified venue can use a labeled generic CCF-A lens.
3. Ground timeliness and closest work when needed for the request. Use `../ccf-common/references/privacy-and-evidence.md` before browsing; search public-safe terms. Use `ccf-literature-monitor` for recent-paper watch and `ccf-literature-searcher` for deeper retrieval. Honor no-browsing requests and label unsearched novelty accurately.
4. When sources are available, use `references/literature-grounded-evolution.md` to retain compact evidence cards, mechanism primitives, protocol anchors, and unresolved relations. Keep source locations rather than loading whole abstracts repeatedly. Trace borrowed ideas and inferred gaps separately.
5. For an underdetermined direction or explicit request for a breakthrough, use `references/frontier-ideation.md` to generate meaningfully different candidates. Three to five is a starting range, not a quota or ceiling; honor requested breadth. One well-specified idea otherwise needs targeted improvement. Keep useful lineage and operations such as refine, combine, transfer, invert, or instrument internally.
6. Use `references/problem-method-blueprint.md` to connect problem, root challenge, insight, mechanism, assumptions, and expected observation. Check incompatible data assumptions, objectives, or resources. Keep the strongest route and a genuinely different fallback when useful.
7. Challenge the route against the closest-overlap concern and its weakest evidence link. Use `ccf-idea-reviewer` for a focused conceptual check when a material uncertainty remains; integrate findings and check affected assumptions. Each return must resolve a concern, add evidence, or test a different mechanism; otherwise stop the review/development ping-pong and name the discriminator. A reviewer's smallest repair is a diagnostic option, not a ceiling on authorized innovation. Requested standalone assessment remains the reviewer's deliverable.
8. Match evidence planning to the requested artifact. Early idea cards need a discriminating observation, proof direction, or question, not an experiment matrix. For a complete research plan or explicitly requested evidence design, use `references/experiment-design.md` to select relevant evidence for the central claim. Full execution protocols belong to `ccf-experiment-designer`; planned results remain predictions, not evidence.
9. Return the developed idea in the user's requested shape. Distinguish current weakness from development potential. Offer a rescue when a specific plausible change preserves value; stop a candidate with a demonstrated contradiction, hard-constraint violation, or no remaining contribution without a compulsory rescue pass. Preserve the broader research objective. If a required decision remains open, explain the exact evidence needed and finish the independent parts.

## Output Contract

Return an idea card, options, mechanism blueprint, or roadmap as requested. A standard plan contains the problem, source-backed gap, insight, method, contribution type, evidence plan, closest-work difference, material assumptions, and next decision. Include candidate alternatives only when developed and useful. Keep branch bookkeeping, reviewer simulation, and generic checklist status out of publication prose.

Use necessary grounding and conceptual checks within development; do not turn their internal findings into an unrequested score report or manuscript. For a combined requested workflow, complete each deliverable with its owner under existing authorization.

## References

- `references/idea-intake.md`: normalize incomplete or multiple seeds.
- `references/frontier-ideation.md`, `references/literature-grounded-evolution.md`: diverse development and source-grounded evolution.
- `references/problem-method-blueprint.md`: problem-to-mechanism reasoning.
- `references/venue-idea-adapters.md`: applicable venue priorities.
- `references/experiment-design.md`: minimum discriminating evidence.
- `references/research-taste.md`: explicit questions about research quality, elegance, and timeliness.
- `references/source-notes.md`: source provenance and current-policy checks.
