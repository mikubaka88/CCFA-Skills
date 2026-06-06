# CCFA Skills Catalog

This catalog is the public trigger-conflict index for the current CCFA family. All installable runtime skills use the `ccf-<object>-<role/action>` style, with `ccf-common` kept as the governance-module exception. If this catalog conflicts with a skill's `SKILL.md`, the `SKILL.md` wins and this catalog should be patched.

## Canonical Skills

| Skill | Group | Startup condition | 中文启动条件 | Do not use for | Linked skills |
| --- | --- | --- | --- | --- | --- |
| `ccf-project-scaffolder` | Project | Creates project folders, copies/selects templates, and initializes ccfa.yaml. | 脚手架：建目录、选模板、初始化 ccfa.yaml。 | Does not create research content. | ccf-pipeline-orchestrator, ccf-paper-writer, ccf-submission-checker |
| `ccf-pipeline-orchestrator` | Project | Coordinates project stages, gates, artifacts, and handoffs. | 编排阶段、gate、artifact 与 handoff。 | Does not do downstream work itself. | All owning skills |
| `ccf-workflow-planner` | Planning | Clarifies goals, constraints, scope, success criteria, and next skill. | 澄清目标、范围、成功标准与下一步 skill。 | Does not optimize, search, write, review, or rebut. | Most CCFA skills |
| `ccf-idea-optimizer` | Ideation | Turns rough directions into problem-gap-insight-method-evidence plans. | 把粗 idea 具象化成问题、gap、insight、方法和证据计划。 | Does not rank ideas as the main task. | ccf-literature-searcher, ccf-experiment-designer, ccf-paper-writer |
| `ccf-idea-reviewer` | Ideation | Scores, ranks, compares, and triages early ideas. | 严格评分、排序、比较早期 idea。 | Does not polish manuscripts. | ccf-literature-searcher, ccf-idea-optimizer |
| `ccf-literature-searcher` | Evidence | Finds related work, prior art, datasets, benchmarks, and citation evidence. | 检索相关工作、prior art、数据集和 benchmark。 | Does not audit only fixed citations. | ccf-idea-optimizer, ccf-experiment-designer, ccf-paper-writer |
| `ccf-experiment-designer` | Evidence | Designs datasets, baselines, metrics, ablations, robustness tests, and result templates. | 设计数据集、baseline、指标、消融、鲁棒性和结果表模板。 | Does not invent results. | ccf-literature-searcher, ccf-figure-table-builder, ccf-paper-writer |
| `ccf-paper-writer` | Manuscript | Plans, drafts, revises, and polishes manuscript text while preserving evidence scope. | 写作、润色、重组论文正文，并保护既有 idea 和证据边界。 | Does not perform full review or rebuttal. | ccf-venue-format-guide, ccf-paper-compressor, ccf-writing-reviewer |
| `ccf-paper-compressor` | Manuscript | Shortens paper text to word/page limits without changing claims or results. | 在不改 claims/results 的前提下压缩篇幅。 | Does not change evidence or limitations. | ccf-paper-writer, ccf-submission-checker |
| `ccf-scientific-reviewer` | Review | Runs full scientific manuscript review, scoring, simulated reviewers, and AC/meta-review. | 做完整科学审稿、评分、模拟 reviewer 和 AC/meta-review。 | Does not rewrite prose or do format-only checks. | ccf-paper-writer, ccf-writing-reviewer, ccf-experiment-designer |
| `ccf-writing-reviewer` | Review | Reviews paragraph logic, writing clarity, consistency, LaTeX/format, and presentation risks. | 评审段落逻辑、表达清晰度、一致性、LaTeX/格式和展示风险。 | Does not score scientific acceptance. | ccf-paper-writer, ccf-venue-format-guide, ccf-submission-checker |
| `ccf-integrity-auditor` | Audit | Audits claim-support, result-to-claim, numeric, terminology, and figure/table consistency. | 审计 claim-support、结果到 claim、数字、术语和图表一致性。 | Does not replace scientific review. | ccf-paper-writer, ccf-scientific-reviewer, ccf-citation-auditor |
| `ccf-citation-auditor` | Audit | Verifies existing citations, BibTeX metadata, paper existence, and citation-context support. | 核验已有引用、BibTeX 元数据、文献存在性和引用上下文支撑。 | Does not search broadly for new papers. | ccf-literature-searcher, ccf-paper-writer |
| `ccf-figure-table-builder` | Output | Builds and audits figures, LaTeX tables, captions, SVG/PDF assets from real results. | 基于真实结果构建和审计图、表、caption、SVG/PDF。 | Does not invent numbers. | ccf-experiment-designer, ccf-paper-writer, ccf-integrity-auditor |
| `ccf-artifact-packager` | Output | Prepares artifact and reproducibility package plans, env notes, seeds, licenses, and README. | 准备 artifact/reproducibility 包、环境、seed、license 和 README。 | Does not promise unavailable releases. | ccf-experiment-designer, ccf-submission-checker, ccf-paper-writer |
| `ccf-venue-format-guide` | Submission | Answers venue LaTeX, template, page-limit, anonymity, and camera-ready format questions. | 回答会议 LaTeX、template、页数、匿名和 camera-ready 格式问题。 | Does not handle manuscript content. | ccf-paper-writer, ccf-writing-reviewer, ccf-submission-checker |
| `ccf-submission-checker` | Submission | Checks LaTeX/PDF builds, page limits, anonymity, fonts, metadata, templates, and policy freshness. | 检查 LaTeX/PDF、页数、匿名、字体、metadata、template 和 policy freshness。 | Does not polish content. | ccf-venue-format-guide, ccf-paper-compressor, ccf-paper-writer |
| `ccf-rebuttal-writer` | Post-review | Writes rebuttals, author responses, response letters, revision summaries, and revision ledgers. | 写 rebuttal、作者回复、response letter、修改说明和 revision ledger。 | Does not trigger for ordinary writing. | ccf-paper-writer, ccf-experiment-designer, ccf-submission-checker |
| `ccf-resubmission-adapter` | Post-review | Adapts an existing paper to a new venue under conservative no-new-experiment defaults. | 把已有论文保守迁移到新 venue，默认不新增实验、不改 bib。 | Does not add experiments or bibliography changes unless authorized. | ccf-venue-format-guide, ccf-paper-writer, ccf-submission-checker |
| `ccf-paper-presenter` | Post-review | Converts a paper into slides, poster, talk script, figure narration, and Q&A bank. | 把论文转成 slides、poster、talk script、图表讲解和 Q&A。 | Does not perform pre-submission review. | ccf-paper-writer |
| `ccf-common` | Governance | Shared routing, trigger registry, handoff modes, source registry, privacy policy, and artifact contracts. | 共享路由、触发注册、handoff、source registry、隐私策略和 artifact 合约。 | Not an ordinary research task skill. | All CCFA skills |
| `ccf-skill-forger` | Governance | Creates, updates, validates, and audits CCFA/Codex skills and family governance. | 创建、更新、校验和审计 CCFA/Codex skills 及家族治理。 | Does not do research writing or review. | ccf-common |

## Naming And Merge Decisions

| Old name | Current name | Reason |
| --- | --- | --- |
| `ccf-brainstorming` | `ccf-workflow-planner` | Clearer role name; avoids overlap with generic brainstorming. |
| `ccf-literature-search` | `ccf-literature-searcher` | Aligns with role/action naming. |
| `ccf-writing-skills` | `ccf-paper-writer` | Replaces plural family-style name with a single owning role. |
| `ccf-conference-reviewer` | `ccf-scientific-reviewer` | Names the review type, not the venue layer. |
| `ccf-conference-writing-reviewer` | `ccf-writing-reviewer` | Keeps writing review distinct from scientific review. |
| `ccf-conference-paper-rebuttal` | `ccf-rebuttal-writer` | Names the output responsibility. |
| `ccf-conference-guides` | `ccf-venue-format-guide` | Clarifies it handles venue format only. |
| `ccf-paper-project-scaffold` | `ccf-project-scaffolder` | Aligns with role/action naming. |
| `ccf-artifact-reproducibility` | `ccf-artifact-packager` | Clarifies owned artifact output. |
| `ccf-revision-ledger` | `merged into ccf-rebuttal-writer` | Ledger tracking is part of post-review response accountability. |
| `ccf-paper-talk` | `ccf-paper-presenter` | Clarifies presentation ownership. |
| `ccf-forge-skills` | `ccf-skill-forger` | Avoids plural skill-family wording. |

## Conflict Boundaries

- `ccf-idea-optimizer` improves a direction; `ccf-idea-reviewer` scores or ranks it.
- `ccf-literature-searcher` finds new literature; `ccf-citation-auditor` verifies already cited literature.
- `ccf-scientific-reviewer` judges scientific contribution and risk; `ccf-writing-reviewer` judges communication and format; `ccf-integrity-auditor` checks internal evidence consistency.
- `ccf-venue-format-guide` answers venue requirement questions; `ccf-submission-checker` checks an actual submission package.
- `ccf-rebuttal-writer` now owns both response prose and revision ledger tracking, so response promises and manuscript actions stay aligned.

## Venue Guide Rule

The 109 legacy venue runtime skills remain migrated into `ccf-paper-writer/references/venue-guides/`. Use `ccf-venue-format-guide` for format-only questions and `ccf-paper-writer` for manuscript text.
