# CCF Conference LaTeX Templates

This directory contains LaTeX templates for CCF-recommended conferences. Templates are downloaded from official conference websites, publisher repositories, or community-maintained GitHub repos.

**Note:** Most conferences use publisher templates (ACM acmart, IEEEtran, Springer LNCS, etc.) which are shared across many conferences. Only conferences with distinctive per-conference templates have dedicated folders with real verified files.

## Structure

Flat directory — all conference folders are at the top level. Each folder contains actual template files ready to compile.

```
ccf-latex-templates/
|-- README.md
|
|-- [Publisher Base Templates - shared across multiple conferences]
|-- ACM/                           # ACM SIGPLAN/SIGPROC acmart class
|   |-- acmart.cls                # Main class (verified real)
|   |-- ACM-Reference-Format.bst    # BibTeX style
|   |-- acmart.dtx / acmart.ins   # Source + installer
|-- IEEE/                          # IEEEtran class
|   |-- IEEEtran.cls              # Main class (verified real)
|-- USENIX/                        # USENIX conference style
|   |-- usenix-2020-09.sty        # Style file
|   |-- usenix2019_v3.sty
|   |-- usenix2019_v3.1.tex       # Template
|-- Springer/                      # Springer LNCS
|   |-- llncs.cls                 # LNCS class (verified real)
|   |-- splncs04.bst             # Bibliography style
|-- ACL/                           # ACL/NAACL/EMNLP/CoNLL style
|   |-- acl.sty                   # ACL style (from github.com/acl-org/acl-style-files)
|   |-- acl_latex.tex             # Template
|-- LIPIcs/                        # LIPIcs (Dagstuhl)
|   |-- lipics.cls               # LIPIcs v2021 class (verified real)
|   |-- lipics-v2021-authors-guidelines.pdf
|   |-- lipics-v2021-sample-article.tex / .bib
|-- SIAM/                          # SIAM
|   |-- siamltex.cls             # SIAM class (verified real)
|   |-- siamltex.sty
|   |-- siam10.clo
|   |-- siam.bst
|   |-- lexample.tex             # Example
|
|-- [Conference-Specific Templates - distinctive per-conference files]
|-- AAAI/                          # AAAI 2026
|   |-- aaai2026.sty             # (from github.com/lizhemin15/AAAI-2026-Latex-Unified)
|   |-- aaai2026.bst
|   |-- aaai2026_template.tex
|-- NeurIPS/                       # NeurIPS 2026
|   |-- neurips_2026.sty         # (verified, Jan 2026)
|   |-- neurips_2026.tex
|   |-- checklist.tex            # Required checklist
|-- ICML/                          # ICML 2026
|   |-- icml2026.sty            # (verified, Oct 2025)
|   |-- icml2026.bst
|   |-- algorithm.sty / algorithmic.sty / fancyhdr.sty / natbib.sty
|   |-- example_paper.tex / .bib
|-- CVPR/                          # CVPR 2026 (CVF/TheCVF)
|   |-- cvpr.sty                 # (verified 2026)
|   |-- main.tex / preamble.tex / rebuttal.tex
|   |-- main.bib
|   |-- ieeenat_fullname.bst
|   |-- sec/
|-- ICCV/                          # ICCV 2026 (CVF/TheCVF, same as CVPR)
|   |-- iccv.sty
|   |-- main.tex / preamble.tex / rebuttal.tex
|   |-- main.bib
|   |-- ieeenat_fullname.bst
|   |-- sec/
|-- ECCV/                          # ECCV 2026
|   |-- eccv.sty                 # (from github.com/paolo-favaro/paper-template)
|   |-- eccvabbrv.sty
|   |-- llncs.cls                # LNCS base class
|   |-- main.tex / main.bib
|   |-- splncs04.bst
|   |-- ECCV_2026_Paper_Template.pdf
|-- IJCAI/                         # IJCAI 2026
|   |-- ijcai26.sty              # (from ijcai.org, Dec 2025)
|   |-- ijcai26.tex
|   |-- ijcai26.bib
|   |-- named.bst
|-- ICLR/                          # ICLR (OpenReview)
|   |-- iclr2026_conference.sty  # (from github.com/ICLR/Master-Template)
|   |-- iclr2025_conference.sty
|   |-- iclr2021_conference.sty
|   |-- iclr2020_conference.sty
|   |-- iclr2019_conference.sty
|-- MICRO/                        # MICRO 2026
|   |-- main.tex                 # (from microarch.org/micro59, Feb 2026)
|   |-- acmart.cls               # Conference-specific version
|   |-- ACM-Reference-Format.bst
|   |-- sample-base.bib
|-- VLDB/                          # VLDB/PVLDB
|   |-- acmart.cls               # VLDB-specific (from github.com/cwida/pvldbstyle)
|   |-- main.tex                 # PVLDB template
|   |-- sample.bib
|   |-- ACM-Reference-Format.bst
|   |-- figures/
|-- MICCAI/                        # MICCAI 2026
|   |-- MICCAI2026-main conference paper template.tex
|   |-- llncs.cls               # LNCS base class
|   |-- splncs04.bst
|   |-- fig1.eps / history.txt / readme.txt
|   |-- (from conferences.miccai.org/2026)
|-- NDSS/                          # NDSS 2026
|   |-- bare_conf_NDSS2026.tex  # (from ndss-symposium.org, Jan 2026)
|   |-- IEEEtran.cls             # Conference-specific version
|-- SoCG/                          # SoCG (Computational Geometry)
|   |-- socg-lipics-v2021.cls  # (from computational-geometry.org, v0.9, 2022)
|   |-- (uses LIPIcs base class, line-counting instead of page-counting)
|
|-- [Per-Conference ACM Folders - full acmart package]
|-- ACM-MM/ / SIGGRAPH/ / SIGCOMM/ / SOSP/ / ASPLOS/ / ...
|
|-- [Per-Conference IEEE Folders]
|-- SC/ / INFOCOM/ / ICDE/ / ICDM/ / RTSS/ / ...
|
|-- [Per-Conference USENIX Folders]
|-- NSDI/ / FAST/ / OSDI/ / USENIX-ATC/ / USENIX-Security/ / LISA/ / HotStorage/ / IMC/
|
|-- [Per-Conference Springer/LNCS Folders]
|-- CRYPTO/ / EUROCRYPT/ / ESORICS/ / CADE/ / CAV/ / CONCUR/ / ...
|
|-- [Per-Conference ACL Folders]
|-- ACL/ / EMNLP/ / NAACL/ / COLING/ / CoNLL/
```

## Verified Template Download Sources

| Conference | Source | URL |
|-----------|--------|-----|
| AAAI 2026 | GitHub (community) | github.com/lizhemin15/AAAI-2026-Latex-Unified |
| NeurIPS 2026 | Official (Jan 2026) | media.neurips.cc / github.com/EmAstro/LaTeX-templates |
| ICML 2026 | Official (Oct 2025) | media.icml.cc/Conferences/ICML2026 |
| CVPR/ICCV 2026 | CVF (TheCVF) | github.com/cvpr-org/author-kit |
| ECCV 2026 | GitHub (paolo-favaro) | github.com/paolo-favaro/paper-template |
| IJCAI 2026 | Official (Dec 2025) | ijcai.org (FormattingGuidelines-IJCAI-ECAI-26.zip) |
| ICLR 2026 | GitHub (emeryberger) | github.com/emeryberger/iclr-tex |
| MICRO 2026 | Official (Feb 2026) | microarch.org/micro59 |
| VLDB/PVLDB | GitHub (cwida) | github.com/cwida/pvldbstyle |
| MICCAI 2026 | Official | conferences.miccai.org/2026 |
| NDSS 2026 | Official | ndss-symposium.org/ndss2026 |
| SoCG | computational-geometry.org | computational-geometry.org/documents/socg-lipics-v2021.cls |
| ACL/NAACL/EMNLP | ACL Org | github.com/acl-org/acl-style-files |
| ACM acmart | borisveytsman | github.com/borisveytsman/acmart |
| IEEEtran | CTAN/mirrors | mirrors.ctan.org/macros/latex/contrib/IEEEtran |
| Springer LNCS | prosysscience | github.com/prosysscience/llncs |
| LIPIcs | Dagstuhl | drops.dagstuhl.de/styles/lipics |
| SIAM | GitHub | github.com/tgkolda/siam-latex |
| USENIX | Official | usenix.org/conferences/author-resources |

## Usage Examples

### ACM Conferences (sigconf)
```latex
\documentclass[sigconf]{acmart}
```

### ACM SIGPLAN (PPoPP, PLDI, POPL, ICFP, ASPLOS)
```latex
\documentclass[sigplan,screen]{acmart}
```

### IEEE Conferences
```latex
\documentclass[conference]{IEEEtran}
```

### USENIX
```latex
\documentclass[11pt]{article}
\usepackage{usenix-2020-09}
```

### Springer/LNCS (CRYPTO, EUROCRYPT, ESORICS, CADE, etc.)
```latex
\documentclass{llncs}
```

### ACL/EMNLP/NAACL/COLING/CoNLL
```latex
\documentclass{article}
\usepackage{acl}
```

### AAAI 2026
```latex
\documentclass{article}
\usepackage{aaai2026}
```

### NeurIPS 2026
```latex
\usepackage{neurips_2026}
```

### ICML 2026
```latex
\usepackage{icml2026}
```

### CVPR / ICCV 2026
```latex
\documentclass{cvpr}
```

### ECCV 2026
```latex
\documentclass{eccv}
\usepackage[year=2026]{eccv}
```

### IJCAI 2026
```latex
\documentclass{article}
\usepackage{ijcai26}
```

### ICLR 2026
```latex
\usepackage[submission]{iclr2026_conference}
```

### MICRO 2026
```latex
\documentclass[sigplan,review,anonymous]{acmart}
```

### VLDB/PVLDB
```latex
\documentclass[sigconf,pagewide]{acmart}
```

### SoCG (uses line-counting)
```latex
\documentclass{socg-lipics-v2021}
```

### MICCAI 2026
```latex
\documentclass{llncs}
```

### NDSS 2026
```latex
\documentclass[conference]{IEEEtran}
% (use provided bare_conf_NDSS2026.tex template)
```

## Notes

- Always verify templates on official conference websites before submission
- Templates may be updated between conference cycles
- Check page limits, anonymity requirements, and supplementary material policies
- Most conferences use the same base templates (ACM, IEEE, Springer) - check publisher folders
- ACM conferences: use `\documentclass[sigconf]{acmart}` for most SIG conferences
- ACM SIGPLAN: use `\documentclass[sigplan,screen]{acmart}` for PLDI, POPL, ICFP, PPoPP, etc.
- CIDR has no LaTeX template (open-access online proceedings only)
- CASA uses Wiley journal format (not a conference template)
