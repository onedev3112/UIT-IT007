#!/usr/bin/env python3
"""Extract text and page indexes from newly added theory PDFs (Week 06–11) once per changed source."""
import argparse
import hashlib
import json
import re
from pathlib import Path
import fitz  # PyMuPDF

VERSION = '1.0'
SOURCES = [
    ('W06-1', '#Week06-Chapter5-1 2024.pdf', 'Chương 5 (Phần 1)'),
    ('W06-2', '#Week06-Chapter5-2 2024.pdf', 'Chương 5 (Phần 2)'),
    ('W08', '#Week08-Chapter6 2024.pdf', 'Chương 6'),
    ('W09', '#Week09-Chapter7 2024.pdf', 'Chương 7'),
    ('W10', '#Week10-Chapter8 2024.pdf', 'Chương 8'),
    ('W11', 'Week11-Chapter9 2024.pdf', 'Chương 9'),
]


def digest(path: Path) -> str:
    h = hashlib.sha256()
    with path.open('rb') as f:
        for chunk in iter(lambda: f.read(1048576), b''):
            h.update(chunk)
    return h.hexdigest()


def extract_one(code: str, filename: str, label: str, src_dir: Path, out_dir: Path, extractor_sha: str, force: bool):
    src = src_dir / filename
    if not src.exists():
        print(f'{code}: MISSING {src}')
        return None
    mf = out_dir / f'{code}-manifest.json'
    md = out_dir / f'{code}.md'
    idx = out_dir / f'{code}-index.md'
    old = json.loads(mf.read_text(encoding='utf-8')) if mf.exists() else {}
    stat = src.stat()
    same = old.get('size_bytes') == stat.st_size and old.get('mtime_ns') == stat.st_mtime_ns
    sha = old.get('sha256') if same and old.get('sha256') else digest(src)
    if (
        not force
        and old.get('sha256') == sha
        and old.get('extractor_sha256') == extractor_sha
        and old.get('extraction_version') == VERSION
        and md.exists()
        and idx.exists()
    ):
        old['mtime_ns'], old['size_bytes'] = stat.st_mtime_ns, stat.st_size
        mf.write_text(json.dumps(old, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
        print(f'{code}: unchanged ({old["page_count"]} pages)')
        return old

    doc = fitz.open(str(src))
    chunks = [
        f'# {code} — {label} ({filename})',
        '',
        'Bản trích xuất chữ từ PDF theo thứ tự trang (tính từ 1). Bản chữ có thể thiếu hình, công thức hoặc nhãn sơ đồ; xem trang PDF gốc khi cần.',
        '',
    ]
    index = [
        f'# {code} — chỉ mục trang PDF ({label})',
        '',
        'Tiêu đề gợi ý từ văn bản đầu trang; số trang PDF tính từ 1.',
        '',
    ]
    pages = []
    for n, page in enumerate(doc, 1):
        content = page.get_text('text') or ''
        lines = [re.sub(r'\s+', ' ', line).strip() for line in content.splitlines() if line.strip()]
        candidates = [
            s for s in lines
            if len(s) >= 3
            and not re.fullmatch(r'[\d\W_]+', s)
            and not s.startswith('Thực hiện bởi Trường Đại học')
            and not s.startswith('Copyright')
        ]
        title = candidates[0][:150] if candidates else '(không có tiêu đề chữ rõ)'
        flags = []
        if len(''.join(lines)) < 80:
            flags.append('ít chữ hoặc không có chữ; xem PDF gốc')
        try:
            if len(page.get_images(full=False)) > 0:
                flags.append('có ảnh; xem PDF gốc')
        except Exception:
            flags.append('không xác định được ảnh; xem PDF gốc')
        safe_title = title.replace('#', '\\#')
        chunks += [f'## Trang PDF {n} — {safe_title}', '']
        if flags:
            chunks += ['> Lưu ý: ' + '; '.join(flags) + '.', '']
        chunks += [content.strip() or '(Không trích được chữ.)', '']
        index.append(f'- {n}: {title}' + (' [' + '; '.join(flags) + ']' if flags else ''))
        pages.append({'number': n, 'title': title, 'flags': flags, 'text_chars': len(content.strip())})
    doc.close()

    md.write_text('\n'.join(chunks), encoding='utf-8')
    idx.write_text('\n'.join(index) + '\n', encoding='utf-8')
    meta = {
        'code': code,
        'label': label,
        'source': 'Lý thuyết/' + filename,
        'sha256': sha,
        'size_bytes': stat.st_size,
        'mtime_ns': stat.st_mtime_ns,
        'page_count': len(pages),
        'extraction_version': VERSION,
        'extractor_sha256': extractor_sha,
        'output': f'Lý thuyết/pdf/{code}.md',
        'pages': pages,
    }
    mf.write_text(json.dumps(meta, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    low = sum(p['text_chars'] < 80 for p in pages)
    imgs = sum(any('có ảnh' in f for f in p['flags']) for p in pages)
    print(f'{code}: extracted {len(pages)} pages; low text: {low}; with images: {imgs}')
    return meta


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--source-root', type=Path, default=Path(__file__).resolve().parent.parent)
    parser.add_argument('--force', action='store_true')
    args = parser.parse_args()
    src_dir = args.source_root / 'Lý thuyết'
    out_dir = Path(__file__).resolve().parent.parent / 'Lý thuyết' / 'pdf'
    out_dir.mkdir(parents=True, exist_ok=True)
    extractor_sha = digest(Path(__file__).resolve())
    for code, filename, label in SOURCES:
        extract_one(code, filename, label, src_dir, out_dir, extractor_sha, args.force)


if __name__ == '__main__':
    main()
