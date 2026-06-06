# CCFA SVG Style Guide

## Diagram Types

- Architecture: show groups and ownership, not every sentence of behavior.
- Workflow: show stage order, gates, and side branches.
- Routing: show ambiguous prompts and their owning skills.
- Artifact: show project state and read/write surfaces.
- Installation: show required, recommended, partial, and forbidden installs.
- Demo: show the end-to-end example journey and verified result callouts.

## Visual Rules

- Prefer swimlanes, timelines, hubs, and decision splits over large card grids.
- Use short labels: one skill name plus a three-to-six-word role line.
- Use Markdown for long descriptions.
- Use a restrained palette with strong contrast and no decorative blobs.
- Avoid diagonal text and tiny labels.
- Use arrows only when they encode real direction.

## Screenshot Checklist

After generating SVG files:

1. Render representative English and Chinese SVGs to PNG with a browser.
2. Inspect for overflow, clipped descenders, accidental mixed-language labels, and unclear arrows.
3. Check that the README preview does not become a tall wall of nearly empty whitespace.
4. Re-run `python ccf-common/scripts/check_v04.py`.
