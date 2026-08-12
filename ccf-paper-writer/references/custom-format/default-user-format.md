# Default User-Custom Writing Format

Use this format whenever the user asks for paper writing, planning, polishing, or review but does not specify a target venue, journal, or conference. State the assumption: "No target venue was specified, so I am using the user-custom writing format."

## Source Exemplars

The current custom format is distilled from two user-provided exemplar cards:

- ICLR family: `references/exemplars/cards/llava-4d.md`
- CVPR: `references/exemplars/cards/vggt.md`

These are not ordinary venue-best-paper defaults. They are the user's own preferred writing examples. Load both cards before drafting unless the user asks to exclude one.

## Writing Shape

Use this structure:

1. Task and capability gap: begin from a concrete capability the field cares about, then show why current systems fail in a physical, dynamic, geometric, or deployment-relevant setting.
2. Prior-work ladder: present prior work as successive partial progress, not as a citation list.
3. Root challenge: identify the missing representation, missing output family, missing temporal/spatial reasoning, or missing direct prediction path.
4. Core insight: express one observation that makes the method feel inevitable.
5. Mechanism preview: name the main modules by their roles in the story.
6. Evidence promise: map each contribution to a measurable task, ablation, benchmark, qualitative example, or downstream use.
7. Boundary: explicitly avoid claims that require an actual target venue, uncollected experiments, or unsupported novelty.

## Section Defaults

Abstract:

- One sentence for the capability gap.
- One sentence for the limitation of current approaches.
- Two to three sentences for method mechanism and outputs.
- One sentence for dataset, benchmark, or evaluation package if present.
- One sentence for results or expected evidence, calibrated to the actual proof available.

Introduction:

- Paragraph 1: field momentum and why the problem matters.
- Paragraph 2: prior-work ladder and remaining failure mode.
- Paragraph 3: root observation or design insight.
- Paragraph 4: method overview with modules and output definitions.
- Paragraph 5: contribution bullets, each linked to evidence.

Method:

- Define inputs and outputs before architecture.
- Explain the representation or token family before fusion or training details.
- Separate model, data, training, and inference if all exist.
- Use module names that reflect reviewer-facing function.

Experiments:

- Main comparison first.
- Then ablations tied to contribution bullets.
- Then qualitative examples that expose the motivating failure mode.
- Then efficiency, scaling, or downstream evidence if claimed.
- Then limitations and failure cases.

## Quality Pass

Apply one internal writing-quality pass after drafting. Check scientific meaning, evidence bounds, terminology, paragraph flow, and format fidelity. Do not simulate reviewers, assign scores, or expose an iterative critique transcript unless the user explicitly requests review. Route a separate scientific review to `ccf-paper-reviewer` instead of mixing it into ordinary writing.

## Citation Rules

When using this custom format, follow the citation workflow in `references/citation-workflow.md`:

- The introduction must carry12-20 citations woven naturally into the argument chain.
- Related Work needs3-8 citations per topic group,20-35 total.
- Every baseline, dataset, and borrowed module must be cited.
- Use claim-first citation style: the sentence makes its point, then the bracket provides attribution.
- Do not use "Author et al. [N]" as a sentence subject. Use the finding or method as the subject.
- No `\textbf{Label:}` scaffolding in prose paragraphs. Write continuous arguments.
- Count total citations before calling the draft complete: under25 for an AI/CV/NLP paper means under-cited.

## Output Contract

When this default format is active, return the artifact the user requested. Mention the format assumption and selected exemplars only when they help the user evaluate a from-scratch draft. Keep story blueprints, claim-evidence maps, and quality checks internal unless the user asks to see them. Exact-output requests override this default.

## Maintenance

The custom exemplar list is intentionally easy to edit. To add or remove future examples, use `ccf-paper-to-exemplar`, which distills user-provided papers and updates the exemplar registry without treating source text as a reusable template.
