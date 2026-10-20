# Changelog

## v0.11.0 - 2026-10-15

Plugin version is `0.11.0`.

### 2026-10-20 autonomous research update

- Fix a controller I/O failure after evaluator launch that could restore candidate files while the evaluator was still running. Stop and wait before restoration; keep the run pending when termination cannot be confirmed, and reconstruct the authoritative event sequence after a cache-write failure. Add two real-process fault-injection regressions, bringing the runner suite to 16 tests.
- Clarify that scalar baseline promotion and scientific value are separate decisions. Document retained discarded-candidate evidence, repeated-seed evaluation, and comparison-parent semantics; distinguish task-local strategy adaptation from shared rules that need independent-task validation. Keep the runner API, seven preferences, and version unchanged.
- Extend the existing orchestrator, experiment designer, and idea optimizer from planning into explicitly requested hypothesis–experiment–feedback campaigns. Keep scientific ownership, concept-only idea review, ordinary writing scope, and the seven version-1 preferences intact. Research campaigns use their own finite budget; the maintenance-only candidate allowance does not cap them.
- Add a standard-library sequential experiment helper with a frozen contract, measured baseline, candidate identities, command execution, attempt/time limits, raw logs, protected-input checks, scoped restoration, and repeat-ID protection. An interrupted controller with unknown execution duration closes the remaining allowance instead of inventing usable budget. The host still proposes hypotheses, edits methods, interprets scientific value, and supervises resources; the helper is neither an OS sandbox nor a background research service.
- Preserve integer metric precision, reject malformed/nonfinite measurements and aliased input paths, and verify raw metric evidence before keeping a candidate. Concurrent file changes prevent automatic restoration. Retain only managed snapshots and necessary experiment records in one task directory.
- Repair the evidence-policy instruction that could substitute plans for authorized execution. Add changes-only handoffs against an identified baseline and reuse campaign records for recovery; preserve original evidence and meaningful negative results. Update task routing, discovery metadata, source provenance, three-language documentation, and the configuration page's maintenance explanation.
- Add 14 execution regressions covering success, discard, crash, timeout, input/evaluator changes, metric corruption, interruption, budget limits, file aliases, and replay. Existing family, preference, continuity, link, source-schema, and configurator checks pass. These are execution-control checks, not measurements of open-ended research quality, model-degradation recovery, or total token savings.

### 2026-10-19 maintenance update

- A further installation/review audit preserves inherited compound issue IDs such as `R1-C2` and `AC-C1`, checks relative-progress labels against frozen thresholds, and rejects nonfinite or boolean scores. Keep short rebuttal checklist results internal unless requested or a material unresolved issue needs attention.
- Complete copy-install instructions with sibling template/resource synchronization, explicit installation targets, and refresh steps after updating a source clone. Correct the remaining Claude Code prerequisite note and explain the skill-only installation boundary in all three READMEs. Keep the 17 skills, seven optional controls, preference schema, and `0.11.0` version unchanged.
- Verify the repair with review regression cases, all 17 family entries, 42 plotting tests, 27 preference tests, 23 continuity tests, and the configurator controller. Test first-copy and repeated-update commands in isolated Bash and PowerShell directories, including Chinese/space-containing paths and unset/custom installation roots. Local runtime files match the repository; real client discovery and provider-degradation gains remain outside this test coverage.
- Update the three CI actions to verified official releases using Node 24, removing their Node 20 runtime deprecation warning while retaining the Python 3.11 and Node 22 test environments.
- Follow-up audit removes duplicated monitor output templates, mandatory reports for short updates, label-driven extra retrieval, routine compression approval/status messages, and novelty-pressure-based repositioning. Keep full monitoring fields in their canonical template and preserve genuinely unresolved scientific decisions.
- Let explicitly selected language conventions use existing exemplar cards and override generic punctuation/rhythm preferences. Add a backward-compatible prose-checker `--em-dash-limit N|off` override so the chosen convention reaches actual checks without disabling other diagnostics.
- Repair ridgeline peak clipping, reversed axes in narrow slopegraphs, and small nonzero correlation labels. Add optional `Theme(stroke_unit="pt")` with physical-width validation and consistent Canvas conversion; preserve default drawing units and donut geometry. No new dependency or preference switch is introduced.
- Follow-up acceptance passes 42 plotting regressions, the new punctuation-override API/CLI checks, all 17 family entries, and all 13 legacy showcase exports. Inspect representative repaired figures and complete two short-task writing/monitoring smoke checks. Local links, source schema, UTF-8, and path-privacy checks pass; these checks do not measure general model-quality gains.
- Repair contradictory writing and review instructions: remove obligatory limitation endings, score-dependent issue closure, compulsory rescue routes, and blanket experiment menus. Preserve legitimate comparisons, uncertainty, controlled studies, and the user's research objective. Keep exemplar analysis in working context unless requested, and format table precision according to the quantity and source evidence.
- Strengthen Humanization across writing, ideas, and experiment plans with concrete objects, operations, and relationships. Extend prose diagnostics to authored Markdown table cells, repeated Chinese comparisons, abstract capability-label clusters, and caution-based justifications. Treat contextual signals as advisory and preserve quoted/code content and meaningful technical terms.
- Complete Humanization → Common references in existing agent default prompts and partial-install guides. Distinguish discovery metadata from actually read instructions, recover missing relevant context, and carry concrete evidence or reader difficulties through review-to-revision handoffs. No startup report or extra agent is added by default.
- Strengthen scientific plotting with physical-size typography, reusable color normalization, stable entity colors and shared legends, aligned shared/free axes, and explicit p/adjusted-p/q labels. Reject invalid statistics and correlations, preserve tiny positive values, require an explicit display policy for zero probabilities, and correct signed-bar, donut, and radial edge cases. Existing positional call signatures remain compatible.
- Refine reference-based composition, biological asset selection, palette consistency, scientific and visual checks, and approved component reuse. Keep additional generations and independent review behind existing preferences; add no runtime plotting dependency, skill, or configuration switch.
- Add runnable plotting examples and data/geometry regression tests to CI. Refresh the three README narratives and usage prompts; retain the 17-skill family, version-1 settings, seven optional controls, and `0.11.0` plugin version. Record inspected external references and reverify the five ICLR 2027 official sources without relabeling historical unverified sources.
- Validate all 17 skills, 36 plotting regressions, 27 preference tests, 23 continuity tests, and the configurator controller. Check 377 local Markdown links and 1,168 text files for path privacy; execute all 13 legacy showcase exports and inspect representative SVG renderings. Six current-model writing/idea/experiment/handoff smoke cases preserve supplied facts and required limits. These are bounded acceptance checks, not a blind comparison, a provider-degradation experiment, or a measurement of quality, time, or token gains.

### Earlier changes in this version

- Rewrite the latest-update story around everyday research: retaining the goal through long tasks, coordinating useful contributions, and choosing where to spend extra effort. Add a real configurator screenshot, three practical setting examples, and user/project setup instructions across the three README languages. Preserve historical release records and version-1 preference compatibility.

- Clarify transition-time goal checks, isolate unreliable summaries during recovery, and preserve valid artifacts while reconciling affected decisions. Do not infer hidden provider capability changes or claim measured resilience gains.
- Add bounded host-supported multi-agent assignments: independent first-pass ideation, selective evidence sharing, version-aware integration, single-owner manuscript arguments, and serialized edits to shared files. Repeated sources and majority agreement do not establish independent scientific support.
- Remove the remaining mandatory-rescue conflict for invalid ideas and admit theory, counterexamples, and observations as discriminating evidence. Consolidate candidate screening around mechanism changes and module necessity. Align experiment-design evidence requirements with the contribution type.
- Strengthen paragraph revision with reverse outlines, sentence relationships, and information ordering. Diagnose both semicolon forms and clustered contrastive phrasing while preserving meaningful scientific comparisons and uncertainty.
- Add daily and weekly Trendshift badges and a compact latest-update link at the top of the READMEs. Consolidate the dated update summary near the end in three languages, move historical ICLR adaptation out of quick start, and retain the Simplified Chinese redirect without duplicating the main document.
- Align integrity-audit output with the requested mode and apply the shared Humanization → Common startup consistently in plugin instructions.
- Validate all 17 skill structures and regressions, including bilingual prose diagnostics and CRLF handling; pass 27 preference tests, 23 continuity tests, the JavaScript controller regression, and six independently executed agent behavior smoke cases. Check 371 local Markdown links, scan 1,167 text files for path privacy, validate the schema of 144 source records while preserving existing unverified statuses, and pass `git diff --check`. Both Trendshift badge endpoints return HTTP 200 with SVG content. These checks do not measure real provider-degradation gains, research quality, latency, or token savings.

- Separate discovery from execution within existing task modes: requested brainstorming can explore distinct mechanisms with optional route comparison off; execution preserves selected content until a material reason reopens a decision. Add a shared progress test across search/review/revision handoffs, preserve novel hypotheses as inferences, and remove hard evidence-card/rescue/revision limits that could suppress useful exploration or required corrections. Keep existing preferences, schemas, and the 17-skill architecture.
- Align optional-route explanations in all three UI languages, retain scientific source acknowledgments under functional method headings, and distinguish actual smoke-test results from unmeasured provider-degradation performance.

- Refresh the preference configurator with an unbroken CCFA-Skills wordmark, larger typography, aligned setting cards, 44px controls, and responsive layouts in the existing light/dark palette. Preserve all seven controls, three languages, configuration inheritance, and save behavior. Check actual headless browser rendering alongside controller regressions.

- Add task continuity with separate current goals, justified routes, and next actions; distinguish proposed/executed/verified work and reconcile actual artifacts after lost or conflicting context. Preserve legitimate corrections, explicit goal changes, prerequisites, and anti-defensive writing. Keep the 17-skill architecture and `ccfa.yaml` ownership/schema unchanged.
- Add optional compact task-local state and a read-only record-consistency checker with transition regressions. Short tasks create no state file or extra judge; checks validate declared records, not hidden model capability, semantic intent, evidence truth, or scientific quality.
- Extend the three-language configurator to seven optional enhancements. New alternative-route and maintenance-evolution controls default to off, retain version-1 sparse-config compatibility, and bound comparisons to one extra candidate in their defined scope. Maintenance compares fixed acceptance and rolls back only task-owned edits; no autonomous self-modification during research or unbounded improvement loop.

- Reconcile anti-defensive behavior across experiment planning, writing, and review: make additional evidence claim-dependent, retain research objectives unless an authorized evidence-based change is needed, remove routine self-attestation fields, and reserve warnings for unresolved decisions. Align paragraph-review severity with the fixed review schema and keep optional detail out of ordinary reports.
- Shorten repeated entrypoint file/collaboration contracts while retaining their top placement, mandatory Humanization -> Common startup, shared working paths, UTF-8 checks, and necessary specialist integration. Label old evaluation conditions as historical rather than current defaults; historical measurements remain unchanged.
- Limit local Markdown link checks to Git publication candidates, retaining tracked files even in ignored directories; exclude generated working backups in non-Git exports. Add regressions for ignored backups, published broken links, Chinese paths, and invalid UTF-8.

- Add a local, dependency-free preference configurator with Simplified Chinese, Traditional Chinese, and English; day/night controls, light/dark appearance, per-option qualitative cost explanations, sparse user/project inheritance, and JSON import/export. The authenticated loopback service saves real settings atomically and detects conflicting edits; static exports are explicitly not applied settings.
- Resolve optional independent review, expanded search, enhanced document parsing, figure alternatives, and extra process reports once per task. Preserve mandatory Humanization -> Common startup, necessary evidence checks, fixed review structures, and concept-only idea scope. User settings live outside installed skills; no settings file is created by reading a skill.
- Reconcile installed writing improvements: complete content-first drafts, intentional result blanks, phase-aware alignment review, evidence-driven citations, and content-aware table layout. Remove conflicting citation quotas and unconditional exemplar loading from legacy defaults.
- Refine targeted metadata retrieval, source-version reuse, affected-dependency handoffs, and optional page-level parsing without importing external runtimes. Preserve source credits and existing canonical working directories. Add preference/HTTP regression checks; no measured model-quality, latency, or token improvement is claimed.
- Make repository privacy scans cover tracked and nonignored untracked publication candidates, while retaining an explicit ignored-file scan and a non-Git fallback. Tracked files remain checked even under ignored directories; local historical build logs are preserved.

- Add a minimal ICLR 2027 adaptation in existing guides: verified author/reviewer/AI-use policies, exact-year template selection, truthful disclosure checks, and decision-relevant review emphasis. Correct legacy ICLR anonymity, layout, and unsupported LaTeX commands; retain historical 2026 templates. Keep the fixed review profiles, 17-skill architecture, and plugin version unchanged.
- Restore mandatory family-wide preflight in the order `ccf-humanization` -> `ccf-common` -> specialist. Apply it to review, retrieval, visuals, planning, and maintenance as well as writing; reuse active rules without recursive startup or duplicate reports. Detailed editing/experiment modes remain conditional. Align entrypoints, discovery prompts, routing, docs, and all partial-install subsets.
- Use project-root `ccfa-workfiles/<purpose>/<artifact-id>/` for new working directories instead of nesting them in a generic application output folder. Preserve established task paths and avoid collisions with unrelated folders.
- Make skill ownership accountable for integration rather than isolated execution. Complete applicable prerequisites and material specialist checks, reuse valid evidence, and revisit affected dependencies after changes.
- Clarify conditional collaboration for idea grounding, substantial writing, review, experiment design, visuals, and rebuttals. Internal specialist findings stay compact; requested reviews retain their fixed templates and full scoped coverage. Preserve concept-only idea review and explicit user limits.
- Synchronize family entrypoints, routing, handoffs, planning guidance, and the three README variants without changing the 17-skill architecture, public CLI contracts, or project-state schema. The maintained-text check excludes the new working cache, with a regression covering that boundary.

## v0.10.0-r2 - 2026-09-16

Plugin version remains `0.10.0`; `r2` identifies this release revision without replacing the original `v0.10.0` tag.

- Included the upstream DASFAA guide correction for its official URL, LNCS `runningheads` option, and table syntax.

- Audited maintained text for invalid UTF-8 and replacement characters. Made CLI output and text-input pipes explicitly UTF-8, accepted UTF-8 BOM inputs, and stopped hiding decoding failures in link checks. Added Chinese path/text regressions, CJK font fallback guidance, and process-scoped PowerShell examples without changing the system locale.

- Promoted the shared file contract to the top of all 17 skill entrypoints. New working directories use descriptive `output/ccfa-workfiles/<purpose>/<artifact-id>/` names; existing paths remain valid. Skills share artifact paths and preserve source evidence while removing only their own verified disposable intermediates.
- Clarified helper return versus next-stage ownership, compact context transfer, and completion conditions. Removed redundant file-output confirmation and first-stage stopping rules, corrected qualitative idea-review routing, and scoped helper searches without mandatory paper-count quotas. Kept the existing skill architecture, metadata, and version.

- Consolidated manuscript review into fixed detailed/writing/brief structures and one seven-criterion scientific scorecard; aligned contribution-aware evidence, confidence, and frozen historical comparisons. Extended the existing validator to inspect Markdown report structure and finding references without requiring another output file.
- Added content-fit compact layout, cross-block alignment, final-size type checks, five coordinated visual presets, and protected selected-object edits. Aspect ratio follows the paper and method; no square default. Conference examples guide design choices without claiming official styles. Inspected public reference workflows and example images without importing external code, assets, or dependencies.

- Refined reference-guided drawing with explicit alignment, scaled pixel gaps, final-size typography, a visible-text inventory, and coherent scientific illustrations. Removed arbitrary prompt-length caps while keeping local edits incremental. Raster precision remains a target, with exact geometry and live fonts checked in requested editable outputs.
- Set the plotting theme default to Times New Roman, retained explicit font overrides including Comic Sans MS, and exposed seven existing showcase palettes without changing earlier palette values or recipe signatures. Preserved the GPT Image-first, pure-SVG, quantitative-code, and editable-export routes, the 17-skill structure, and current-file artifact handling.

- Use functional names in method introductions, skill descriptions, invocation prompts, and report titles while preserving source references, acknowledgments, quotations, and narrative context.

- Made natural concept judgments and manuscript assessments select their respective reviewers without requiring numeric-score wording. A full PDF can still receive concept-only review.
- Replaced the default idea rubric with six conceptual dimensions. Experimental completeness, results, baselines, ablations, and submission readiness no longer affect default idea scores; requested experiment/feasibility extensions remain separate.
- Organized assessment scope, substantive findings, and ratings into detailed manuscript and concept reports by default, with brief output on explicit request. Aligned templates, entry instructions, and agent prompts; consolidated duplicate audit/role reports while preserving manuscript version-comparison contracts and historical evaluations.
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
