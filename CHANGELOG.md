# Changelog

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
