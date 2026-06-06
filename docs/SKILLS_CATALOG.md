# CCFA Skills Catalog

This catalog is the public trigger-conflict index for the current CCFA family. If this document conflicts with a skill's `SKILL.md`, `SKILL.md` is authoritative.

## Runtime Skills

| Skill | Stage | Startup condition | 中文启动条件 | Included modes | Do not use for |
| --- | --- | --- | --- | --- | --- |
| `ccf-project-scaffolder` | Setup | Create project folders, copy/select templates, initialize `ccfa.yaml`. | 建项目目录、选模板、初始化 `ccfa.yaml`。 | scaffold | Research content generation. |
| `ccf-pipeline-orchestrator` | Planning | Plan workflow, decompose tasks, coordinate gates and handoffs. | 拆任务、排阶段、定 gate、决定下一个 owner。 | planning, status, gate | Writing, review, search, experiment design, rebuttal. |
| `ccf-idea-optimizer` | Idea | Turn rough directions into problem-gap-insight-method-evidence plans. | 把粗 idea 具象化成问题、gap、insight、方法和证据计划。 | idea shaping | Ranking multiple ideas as the main task. |
| `ccf-idea-reviewer` | Idea | Score, compare, rank, and triage early ideas. | 严格评分、比较、排序早期 idea。 | idea scoring | Manuscript polishing or single-idea development. |
| `ccf-literature-searcher` | Evidence | Search and screen literature, prior art, datasets, benchmarks. | 检索相关工作、prior art、数据集和 benchmark。 | search, screening | Auditing only already cited papers. |
| `ccf-experiment-designer` | Evidence | Design experiments and build real-result tables/figures. | 设计实验、baseline、消融、结果表和真实结果图。 | experiment design, result templates, result figures/tables | Inventing results or drawing CCFA docs diagrams. |
| `ccf-paper-writer` | Manuscript | Draft, revise, polish, compress, and presentation-adapt paper text. | 写作、润色、压缩论文，并生成 slides/poster/talk/Q&A。 | draft, polish, compression, presentation | Full review, evidence audit, package check, rebuttal. |
| `ccf-paper-reviewer` | Review | Review manuscripts scientifically and stylistically. | 做科学审稿、写作评审、格式表达风险和 AC/meta-review。 | scientific review, writing review, format-facing review | Rewriting manuscript text or drafting rebuttals. |
| `ccf-integrity-auditor` | Audit | Audit claims, numbers, figures/tables, citations, and BibTeX. | 审计 claim、数字、图表、引用、BibTeX 和上下文支撑。 | claim audit, numeric audit, citation audit | Full scientific review or broad literature search. |
| `ccf-submission-checker` | Submission | Check venue rules, LaTeX/PDF package, anonymity, metadata, artifacts. | 查会议格式、模板页数、匿名、PDF metadata、artifact/reproducibility。 | venue format, package check, artifact | Polishing manuscript content. |
| `ccf-rebuttal-writer` | Post-review | Write rebuttals, response letters, revision ledgers, resubmission plans. | 写 rebuttal、response letter、revision ledger 和保守重投计划。 | rebuttal, ledger, response letter, resubmission | Ordinary manuscript writing. |
| `ccf-common` | Governance | Maintain shared routing, source registry, privacy/evidence policy, artifact contracts. | 维护共享路由、source registry、隐私/证据策略和 artifact 合约。 | governance | Ordinary research work. |
| `ccf-skill-forger` | Governance | Maintain skills, routing, docs, SVG diagrams, validation, and releases. | 维护 skills、路由、README、SVG、校验和 release。 | skill maintenance, docs/SVG maintenance | Research writing, review, or experiments. |

## Merged Entries

| Removed standalone skill | Current owner | Why |
| --- | --- | --- |
| `ccf-workflow-planner` | `ccf-pipeline-orchestrator` | Planning and orchestration are the same project-control layer. |
| `ccf-paper-compressor` | `ccf-paper-writer` | Compression changes manuscript text and must share writing safeguards. |
| `ccf-writing-reviewer` | `ccf-paper-reviewer` | Writing review is a review mode, not a separate runtime owner. |
| `ccf-citation-auditor` | `ccf-integrity-auditor` | Citation verification is evidence integrity. |
| `ccf-figure-table-builder` | `ccf-experiment-designer` | Result figures/tables depend on experiment evidence and real numbers. |
| `ccf-artifact-packager` | `ccf-submission-checker` | Artifact readiness is submission readiness. |
| `ccf-venue-format-guide` | `ccf-submission-checker` | Venue format lookup is a submission gate; writing still reads venue references. |
| `ccf-resubmission-adapter` | `ccf-rebuttal-writer` | Resubmission follows reviewer-response and revision-ledger logic. |
| `ccf-paper-presenter` | `ccf-paper-writer` | Slides/posters/talk scripts are paper-derived writing outputs. |
| `ccf-doc-diagram-designer` | `ccf-skill-forger` | Docs SVGs are repository maintenance. |

## Conflict Rules

- Idea shaping goes to `ccf-idea-optimizer`; idea scoring/ranking goes to `ccf-idea-reviewer`.
- New literature discovery goes to `ccf-literature-searcher`; existing citation verification goes to `ccf-integrity-auditor`.
- Manuscript rewriting, compression, and presentation outputs go to `ccf-paper-writer`; judgment goes to `ccf-paper-reviewer`.
- Real result tables and figures go to `ccf-experiment-designer`; docs diagrams go to `ccf-skill-forger`.
- Venue requirements, package checks, anonymity, and artifact readiness go to `ccf-submission-checker`.
- Reviewer responses, revision ledgers, and resubmission plans go to `ccf-rebuttal-writer`.

## Venue Guides

The legacy per-venue runtime layer remains reference-only:

- `ccf-paper-writer/references/venue-guides/index.md`
- `ccf-paper-writer/references/venue-guides/<venue>.md`

Use `ccf-paper-writer` for venue-aware manuscript text and `ccf-submission-checker` for venue/package compliance.
