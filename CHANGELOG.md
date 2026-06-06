# Changelog

## v0.4.4 - 2026-06-06

- Tightened `ccf-paper-writer` output behavior: polish/rewrite/compression preserves the user's original Markdown/LaTeX format, while from-scratch manuscript requests draft the requested artifact instead of a process report.
- Added writer NeurIPS fallback rules: search target venue guides first, then use the NeurIPS LaTeX template when the venue is missing or unspecified.
- Added `ccf-paper-writer/references/output-style-policy.md` and updated shared task modes so non-review skills stay flexible while review/audit gates remain structured.
- Reworked the Attention demo writing step into a real NeurIPS-style LaTeX draft with a copied style file and successful `pdflatex` validation.

## v0.4.3 - 2026-06-06

- Consolidated the runtime surface from 23 skills to 13 clear owner skills.
- Merged helper skills into owner modes: workflow planning, compression, writing review, citation audit, result figures/tables, artifact packaging, venue format, resubmission, paper presentation, and docs SVG maintenance.
- Renamed the review owner to `ccf-paper-reviewer` and made it responsible for both scientific and writing/format review modes.
- Rewrote README EN/zh-CN/zh-TW, routing, trigger registry, catalog, architecture docs, installation matrices, and merge audit docs around the 13-skill family.
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
