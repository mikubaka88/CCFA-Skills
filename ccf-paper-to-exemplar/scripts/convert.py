"""Convert research paper PDFs to distilled markdown exemplar cards.

Usage:
 python convert.py paper.pdf --venue CVPR --full-text
 python convert.py paper-a.pdf paper-b.pdf --output-dir cards/ --full-text --set-default

For each PDF, produces a distilled .md card with writing-pattern analysis.
Pass --full-text to also save the complete extracted text.
"""

import argparse, re, sys
from os import replace
from tempfile import NamedTemporaryFile
import unicodedata
from pathlib import Path


def _check_pymupdf():
    try:
        __import__('pymupdf')
    except ImportError:
        print('ERROR: pymupdf not installed. Run: pip install pymupdf', file=sys.stderr)
        sys.exit(1)

def extract_text(pdf_path):
    import pymupdf

    parts = []
    with pymupdf.open(pdf_path) as doc:
        for i, page in enumerate(doc,1):
            t = page.get_text('text')
            if t.strip():
                parts.append('## Page ' + str(i) + chr(10) + chr(10) + t)
    if not parts:
        raise ValueError('No extractable text; inspect the PDF or use an authorized OCR workflow.')
    return chr(10) + chr(10).join(parts)


def clean_text(text):
    text = re.sub(r'(?<!' + chr(92) + 'n)' + chr(92) + 'n(?!' + chr(92) + 'n)', ' ', text)
    text = re.sub(r'' + chr(92) + 'n{3,}', chr(92) + 'n' + chr(92) + 'n', text)
    text = text.replace(chr(0xfb01), 'fi').replace(chr(0xfb02), 'fl')
    text = text.replace(chr(0x2013), '--').replace(chr(0x2014), '---')
    return text.strip()


def slugify(name):
    name = unicodedata.normalize('NFKC', name).lower().replace('_', '-')
    name = re.sub(r'[^\w]+', '-', name, flags=re.UNICODE)
    return name.strip('-') or 'paper'


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


def write_current(path, text):
    """Replace one generated text artifact after a complete sibling write."""
    path = Path(path).resolve()
    if path.is_file() and path.read_text(encoding='utf-8') == text:
        return
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = None
    try:
        with NamedTemporaryFile(mode='w', encoding='utf-8', newline='\n', dir=path.parent, prefix=f'.{path.name}.', suffix='.tmp', delete=False) as handle:
            temporary = Path(handle.name)
            handle.write(text)
        replace(temporary, path)
    finally:
        if temporary is not None:
            temporary.unlink(missing_ok=True)


def main():
    parser = argparse.ArgumentParser(description='Convert PDFs to exemplar cards')
    parser.add_argument('pdf', nargs='+', help='PDF files to convert')
    parser.add_argument('--venue', help='Target venue, e.g. CVPR, NeurIPS, ICLR')
    parser.add_argument('--output-dir', default='.', help='Output directory')
    parser.add_argument('--set-default', action='store_true', help='Print default-exemplar registration instructions')
    parser.add_argument('--full-text', action='store_true', help='Also save full extracted text')
    parser.add_argument('--full-text-dir', help='Extracted-text cache directory; defaults to --output-dir')
    args = parser.parse_args()
    _check_pymupdf()
    slugs = [slugify(Path(pdf).stem) for pdf in args.pdf]
    if len({slug.casefold() for slug in slugs}) != len(slugs):
        parser.error('Input names map to the same card filename; convert them to distinct authorized directories.')
    out_dir = Path(args.output_dir)
    text_dir = Path(args.full_text_dir) if args.full_text_dir else out_dir
    results = []
    failures = 0
    for pdf_path in args.pdf:
        pdf_file = Path(pdf_path)
        if not pdf_file.exists():
            print('Not found:', pdf_file)
            failures += 1
            continue
        print('Processing:', pdf_file.name)
        try:
            text = extract_text(str(pdf_file))
            text = clean_text(text)
        except Exception as e:
            print(' ERROR:', e)
            failures += 1
            continue
        venue = detect_venue(text, args.venue)
        secs = detect_sections(text)
        meta = {'title': pdf_file.stem, 'venue': venue, 'basename': pdf_file.stem, 'sections': secs}
        card = make_card(meta)
        slug = slugify(pdf_file.stem)
        card_path = out_dir / (slug + '.md')
        try:
            # Refresh extraction first; never erase a completed human/agent analysis.
            if args.full_text:
                full_path = text_dir / (slug + '.full.md')
                write_current(full_path, text)
                print(' Full text ->', full_path)
            if card_path.exists():
                print(' Reusing existing card; review it against the current source ->', card_path)
            else:
                write_current(card_path, card)
                print(' Card skeleton ->', card_path)
        except OSError as e:
            print(' ERROR writing current artifacts:', e)
            failures += 1
            continue
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
    print('IMPORTANT: New card skeletons contain [ANALYZE] placeholders; existing cards are preserved.')
    print('Fill them in by reading the full extracted text.')
    return 1 if failures else 0


if __name__ == '__main__':
    raise SystemExit(main())
