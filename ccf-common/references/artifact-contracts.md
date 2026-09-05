# CCFA Artifact Contracts

These contracts prevent CCFA skills from overwriting each other's work. Read broadly, write narrowly.

## Resolve Paths Before Writing

Apply this policy whenever any CCFA skill writes files. Resolve the project root from the user's path, existing `ccfa.yaml`, or established project layout; do not infer it from a tool's temporary working directory. Path priority is: explicit user destination, existing artifact mapping, established project convention, then the defaults below. Resolve relative paths against that project root. Preserve existing locations and references; this policy does not migrate or reorganize user files.

Keep requested deliverables at their canonical project locations, such as `manuscript/`, `figures/`, `tables/`, and `reviews/`. For generated working material, reuse the existing task directory, including an established `visual-composer/` or literature folder. If none exists, use `output/<task>/<artifact-id>/` under the project root. Choose a stable descriptive ID, such as `architecture`, `main-results`, or a literature topic; keep it across iterations. Two unrelated figures must not share a working specification or preview path.

Create only needed files and subdirectories:

| Material | Within the chosen working directory | Lifetime |
| --- | --- | --- |
| Reusable authoring source | `source/plot.py`, `source/figure.svg`, or `source/spec.md` as applicable | One current source; retain what reproduces or edits the requested output. Existing authoring paths win. |
| Required icon/reference assets | `assets/<semantic-name>.<ext>` | Reuse across iterations; retain provenance in the source/specification. Do not duplicate the same asset per format. |
| Downloaded/extracted source cache | `cache/<source-id>.full.md` or equivalent | One current extraction per source version; retain exact source identity and page/section anchors. |
| Build products and previews | `build/preview.png`, `build/render.pdf`, build log or converter input | Replace on rebuild; keep only useful current debugging/continuation material. |

This is a placement convention, not a folder-generation checklist. A one-file edit creates none of these by default. Do not scatter scratch scripts, downloaded PDFs, screenshots, prompts, logs, or conversion files at the repository root or next to final manuscript files. A tool may emit into its own managed location; reference that path when stable, or copy only the needed output into the chosen project location. Do not clean the tool's global output directory.

Reuse existing `ccfa.yaml` artifact fields or the current report/specification when a durable path map is needed. Do not require a new manifest, process log, or state file for every task. Explicit no-new-files or exact-path requests override these defaults.

## Canonical Artifact And Overwrite Policy

1. Use one canonical generated artifact per purpose and requested format. Update it in place on an ordinary iteration; do not create `v2`, `revised`, `final-final`, date-stamped attempts, `_attempts`, or backup trees. Named alternatives and requested snapshots remain distinct.
2. Reuse existing user files only within an authorized edit. Raw measurements, submitted packages, source versions needed for comparison, recurring monitoring observations, and externally required evidence are retained inputs, not replaceable process files.
3. Generate and check a candidate before replacing the last usable artifact. When practical, write to a temporary sibling, close it, and atomically replace the target. Remove only that task-created temporary file on success or failure. A failed generation must not truncate the previous result or be reported as a completed refresh.
4. Keep one editable source for each visual. Export only the requested dependent formats from that source; refresh the affected exports and preview after an edit. Do not present stale exports as the current figure. Never round-trip the editable source through a flattened preview.
5. Update ledger rows and current reports in place. Put evidence versions, review rounds, dates, status, and source locations inside them. Preserve the original evidence needed to compare versions; avoid duplicating full reports for each role or critique pass.
6. Save only working material required for continuation, reproducibility, editing, or an explicitly requested audit trail. Keep ephemeral reasoning in context. Do not persist every prompt, critique, screenshot, or failed attempt merely because a tool produced it.
7. Before delivery, check the actual created/changed paths, current exports, and unresolved temporary files. Remove only disposable files created by this task at verified paths. Do not recursively clean existing user directories or discard required baselines, measurements, or snapshots. Report an incomplete build beside the affected deliverable.
8. Use version control for rollback when available. When rollback would otherwise be lost and the user requests a retained comparison or history, preserve the necessary baseline deliberately rather than multiplying automatic backups.

| Artifact | Primary owner | Contract |
| --- | --- | --- |
| `humanization-warnings.md` | `ccf-humanization`, user | Store inside the chosen task/report directory only when the user asks to persist warnings; update the single record in place. It stores advisory/blocking concerns that were not inserted into manuscript, experiment, code, table, or configuration files. Each record states that no artifact change was made for the warning; scientific changes beyond existing authorization require a concrete user decision. Known material facts remain in authorized manuscript edits. |
| `ccfa.yaml` | `ccf-project-scaffolder`, `ccf-pipeline-orchestrator` | Scaffold creates it; orchestrator updates stage/gate state. Other skills may read and propose updates. |
| `literature-monitor/*.md`, `output/literature-monitor/*` | `ccf-literature-monitor` | Stores monitoring reports, overlap flags, and watch summaries. Update one-time scans in place; retain dated observations only for a recurring watch or requested history. Literature searcher may deep-retrieve flagged papers; reviewer/optimizer may use the flags for score or rescue decisions. |
| `output/literature-search/<topic>/papers.md` or an existing search folder; optional `papers.csv`, `search-notes.md`, `idea-grounding.md` | `ccf-literature-searcher` | Searcher owns verified sources, screening notes, clusters, and the optional compact idea-grounding packet. Idea optimizer may read the packet and create new idea plans, but must not rewrite source evidence or turn inferred gaps into sourced facts. |
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
