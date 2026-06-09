---
name: ccf-literature-monitor
description: "Monitor arXiv, OpenReview, conference feeds, labs, projects, and competitor papers for new work that may overlap with a user's idea. Use for arxiv-watch, novelty-check, trend-scouting, competitor-tracking, paper tracking, 竞品监控, 新论文追踪, 论文跟踪, 类似 idea 监控. Link findings to ccf-literature-searcher, ccf-idea-reviewer, ccf-idea-optimizer, ccf-paper-writer, and ccf-integrity-auditor."
metadata:
  ccf_skill_controls:
    handoff_question_mode: partial
    respect_session_denylists: true
    protect_idea_scope_in_writing: true
    private_material_safety: moderate
    shared_controls: ../ccf-common/references/
---

# CCF Literature Monitor

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
6. Report findings with precise implications for other CCFA skills.
7. Offer optional handoff to `ccf-literature-searcher` for deep retrieval, `ccf-idea-reviewer` for score impact, `ccf-idea-optimizer` for differentiation, or `ccf-paper-writer` for related-work integration.

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
