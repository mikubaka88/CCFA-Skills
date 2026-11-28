#!/usr/bin/env python3
"""Render public numerical examples from saved, independently synthetic inputs.

Run with --refresh-data only to replace the saved public demonstration inputs.
No manuscript, user image or private working directory is read by this builder.
"""
from __future__ import annotations

import argparse
import copy
import json
from pathlib import Path
import secrets
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'ccf-visual-composer/resources/python'))
import ccfa_analysis_templates as templates
import ccfa_figure_layouts as layouts
from ccfa_figure_library import export, _plain

DEFAULT = ROOT / 'assets/visual-showcase/analysis-showcase.json'


def public_specs():
    examples = templates.demo_data(secrets.randbits(32))
    specs = {}
    for name, pair, width, height in [
        ('analysis-density-quantiles', 'sensitivity', 145, 90),
        ('analysis-dynamics-categories', 'dynamics', 220, 83),
    ]:
        data = copy.deepcopy(examples['sensitivity_dynamics'])
        data['panel_pair'] = pair
        for unused in (('dynamics', 'categories') if pair == 'sensitivity' else ('density', 'sensitivity')):
            data.pop(unused, None)
        specs[name] = {'version': 1, 'template': 'sensitivity_dynamics', 'data': data,
                       'width_mm': width, 'height_mm': height, 'font': 'serif',
                       'font_size': 9, 'palette': 'ccfa_gem'}
    for name, kind, width, height in [
        ('analysis-joint-distribution', 'joint_marginals', 160, 115),
        ('analysis-response-slices', 'matrix_slices', 183, 122),
    ]:
        data = _plain(layouts.demo_data(kind))
        if kind == 'joint_marginals':
            import numpy as np
            rng = np.random.default_rng()
            x = rng.beta(2.3, 3.0, 1200)
            y = .13 + .62*x + rng.normal(0, .09, len(x))
            data.update(x=x.tolist(), y=y.tolist(), xlabel='Input signal (a.u.)',
                        ylabel='Output response (a.u.)')
        else:
            import numpy as np
            rng = np.random.default_rng()
            x = np.linspace(0, 1, 36)
            y = np.linspace(0, 1, 25)
            xx, yy = np.meshgrid(x, y)
            response = (.12 + .70*np.exp(-((xx-.35)/.22)**2-((yy-.60)/.29)**2)
                        + .27*np.exp(-((xx-.78)/.18)**2-((yy-.24)/.24)**2)
                        + .03*np.sin(xx*9)*np.cos(yy*7) + rng.normal(0, .006, xx.shape))
            data.update(x=x.tolist(), y=y.tolist(), response=response.tolist(), row_index=15,
                        column_index=14, xlabel='Control A', ylabel='Control B',
                        response_label='Response (a.u.)', cmap='YlGnBu_r')
        specs[name] = {'version': 1, 'layout': kind, 'data': data, 'width_mm': width,
                       'height_mm': height, 'font': 'serif', 'font_size': 9,
                       'palette': 'ccfa_gem'}
    for name, template, palette in [
        ('analysis-paired-effects', 'paired_effects', 'ccfa_ceramic'),
        ('analysis-biological-atlas', 'biological_atlas', 'nejm'),
    ]:
        specs[name] = {'version': 1, 'template': template, 'data': _plain(examples[template]),
                       'width_mm': 183, 'font': 'serif', 'font_size': 9, 'palette': palette}
    for name, spec in specs.items():
        spec['_meta'] = {'synthetic': True, 'purpose': 'public numerical design demonstration',
                         'source_policy': 'independent synthetic inputs; no private reference data or text',
                         'showcase_id': name}
    return {'version': 1, 'synthetic': True, 'figures': _plain(specs)}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--spec', type=Path, default=DEFAULT)
    parser.add_argument('--outdir', type=Path, default=DEFAULT.parent)
    parser.add_argument('--refresh-data', action='store_true')
    parser.add_argument('--overview', type=Path, help='Optional overview PNG destination')
    args = parser.parse_args()
    if args.refresh_data or not args.spec.exists():
        data = public_specs()
        args.spec.parent.mkdir(parents=True, exist_ok=True)
        args.spec.write_text(json.dumps(data, ensure_ascii=False, allow_nan=False,
                                        separators=(',', ':'))+'\n', encoding='utf-8')
    else:
        data = json.loads(args.spec.read_text(encoding='utf-8'))
    if data.get('synthetic') is not True:
        parser.error('The public showcase accepts explicitly synthetic specifications only')
    args.outdir.mkdir(parents=True, exist_ok=True)
    for name, spec in data['figures'].items():
        if spec.get('_meta', {}).get('synthetic') is not True:
            parser.error('Every public demonstration must be explicitly synthetic')
        paths = export(spec, args.outdir/name, python_source=False, protected_paths=(args.spec,))
        # One canonical JSON preserves inputs and styling; renderer metadata is disposable.
        paths['metadata'].unlink(missing_ok=True)
        print(paths['png'].relative_to(args.outdir).as_posix())
    # Build a numerical overview from these same public renders, never old previews.
    import matplotlib.pyplot as plt
    titles = ['Density and grouped response', 'Process and category comparison',
              'Joint distribution and marginals', 'Response surface and slices',
              'Paired and subgroup effects', 'Biological analysis']
    fig, axes = plt.subplots(3, 2, figsize=(12, 13), layout='constrained', facecolor='white')
    for ax, (name, _), title in zip(axes.flat, data['figures'].items(), titles):
        ax.imshow(plt.imread(args.outdir/(name+'.png')))
        ax.axis('off')
        ax.set_title(title, fontsize=12, fontfamily='DejaVu Serif', weight='bold', pad=5)
    overview = args.overview or (ROOT/'assets/analytical-figures-gallery.png'
                                if args.outdir.resolve() == DEFAULT.parent.resolve()
                                else args.outdir/'analysis-overview.png')
    overview.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(overview, dpi=180, facecolor='white')
    plt.close(fig)


if __name__ == '__main__':
    main()
