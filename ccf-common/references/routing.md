# CCFA Routing

Route by the user's primary intent. Do not activate every downstream skill just because it may become useful later.

## Single-Owner Invariant

Choose exactly one primary owner for each user-requested deliverable. A skill's handoff list declares possible next-stage owners; it is not permission to load them together. Add a sidecar only when the current request itself needs a distinct cross-cutting preflight or explicitly combines two deliverables. Future usefulness, checklist completeness, or a broad end-to-end workflow is not enough.

Resolve common collisions by the requested deliverable:

- Revised, polished, compressed, or newly drafted prose -> `ccf-paper-writer`; assessment, scoring, issue diagnosis, or version comparison without rewriting -> `ccf-paper-reviewer`. If the request says full review, scientific review, scoring, assessment-only, or no rewrite, choose reviewer.
- External source discovery -> `ccf-literature-searcher`; end-to-end manuscript assessment remains `ccf-paper-reviewer`, which may request search only when current evidence is actually needed. Supplied-result evidence schemas and result-table structure belong to `ccf-experiment-designer`, not search.
- Datasets, baselines, metrics, ablations, evidence schemas, and what a result table should contain -> `ccf-experiment-designer`; plotting, styling, layout, rendering, result-table color/readability improvement, or editable reconstruction from supplied content/values -> `ccf-visual-composer`.
- `ccf-humanization` is a sidecar only for manuscript-facing writing or final publication-facing experiment prose/tables/captions. It is never the primary owner and is not loaded for raw experiment planning, retrieval, review, auditing, routing, visual rendering, or assessment-only tasks without publication prose.

The current runtime surface contains 17 installable `ccf-*` skills plus the LaTeX/template reference tree. Removed helper names must not be installed as standalone skills.

## Priority Overlay

`ccf-humanization` has first priority for manuscript-facing writing and final publication-facing experiment prose, tables, captions, or method descriptions. Run it as a sidecar preflight, then return ownership to the content skill. Do not load it for raw experiment planning or evidence-schema design. It removes defensive prose and unproductive test sprawl, enforces confirmed full methods, and keeps judgment-sensitive warnings outside artifacts. It does not replace the writer/designer or authorize hiding material evidence.

## Canonical Runtime Skills

| Intent | Owning skill | Included modes | Boundary |
| --- | --- | --- | --- |
| Humanize manuscript/experiment artifacts, remove defensive writing and improbable case sprawl, isolate warnings, deduplicate smoke tests, disable generic SHA-256 requirements, and reject simplified publication methods. | `ccf-humanization` | manuscript-humanization, experiment-humanization, warning-only | Does not conceal material evidence, fabricate results, write the paper, design experiments, or override mandatory disclosures. |
| Create project folders, copy/select templates, initialize `ccfa.yaml`. | `ccf-project-scaffolder` | scaffold | Does not create research content. |
| Plan workflow, decompose tasks, coordinate stages/gates/handoffs. | `ccf-pipeline-orchestrator` | planning, status, gate | Does not perform downstream research work. |
| Explore, rescue, or turn a rough direction into a problem-gap-insight-method-evidence plan. | `ccf-idea-optimizer` | exploratory idea shaping, rescue routes | Does not rank multiple ideas as the main task. |
| Score, compare, rank, and triage early ideas when the user explicitly asks for judgment. | `ccf-idea-reviewer` | idea scoring, stage-aware triage | Does not brainstorm directions or optimize a single idea as the main task. |
| Monitor recent papers, arXiv/OpenReview/venue feeds, labs, competitors, and recurring novelty threats. | `ccf-literature-monitor` | arxiv-watch, venue-watch, novelty-check, trend-scouting, competitor-tracking | Does not replace deep related-work search, citation audit, or final idea scoring. |
| Search literature, prior art, datasets, benchmarks, citation evidence, and opportunity gaps. | `ccf-literature-searcher` | search, screening, opportunity map | Does not audit only already cited papers or act as a final idea kill gate. |
| Design experiments and real-result tables/figures. | `ccf-experiment-designer` | experiment design, result templates, result figures/tables | Does not invent results. |
| Compose publication-grade data figures/tables and scientific method/architecture diagrams, using GPT Image 2 as the default architecture/schematic renderer, followed by optional editable SVG/PDF/PPTX reconstruction; use pure SVG first only on explicit opt-out. | `ccf-visual-composer` | visual-contract, figure-design, architecture-generation, pure-svg-generation, editable-reconstruction, python-plotting, table-design, layout-integration, render-qa | Does not design experiments, invent results/components, write manuscript prose, or perform final submission compliance. |
| Draft, revise, polish, compress, and presentation-adapt paper text. | `ccf-paper-writer` | writing, polishing, compression, venue-aware LaTeX drafting, slides/poster/talk/Q&A | Preserves user format for edits; does not run full review or rebuttal. |
| Convert user-provided paper PDFs into reusable writing exemplar cards. | `ccf-paper-to-exemplar` | exemplar extraction, writing-pattern cards, custom exemplar registration | Does not write papers or perform review. |
| Review manuscripts scientifically and stylistically, including score drift and cross-version comparison with separate relative-progress and absolute-readiness scorecards. | `ccf-paper-reviewer` | scientific review, writing review, format-facing review, version comparison, AC/meta-review | Does not combine the two scorecards, rewrite, rebut, or own the revision ledger. |
| Audit evidence integrity, numbers, figures/tables, and existing citations. | `ccf-integrity-auditor` | claim audit, numeric audit, citation audit | Does not replace review or broad literature search. |
| Check venue rules, LaTeX/PDF package, anonymity, metadata, and artifacts. | `ccf-submission-checker` | venue format, package check, artifact/reproducibility | Does not polish content. |
| Write rebuttals, revision ledgers, response letters, and resubmission plans. | `ccf-rebuttal-writer` | rebuttal, revision ledger, response letter, resubmission | Does not trigger for ordinary writing. |
| Shared routing, source registry, privacy/evidence, artifact contracts. | `ccf-common` | governance | Not an ordinary research task skill. |
| Maintain skills, docs, SVG diagrams, routing, validation, and releases. | `ccf-skill-forger` | skill maintenance, docs/SVG maintenance, release validation | Does not do research writing or review. |

## Default Paper Project Flow

```text
Priority preflight: ccf-humanization

ccf-project-scaffolder
  -> ccf-pipeline-orchestrator
  -> ccf-idea-optimizer
  -> ccf-idea-reviewer
  -> ccf-literature-monitor
  -> ccf-literature-searcher
  -> ccf-experiment-designer
  -> ccf-visual-composer
  -> ccf-paper-to-exemplar (optional style-reference sidecar)
  -> ccf-paper-writer
  -> ccf-paper-reviewer
  -> ccf-integrity-auditor
  -> ccf-submission-checker
  -> ccf-rebuttal-writer

Governance: ccf-common / ccf-skill-forger
```

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
| 给三个 idea 评分排名 / 明确让我严格取舍 | `ccf-idea-reviewer` |
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
| 完整审稿、逐段写作评审或 LaTeX 表达检查 | `ccf-paper-reviewer` |
| 对比论文新旧版本、检查复审分数漂移或 moving-target review | `ccf-paper-reviewer` |
| 检查 claim、数字、引用是否一致且有支撑 | `ccf-integrity-auditor` |
| NeurIPS page limit / template / anonymity / artifact checklist | `ccf-submission-checker` |
| 根据 R1/R2 写 rebuttal 并维护修改表 | `ccf-rebuttal-writer` |
| 迁移到 ICLR 但不新增实验 | `ccf-rebuttal-writer` |
| 维护 CCFA skill、README、SVG 或 release | `ccf-skill-forger` |
