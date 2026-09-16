# CCFA Artifact Contracts

These contracts prevent CCFA skills from overwriting each other's work or accumulating unmanaged intermediate files. Read broadly, write narrowly.

## Resolve Paths Before Writing

Apply this policy whenever any CCFA skill writes files. Resolve the project root from the user's path, existing `ccfa.yaml`, or established project layout; do not infer it from a tool's temporary working directory. Path priority is: explicit user destination, an existing mapping for this artifact, its established task directory, then the defaults below. Resolve relative paths against that project root. Preserve existing locations and references; this policy does not migrate or reorganize user files.

Keep requested deliverables at their canonical project locations, such as `manuscript/`, `figures/`, `tables/`, and `reviews/`. For generated working material, reuse the existing task directory, including an established `visual-composer/` or literature folder. If none exists, use `ccfa-workfiles/<purpose>/<artifact-id>/` under the project root. The name identifies CCFA working files, the task purpose, and the specific artifact; use the naming guide below. Keep it across iterations. Two unrelated figures must not share a working specification or preview path.

`ccfa-workfiles/` is a dedicated project-root directory, not a child of `output/`, `outputs/`, or another application's build folder. The presence of a generic output directory is not a reason to adopt it for new CCFA tasks. An existing task mapped there keeps its path unless migration is requested. If the default name is already used for unrelated material, use a stable project-specific name such as `ccfa-workfiles-<project-id>/` and retain that choice in existing task context; never merge unrelated contents or rename user folders.

Bind the working directory to the task/artifact, not the current skill. A helper or next owner inherits its canonical paths and reusable source/cache locations; changing skills does not create another working directory or a copied input tree. Distinct requested artifacts may have distinct stable IDs. For a shared file, serialize edits through its current owner; other contributors return evidence or proposed changes instead of concurrently overwriting it.

For an inline answer or read-only check, create no working directory unless the tool actually needs one. Keep generated intermediates out of the project root, manuscript source folders, and installed skill packages unless explicitly required there. Preserve established build conventions and user-specified destinations; this rule does not relocate existing files or prevent an authorized edit to repository/skill sources.

Before running a command that generates files, direct its intermediate outputs to this working directory while keeping final deliverables at their canonical paths. Use tool output options or process-scoped temporary settings; if the tool requires a working directory, keep input paths explicit so changing it does not redirect inputs. Keep small one-off checks in memory or a shell pipeline when practical. Do not create a scratch script, report, screenshot, or full tool-output dump unless it is needed for the requested result, verification, or continuation. Reference existing code, datasets, models, and checkpoints at their original paths; do not copy a project or its inputs merely to populate a working directory.

Create only needed files and subdirectories:

| Material | Within the chosen working directory | Lifetime |
| --- | --- | --- |
| Reusable authoring source | `source/plot.py`, `source/figure.svg`, or `source/spec.md` as applicable | One current source; retain what reproduces or edits the requested output. Existing authoring paths win. |
| Required icon/reference assets | `assets/<semantic-name>.<ext>` | Reuse across iterations; retain provenance in the source/specification. Do not duplicate the same asset per format. |
| Downloaded/extracted source cache | `cache/<source-id>.full.md` or equivalent | One current extraction per source version; retain exact source identity and page/section anchors. |
| Build products and previews | `build/preview.png`, `build/render.pdf`, build log or converter input | Replace on rebuild; remove disposable products after verification. Retain current material only when needed to debug, resume, reproduce, or deliver the result. |

This is a placement convention, not a folder-generation checklist. A one-file edit creates none of these by default. Do not scatter scratch scripts, downloaded PDFs, screenshots, prompts, logs, or conversion files at the repository root or next to final manuscript files. A tool may emit into its own managed location; reference that path when stable, or copy only the needed output into the chosen project location. Do not clean the tool's global output directory.

Reuse existing `ccfa.yaml` artifact fields or the current report/specification when a durable path map is needed. Do not require a new manifest, process log, or state file for every task. Explicit no-new-files or exact-path requests override these defaults.

## Recognizable Folder Names

For a new default directory, name the purpose by the work and the artifact by its content. Prefer short lowercase ASCII words separated by hyphens for portable commands; preserve established or explicitly requested names, including Chinese names. Use the same concrete artifact name across skills instead of substituting the receiving skill's name.

| Purpose | Example under `ccfa-workfiles/` |
| --- | --- |
| Figure/table composition | `figures/method-overview/`, `tables/main-results/` |
| Manuscript writing or compression | `writing/introduction/`, `writing/paper-short-title/` |
| Idea or manuscript review | `reviews/idea-memory-routing/`, `reviews/paper-short-title/` |
| Literature retrieval, monitoring, or exemplars | `literature/retrieval-memory/`, `literature/novelty-watch/`, `exemplars/paper-short-title/` |
| Research/experiment planning | `ideas/memory-routing/`, `experiments/ablation-plan/` |
| Integrity, submission, or response work | `checks/citation-integrity/`, `submission/neurips-main/`, `responses/paper-short-title/` |
| Project planning or skill maintenance | `planning/paper-roadmap/`, `skill-maintenance/family-governance/` |

These are naming examples, not folders to scaffold. Choose only what the current artifact needs. Avoid new catch-all names such as `temp`, `misc`, `stuff`, `new-folder`, or `task1`, and iteration suffixes such as `v2` or `final-final`. Source versions, review rounds, and dates belong in existing report/specification metadata; retain separate dated observations or immutable snapshots only when they are required evidence.

Within an artifact, `source/` holds reusable authoring code/specifications, `assets/` holds required reference/icon assets, `cache/` holds replaceable downloads/extractions, and `build/` holds current renders, previews, and logs. Name files by their role, such as `method-overview.svg`, `review-extraction.md`, or `latex-build.log`; preserve canonical names already used by tools. A requested report may be the canonical file in its established report folder. Do not copy it merely to populate this tree, and do not treat the entire `ccfa-workfiles/` directory as disposable.

## Text Encoding And Chinese Output

- Write new Markdown, JSON, YAML, code, SVG/XML, and text reports as UTF-8 without a BOM, respecting an explicit target-format requirement. Read incoming UTF-8 text with optional BOM support where applicable, especially JSON and Windows-authored files. Preserve Unicode paths and labels through the whole pipeline. JSON `\uXXXX` escapes are valid Unicode serialization, not evidence of corruption.
- Set encoding at every file/pipe boundary; a UTF-8 source file alone is insufficient. For Python use explicit file encodings and match each subprocess's actual input/output encoding. The supplied CLIs emit UTF-8; their text-input pipes expect UTF-8. External converters may use a different log encoding: retain raw bytes until it is verified instead of silently replacing undecodable text. On PowerShell 5.1, use `Get-Content -Encoding UTF8`, set `$OutputEncoding` and `[Console]::OutputEncoding` to UTF-8 for native pipelines, and use explicit UTF-8 writes instead of encoding-implicit `>`, `>>`, or `Out-File`. `python -X utf8` cannot recover characters already lost by the shell. For family maintenance, concrete command examples are in `../../ccf-skill-forger/references/local-commands.md`.
- Decode strictly. Do not hide errors with `errors="ignore"`, replacement decoding, repeated speculative transcoding, or by replacing Chinese with question marks. Verify a legacy source's encoding before converting it. If saved text already contains U+FFFD or lost characters, recover it from the original source; changing its declared encoding cannot restore missing information.
- Check the actual saved/exported artifact, including Chinese headings, citation text, labels, and filenames where present. Round-trip representative text and inspect the rendered output when visual delivery is requested. A terminal display error is distinct from damaged file bytes; preserve a correct source while fixing the display/transport boundary.
- Times New Roman and Comic Sans MS do not cover every Chinese glyph. Keep the requested Latin font and choose an available CJK fallback, such as an appropriate Noto/Source Han family, SimSun, or Microsoft YaHei. Verify actual glyphs in SVG/PDF/PPTX output; use the document format's font embedding or subset controls when available. For Chinese LaTeX, use the project's configured CJK-capable engine/packages; do not switch a venue build blindly or disguise missing glyphs as an encoding fix.
- Use UTF-8 for CSV by default; use UTF-8 with BOM when the requested spreadsheet workflow needs that compatibility. Preserve delimiters, values, and column names. Garbled PDF extraction needs inspection of the source font/text mapping or an authorized OCR route, not invented text or blind re-encoding.

## Canonical Artifact And Overwrite Policy

1. Use one canonical generated artifact per purpose and requested format. Update it in place on an ordinary iteration; do not create `v2`, `revised`, `final-final`, date-stamped attempts, `_attempts`, or backup trees. Named alternatives and requested snapshots remain distinct.
2. Reuse existing user files only within an authorized edit. Raw measurements, submitted packages, source versions needed for comparison, recurring monitoring observations, and externally required evidence are retained inputs, not replaceable process files.
3. Generate and check a candidate before replacing the last usable artifact. When practical, write to a temporary sibling, close it, and atomically replace the target. Remove only that task-created temporary file on success or failure. A failed generation must not truncate the previous result or be reported as a completed refresh.
4. Keep one editable source for each visual. Export only the requested dependent formats from that source; refresh the affected exports and preview after an edit. Do not present stale exports as the current figure. Never round-trip the editable source through a flattened preview.
5. Update ledger rows and current reports in place. Put evidence versions, review rounds, dates, status, and source locations inside them. Preserve the original evidence needed to compare versions; avoid duplicating full reports for each role or critique pass.
6. Save only working material required for continuation, reproducibility, editing, or an explicitly requested audit trail. Keep ephemeral reasoning in context. Do not persist every prompt, critique, screenshot, or failed attempt merely because a tool produced it.
7. Apply the working-file closeout below at completed stage boundaries and before delivery. Check the actual created/changed paths and current exports; report an incomplete build beside the affected deliverable.
8. Use version control for rollback when available. When rollback would otherwise be lost and the user requests a retained comparison or history, preserve the necessary baseline deliberately rather than multiplying automatic backups.

## Working File Closeout

- Track task-created paths in the current context or an existing task record. Reuse this ownership information when resuming; do not generate a separate cleanup manifest or daily log by default. During iteration, reuse canonical scratch, preview, and log paths. For long-running logs, use supported rotation or size limits where appropriate; do not truncate evidence or files still being written.
- Once a replacement is verified and dependencies are no longer active, remove this task's superseded previews, temporary conversion inputs, disposable check scripts, duplicate downloads, and resolved-failure dumps. Keep the editable source, requested exports, required evidence, and anything necessary to resume or reproduce the result. Preserve enough diagnostics for an unresolved failure; do not retain every failed attempt after it is resolved.
- Clean up disposable files created by this task as part of the authorized work without another confirmation, unless an explicit instruction requires one. Before deletion, verify the resolved paths and ownership, check that no retained artifact or running process depends on them, and avoid following links outside the task directory. Never treat a filename, age, extension, or location in `tmp`/`build`/`cache` as proof that an existing file is disposable. Preserve pre-existing user files, shared tool caches, original data, experiment records, and other tasks' outputs; do not move or reorganize them to make the directory look tidy. When ownership or dependencies are uncertain, leave the file in place and report it if material.
- Finish with one current deliverable per requested format and only necessary supporting files. Remove an empty working directory only if this task created it. Give the canonical result paths; if substantial intermediate files remain, briefly state their location, purpose, and approximate size when available. Do not create another inventory document just to report cleanup.

## Artifact Ownership

| Artifact | Primary owner | Contract |
| --- | --- | --- |
| `humanization-warnings.md` | `ccf-humanization`, user | Store inside the chosen task/report directory only when the user asks to persist warnings; update the single record in place. It stores advisory/blocking concerns that were not inserted into manuscript, experiment, code, table, or configuration files. Each record states that no artifact change was made for the warning; scientific changes beyond existing authorization require a concrete user decision. Known material facts remain in authorized manuscript edits. |
| `ccfa.yaml` | `ccf-project-scaffolder`, `ccf-pipeline-orchestrator` | Scaffold creates it; orchestrator updates stage/gate state. Other skills may read and propose updates. |
| `ccfa-workfiles/literature/<watch-topic>/` or an existing monitoring folder | `ccf-literature-monitor` | Stores monitoring reports, overlap flags, and watch summaries. Update one-time scans in place; retain dated observations only for a recurring watch or requested history. Literature searcher may deep-retrieve flagged papers; reviewer/optimizer may use the flags for score or rescue decisions. |
| `ccfa-workfiles/literature/<topic>/papers.md` or an existing search folder; optional `papers.csv`, `search-notes.md`, `idea-grounding.md` | `ccf-literature-searcher` | Searcher owns verified sources, screening notes, clusters, and the optional compact idea-grounding packet. Idea optimizer may read the packet and create new idea plans, but must not rewrite source evidence or turn inferred gaps into sourced facts. |
| `manuscript/*.tex` | `ccf-paper-writer` | Review and audit skills suggest edits; writing changes route back to paper writer unless user explicitly authorizes otherwise. |
| `references/*.bib` | `ccf-integrity-auditor`, `ccf-paper-writer` | Auditor verifies metadata and citation support; searcher obtains candidates; writer may insert verified entries needed for authorized drafting. Preserve existing keys and unrelated entries. |
| `experiments/results.*` | user, `ccf-experiment-designer` | Figure/table and integrity skills read supplied numbers only. |
| `figures/*`, `tables/*` | `ccf-experiment-designer`, `ccf-visual-composer` | Experiment designer owns evidence/result content and real values; visual composer owns plotting code, method/architecture diagram composition, palette, panel/table layout, caption placement, manuscript integration, editable vector reconstruction, and render QA. Data and depicted method components must be real. |
| `visual-composer/*` | `ccf-visual-composer` | Reuse this established working location when present; otherwise resolve the shared output default. Use a stable subdirectory per unrelated figure. Store only requested canonical deliverables and reusable source artifacts, such as plotting code, the current architecture specification, the current raster draft, editable SVG/PPTX, and derived vector PDF. Repeated generation overwrites the matching canonical file. Keep a QA record or prompt only when the user requests it or it is needed to reproduce the final deliverable; do not retain visual iteration logs or render-attempt folders by default. It must not become a hidden source of invented numbers, modules, labels, or flows. |
| `ccfa-review-reports/<paper-slug>-<venue>-review.md` | `ccf-paper-reviewer`, user | Canonical review report. Independent reviews and version comparisons overwrite this file unless the user requests snapshots. Store the review date and compared manuscript versions inside the report, not in the filename. |
| `reviews/revision-ledger.md` | `ccf-rebuttal-writer` | Single canonical ledger updated in place. Tracks reviewer comment, first-seen version, issue origin, response promise, manuscript action, affected score dimension, and status across rounds. |
| `submission/*` | `ccf-submission-checker` | Stores build, anonymity, page, metadata, and policy readiness results. |
| `artifact/*` | `ccf-submission-checker` | Tracks code/data/model release and reproducibility package status. |
| `talk/*` | `ccf-paper-writer` | Presentation outputs only; not submission evidence. |
| `assets/ccfa-skills-*.svg` | `ccf-skill-forger` | Generated by `tools/build_ccfa_diagrams.py`; must pass browser screenshot QA, not only XML parsing. |
| governance docs | `ccf-common`, `ccf-skill-forger` | Routing, naming, trigger registry, source registry, validation, and policy documents. |
