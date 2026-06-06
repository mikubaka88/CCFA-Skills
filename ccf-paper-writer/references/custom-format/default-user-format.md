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

## Closed-Loop Generation

Run the same loop used by `references/expert-review-loop.md`:

1. Draft using this custom format.
2. Simulate at least three reviewer views: method expert, experiment expert, and writing/storyline expert.
3. Assign a provisional score on a 1-10 scale with reasons.
4. Revise high-severity issues first: unclear contribution, unsupported evidence, missing outputs, weak baselines, overclaiming, or format drift.
5. Re-review the revision.
6. Repeat until no high-severity issue remains, or clearly list the remaining unresolved risk.

## Output Contract

When this default format is active, return:

1. Custom-format assumption.
2. Loaded custom exemplars.
3. Global story blueprint.
4. Draft or revision.
5. Claim-evidence map.
6. Review score and critique.
7. Revision pass and re-review score.

## Maintenance

The custom exemplar list is intentionally easy to edit. To add or remove future examples, use the separate skill `custom-exemplar-curator`. That skill should generate candidate cards, schemas, and edit instructions for the user to review manually; it should not silently change the custom exemplar set.
