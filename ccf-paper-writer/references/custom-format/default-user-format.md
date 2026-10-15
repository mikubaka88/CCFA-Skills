# Default User-Custom Writing Format

Use this format when the user requests it or an established project preference selects it. An unspecified venue alone does not activate it. Preserve a supplied document format; a new LaTeX manuscript without a usable target template follows the disclosed NeurIPS format fallback in `references/output-style-policy.md`. Do not impose a LaTeX template on Markdown or another requested format. Review remains owned by `ccf-paper-reviewer`.

## Source Exemplars

The current custom format is distilled from two user-provided exemplar cards:

- ICLR family: `references/exemplars/cards/llava-4d.md`
- CVPR: `references/exemplars/cards/vggt.md`

These are user-supplied writing references, not compulsory sources or venue requirements. Select a card only when its scientific object, evidence type, or writing question matches the current work; a task may need neither. Preserve source attribution. Transfer useful argument structure without copying scientific claims or wording.

## Writing Shape

Choose useful functions from this structure according to the contribution; neither their count nor their paragraph allocation is fixed. `references/materials-to-manuscript.md` governs content-first drafting, evidence status, and later fitting:

1. Task and capability gap: begin from a concrete capability the field cares about, then show why current systems fail in a physical, dynamic, geometric, or deployment-relevant setting.
2. Prior-work ladder: present prior work as successive partial progress, not as a citation list.
3. Root challenge: identify the missing representation, missing output family, missing temporal/spatial reasoning, or missing direct prediction path.
4. Scientific insight: explain the connected observations that motivate the actual contribution; retain multiple related insights when needed.
5. Mechanism preview: name the main modules by their roles in the story.
6. Evidence relation: connect claims to applicable supplied support. Distinguish planned evaluation from observed findings; not every contribution needs a model experiment.
7. Scientific conditions: explain material assumptions where they affect interpretation, without appending a generic cautionary ending.

## Section Defaults

Abstract:

- Explain the question, relevant gap, actual contribution, and mechanism at a readable level.
- Describe a dataset, benchmark, or evaluation package only when supplied and relevant.
- Include findings only when supported; planned evidence is not an observed result. Sentence count follows the content and requested length.

Introduction:

- Establish why the problem matters, relevant prior work, the scientific gap, and the observations motivating the contribution.
- Introduce the actual method or other contribution with sufficient definitions.
- Organize these functions into as many paragraphs as the argument needs. Contribution statements must match completed work or clearly proposed mechanisms.

Method:

- Define inputs and outputs before architecture.
- Explain the representation or token family before fusion or training details.
- Separate model, data, training, and inference if all exist.
- Use module names that reflect reviewer-facing function.

Experiments:

- Follow the supplied design and contribution type; select comparisons, ablations, analyses, or case studies only when applicable.
- Explain supported results in a logical order, including relevant negative findings.
- For pending results, retain the authorized setup and table scaffold with missing values; do not generate outcome analysis. An explicitly deferred whole experiment section remains deferred.

## Quality Pass

Apply one internal writing-quality pass after drafting. Check scientific meaning, evidence bounds, terminology, paragraph flow, and format fidelity. A substantial new draft or evidence change uses the writer entry's scoped reviewer handoff when not already covered; preserve phase and pending-result status. Do not automatically create a panel, acceptance score, or repeated critique transcript. An additional independent review follows the effective shared preferences.

## Citation Rules

When using this custom format, follow the citation workflow in `references/citation-workflow.md`:

- Support substantive prior-work claims, borrowed mechanisms, and external datasets or baselines with verified sources.
- Coverage follows the scientific argument and closest work, without section or total citation quotas.
- Usually make the finding or method the subject; author-name subjects remain appropriate when attribution matters.
- Define newly introduced resources directly and cite actual predecessors where applicable. Do not invent a source for the current work.
- Follow `references/prose-quality-guardrails.md` for selective emphasis and useful brief headings.

## Output Contract

When this default format is active, return the artifact the user requested. Mention the format assumption and selected exemplars only when they help the user evaluate a from-scratch draft. Keep story blueprints, claim-evidence maps, and quality checks internal unless the user asks to see them. Exact-output requests override this default.

## Maintenance

The custom exemplar list is intentionally easy to edit. To add or remove future examples, use `ccf-paper-to-exemplar`, which distills user-provided papers and updates the exemplar registry without treating source text as a reusable template.
