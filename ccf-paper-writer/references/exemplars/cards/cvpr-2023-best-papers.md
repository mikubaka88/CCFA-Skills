# CVPR 2023 Best Papers

Venue/year: CVPR 2023.
Source: CVF awards list `https://www.thecvf.com/?page_id=413`.
Use when: the user explicitly asks for recent CVPR best-paper style, especially visual reasoning without training or autonomous-driving planning.

## Award Papers

- `Visual Programming: Compositional Visual Reasoning Without Training`
- `Planning-Oriented Autonomous Driving`

## Shared Writing Signals

- Frame the task around an end-to-end behavior that matters: compositional reasoning or planning.
- Make the intermediate representation explicit: programs, perception-planning links, or task-oriented outputs.
- Show that the method changes the problem formulation, not only a network component.
- Evaluate in a way that mirrors the final decision process.

## Transferable Moves

- For reasoning papers: define compositional units and show how they combine.
- For driving/planning papers: connect perception outputs to planning objectives instead of treating them as separate metrics.
- Use qualitative chains or trajectories to make decision structure inspectable.
- Let the method section mirror the task decomposition.

## Reviewer-Facing Warnings

- Do not claim "without training" or "planning-oriented" unless the experimental protocol proves that exact property.
- Make sure the output evaluated is the output the paper claims to optimize.
