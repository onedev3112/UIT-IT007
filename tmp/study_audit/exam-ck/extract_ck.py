#!/usr/bin/env python3
"""Extract text (stopping before any answer key) from Cuối Kỳ/Đề thi/*.pdf into tmp/study_audit/exam-ck/."""
import hashlib
import json
import re
from pathlib import Path
import fitz

ROOT = Path(__file__).resolve().parents[3]
SRC_DIR = ROOT / 'Cuối Kỳ' / 'Đề thi'
OUT_DIR = Path(__file__).resolve().parent
STOP_RE = re.compile(r'^\s*(?:đáp\s*án|hướng\s*dẫn\s*giải|lời\s*giải|answer\s*key)\s*[:\-]?\s*$', re.I)


def main():
    manifest = []
    for pdf in sorted(SRC_DIR.glob('*.pdf')):
        doc = fitz.open(str(pdf))
        blocks = []
        char_counts = []
        ended = False
        for i, page in enumerate(doc, 1):
            if ended:
                break
            txt = page.get_text('text') or ''
            lines = txt.splitlines()
            for j, line in enumerate(lines):
                if STOP_RE.match(line):
                    lines = lines[:j]
                    ended = True
                    break
            cleaned = '\n'.join(lines).strip()
            char_counts.append(len(cleaned))
            blocks.append(f'--- PDF PAGE {i} ---\n{cleaned}\n')
        page_total = len(doc)
        doc.close()
        slug = re.sub(r'[^A-Za-z0-9\-]+', '_', pdf.stem).strip('_')
        out_txt = OUT_DIR / f'{slug}.txt'
        out_txt.write_text('\n'.join(blocks), encoding='utf-8')
        manifest.append({
            'file': f'Cuối Kỳ/Đề thi/{pdf.name}',
            'sha256': hashlib.sha256(pdf.read_bytes()).hexdigest(),
            'pages': page_total,
            'pages_extracted': len(char_counts),
            'char_counts': char_counts,
            'answer_section_stopped': ended,
            'cache': f'tmp/study_audit/exam-ck/{out_txt.name}',
        })
        print(f'{pdf.name}: {page_total}p, chars={char_counts}, stopped={ended}')
    (OUT_DIR / 'manifest.json').write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')


if __name__ == '__main__':
    main()
