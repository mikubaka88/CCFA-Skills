#!/usr/bin/env python3
import argparse, os, re, sys
from pathlib import Path
try:
 import pymupdf
except ImportError:
 print('ERROR: pymupdf not installed. Run: pip install pymupdf', file=sys.stderr)
 sys.exit(1)

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
 text = re.sub(r'(?<!'+chr(92)+'n)'+chr(92)+'n(?!'+chr(92)+'n)', ' ', text)
 text = re.sub(r''+chr(92)+'n{3,}', chr(92)+'n'+chr(92)+'n', text)
 text = text.replace(chr(0xfb01), 'fi').replace(chr(0xfb02), 'fl')
 text = text.replace(chr(0x2013), '--').replace(chr(0x2014), '---')
 return text.strip()

def slugify(name):
 name = name.lower()
 name = re.sub(r'[^a-z0-9]+', '-', name)
 return name.strip('-')

def guess_meta(text, filename):
 bn = os.path.splitext(os.path.basename(filename))[0]
 year = ''
 m = re.search(r'(20'+chr(92)+'d{2})', bn)
 if m:
 year = m.group(1)
 venue = ''
 lower = (bn + ' ' + text[:2000]).lower()
 for k, v in {'cvpr':'CVPR','iccv':'ICCV','eccv':'ECCV','neurips':'NeurIPS','iclr':'ICLR','icml':'ICML','aaai':'AAAI'}.items():
 if k in lower:
 venue = v
 break
 return {'venue':venue,'year':year,'basename':bn}

def make_card(text, meta):
 venue = meta.get('venue','Unknown')
 year = meta.get('year','')
 slug = slugify(meta.get('basename','unknown'))
 venuestr = venue + (' ' + year if year else '')
 sections = []
 if re.search(r'(?i)abstract', text[:2000]): sections.append('abstract')
 if re.search(r'(?i)'+chr(92)+'bintroduction'+chr(92)+'b', text): sections.append('introduction')
 if re.search(r'(?i)'+chr(92)+'b(related.work|background)'+chr(92)+'b', text): sections.append('related work')
 if re.search(r'(?i)'+chr(92)+'b(method|approach|model|architecture)'+chr(92)+'b', text): sections.append('method')
 if re.search(r'(?i)'+chr(92)+'b(experiment|evaluation|results)'+chr(92)+'b', text): sections.append('experiments')
 lines = []
 lines.append('# ' + meta.get('title', venuestr + ' Paper'))
 lines.append('')
 lines.append('Venue/year: ' + venuestr + '.')
 lines.append('Source: auto-extracted from PDF. Needs manual review.')
 lines.append('')
 lines.append('## Story Pattern')
 lines.append('')
 lines.append('[MANUAL] Describe the story arc.')
 lines.append('')
 lines.append('## Abstract Moves')
 lines.append('')
 lines.append('[MANUAL] Abstract compression moves.')
 lines.append('')
 lines.append('## Introduction Moves')
 lines.append('')
 lines.append('[MANUAL] Paragraph role analysis.')
 lines.append('')
 lines.append('## Method Moves')
 lines.append('')
 lines.append('[MANUAL] Method presentation style.')
 lines.append('')
 lines.append('## Evidence Moves')
 lines.append('')
 lines.append('[MANUAL] Evidence types and mapping.')
 lines.append('')
 lines.append('## Reusable Techniques')
 lines.append('')
 lines.append('[MANUAL] Transferable patterns.')
 lines.append('')
 lines.append('## Do-Not-Copy Boundary')
 lines.append('')
 lines.append('Do not copy task, claims, examples, or technical content.')
 lines.append('')
 lines.append('## Auto-Detected')
 lines.append('')
 lines.append('- Sections: ' + ' + '.join(sections))
 return chr(10).join(lines)

def main():
 p = argparse.ArgumentParser(description='Convert PDFs to exemplar cards')
 p.add_argument('pdf_path', nargs='?', help='Single PDF file')
 p.add_argument('--batch', help='Directory of PDFs')
 p.add_argument('--output-dir', default='.', help='Output directory')
 p.add_argument('--full-text', action='store_true', help='Also save full text')
 args = p.parse_args()
 pdfs = []
 if args.batch:
 pdfs = list(Path(args.batch).glob('*.pdf'))
 elif args.pdf_path:
 pdfs = [Path(args.pdf_path)]
 else:
 p.print_help()
 sys.exit(1)
 out = Path(args.output_dir)
 out.mkdir(parents=True, exist_ok=True)
 for pdf in pdfs:
 print('Processing:', pdf.name)
 try:
 text = extract_text(str(pdf))
 text = clean_text(text)
 except Exception as e:
 print(' ERROR:', e)
 continue
 meta = guess_meta(text, pdf.name)
 card = make_card(text, meta)
 slug = slugify(meta['basename'])
 card_path = out / (slug + '.md')
 card_path.write_text(card, encoding='utf-8')
 print(' Card:', card_path)
 if args.full_text:
 full_path = out / (slug + '.full.md')
 full_path.write_text(text, encoding='utf-8')
 print(' Full text:', full_path)
 print(chr(10) + 'Done.', len(pdfs), 'PDF(s) processed.')
 print('IMPORTANT: Cards contain [MANUAL] placeholders.')

if __name__ == '__main__':
 main()
