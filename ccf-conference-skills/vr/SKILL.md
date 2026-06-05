---
name: vr
description: Writing and formatting guidance for VR (IEEE Virtual Reality Conference) papers. Use when drafting, formatting, or submitting to VR 2026. Covers IEEEtran LaTeX class with conference mode, VR page limits, double-blind anonymity, VR/AR/3DUI-specific conventions (user study methodology, hardware setup, presence questionnaires), and IEEE camera-ready preparation.
metadata:
  ccf_skill_controls:
    handoff_question_mode: partial
    respect_session_denylists: true
    protect_idea_scope_in_writing: true
    private_material_safety: moderate
    shared_controls: ../ccf-common/references/
---

# VR 2026 Conference Writing Skill

**CCF-A | VR | Publisher: IEEE**
**Conference:** https://ieeevr.org/2026
**Template:** `VR/IEEEtran.cls` (IEEEtran, conference format)

## Document Setup

### Preamble Structure

```latex
% === SUBMISSION MODE (anonymous, double-blind) ===
\documentclass[conference]{IEEEtran}

% Author block for anonymous submission:
\author{
  \IEEEauthorblockN{Anonymous Author}
  \IEEEauthorblockA{
    \IEEEauthorrefmark{1}Anonymous Institution\\
    anonymous@institution.edu}
}

% === CAMERA-READY MODE ===
\documentclass[conference]{IEEEtran}
% Restore full author/affiliation information
% Add conference-specific copyright notice
```

### Required Packages

```latex
\usepackage{amsmath}
\usepackage{amsthm}
\usepackage{booktabs}
\usepackage{graphicx}
\usepackage{cite}
\usepackage{balance}
\usepackage{cleveref}
\usepackage{algorithm}
\usepackage{algorithmic}
\usepackage{url}
\usepackage{xcolor}
```

## Page Limits

| Section | Limit |
|---------|-------|
| Main paper (submission) | **8 pages** |
| References | No limit |
| Appendix | Check CFP |

VR typically enforces an 8-page limit for the main body. References do not count toward the limit. Verify the current CFP for exact limits.

## Anonymity Requirements

VR uses double-blind review. Since IEEEtran does not have built-in anonymous mode:

1. Remove or replace author names/affiliations in the submission
2. Use "Anonymous" as author during submission
3. Third-person self-citations: "Smith et al. showed..." not "we showed..."
4. Anonymize all URLs, GitHub links, project pages, video links
5. Clear PDF metadata
6. Remove acknowledgments
7. Anonymize hardware identifiers and system configurations

## Camera-Ready Differences

After acceptance:

1. Restore all author names and affiliations
2. Add the conference-specific copyright notice provided by IEEE
3. Ensure Xplore-compatible PDF (CMYK colors, embedded fonts)
4. Submit via IEEE PDF eXpress

## Section Organization

VR papers typically follow a human-centered VR research structure:

1. **Abstract** — Concise summary
2. **Introduction** — VR/AR problem, user experience challenge, contributions
3. **Background & Related Work** — VR/AR foundations, prior systems
4. **System Design** — Hardware setup, software architecture
5. **User Study / Evaluation** — Methodology, participants, tasks, metrics
6. **Results** — Quantitative and qualitative findings
7. **Discussion** — Implications, limitations, design guidelines
8. **Conclusion**
9. References
10. Appendix (optional)

## VR/AR-Specific Content

### Hardware Setup Description

VR papers require detailed hardware descriptions:

```latex
\section{System Design}
\subsection{Hardware Configuration}
We implemented the system on an Oculus Quest 3 headset running at
90 Hz refresh rate with a display resolution of 2064x2208 pixels
per eye. The participant's position was tracked using the headset's
inside-out tracking system with sub-millimeter accuracy.
The application was developed in Unity 2023.2 with the XR Interaction
Toolkit. Audio feedback was delivered via the headset's integrated
speakers with head-related transfer function (HRTF) processing.
```

### User Study Methodology

VR papers require rigorous user study methodology:

```latex
\section{Evaluation}
\subsection{Participants}
We recruited 24 participants (12 female, 12 male, age $M=28.3$, $SD=4.2$)
from the university community. All participants had normal or
corrected-to-normal vision and reported no history of motion sickness.
Participants were randomly assigned to two conditions in a between-subjects
design. Sample size was determined via power analysis ($\alpha=0.05$, power=0.8$).

\subsection{Procedure}
After providing informed consent, participants completed a demographic
questionnaire and a simulator sickness questionnaire (SSQ) baseline.
They then underwent a 5-minute training period followed by the main
experimental task. After each condition, participants completed the
SSQ, the presence questionnaire (PQ), and a subjective preference questionnaire.

\subsection{Metrics}
We measured: (1) task completion time, (2) error rate, (3) SSQ scores,
(4) presence questionnaire (PQ) scores, and (5) subjective preference rankings.
```

## Presence and Simulator Sickness

VR papers commonly report standardized questionnaires:

```latex
% Common VR metrics to report:
\begin{itemize}
  \item \textbf{Simulator Sickness Questionnaire (SSQ)}: Kennedy et al.
  \item \textbf{Presence Questionnaire (PQ)}: Slater et al.
  \item \textbf{ITQ (Immersive Tendency Questionnaire)}: Slater et al.
  \item \textbf{SSQ subscales}: Nausea, Oculomotor, Disorientation
\end{itemize}
```

## Figures and Tables

- IEEE single-column format
- Grayscale legibility required
- Use high-resolution figures (minimum 300 DPI)
- Include hardware setup photos when relevant

```latex
\begin{figure}[t]
  \centering
  \includegraphics[width=0.9\linewidth]{figs/system-setup}
  \caption{The VR training system setup showing: (a) the head-mounted
    display with hand controllers, (b) the tracked workspace boundaries,
    and (c) the experimenter's monitoring station.}
  \label{fig:setup}
\end{figure}
```

## References

```latex
\bibliographystyle{IEEEtran}
\bibliography{references}

% Numeric citations
\cite{kennedy1993simulator}
```

## Formatting Rules

- **Format:** IEEE conference (single-column)
- **Paper size:** US Letter
- **Body font:** 10pt minimum
- **Margins:** 1" all sides
- **Xplore-compatible PDF**: CMYK colors, embedded fonts

## Submission Checklist

- [ ] 8 pages or fewer (main body)
- [ ] Author information removed/anonymized
- [ ] Third-person self-citations only
- [ ] Anonymized all URLs and video links
- [ ] PDF metadata cleared
- [ ] User study methodology clearly described
- [ ] Hardware setup specified
- [ ] Standard VR metrics reported (SSQ, presence)
- [ ] Grayscale-legible figures

## Camera-Ready Checklist

- [ ] Restore author information
- [ ] Add IEEE copyright notice
- [ ] Generate Xplore-compatible PDF
- [ ] Use CMYK colors for figures
- [ ] Embed all fonts
- [ ] Submit via IEEE PDF eXpress
