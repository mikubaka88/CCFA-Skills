# CCFA Routing

Route by the user's primary intent. Do not activate every downstream skill just because it might become useful later. Canonical names now follow `ccf-<object>-<role/action>`; the only exception is `ccf-common`, which is a shared governance module.

## Canonical Routes

| User intent | Owning skill | Boundary |
| --- | --- | --- |
| Creates project folders, copies/selects templates, and initializes ccfa.yaml. | `ccf-project-scaffolder` | Does not create research content. |
| Coordinates project stages, gates, artifacts, and handoffs. | `ccf-pipeline-orchestrator` | Does not do downstream work itself. |
| Clarifies goals, constraints, scope, success criteria, and next skill. | `ccf-workflow-planner` | Does not optimize, search, write, review, or rebut. |
| Turns rough directions into problem-gap-insight-method-evidence plans. | `ccf-idea-optimizer` | Does not rank ideas as the main task. |
| Scores, ranks, compares, and triages early ideas. | `ccf-idea-reviewer` | Does not polish manuscripts. |
| Finds related work, prior art, datasets, benchmarks, and citation evidence. | `ccf-literature-searcher` | Does not audit only fixed citations. |
| Designs datasets, baselines, metrics, ablations, robustness tests, and result templates. | `ccf-experiment-designer` | Does not invent results. |
| Plans, drafts, revises, and polishes manuscript text while preserving evidence scope. | `ccf-paper-writer` | Does not perform full review or rebuttal. |
| Shortens paper text to word/page limits without changing claims or results. | `ccf-paper-compressor` | Does not change evidence or limitations. |
| Runs full scientific manuscript review, scoring, simulated reviewers, and AC/meta-review. | `ccf-scientific-reviewer` | Does not rewrite prose or do format-only checks. |
| Reviews paragraph logic, writing clarity, consistency, LaTeX/format, and presentation risks. | `ccf-writing-reviewer` | Does not score scientific acceptance. |
| Audits claim-support, result-to-claim, numeric, terminology, and figure/table consistency. | `ccf-integrity-auditor` | Does not replace scientific review. |
| Verifies existing citations, BibTeX metadata, paper existence, and citation-context support. | `ccf-citation-auditor` | Does not search broadly for new papers. |
| Builds and audits figures, LaTeX tables, captions, SVG/PDF assets from real results. | `ccf-figure-table-builder` | Does not invent numbers. |
| Prepares artifact and reproducibility package plans, env notes, seeds, licenses, and README. | `ccf-artifact-packager` | Does not promise unavailable releases. |
| Answers venue LaTeX, template, page-limit, anonymity, and camera-ready format questions. | `ccf-venue-format-guide` | Does not handle manuscript content. |
| Checks LaTeX/PDF builds, page limits, anonymity, fonts, metadata, templates, and policy freshness. | `ccf-submission-checker` | Does not polish content. |
| Writes rebuttals, author responses, response letters, revision summaries, and revision ledgers. | `ccf-rebuttal-writer` | Does not trigger for ordinary writing. |
| Adapts an existing paper to a new venue under conservative no-new-experiment defaults. | `ccf-resubmission-adapter` | Does not add experiments or bibliography changes unless authorized. |
| Converts a paper into slides, poster, talk script, figure narration, and Q&A bank. | `ccf-paper-presenter` | Does not perform pre-submission review. |
| Shared routing, trigger registry, handoff modes, source registry, privacy policy, and artifact contracts. | `ccf-common` | Not an ordinary research task skill. |
| Creates, updates, validates, and audits CCFA/Codex skills and family governance. | `ccf-skill-forger` | Does not do research writing or review. |

## Default Paper Project Flow

```text
ccf-project-scaffolder
  -> ccf-pipeline-orchestrator
  -> ccf-workflow-planner
  -> ccf-idea-optimizer
  -> ccf-idea-reviewer
  -> ccf-literature-searcher
  -> ccf-experiment-designer
  -> ccf-paper-writer
  -> ccf-paper-compressor
  -> ccf-scientific-reviewer / ccf-writing-reviewer
  -> ccf-integrity-auditor / ccf-citation-auditor
  -> ccf-figure-table-builder / ccf-artifact-packager
  -> ccf-venue-format-guide / ccf-submission-checker
  -> ccf-rebuttal-writer / ccf-resubmission-adapter / ccf-paper-presenter
```

## Handoff Map

- `ccf-project-scaffolder` -> ccf-pipeline-orchestrator, ccf-paper-writer, ccf-submission-checker
- `ccf-pipeline-orchestrator` -> All owning skills
- `ccf-workflow-planner` -> Most CCFA skills
- `ccf-idea-optimizer` -> ccf-literature-searcher, ccf-experiment-designer, ccf-paper-writer
- `ccf-idea-reviewer` -> ccf-literature-searcher, ccf-idea-optimizer
- `ccf-literature-searcher` -> ccf-idea-optimizer, ccf-experiment-designer, ccf-paper-writer
- `ccf-experiment-designer` -> ccf-literature-searcher, ccf-figure-table-builder, ccf-paper-writer
- `ccf-paper-writer` -> ccf-venue-format-guide, ccf-paper-compressor, ccf-writing-reviewer
- `ccf-paper-compressor` -> ccf-paper-writer, ccf-submission-checker
- `ccf-scientific-reviewer` -> ccf-paper-writer, ccf-writing-reviewer, ccf-experiment-designer
- `ccf-writing-reviewer` -> ccf-paper-writer, ccf-venue-format-guide, ccf-submission-checker
- `ccf-integrity-auditor` -> ccf-paper-writer, ccf-scientific-reviewer, ccf-citation-auditor
- `ccf-citation-auditor` -> ccf-literature-searcher, ccf-paper-writer
- `ccf-figure-table-builder` -> ccf-experiment-designer, ccf-paper-writer, ccf-integrity-auditor
- `ccf-artifact-packager` -> ccf-experiment-designer, ccf-submission-checker, ccf-paper-writer
- `ccf-venue-format-guide` -> ccf-paper-writer, ccf-writing-reviewer, ccf-submission-checker
- `ccf-submission-checker` -> ccf-venue-format-guide, ccf-paper-compressor, ccf-paper-writer
- `ccf-rebuttal-writer` -> ccf-paper-writer, ccf-experiment-designer, ccf-submission-checker
- `ccf-resubmission-adapter` -> ccf-venue-format-guide, ccf-paper-writer, ccf-submission-checker
- `ccf-paper-presenter` -> ccf-paper-writer
- `ccf-common` -> All CCFA skills
- `ccf-skill-forger` -> ccf-common

## Venue Layer Rule

Venue knowledge is reference material, not 109 runtime skills. Use:

- `ccf-paper-writer/references/venue-guides/index.md`
- `ccf-paper-writer/references/venue-guides/<venue>.md`
- `ccf-venue-format-guide` for format-only questions

## Smoke Prompts

| Prompt | Expected route |
| --- | --- |
| 先帮我把论文项目流程和下一步拆清楚 | `ccf-workflow-planner` |
| 优化一个 CVPR idea | `ccf-idea-optimizer` |
| 给三个 idea 评分排名 | `ccf-idea-reviewer` |
| 搜索 related work 和 benchmark | `ccf-literature-searcher` |
| 设计对比实验和消融 | `ccf-experiment-designer` |
| 润色 introduction 并降低 reviewer 风险 | `ccf-paper-writer` |
| CVPR page limit / LaTeX template / anonymity | `ccf-venue-format-guide` |
| 完整审稿并给分 | `ccf-scientific-reviewer` |
| 逐段写作评审和 LaTeX 检查 | `ccf-writing-reviewer` |
| 检查引用是否真实且支持上下文 | `ccf-citation-auditor` |
| 审计 claim 和数字是否一致 | `ccf-integrity-auditor` |
| 检查投稿 PDF 是否匿名、超页、字体合规 | `ccf-submission-checker` |
| 根据 R1/R2 写 rebuttal 并维护修改表 | `ccf-rebuttal-writer` |
| 迁移到 SIGMOD 但不新增实验 | `ccf-resubmission-adapter` |
| 把论文做成 slides 和 Q&A | `ccf-paper-presenter` |
| 维护 CCFA skill | `ccf-skill-forger` |
