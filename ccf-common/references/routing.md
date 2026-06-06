# CCFA Routing

Use this file to prevent trigger overlap across the CCFA Skills family. Route by the user's current task, not by every possible downstream action. `SKILL.md` remains authoritative if this file conflicts with an individual skill.

## Canonical Routes

| User intent | Owning skill | Boundary |
| --- | --- | --- |
| Complex research workflow clarification, task decomposition, and skill-routing planning. | `ccf-brainstorming` | Do not optimize ideas, search literature, write, review, or rebut as the primary output. |
| Make rough research directions concrete: problem, method, novelty, and evidence plan. | `ccf-idea-optimizer` | Do not rank or score ideas as the main job. |
| Strictly score, rank, compare, and triage early research ideas. | `ccf-idea-reviewer` | Do not polish manuscripts or optimize a single fuzzy idea unless scoring is explicit. |
| Find prior art, related work, datasets, benchmarks, and citation evidence online. | `ccf-literature-search` | Do not write the paper or audit an already fixed bibliography as the main task. |
| Design evaluation protocols, baselines, ablations, metrics, and result table templates. | `ccf-experiment-designer` | Do not invent experimental results. |
| Plan, draft, revise, polish, and reviewer-proof manuscript text. | `ccf-writing-skills` | Do not change idea scope without confirmation; do not replace full scientific review or rebuttal. |
| Reduce paper, section, abstract, related-work, method, or experiment length. | `ccf-paper-compressor` | Do not change claims, evidence, results, or limitations. |
| Full scientific manuscript review, simulated reviewers, AC/meta-review, scoring, and acceptance-risk diagnosis. | `ccf-conference-reviewer` | Do not rewrite prose or perform venue-format-only checks. |
| Writing-only review, paragraph logic, consistency, LaTeX/format audit, and presentation risks. | `ccf-conference-writing-reviewer` | Do not score scientific acceptance as a full reviewer. |
| Draft rebuttal, author response, response letter, and revision summary after real reviews. | `ccf-conference-paper-rebuttal` | Do not trigger for ordinary manuscript writing. |
| Query conference LaTeX, template, anonymity, page limit, camera-ready, and venue-format requirements. | `ccf-conference-guides` | Do not write, polish, review, or rebut paper content. |
| Coordinate project stages, gates, handoffs, and ccfa.yaml state. | `ccf-pipeline-orchestrator` | Do not write, review, search, or design experiments itself. |
| Create a paper-project directory, copy templates, and initialize ccfa.yaml. | `ccf-paper-project-scaffold` | Do not generate research content. |
| Audit claim-support, result-to-claim alignment, numbers, terminology, and evidence consistency. | `ccf-integrity-auditor` | Do not perform full scientific acceptance review. |
| Verify existing citations, BibTeX metadata, existence, and citation-context support. | `ccf-citation-auditor` | Do not perform broad literature search for new papers. |
| Check LaTeX/PDF build, page limit, anonymity, metadata, fonts, templates, and policy freshness. | `ccf-submission-checker` | Do not polish or rewrite manuscript content. |
| Generate or audit figures, LaTeX tables, SVG/PDF outputs, and QA from real supplied results. | `ccf-figure-table-builder` | Do not invent data. |
| Prepare artifact checklist, code/data/model release plan, seed/env notes, and reproducibility appendix. | `ccf-artifact-reproducibility` | Do not claim reproducibility without evidence. |
| Maintain reviewer-comment to action to manuscript-location to status tracking. | `ccf-revision-ledger` | Do not replace rebuttal wording. |
| Adapt an existing manuscript to a new venue under conservative default constraints. | `ccf-resubmission-adapter` | Do not add experiments or edit bibliography unless authorized. |
| Convert a paper into slides, poster, talk script, Q&A, or presentation plan. | `ccf-paper-talk` | Do not perform pre-submission scientific review. |
| Shared routing, handoff, task modes, source registry, privacy/evidence, and artifact governance. | `ccf-common` | Not an ordinary research task skill. |
| Create, update, validate, or audit CCFA/Codex skills and shared controls. | `ccf-forge-skills` | Do not perform research writing or review work. |

## Venue Layer Rule

`ccf-conference-skills/<venue>/SKILL.md` is removed as a runtime layer in v0.4. Venue knowledge now enters through:

- `ccf-writing-skills/references/venue-guides/index.md`
- `ccf-writing-skills/references/venue-guides/<venue>.md`
- `ccf-conference-guides` for format-only user questions

Writing, polishing, review, rebuttal, resubmission, and submission-package checks must route to their owning skills.

## Default Paper Project Flow

```text
ccf-paper-project-scaffold
  -> ccf-pipeline-orchestrator
  -> ccf-brainstorming
  -> ccf-idea-optimizer
  -> ccf-idea-reviewer
  -> ccf-literature-search
  -> ccf-experiment-designer
  -> ccf-writing-skills
  -> ccf-integrity-auditor / ccf-citation-auditor
  -> ccf-figure-table-builder / ccf-artifact-reproducibility
  -> ccf-paper-compressor
  -> ccf-conference-reviewer
  -> ccf-conference-writing-reviewer
  -> ccf-submission-checker
  -> ccf-conference-paper-rebuttal / ccf-revision-ledger
  -> ccf-resubmission-adapter / ccf-paper-talk
```

## Handoff Map

- `ccf-brainstorming` -> Most CCFA skills through partial handoff.
- `ccf-idea-optimizer` -> ccf-literature-search, ccf-experiment-designer, ccf-writing-skills.
- `ccf-idea-reviewer` -> ccf-literature-search, ccf-idea-optimizer.
- `ccf-literature-search` -> ccf-idea-optimizer, ccf-idea-reviewer, ccf-experiment-designer, ccf-writing-skills.
- `ccf-experiment-designer` -> ccf-literature-search, ccf-writing-skills, ccf-figure-table-builder.
- `ccf-writing-skills` -> ccf-conference-guides, ccf-paper-compressor, ccf-conference-writing-reviewer, ccf-conference-reviewer.
- `ccf-paper-compressor` -> ccf-writing-skills, ccf-submission-checker.
- `ccf-conference-reviewer` -> ccf-writing-skills, ccf-conference-writing-reviewer, ccf-experiment-designer.
- `ccf-conference-writing-reviewer` -> ccf-writing-skills, ccf-conference-guides, ccf-submission-checker.
- `ccf-conference-paper-rebuttal` -> ccf-revision-ledger, ccf-writing-skills.
- `ccf-conference-guides` -> ccf-writing-skills, ccf-conference-writing-reviewer, ccf-submission-checker.
- `ccf-pipeline-orchestrator` -> All stage-owning CCFA skills.
- `ccf-paper-project-scaffold` -> ccf-pipeline-orchestrator, ccf-writing-skills, ccf-submission-checker.
- `ccf-integrity-auditor` -> ccf-writing-skills, ccf-conference-reviewer, ccf-citation-auditor.
- `ccf-citation-auditor` -> ccf-literature-search, ccf-writing-skills.
- `ccf-submission-checker` -> ccf-conference-guides, ccf-paper-compressor, ccf-writing-skills.
- `ccf-figure-table-builder` -> ccf-experiment-designer, ccf-writing-skills, ccf-integrity-auditor.
- `ccf-artifact-reproducibility` -> ccf-experiment-designer, ccf-submission-checker, ccf-writing-skills.
- `ccf-revision-ledger` -> ccf-conference-paper-rebuttal, ccf-writing-skills.
- `ccf-resubmission-adapter` -> ccf-conference-guides, ccf-writing-skills, ccf-submission-checker.
- `ccf-paper-talk` -> ccf-writing-skills.
- `ccf-common` -> All CCFA skills.
- `ccf-forge-skills` -> ccf-common.

## Smoke Prompts

| Prompt | Expected route |
| --- | --- |
| 优化一个 CVPR idea | `ccf-idea-optimizer` |
| 给三个 idea 评分排名 | `ccf-idea-reviewer` |
| 搜索 related work 和 benchmark | `ccf-literature-search` |
| 设计对比实验和消融 | `ccf-experiment-designer` |
| 润色 introduction 并降低 reviewer 风险 | `ccf-writing-skills` |
| CVPR page limit / LaTeX template / anonymity | `ccf-conference-guides` |
| 完整审稿并给分 | `ccf-conference-reviewer` |
| 逐段写作评审和 LaTeX 检查 | `ccf-conference-writing-reviewer` |
| 根据 R1/R2 写 rebuttal | `ccf-conference-paper-rebuttal` |
| 检查引用是否真实且支持上下文 | `ccf-citation-auditor` |
| 审计 claim 和数字是否一致 | `ccf-integrity-auditor` |
| 迁移到 SIGMOD 但不新增实验 | `ccf-resubmission-adapter` |
| 把论文做成 slides 和 Q&A | `ccf-paper-talk` |
