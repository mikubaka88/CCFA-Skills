---
name: iccv
description: Writing and formatting guidance for ICCV (International Conference on Computer Vision) papers. Use when drafting, formatting, and submitting to ICCV 2026. ICCV and CVPR share the same cvpr.sty class and formatting rules. Covers iccv.sty, double-blind anonymity with 8-page limit, rebuttal preparation, and camera-ready submission. Reference the CVPR skill for shared formatting details.
metadata:
  ccf_skill_controls:
    handoff_question_mode: partial
    respect_session_denylists: true
    protect_idea_scope_in_writing: true
    private_material_safety: moderate
    shared_controls: ../ccf-common/references/
---

# ICCV 2026 Conference Writing Skill

**CCF-A | AI | Publisher: CVF (IEEE)**
**Conference:** https://iccv2026.thecvf.com
**Template:** `ccf-latex-templates/ICCV/main.tex`, `ICCV/preamble.tex`, `ICCV/iccv.sty`
**Shared with CVPR** — same `cvpr.sty` class and formatting

## IMPORTANT: Shared Template with CVPR

ICCV and CVPR use **identical formatting rules** via the same `cvpr.sty` class. See the CVPR skill for complete formatting guidance. This skill covers ICCV-specific details only.

## Document Setup

### Preamble Structure

```latex
\documentclass[10pt,twocolumn,letterpaper]{article}

% === MODE SELECTION ===
\usepackage{cvpr}              % Camera-ready
\usepackage[review]{cvpr}      % Review version
% \usepackage[pagenumbers]{cvpr} % ArXiv version

% ICCV-specific packages:
\input{preamble}

% Conference-specific:
\def\paperID{*****}   % Enter Paper ID
\def\confName{ICCV}
\def\confYear{2026}
```

## Page Limits

- **Main content:** 8 pages maximum
- **Excluded:** References, appendix, supplementary
- **Same as CVPR** — papers exceeding limit may be rejected

## Anonymity Requirements (Double-Blind)

Identical to CVPR:
1. No author names or affiliations in submission
2. Use placeholder author block
3. Third-person self-citations
4. Anonymize identifying URLs
5. Paper ID on each page

## Title and Author Formatting

```latex
\title{\LaTeX\ Author Guidelines for \confName~\confYear~Proceedings}

\author{First Author\\
Institution1\\
{\tt\small first@inst.edu}
\and
Second Author\\
Institution2\\
{\tt\small second@inst.edu}
}
```

## CVPR vs ICCV Differences

| Aspect | CVPR | ICCV |
|--------|------|------|
| Template | cvpr.sty | cvpr.sty + iccv.sty |
| Conference | CVPR 2026 | ICCV 2026 |
| Submission System | CVF | CVF |
| Timing | Usually June | Usually October |

## Camera-Ready Submission

1. Change to: `\usepackage{cvpr}`
2. Add complete author information
3. Set correct `\paperID` and `\confName{ICCV}`
4. Remove anonymization
5. Verify 8-page limit
6. Upload to ICCV submission system

## Checklist Before Submission

- [ ] 8 pages or fewer
- [ ] No author identification
- [ ] Paper ID on each page
- [ ] `\confName{ICCV}` set correctly
- [ ] Third-person self-citations
- [ ] References in correct format
- [ ] Figure captions below figures
- [ ] Table captions above tables

## Reference: CVPR Skill

For complete formatting details (margins, fonts, packages), see the CVPR skill at `cvpr/SKILL.md`. The core formatting is identical.
