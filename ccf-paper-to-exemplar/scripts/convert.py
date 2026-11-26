"""Extract paper text and create unfinished Markdown writing-card skeletons.

Usage:
 python convert.py paper.pdf --venue CVPR --full-text
 python convert.py paper-a.pdf paper-b.pdf --output-dir cards/ --full-text --set-default

For each PDF, creates a skeleton for source-grounded analysis by the agent.
Pass --section for selected writing functions and --full-text for extraction.
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


def make_card(meta, requested=None):
    venue = meta.get('venue','Unknown')
    secs = meta.get('sections',[])
    out = []
    out.append('# ' + meta.get('title', venue + ' Paper'))
    out.append('')
    out.append('Venue/year: [ANALYZE] Verify the publication venue and year; venue hint: ' + venue + '.')
    out.append('Source: [ANALYZE] Identify the supplied PDF and source version; this skeleton is not an analysis.')
    out.append('Use when: [ANALYZE] Match an observed writing technique to the scientific object and writing question; a venue hint alone does not establish fit.')
    out.append('')
    moves = {
        'story': ('Story Pattern', 'Anchor the observed argument to source sections. Distinguish source description from adaptation advice.'),
        'abstract': ('Abstract Moves', 'At an identified source passage, explain how subjects, verbs, definitions, and sentence relationships convey the contribution.'),
        'introduction': ('Introduction Moves', 'Trace the actual paragraph progression with source anchors; do not impose a generic paragraph count or outline.'),
        'method': ('Method Moves', 'Show how a source passage connects an operation, its dependencies, and its purpose. Identify the location.'),
        'evidence': ('Evidence Moves', 'Locate a result passage and explain how comparison, observation, and interpretation are connected.'),
        'citation': ('Citation Patterns', 'Identify what a cited sentence attributes or supports and how it connects to the surrounding argument.'),
    }
    selected = list(dict.fromkeys(requested)) if requested else list(moves)
    for name in selected:
        heading, instruction = moves[name]
        out.extend(['## ' + heading, '', '[ANALYZE] ' + instruction, ''])
    out.append('## Reusable Techniques')
    out.append('')
    out.append('[ANALYZE] Label adaptation advice separately from source observations. Explain when a sentence or paragraph technique fits new scientific material.')
    out.append('')
    out.append('## Do-Not-Copy Boundary')
    out.append('')
    out.append('Do not copy task, claims, examples, or technical content.')
    out.append('Only the writing patterns transfer.')
    out.append('')
    out.append('## Auto-Detected')
    out.append('')
    out.append('Keyword matches are navigation hints, not verified section names or boundaries.')
    out.append('- Sections: ' + (' + '.join(secs) if secs else 'none detected'))
    return chr(10).join(out)


def write_current(path, text):
    """Replace one generated text artifact after a complete sibling write."""
    path = Path(path).resolve()
    if path.is_file() and path.read_text(encoding='utf-8-sig') == text:
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
    # Standalone reports and redirected diagnostics use UTF-8 on every platform.
    for stream in (sys.stdout, sys.stderr):
        if hasattr(stream, "reconfigure"):
            stream.reconfigure(encoding="utf-8", errors="strict")
    parser = argparse.ArgumentParser(description='Extract PDFs and create writing-card skeletons requiring source analysis')
    parser.add_argument('pdf', nargs='+', help='PDF files to convert')
    parser.add_argument('--venue', help='Target venue, e.g. CVPR, NeurIPS, ICLR')
    parser.add_argument('--output-dir', default='.', help='Output directory')
    parser.add_argument('--set-default', action='store_true', help='Print default-exemplar registration instructions')
    parser.add_argument('--full-text', action='store_true', help='Also save full extracted text')
    parser.add_argument('--full-text-dir', help='Extracted-text cache directory; defaults to --output-dir')
    parser.add_argument('--section', action='append', choices=['story', 'abstract', 'introduction', 'method', 'evidence', 'citation'],
                        help='Analyze selected writing functions; repeat when useful, omit for a whole-paper skeleton')
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
        card = make_card(meta, args.section)
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
        print('=== Registration requires completed source analysis ===')
        print('Complete and check each card against its original passages first.')
        print('Use personal_library.py register --project <project> with the card, original source, source ID/version, locations and writing functions.')
        print('After registering a completed card, an explicit default request can use:')
        print(' python personal_library.py set-default --project <project> --id <registered-id>')
        print('Explicit --scope user selects the personal library under $CODEX_HOME/ccfa/exemplars/.')
        print('This compatibility flag prints guidance only; it does not change defaults or the built-in library.')
    print()
    print('IMPORTANT: New card skeletons contain [ANALYZE] placeholders; existing cards are preserved.')
    print('Fill them in by reading the full extracted text.')
    return 1 if failures else 0


if __name__ == '__main__':
    raise SystemExit(main())
