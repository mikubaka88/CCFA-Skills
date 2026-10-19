---
name: ccf-literature-monitor
description: "Scan recent arXiv/OpenReview papers, venue feeds, labs, and competitors for overlap. Use for 竞品监控, 新论文追踪, 论文跟踪, and recurring novelty watch. Give dated evidence and changes since the prior scan. Broad related-work retrieval belongs to ccf-literature-searcher."
metadata:
  ccf_skill_controls:
    handoff_question_mode: partial
    respect_session_denylists: true
    protect_idea_scope_in_writing: true
    private_material_safety: moderate
    shared_controls: ../ccf-common/references/
---

# CCF Literature Monitor

## Family File Contract

Before file work, reuse canonical paths and one task/artifact working directory; default to project-root `ccfa-workfiles/<purpose>/<artifact-id>/`. Update in place, preserve inputs, and use UTF-8 with Chinese-text checks. Apply [artifact-contracts.md](../ccf-common/references/artifact-contracts.md) for naming, ownership, and task-created cleanup; handoffs inherit these paths.

## Collaboration Contract

Before specialist execution, read and apply [ccf-humanization](../ccf-humanization/SKILL.md) first, then [ccf-common](../ccf-common/SKILL.md). At every handoff, reuse their applicable active rules or refresh missing/changed ones. Both preflights are required even without prose; detailed editing, experiment, and maintenance modes run only when relevant.

Integrate necessary specialist contributions under one owner; reuse valid prerequisites and verify affected results. Follow the [cooperation routes](../ccf-common/references/routing.md) without duplicate reports.

## Core Rule

Monitor arXiv, OpenReview, conference/proceedings feeds, project pages, labs, and named competitors for new papers that could overlap with the user's idea or paper. Report findings factually. Do not exaggerate novelty threats, dismiss real overlap, or infer priority from weak evidence. Provide actionable signals: RELAX, RESEARCH, FOLLOW-UP.

## Modes

- `arxiv-watch`: scan recent papers in target categories or keyword clusters.
- `venue-watch`: scan OpenReview, proceedings, accepted-paper lists, or official venue pages.
- `novelty-check`: compare a given idea with recent papers and flag overlap.
- `trend-scouting`: summarize emerging directions, crowded areas, and under-tested gaps.
- `competitor-tracking`: monitor named research groups, labs, repositories, datasets, benchmarks, or authors.
- `paper-alert-digest`: produce a recurring watch report suitable for saving into a project folder.

## Skill Linkage

- @READS `ccfa.yaml` for idea state.
- @SHARES findings with `ccf-literature-searcher`.
- @SHARES novelty implications with `ccf-idea-reviewer`.
- @SHARES rescue or differentiation opportunities with `ccf-idea-optimizer`.
- @SHARES citation and positioning candidates with `ccf-paper-writer`.
- @FLAGS conflicting papers for `ccf-integrity-auditor`.

## Invocation Controls

**CCFA Handoff Mode: PARTIAL (Recommended).** Follow `metadata.ccf_skill_controls.handoff_question_mode` and `../ccf-common/references/handoff-modes.md`.

Load `../ccf-common/references/task-modes.md` before deciding exploratory, quick, or standard mode.

Treat unpublished ideas, draft abstracts, methods, and results as private material. Load `../ccf-common/references/privacy-and-evidence.md` before using private text in queries. Use public-safe keywords, public method names, venue names, and user-approved query text.

Load `../ccf-common/references/review-output-standards.md` when monitor results feed idea scoring, paper review, or score-risk language.

## Workflow

1. Load `references/monitoring-workflow.md`.
2. If project state is available (`ccfa.yaml`), read the current idea, target venue, claims, and tracked competitors.
3. Choose the mode and time window. If the user says "latest", "recent", "new", "this week", or "today", verify the current date and use an explicit date range.
4. Execute the requested monitoring mode using public-safe queries and source-quality exclusions from the shared policy.
5. Classify overlaps by problem, mechanism, evidence, benchmark, dataset, claim, and venue positioning.
6. Report new or materially changed findings, with precise implications for the requested research decision. Use existing report history to avoid presenting the same paper as new.
   Reuse stable paper IDs and versioned source evidence from the existing topic report; fetch targeted metadata before full text. Check updates within the actual requested window even when older content is cached. Optional expansion into extra topics follows Common's `extended_search` preference and never replaces the required current scan.
7. Resolve a concrete evidence gap needed for the current deliverable through its owner and integrate the result. Complete requested downstream work; offer unrelated follow-up only when useful. `RESEARCH` and `FOLLOW-UP` describe findings, not automatic instructions to start retrieval, scoring, redesign, or rewriting.

## Output Contract

Honor the user's requested shape and brevity. A short update gives the time range, source basis, new or changed findings, and their relevant consequence. An internal contribution returns those findings to its owner without a standalone report. Full monitoring reports use `references/report-template.md` as the single canonical structure; keep only relevant handoff signals and keep routine self-checks internal. Preserve actual coverage limits without repeating a disclaimer for every paper.

## References

- `references/monitoring-workflow.md` — Workflow, api-key-management, search strategy.
- `references/report-template.md` — Output template and formatting.
- `../ccf-common/references/source-registry.yaml` — Competitor and arxiv links.

## Execution And Persistence

Distinguish a single scan from recurring monitoring. A recurring report format is not a scheduler: claim ongoing monitoring only after an actual authorized scheduled job exists. Record the time window and coverage; an empty scan is not proof of novelty. Deduplicate by stable paper identity and version, separating first publication from revisions. Batch independent feeds when supported; preserve real monitoring history under `../ccf-common/references/artifact-contracts.md`. Follow no-new-files and existing project-state authorization.
