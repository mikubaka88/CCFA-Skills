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

Before writing, resolve the canonical output and one stable working directory per task/artifact. Reuse explicit or established task paths; otherwise use project-root `ccfa-workfiles/<purpose>/<artifact-id>/`, with `source/`, `assets/`, `cache/`, and `build/` only as needed. Update current files in place; do not scatter intermediates or create iteration copies. Preserve inputs and required evidence; clean only verified disposable files created by this task. Use UTF-8 text I/O and check Chinese text after saving or rendering. For file work, apply [artifact-contracts.md](../ccf-common/references/artifact-contracts.md) and reuse the same paths across skill transitions.

## Collaboration Contract

Before specialist execution, read and apply [ccf-humanization](../ccf-humanization/SKILL.md) first, then [ccf-common](../ccf-common/SKILL.md). At every handoff, reuse their applicable active rules or refresh missing/changed ones. Both preflights are required even without prose; detailed editing, experiment, and maintenance modes run only when relevant.

Keep one integrating owner and actively use other skills to resolve missing prerequisites or check material findings. Reuse applicable evidence; do not skip necessary groundwork to save tokens. Before finalizing, integrate contributions and verify affected results. Follow the conditional [cooperation routes](../ccf-common/references/routing.md); avoid unrelated stages and duplicate reports.

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
7. Execute already requested downstream work through its owner; otherwise offer optional handoff to `ccf-literature-searcher` for deep retrieval, `ccf-idea-reviewer` for score impact, `ccf-idea-optimizer` for differentiation, or `ccf-paper-writer` for related-work integration.

## Output Contract

For each monitoring execution, report in this structure:

```markdown
## Literature Monitoring Report: [Mode] - [Topic/Venue]

**As of:** [YYYY-MM-DD]
**Time range:** [from] to [to]
**Sources scanned:** [arXiv categories / venues / labs / APIs]
**Papers scanned:** [count]
**High-relevance papers:** [count]
**Overall signal:** RELAX / RESEARCH / FOLLOW-UP

| Title | Source | Overlap level | Overlap type | Evidence basis | Action |
|:---|:---|:---:|:---|:---|:---:|
| [title] | [arXiv/OpenReview/venue] | None/Low/Medium/High | Problem/Method/Evidence/Benchmark | [abstract/intro/result] | RELAX/RESEARCH/FOLLOW-UP |

**Actionable flags:**
- RELAX: no material overlap found in the scanned window; continue, but do not claim full novelty proof.
- RESEARCH: partial overlap or possible close work; deep retrieve via `ccf-literature-searcher`.
- FOLLOW-UP: significant overlap in problem, mechanism, and evidence; route to `ccf-idea-reviewer` or `ccf-idea-optimizer` before writing stronger novelty claims.

**Handoff signals:**
- `ccf-literature-searcher`: [papers or clusters to retrieve deeply]
- `ccf-idea-reviewer`: [novelty or score implications]
- `ccf-idea-optimizer`: [differentiation or rescue direction]
- `ccf-paper-writer`: [related-work or positioning update]
- `ccf-integrity-auditor`: [citation/attribution conflict]

**Output self-check:** [date range explicit, source basis stated, table valid, no unsupported novelty conclusion]
```

## References

- `references/monitoring-workflow.md` — Workflow, api-key-management, search strategy.
- `references/report-template.md` — Output template and formatting.
- `../ccf-common/references/source-registry.yaml` — Competitor and arxiv links.

## Execution And Persistence

Distinguish a single scan from recurring monitoring. A recurring report format is not a scheduler: claim ongoing monitoring only after an actual authorized scheduled job exists. Record the time window and coverage; an empty scan is not proof of novelty. Deduplicate by stable paper identity and version, separating first publication from revisions. Batch independent feeds when supported; preserve real monitoring history under `../ccf-common/references/artifact-contracts.md`. Follow no-new-files and existing project-state authorization.
