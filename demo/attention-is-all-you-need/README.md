# Attention Is All You Need - CCFA NeurIPS Demo

This demo shows how the current 13-skill CCFA family should be used on one paper-project scenario.

Scenario: read the original *Attention Is All You Need* paper, extract the research idea, assume the project is being prepared for a NeurIPS-style submission, and then walk through idea optimization, evidence/experiment planning, writing, review, integrity audit, submission check, and rebuttal.

Primary sources:

- Official NeurIPS PDF: https://papers.nips.cc/paper_files/paper/2017/file/3f5ee243547dee91fbd053c1c4a845aa-Paper.pdf
- arXiv mirror: https://arxiv.org/abs/1706.03762

![Demo journey](../../assets/ccfa-skills-demo-attention.svg)

## Reading Order

1. `ccfa.yaml` - shared project state for the demo.
2. `artifacts/00-original-paper-reading.md` - source-reading notes from the original paper.
3. `artifacts/01-idea-document.md` - the idea brief extracted from the original paper.
4. `artifacts/02-neurips-skill-run.md` - the step-by-step CCFA run using all 13 runtime skills.
5. `artifacts/03-writing-draft.md` - how `ccf-paper-writer` produced the NeurIPS-style writing output.
6. `paper/attention_neurips_demo.tex` - the actual LaTeX manuscript draft generated from the idea and official data.
7. `artifacts/04-review-and-rebuttal.md` - review simulation, action ledger, and rebuttal draft.
8. `artifacts/05-submission-check.md` - venue/package/artifact readiness check.
9. `artifacts/official-data.md` and `artifacts/result-tables.md` - official values and real-result tables.
10. `skill-self-tests.md` - smoke prompts proving the consolidated 13-skill routing.

## What This Demo Is

- A deterministic dry run of the CCFA family.
- A source-grounded walkthrough that uses official paper data only.
- A routing and artifact demo for NeurIPS-style paper preparation.

## What This Demo Is Not

- Not a reproduction of Transformer training.
- Not a claim about current NeurIPS policy; real submissions must re-check current official rules.
- Not a new paper and not a source of extra unverified benchmark numbers.
