"""Convert research paper PDFs to distilled markdown exemplar cards.

Usage:
 python convert.py paper.pdf --venue CVPR
 python convert.py *.pdf --output-dir cards/ --set-default

For each PDF, produces a distilled .md card with writing-pattern analysis.
Pass --full-text to also save the complete extracted text.
"""

import argparse, os, re, sys
from pathlib import Path


def _check_pymupdf():
    try:
        __import__('pymupdf')
    except ImportError:
        print('ERROR: pymupdf not installed. Run: pip install pymupdf', file=sys.stderr)
        sys.exit(1)

_check_pymupdf()
import pymupdf


def extract_text(pdf_path):
    doc = pymupdf.open(pdf_path)
    parts = []
    for i, page in enumerate(doc,1):
        t = page.get_text('text')
        if t.strip():
            parts.append('## Page ' + str(i) + chr(10) + chr(10) + t)
    doc.close()
    return chr(10) + chr(10).join(parts)


def clean_text(text):
    text = re.sub(r'(?<!' + chr(92) + 'n)' + chr(92) + 'n(?!' + chr(92) + 'n)', ' ', text)
    text = re.sub(r'' + chr(92) + 'n{3,}', chr(92) + 'n' + chr(92) + 'n', text)
    text = text.replace(chr(0xfb01), 'fi').replace(chr(0xfb02), 'fl')
    text = text.replace(chr(0x2013), '--').replace(chr(0x2014), '---')
    return text.strip()


def slugify(name):
    name = name.lower()
    name = re.sub(r'[^a-z0-9]+', '-', name)
    return name.strip('-')


def detect_venue(text, user_venue):
    if user_venue:
        return user_venue.upper()
    lower = text[:2000].lower()
    for k in ['cvpr','iccv','neurips','iclr','icml','aaai','acl','eccv']:
        if k in lower:
            return k.upper()
    return 'Unknown'


def detect_sections(text):
    secs = []
    if re.search(r'(?i)abstract', text[:2000]): secs.append('abstract')
    if re.search(r'(?i)' + chr(92) + 'bintroduction' + chr(92) + 'b', text): secs.append('introduction')
    if re.search(r'(?i)' + chr(92) + 'b(related.work|background)' + chr(92) + 'b', text): secs.append('related work')
    if re.search(r'(?i)' + chr(92) + 'b(method|approach|architecture)' + chr(92) + 'b', text): secs.append('method')
    if re.search(r'(?i)' + chr(92) + 'b(experiment|evaluation|results)' + chr(92) + 'b', text): secs.append('experiments')
    return secs


def make_card(meta):
    venue = meta.get('venue','Unknown')
    secs = meta.get('sections',[])
    out = []
    out.append('# ' + meta.get('title', venue + ' Paper'))
    out.append('')
    out.append('Venue/year: ' + venue + '.')
    out.append('Source: distilled from PDF by ccf-paper-to-exemplar skill.')
    out.append('Use when: writing in the ' + venue + ' venue family.')
    out.append('')
    out.append('## Story Pattern')
    out.append('')
    out.append('[ANALYZE] Describe the story arc: task, gap, insight, method, evidence flow.')
    out.append('')
    out.append('## Abstract Moves')
    out.append('')
    out.append('[ANALYZE] How does the abstract compress the contribution?')
    out.append('')
    out.append('## Introduction Moves')
    out.append('')
    out.append('[ANALYZE] Paragraph-by-paragraph role analysis of the introduction.')
    out.append('')
    out.append('## Method Moves')
    out.append('')
    out.append('[ANALYZE] How is the method presented? Module-by-module or concept-first?')
    out.append('')
    out.append('## Evidence Moves')
    out.append('')
    out.append('[ANALYZE] Evidence types, table/figure strategy, claim mapping.')
    out.append('')
    out.append('## Citation Patterns')
    out.append('')
    out.append('[ANALYZE] How are citations woven into the text? Density?')
    out.append('[ANALYZE] Are citations natural (claim-first) or parenthetical?')
    out.append('')
    out.append('## Reusable Techniques')
    out.append('')
    out.append('[ANALYZE] Transferable writing techniques for other papers.')
    out.append('')
    out.append('## Do-Not-Copy Boundary')
    out.append('')
    out.append('Do not copy task, claims, examples, or technical content.')
    out.append('Only the writing patterns transfer.')
    out.append('')
    out.append('## Auto-Detected')
    out.append('')
    out.append('- Sections: ' + (' + '.join(secs) if secs else 'none detected'))
    return chr(10).join(out)


def main():
    parser = argparse.ArgumentParser(description='Convert PDFs to exemplar cards')
    parser.add_argument('pdf', nargs='+', help='PDF files to convert')
    parser.add_argument('--venue', help='Target venue, e.g. CVPR, NeurIPS, ICLR')
    parser.add_argument('--output-dir', default='.', help='Output directory')
    parser.add_argument('--set-default', action='store_true', help='Print default-exemplar registration instructions')
    parser.add_argument('--full-text', action='store_true', help='Also save full extracted text')
    args = parser.parse_args()
    out_dir = Path(args.output_dir)
    out_dir.mkdir(parents=True, exist_ok=True)
    results = []
    for pdf_path in args.pdf:
        pdf_file = Path(pdf_path)
        if not pdf_file.exists():
            print('Not found:', pdf_file)
            continue
        print('Processing:', pdf_file.name)
        try:
            text = extract_text(str(pdf_file))
            text = clean_text(text)
        except Exception as e:
            print(' ERROR:', e)
            continue
        venue = detect_venue(text, args.venue)
        secs = detect_sections(text)
        meta = {'title': pdf_file.stem, 'venue': venue, 'basename': pdf_file.stem, 'sections': secs}
        card = make_card(meta)
        slug = slugify(pdf_file.stem)
        card_path = out_dir / (slug + '.md')
        card_path.write_text(card, encoding='utf-8')
        print(' Card ->', card_path)
        if args.full_text:
            full_path = out_dir / (slug + '.full.md')
            full_path.write_text(text, encoding='utf-8')
            print(' Full text ->', full_path)
        results.append(slug)
    print()
    print('Done.', len(results), 'PDF(s) processed.')
    if args.set_default:
        print()
        print('=== To register as default writing exemplars ===')
        print('1. Copy generated .md card(s) to:')
        print(' ccf-paper-writer/references/exemplars/cards/')
        print('2. Update index: ccf-paper-writer/references/exemplars/index.md')
        print('3. Set as default: ccf-paper-writer/references/custom-format/default-user-format.md')
    print()
    print('IMPORTANT: Cards contain [ANALYZE] placeholders.')
    print('Fill them in by reading the full extracted text.')


if __name__ == '__main__':
    main()
