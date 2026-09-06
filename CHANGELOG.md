# Changelog

## Unreleased - review refinement (version remains 0.10.0)

- Made natural concept judgments and manuscript assessments select their respective reviewers without requiring numeric-score wording. A full PDF can still receive concept-only review.
- Replaced the default idea rubric with six conceptual dimensions. Experimental completeness, results, baselines, ablations, and submission readiness no longer affect default idea scores; requested experiment/feasibility extensions remain separate.
- Expanded CSPaper's public assessment, substantive-review, and rating organization into detailed manuscript and concept reports by default, with brief output on explicit request. Aligned templates, entry instructions, and agent prompts; consolidated duplicate audit/role reports while preserving manuscript version-comparison contracts and historical evaluations.
- Adapted evidence anchors, stable concern IDs, revision follow-up, explicit rating fields, and finding-quality checks from inspected open-source review projects. Recorded public provenance; no third-party runtime, dependency, calibration model, or benchmark result was imported.
- Updated three-language README guidance and shared routing, modes, and score rules. Existing package names, directory layout, and plugin version remain unchanged.

## v0.10.0 - 2026-09-05

- Updated all 17 existing skill entries and 16 existing agent prompts for concise routing, mode-specific reference loading, persistent authorization, bounded execution, and proportionate checks, using current official GPT-6 Astra and skill-authoring guidance.
- Strengthened humanization around scientific information: remove imagined reviewer objections, contribution apologies, empty assurances, stacked hedges, and ritual caveats while preserving supported facts, real uncertainty, negative findings, and required disclosures. Removed conflicting forced-limitation and reviewer-defense instructions from writing references.
- Aligned workflow handoffs and requested editable visuals with existing authorization; corrected scaffolding initialization and conditional publication-prose preflight.
- Improved the existing prose checker with bilingual defensive-language candidates, source-line locations, and code/math/quotation exclusions. Repaired the legacy PDF-to-exemplar command, reused the canonical converter, and handled extraction failures and filename collisions.
- Strengthened the existing validator with YAML, resource, Python syntax, project/plugin contract, prose, and version-comparison regression checks. Declared the Codex skill root explicitly without moving packages.
- Made visual work incremental: existing editable sources, palettes, and icons are reused; only affected requested formats are exported and inspected. Consolidated overlapping specifications, prompts, wireframes, asset inventories, and QA records, with reference loading scoped by mode.
- Unified intermediate-file placement under existing project paths or stable task/artifact working directories. Source/assets/cache/build folders are created on demand; current files update in place while raw evidence and required history are preserved.
- Removed citation-count-driven retrieval, redundant report/export defaults, and mandatory exemplar-bundle loading. Literature updates reuse existing topic folders; full scientific assessments retain necessary source coverage.
- Made SVG/text publication atomic and unchanged-content writes reusable. Exemplar conversion preserves completed cards and supports an optional `--full-text-dir` cache destination while retaining existing CLI defaults.
- Switched all three README Star sections to automatically refreshed light/dark history charts and a live count badge; retained the dated local SVG snapshots and documented cache latency. No scheduled commits or new workflow files are required.
- Preserved the 17-skill directory layout, shared metadata fields, project schema, template tree, generated diagrams, and historical evaluation data. No files or dependencies added. Static checks do not establish a GPT-6 quality or speed gain; no new model A/B benchmark or client installation test is claimed.

## v0.9.0 - 2026-08-13

- Refined family-wide skill selection so one task has one clear owner and adjacent skills join only when they materially improve the result, reducing conflicting instructions and unnecessary context.
- Strengthened academic writing guidance with natural terminology, controlled dash use, preserved user-provided exemplars, isolated warnings, and separate judgments for current readiness and improvement over the previous version.
- Expanded `ccf-visual-composer` around GPT Image 2-first method and architecture figures, reference-guided composition, custom icon creation, paper-versus-presentation styles, and genuinely editable SVG, vector PDF, and PPTX reconstruction.
- Reorganized the evaluation report around skill ablations, visual comparisons, model-level regression, latency, token use, and cost, with sampled checks for the optimized family behavior.
- Rewrote the Simplified Chinese, English, and Traditional Chinese README files around the research story, family responsibilities, real visual examples, and clearer non-engineering language.
- Added separate installation and automatic-update guides for Codex, Claude Code, Cursor, Gemini CLI, and other compatible agents.
- Added the DynTrace paper architecture, GPT Image 2 concept, PPT/poster exploration, and LLaVA-4D reference figure to the visual showcase with source and usage notes.
- Rebuilt all 30 documentation diagrams in three languages, added language-specific hero figures, and corrected English hero and workflow layouts to prevent text and connector overlap.
- Added multilingual README navigation and a comic-style Star history chart backed by daily GitHub Stargazers API data through 2026-08-13.

## v0.8.0 - 2026-08-07

- Added `ccf-humanization` as the first-priority manuscript/experiment preflight for direct academic prose, warning-only non-injection, generic SHA-256/checksum removal, effective non-duplicative smoke scope, and confirmed full publication methods.
- Integrated humanization gates into `ccf-paper-writer` and `ccf-experiment-designer`; simplified/toy/proxy/debug methods cannot enter manuscript text or final result tables, and material concerns are surfaced for user review without automatic file changes.
- Expanded the runtime family from 16 to 17 skills and updated routing, artifact contracts, installation sets, manifests, docs, demo smoke coverage, validators, and generated diagrams.
- Extended `ccf-visual-composer` with scientific method/architecture diagram routing, content-derived research-figure prompts, an explicit pre-call GPT Image 2 confirmation gate, generated-draft inspection, and a mandatory post-generation offer to reconstruct editable SVG/vector PDF.
- Defined semantic vector reconstruction requirements so editable deliverables use live text, selectable groups, and typed connectors instead of relabeling an embedded or auto-traced raster as editable.
- Updated routing, trigger registry, artifact ownership, agent guidance, catalog, architecture docs, manifests, and validation for the new visual workflow.
- Added a figure-wide capitalization rule: ordinary English uses natural title or sentence case, while canonical acronyms and initialisms such as `CCF`, `GPT`, `QA`, `SVG/PDF`, `AI`, `PNG`, and `SHA-256` remain uppercase.
- Added three v0.8 visual assets with Chinese titles and English internal labels: the dual-upgrade concept map, a concrete Transformer `Visual Composer` before/after demo, and a concrete `CCF Humanization` manuscript/experiment demo.
- Kept method confirmation as an internal experiment gate while removing confirmation, approval, and publication-readiness status language from manuscript prose; papers state the actual method and scientifically relevant configuration directly.
- Updated all README variants to present the v0.8 visuals without changing the established 17-skill architecture or lifecycle order.

## v0.7.0 - 2026-07-08

- Added `ccf-visual-composer` for publication-grade figure/table visual contracts, palettes, panel maps, caption placement, manuscript integration, and render QA from supplied results.
- Added bundled standard-library Python SVG plotting recipes under `ccf-visual-composer/resources/python/`, including lollipop, slopegraph, heatmap, ridgeline, small-multiple, and radial-scorecard recipes.
- Added `demo/attention-is-all-you-need/visual-composer/` with runnable plotting examples and generated SVG figures from verified Transformer demo data.
- Added plotting inspiration references for Matplotlib, Seaborn, Plotly, Bokeh, Altair, Plotnine, Python Graph Gallery, Scientific Visualization, SciencePlots, and LovelyPlots as design inspiration without code copying.
- Added a multi-expert storyline generation/review/fusion framework to `ccf-paper-writer/references/storyline-blueprint.md` and wired writer routing for scientific storytelling, paper/story structure, insight framing, and claim generation.
- Updated routing, trigger registry, artifact contracts, source registry, installation matrices, docs, manifests, generated SVG diagrams, and handoff rules for the 16-skill family.

## v0.5.1 - 2026-06-09

- Added `ccf-literature-monitor` as the competitor-monitoring and new-paper tracking owner, with overlap scoring, RELAX/RESEARCH/FOLLOW-UP actions, and handoffs to literature search, idea review, idea optimization, paper writing, and integrity audit.
- Standardized quantitative review feedback across idea review, paper review, and writing review: scorecards now require confidence, evidence basis, deductions, repair conditions, and score-change conditions.
- Added shared multi-reviewer panel discipline so reviewers stay independent, evidence-grounded, and factual without forced praise, forced disagreement, or unsupported rejection.
- Updated routing, trigger registry, artifact contracts, installation matrices, README variants, catalog, architecture docs, plugin manifests, validators, and generated-diagram source for the 15-skill family.

## v0.4.5 - 2026-06-06

- Made Simplified Chinese the default `README.md` entry, added `README.en.md`, kept `README.zh-CN.md` as a Simplified Chinese compatibility entry, and preserved free switching between Simplified Chinese, English, and Traditional Chinese.
- Standardized the README top introduction around the research-storyline positioning and expanded the default README so core skill family logic, routing, artifact contracts, installation sets, and merged helper ownership are explained inline.
- Relaxed early idea and literature behavior without weakening strict review: added exploratory mode, rescue routes, stage-aware development potential, literature opportunity maps, and stricter rules for when `abandon` may be used.
- Updated installed-skill guidance, routing docs, catalog text, agent guide, and generated SVG labels so "find/rescue a direction" routes to `ccf-idea-optimizer`, explicit scoring routes to `ccf-idea-reviewer`, and literature scouting returns open gaps rather than acting as a kill gate.
- Added length-budget-aware manuscript drafting: from-scratch submission papers now establish venue page targets, expand underfilled drafts, compress overfilled drafts, and leave final page compliance to `ccf-submission-checker`.
- Reworked the generated architecture SVG layout into a clearer two-row chain with explicit revision loop, `ccfa.yaml`, and governance layer, then regenerated all EN/zh-CN/zh-TW SVGs from `tools/build_ccfa_diagrams.py`.
- Restored `assets/ccfaskills.png` as the README top visual and rewrote README EN/zh-CN/zh-TW around the 13-owner lifecycle, helper-mode merges, installation sets, venue branch, and demo loop.
- Rebuilt all generated SVG diagrams with a clearer family-chain layout: architecture, workflow, catalog, routing, artifact contract, review boundaries, installation, and Attention demo in EN/zh-CN/zh-TW.
- Rewrote `docs/ARCHITECTURE.md` and `docs/SKILLS_CATALOG.md` to explain ownership, artifact state, route boundaries, and merged helper capabilities without ambiguity.
- Expanded the Attention demo TeX bibliography and marked it as a demo reference list that should be refreshed by `ccf-literature-searcher` in real use.
- Audited `Master-cai/Research-Paper-Writing-Skills` and added CCFA-native section writing patterns for abstract, introduction, related work, method, experiments, conclusion, exemplar adaptation, and end-of-draft self-review.
- Strengthened high-information-density output rules: broad/full workflow requests must produce complete artifacts rather than short route summaries or fragmented notes.
- Fixed ICLR venue guidance for 2026 double-blind review basics, page-limit basics, and local style usage.
- Rebuilt the Attention demo as an ICLR closed-loop run with idea review, full compiling LaTeX manuscript, writing/scientific review, integrity audit, rebuttal, submission check, and family self-audit.

## v0.4.4 - 2026-06-06

- Tightened `ccf-paper-writer` output behavior: polish/rewrite/compression preserves the user's original Markdown/LaTeX format, while from-scratch manuscript requests draft the requested artifact instead of a process report.
- Added writer NeurIPS fallback rules: search target venue guides first, then use the NeurIPS LaTeX template when the venue is missing or unspecified.
- Added `ccf-paper-writer/references/output-style-policy.md` and updated shared task modes so non-review skills stay flexible while review/audit gates remain structured.
- Reworked the Attention demo writing step into a real NeurIPS-style LaTeX draft with a copied style file and successful `pdflatex` validation.

## v0.4.3 - 2026-06-06

- Consolidated the runtime surface from 23 skills to 13 clear owner skills.
- Merged helper skills into owner modes: workflow planning, compression, writing review, citation audit, result figures/tables, artifact packaging, venue format, resubmission, paper presentation, and docs SVG maintenance.
- Renamed the review owner to `ccf-paper-reviewer` and made it responsible for both scientific and writing/format review modes.
- Rewrote README EN/zh-CN/zh-TW, routing, trigger registry, catalog, architecture docs, installation matrices, and merge audit docs around the consolidated skill family.
- Rebuilt all 24 CCFA SVG diagrams from `tools/build_ccfa_diagrams.py` using the consolidated family.
- Reworked `demo/attention-is-all-you-need/` into a NeurIPS-style dry run: original-paper reading, idea document, ordered skill run, writing draft, review/rebuttal, submission check, official data, and result tables.
- Bumped plugin manifests to `0.4.3`.

## v0.4.2 - 2026-06-06

- Unified runtime skill names to the `ccf-<object>-<role/action>` style.
- Added installation matrix docs and generated SVG diagrams.
- Added the Attention demo with official NeurIPS 2017 paper data.

## v0.4.0 - 2026-06-06

### Added

- v0.4 workflow structure, `ccfa.yaml` project-state contract, artifact contracts, trigger registry, architecture docs, agent guide, skills catalog, plugin manifests, and GitHub Actions validation.

### Changed

- Migrated 109 legacy venue runtime skills into `ccf-paper-writer/references/venue-guides/`.
- Updated routing so venue requirements are reference material rather than standalone runtime skills.
