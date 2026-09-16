# CCFA Routing

Activate `ccf-humanization` first and `ccf-common` second before any CCFA specialist, including helpers, review, retrieval, visuals, and maintenance. Then route by the user's primary intent and necessary dependencies. These two universal preflights do not imply running every downstream skill.

## Accountable Owner, Collaborative Execution

Assign one integrating owner to each requested deliverable. Ownership determines who combines evidence, resolves findings, and delivers the result; it does not restrict the work to one skill. Proactively use specialist skills for missing prerequisites, material uncertainties, or checks that can change the result. The user need not name those skills or request separate reports. Role exclusions define primary responsibilities, not a ban on collaboration. Registry handoffs are common routes, not an exhaustive permission list or a mandatory sequence.

Use `handoff-modes.md` to carry evidence and integrate contributions. A specialist can resolve an upstream dependency or check a result and return to the integrating owner; requested next-stage artifacts may transfer ownership. Necessary internal work is within the deliverable's scope, subject to explicit limits and host permissions. `ccf-common` is active as shared control, not an additional research deliverable.

Resolve common collisions by the requested deliverable:

- Judge a research concept (“思路审核”, “靠谱吗”, “值得做吗”, “创新够不够”, or mechanism logic) -> `ccf-idea-reviewer`, without requiring scores. Judge manuscript evidence, completeness, writing, or revision readiness -> `ccf-paper-reviewer`. A full PDF can still be input to concept-only review. Idea review excludes experiment assessment by default; manuscript scientific review evaluates the evidence supporting its claims. Develop an idea -> `ccf-idea-optimizer`. A combined request has each deliverable handled by its owner.

- Revised, polished, compressed, or newly drafted prose -> `ccf-paper-writer`; assessment, scoring, issue diagnosis, or version comparison without rewriting -> `ccf-paper-reviewer`. If the request says full review, scientific review, scoring, assessment-only, or no rewrite, choose reviewer.
- External source discovery -> `ccf-literature-searcher`; end-to-end manuscript assessment remains `ccf-paper-reviewer`, which may request search only when current evidence is actually needed. Supplied-result evidence schemas and result-table structure belong to `ccf-experiment-designer`, not search.
- Datasets, baselines, metrics, ablations, evidence schemas, and what a result table should contain -> `ccf-experiment-designer`; plotting, styling, layout, rendering, result-table color/readability improvement, or editable reconstruction from supplied content/values -> `ccf-visual-composer`.
- `ccf-humanization` is the mandatory first preflight for every CCFA skill; its baseline also applies to planning, retrieval, review, audit, and visuals. Prose rewriting and detailed experiment checks run only when applicable and authorized. It does not take over the specialist's artifact or soften evidence-backed criticism.

The current runtime surface contains 17 installable `ccf-*` skills plus the LaTeX/template reference tree. Removed helper names must not be installed as standalone skills.

## Priority Overlay

The startup order is `ccf-humanization` -> `ccf-common` -> specialist owner/contributors. Read and apply both preflight entries at the start of a task, then reuse them while their rules, scope, and source versions remain applicable. Every transition inherits active preflights; it does not repeat the complete editing or maintenance workflow. Restore missing context after compaction and refresh affected rules after a change. Bootstrap the two shared skills once without recursively invoking each other. Host permissions and explicit user exclusions still take precedence; do not claim an unavailable or disabled preflight ran.

Humanization removes empty self-defense while preserving material facts, rigorous criticism, and calibrated uncertainty. Common establishes scope, routing, evidence, handoffs, and artifact controls. Neither requires another user-visible report or separate agent. For non-prose tasks, apply the baseline without fabricating text to edit. Full-method checks remain conditional on reported comparisons or actual relevant experiment work.

## Canonical Runtime Skills

| Intent | Owning skill | Included modes | Boundary |
| --- | --- | --- | --- |
| First preflight for every CCFA task; keep communication direct, preserve facts and critique, and apply detailed prose/experiment checks when relevant. | `ccf-humanization` | family-preflight, manuscript-humanization, experiment-humanization, warning-only | Does not conceal material evidence, soften valid criticism, fabricate results, take over specialist ownership, or authorize unrequested rewrites. |
| Create project folders, copy/select templates, initialize `ccfa.yaml`. | `ccf-project-scaffolder` | scaffold | Does not create research content. |
| Plan workflow, decompose tasks, coordinate stages/gates/handoffs. | `ccf-pipeline-orchestrator` | planning, status, gate | Does not perform downstream research work. |
| Explore, rescue, or turn a rough direction into a problem-gap-insight-method-evidence plan. | `ccf-idea-optimizer` | exploratory idea shaping, rescue routes | Does not rank multiple ideas as the main task. |
| Assess research value, novelty, insight, and mechanism, including natural qualitative judgments without scores. | `ccf-idea-reviewer` | concept assessment, idea scoring/ranking, stage-aware triage | Experiments are outside default scope; development and manuscript evidence review have separate owners. |
| Monitor recent papers, arXiv/OpenReview/venue feeds, labs, competitors, and recurring novelty threats. | `ccf-literature-monitor` | arxiv-watch, venue-watch, novelty-check, trend-scouting, competitor-tracking | Does not replace deep related-work search, citation audit, or final idea scoring. |
| Search literature, prior art, datasets, benchmarks, citation evidence, and opportunity gaps. | `ccf-literature-searcher` | search, screening, opportunity map | Does not audit only already cited papers or act as a final idea kill gate. |
| Design experiments and real-result tables/figures. | `ccf-experiment-designer` | experiment design, result templates, result figures/tables | Does not invent results. |
| Compose publication-grade data figures/tables and scientific method/architecture diagrams, using GPT Image 2 as the default architecture/schematic renderer, followed by requested editable SVG/PDF/PPTX reconstruction or an optional offer; use pure SVG first only on explicit opt-out. | `ccf-visual-composer` | visual-contract, figure-design, architecture-generation, pure-svg-generation, editable-reconstruction, python-plotting, table-design, layout-integration, render-qa | Does not design experiments, invent results/components, write manuscript prose, or perform final submission compliance. |
| Draft, revise, polish, compress, and presentation-adapt paper text. | `ccf-paper-writer` | writing, polishing, compression, venue-aware LaTeX drafting, slides/poster/talk/Q&A | Preserves user format for edits; does not run full review or rebuttal. |
| Convert user-provided paper PDFs into reusable writing exemplar cards. | `ccf-paper-to-exemplar` | exemplar extraction, writing-pattern cards, custom exemplar registration | Does not write papers or perform review. |
| Review manuscripts scientifically and stylistically, including score drift and cross-version comparison with separate relative-progress and absolute-readiness scorecards. | `ccf-paper-reviewer` | scientific review, writing review, format-facing review, version comparison, AC/meta-review | Does not combine the two scorecards, rewrite, rebut, or own the revision ledger. |
| Audit evidence integrity, numbers, figures/tables, and existing citations. | `ccf-integrity-auditor` | claim audit, numeric audit, citation audit | Does not replace review or broad literature search. |
| Check venue rules, LaTeX/PDF package, anonymity, metadata, and artifacts. | `ccf-submission-checker` | venue format, package check, artifact/reproducibility | Does not polish content. |
| Write rebuttals, revision ledgers, response letters, and resubmission plans. | `ccf-rebuttal-writer` | rebuttal, revision ledger, response letter, resubmission | Does not trigger for ordinary writing. |
| Shared preflight for every CCFA task after Humanization; routing, evidence, handoffs, artifact controls, and their maintenance. | `ccf-common` | family-preflight, governance | Does not replace research specialists or run maintenance checks merely because it was activated. |
| Maintain skills, docs, SVG diagrams, routing, validation, and releases. | `ccf-skill-forger` | skill maintenance, docs/SVG maintenance, release validation | Does not do research writing or review. |

## Prerequisites And Cooperation

Before making a dependent claim or building its artifact, identify the inputs and checks that make it trustworthy. Classify each relevant prerequisite as satisfied by applicable evidence, missing, conflicting, or outside the explicit scope. Keep this compact in context or existing project state; no new checklist file is required.

- Reuse a completed prerequisite only when its source, assumptions, coverage, and freshness still support the current decision. A stored summary or file's existence alone does not establish this.
- Resolve missing or conflicting prerequisites through the appropriate skill before treating the dependent conclusion as verified. Continue independent work; use a clearly provisional result when the requested scope allows it. A blocked lookup is not a passed check, and an unknown empirical result cannot be obtained by adding more skills.
- Select a specialist when its contribution can change evidence, design, judgment, presentation, or a material completion check. Ask a concrete question and use its answer. Skip duplicate passes and unrelated stages, not necessary groundwork. Do not impose a fixed skill count or full-family sequence.
- After integrating changes, check affected claims and dependencies. Reopen a check when new evidence, a changed assumption, or an unresolved finding warrants it. Finish when requested outputs and applicable prerequisites/checks are satisfied, or clearly identify the dependent part that remains incomplete.

The following are conditional dependency routes, not a mandatory pipeline:

| Requested outcome | Prerequisite or useful specialist contribution |
| --- | --- |
| Develop or judge an idea | Searcher grounds decisive closest-work/novelty claims when verified evidence is missing. During development, idea reviewer can check an unresolved conceptual weakness and return findings to optimizer. A requested standalone assessment keeps its review format. Concept review does not acquire experiment requirements. |
| Draft or substantially revise a paper | Writer establishes claims, evidence, citations, and relevant venue constraints; uses searcher for missing sources and auditor for unresolved citation/number conflicts. Humanization accompanies prose. Reviewer checks materially changed argument/evidence links before finalizing; a spelling edit does not trigger a full review. |
| Design experiments | Designer establishes claims, method, baseline provenance, metrics, and data compatibility. Searcher fills missing external evidence; reviewer can challenge a consequential claim-to-test mismatch. Plans and expected results remain distinct from observations. |
| Compose a figure or table | Resolve data, units, metric meaning, topology, and intended message before rendering dependent content. Designer clarifies result semantics, the method's owner clarifies topology, and auditor resolves source conflicts when needed. Reuse established semantics for a local visual edit; check layout and exports afterward. |
| Review a manuscript | Reviewer inspects the required manuscript evidence; searcher resolves consequential novelty gaps, auditor checks decisive numerical/citation conflicts, and designer clarifies consequential protocol ambiguities. Return findings to reviewer without rewriting the paper or proposing an unrequested experiment campaign. |
| Review and revise | Reviewer findings -> writer changes -> affected reviewer/auditor checks. Reuse stable concern IDs and unchanged evidence; do not treat the first revision as verified merely because it was written. |
| Rebuttal or submission readiness | Verify actual changes, results, and applicable current rules through their owners before asserting completion/compliance. Submission checker verifies venue/year/track policy; rebuttal writer integrates verified edits and responses. |

Use the orchestrator when coordinating multiple dependencies, conflicting findings, or project gates materially helps completion; ordinary specialist collaboration needs no extra coordinator. A contributor's output is intermediate to the active task. Its integrating owner must use the evidence and resolve material findings before delivery.

## Merged Capability Map

| Old standalone entry | Current owner | Reason |
| --- | --- | --- |
| `ccf-workflow-planner` | `ccf-pipeline-orchestrator` | Planning and stage routing are one project-control responsibility. |
| `ccf-paper-compressor` | `ccf-paper-writer` | Compression changes manuscript text and must preserve writing scope. |
| `ccf-writing-reviewer` | `ccf-paper-reviewer` | Writing review and scientific review are review modes over the same manuscript. |
| `ccf-citation-auditor` | `ccf-integrity-auditor` | Citation verification is evidence integrity, not broad literature search. |
| `ccf-figure-table-builder` | `ccf-experiment-designer`, then `ccf-visual-composer` | Experiment designer owns evidence design and real result values; visual composer owns publication layout, data plotting, scientific architecture diagrams, captions, vector reconstruction, and render QA. |
| `ccf-artifact-packager` | `ccf-submission-checker` | Artifact readiness is part of submission package readiness. |
| `ccf-venue-format-guide` | `ccf-submission-checker` | Venue format lookup is a submission/package gate; paper writing still reads venue references. |
| `ccf-resubmission-adapter` | `ccf-rebuttal-writer` | Resubmission follows review-response and revision-ledger ownership. |
| `ccf-paper-presenter` | `ccf-paper-writer` | Talks, posters, and Q&A are paper-derived writing outputs. |
| `ccf-doc-diagram-designer` | `ccf-skill-forger` | Documentation SVGs are repository maintenance, not research workflow. |

## Venue Layer Rule

Venue knowledge is reference material, not venue-specific runtime skills. Use:

- `ccf-paper-writer/references/venue-guides/index.md`
- `ccf-paper-writer/references/venue-guides/<venue>.md`
- `ccf-submission-checker` for venue format, template, page-limit, anonymity, and package questions

For manuscript writing from only an idea, `ccf-paper-writer` checks the venue guide first and drafts in that venue's LaTeX style. If no target venue guide exists or no venue is named, it uses the NeurIPS guide/template as the fallback and leaves final policy freshness to `ccf-submission-checker`.

## Smoke Prompts

| Prompt | Expected route |
| --- | --- |
| 去掉防御性写作 / 不要把 warning 注入论文 / 精简重复 smoke / 论文只用确认的完整方法 | `ccf-humanization` |
| 先帮我把论文项目流程和下一步拆清楚 | `ccf-pipeline-orchestrator` |
| 优化一个 NeurIPS idea / 找几个可做方向 / 这个方向还能怎么救 | `ccf-idea-optimizer` |
| 给三个 idea 评分排名 / 这个思路靠谱吗 / 值得做吗 / 创新够不够 | `ccf-idea-reviewer` |
| 这份完整 PDF 只审核心思路，不看实验 | `ccf-idea-reviewer` |
| 想法还很粗糙，先判断逻辑是否成立，不用打分 | `ccf-idea-reviewer` |
| 先判断思路是否值得做，再帮我完善 | `ccf-idea-reviewer`, then `ccf-idea-optimizer` |
| 监控竞品 / 追踪新论文 / 最近有没有类似 idea | `ccf-literature-monitor` |
| 搜索 related work、benchmark 和还有哪些 open gap | `ccf-literature-searcher` |
| 设计对比实验、消融和结果表 | `ccf-experiment-designer` |
| 根据真实结果规划论文图表的数据和证据结构 | `ccf-experiment-designer` |
| 优化图表排版 / 选择论文配色 / 多面板 figure 放正文里 | `ccf-visual-composer` |
| 用 Python 画漂亮数据分析图 / 创造有趣但可信的论文图 | `ccf-visual-composer` |
| 根据论文方法生成架构图 / 默认调用 GPT Image 2 / 确认后转成可编辑 SVG、PDF 或 PPTX / 明确要求纯 SVG | `ccf-visual-composer` |
| 把这篇 PDF 做成写作范例 / 添加 exemplar | `ccf-paper-to-exemplar` |
| 润色 introduction 或压缩到页数限制 | `ccf-paper-writer` |
| 把论文做成 slides 和 Q&A | `ccf-paper-writer` |
| 完整审稿 / 稿件有什么硬伤 / 结论站得住吗 / 逐段写作评审 | `ccf-paper-reviewer` |
| 对比论文新旧版本、检查复审分数漂移或 moving-target review | `ccf-paper-reviewer` |
| 检查 claim、数字、引用是否一致且有支撑 | `ccf-integrity-auditor` |
| NeurIPS page limit / template / anonymity / artifact checklist | `ccf-submission-checker` |
| 根据 R1/R2 写 rebuttal 并维护修改表 | `ccf-rebuttal-writer` |
| 迁移到 ICLR 但不新增实验 | `ccf-rebuttal-writer` |
| 维护 CCFA skill、README、SVG 或 release | `ccf-skill-forger` |
