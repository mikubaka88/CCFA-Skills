# Passive Ultra-Wideband Single-Photon Imaging

Venue/year: ICCV 2023.
Source: CVF `https://openaccess.thecvf.com/content/ICCV2023/html/Wei_Passive_Ultra-Wideband_Single-Photon_Imaging_ICCV_2023_paper.html`.
Use when: writing computational imaging, passive sensing, photon-limited reconstruction, hardware plus algorithm, or extreme-dynamic-range papers.

## Story Pattern

The paper defines an unusually difficult imaging regime: dynamic scenes over seconds-to-picoseconds timescales, passively, with little light, and without timing signals from the source. The writing strength is that the sensing constraints are stated as the problem itself, then the method and experiments are organized around making that impossible-looking regime measurable.

## Abstract Moves

- Open with the extreme imaging regime.
- Bundle constraints explicitly so reviewers understand the novelty boundary.
- Present the system as passive and timing-signal-free, not merely improved reconstruction.
- Emphasize simultaneous timescale coverage.

## Introduction Moves

- Contrast active illumination setups with passive real-world sensing.
- Explain why source timing is normally needed.
- Frame the method as expanding what can be observed, not only improving a metric.

## Method Moves

- Introduce the sensing model before reconstruction.
- Make hardware assumptions explicit.
- Separate physical acquisition from computational recovery.

## Evidence Moves

- Show examples across the claimed timescale range.
- Include controlled experiments that verify the passive measurement assumption.
- Use qualitative visualizations to make invisible transient information interpretable.

## Reusable Techniques

- Let multiple constraints define the novelty.
- Make the physical regime clear before algorithm details.
- Use demonstrations to show a new measurement capability.

## Do-Not-Copy Boundary

Do not reuse passive-imaging claims, timescale ranges, or single-photon constraints unless the user's system actually operates there.
