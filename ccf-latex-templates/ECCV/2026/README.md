# Official ECCV 2026 Template

**History** (in reverse chronological order):
- Further modernized for ECCV 2024 by [Stefan Roth](https://github.com/sroth-visinf)
- Imported various features from the [CVPR 2024 templates](https://github.com/cvpr-org/author-kit)
- Based on CVPR 07 and [LNCS](https://www.springer.com/gp/computer-science/lncs/conference-proceedings-guidelines), with modifications by DAF, AZ and elle, 2008 and AA, 2010, and CC, 2011; TT, 2014; AAS, 2016; AAS, 2020; TH, 2022
- Updated April 2002 by Antje Endemann


## Instructions
- Modify the example document `main.tex` following the instructions therein
- Please make sure to look at all `TODO REVIEW` and `TODO FINAL` comments, which provide important instructions and todos for the review and camera-ready versions, respectively
- Either compile with `pdflatex` as

        pdflatex main
        bibtex main
        pdflatex main
        pdflatex main

    or compile with plain `latex` as

        latex main
        bibtex main
        latex main
        latex main
        dvips main
        pstopdf main.ps
