# Attention Is All You Need - CCFA ICLR Closed-Loop Demo

This demo reads the original *Attention Is All You Need* paper, extracts the research idea, and runs the current 13-skill CCFA family as if the project were being prepared as an ICLR-style submission.

Primary sources:

- Official NeurIPS PDF: https://papers.nips.cc/paper_files/paper/2017/file/3f5ee243547dee91fbd053c1c4a845aa-Paper.pdf
- arXiv mirror: https://arxiv.org/abs/1706.03762
- ICLR 2026 Author Guide: https://iclr.cc/Conferences/2026/AuthorGuide

![Demo journey](../../assets/ccfa-skills-demo-attention.svg)

## Reading Order

1. `ccfa.yaml` - shared project state.
2. `artifacts/00-original-paper-reading.md` - motivation, problem, insight, method, results, contribution idea, and source writing pattern.
3. `artifacts/01-idea-document.md` - ICLR idea brief.
4. `artifacts/02-iclr-closed-loop-skill-run.md` - all 13 skills and their concrete artifacts.
5. `artifacts/03-idea-review.md` - strict idea review before writing.
6. `artifacts/03-writing-draft.md` - writing-stage decisions and optimization record.
7. `paper/attention_iclr_submission.tex` - complete ICLR-style LaTeX manuscript.
8. `artifacts/04-review-and-rebuttal.md` - writing review, scientific review, integrity audit, rebuttal, and revision ledger.
9. `artifacts/05-submission-check.md` - ICLR format, build, anonymity, page, and artifact checks.
10. `artifacts/06-family-self-audit.md` - remaining CCFA family issues found by this demo.
11. `artifacts/official-data.md` and `artifacts/result-tables.md` - official values and evidence tables.
12. `skill-self-tests.md` - smoke prompts proving consolidated routing.

## What Changed From The Earlier Demo

The earlier demo was too short and route-oriented. This version produces a full manuscript, compiles the TeX, runs idea review before writing, records writing and scientific review, drafts rebuttal text, and lists remaining family problems. It keeps unsupported evidence explicit instead of filling gaps with invented values.
