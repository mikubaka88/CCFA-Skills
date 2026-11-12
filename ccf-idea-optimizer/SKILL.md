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

Turn a rough direction into a concrete question, an explanation of its difficulty, and a proposed mechanism or research approach. Distinguish source-backed observations from inferred opportunities. Do not invent prior work, results, reviewer sentiment, or novelty. Related work should clarify differentiation; an unsearched or crowded direction is uncertain, not automatically dead.

Preserve the user's research objective and hard constraints, separating them from the current baseline and provisional diagnosis. Before selecting components, ask what distinction, information, objective or computation prevents the desired behavior; use a concrete failure, limiting case or competing explanation when useful. Vary the assumption or mechanism that causes that difficulty, and explain why the change matters. Adding a module or making a design easier to run is not by itself progress toward the objective.

Requested innovation authorizes distinct candidate mechanisms even with optional route comparison off. Preserve the user's objective and hard constraints; an exploratory working question may change when a new phenomenon, missing distinction, or useful connection gives a better formulation within that scope. Preserve a selected mechanism during execution unless a material reason reopens it. Use Common's progress test to stop repeated critique or search that adds no decision-relevant information.

When contributing to explicitly requested autonomous research, use the current observations and failed assumptions to propose the next mechanism, analysis, or search strategy. A stable research objective does not freeze the initial method; change the operation or underlying assumption when the evidence calls for it. Return the hypothesis and discriminating prediction to `ccf-pipeline-orchestrator`, following its [research loop](../ccf-pipeline-orchestrator/references/autonomous-research.md). The authorized campaign's scope and resources govern candidate breadth, not the one-extra-candidate rule for skill maintenance. Ordinary idea development still needs no executed experiments.

## Modes

- Exploratory: develop rough seeds, find directions, and rescue promising ingredients before judging readiness.
- Quick: repair one local mechanism or give a concise idea card.
- Standard: ground a mature direction and produce a handoff-ready research plan.

## Workflow

1. Extract the user's decision, field, stage, resources, timeline, and available sources. Infer routine details and mark unknowns. Load `references/idea-intake.md` only for messy or incomplete inputs; do not restart intake when the conversation already supplies them.
2. When venue fit matters, use `../ccf-common/references/ccf-a-venue-map.md` and the relevant `references/venue-idea-adapters.md` passage. An unspecified venue can use a labeled generic CCF-A lens.
3. Start from a concrete field need or an unresolved scientific phenomenon, not a preferred module. Ground timeliness, useful inspirations, and closest work at the depth the request needs; perform explicitly requested retrieval. Use `../ccf-common/references/privacy-and-evidence.md` before public-safe browsing, `ccf-literature-monitor` for recent-paper watch, and `ccf-literature-searcher` for deeper retrieval. Good technical reports, conference and journal papers, and arXiv originals may all contribute; inspect their content and version. Honor no-browsing requests and do not invent novelty.
4. When sources are available, use `references/literature-grounded-evolution.md` to retain compact evidence cards, mechanism primitives, protocol anchors, and unresolved relations. Keep source locations rather than loading whole abstracts repeatedly. Trace borrowed ideas and inferred gaps separately.
5. For a model-capability or fundamental-bottleneck question, use the diagnosis in `references/problem-method-blueprint.md` to distinguish plausible causes before proposing components. For an underdetermined direction or requested breakthrough, use `references/frontier-ideation.md` to explore distinct explanations, source relationships, and mechanisms at the requested breadth, including its bounded sampling when varied inspiration is requested. A well-specified local question otherwise needs targeted improvement.
6. Connect problem, root challenge, insight, mechanism, assumptions, and expected observation using the blueprint as needed. Favor explanatory value and substantive differences during exploration; compare execution costs when planning investment. Check actual incompatibilities without treating missing results as a conceptual defect. Keep a genuinely different fallback when it would help the user's decision.
7. Check whether the proposed operation addresses the diagnosed difficulty and differs meaningfully from the closest known alternative. Use `ccf-idea-reviewer` for a focused conceptual check when a material uncertainty remains; integrate findings and check affected assumptions. Each return must resolve a concern, add information, or examine a different explanation; otherwise stop the review/development ping-pong and name the discriminator. A reviewer's smallest repair is a diagnostic option, not a ceiling on authorized innovation. Requested standalone assessment remains the reviewer's deliverable.
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
