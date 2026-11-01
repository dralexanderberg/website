"""Footnote placement check for a typeset PDF.
Usage: python fncheck.py PDF SOURCE_HTML [--json OUT] [--summary]
With --summary it prints one line and exits with status 1 if a note is misplaced or missing.
Reports, for every footnote number, the page of its call in the text and the page where the
note starts in the footnote area; a note that starts on a later page than its call is a
violation. Also reports continued (split) notes, white space above the footnote area, and a
letter-by-letter comparison with the source HTML (to catch lost or duplicated text)."""
import sys, re, html, json, collections
import pymupdf

pdf, src = sys.argv[1], sys.argv[2]
out_json = sys.argv[sys.argv.index('--json') + 1] if '--json' in sys.argv else None
doc = pymupdf.open(pdf)
DIGITS = re.compile(r'^\d+$')

def lines_of(page):
    res = []
    for b in page.get_text('dict')['blocks']:
        for l in b.get('lines', []):
            spans = [s for s in l['spans'] if s['text'].strip()]
            if spans: res.append({'bbox': l['bbox'], 'spans': spans})
    res.sort(key=lambda l: (round(l['bbox'][1], 1), l['bbox'][0]))
    return res

calls, markers, conts, gaps, pages_text = [], [], [], [], []
for pno, page in enumerate(doc, 1):
    H = page.rect.height
    ls = lines_of(page)
    footer = [l for l in ls if l['bbox'][1] > H - 50 and max(s['size'] for s in l['spans']) < 8]
    body = [l for l in ls if l not in footer]
    # footnote region: the run of lines at the bottom whose main font size (by number of
    # characters, so that a slightly larger Greek word does not count) is <= 9.3 pt
    def main_size(l):
        w = collections.Counter()
        for s in l['spans']: w[round(s['size'], 1)] += len(s['text'].strip())
        return w.most_common(1)[0][0]
    k = len(body)
    while k > 0 and main_size(body[k - 1]) <= 9.3:
        k -= 1
    text_lines, fn_lines = body[:k], body[k:]
    # a footnote region must start below the last text line; tiny regions at the very top are notices
    for l in text_lines:
        big = [s['origin'][1] for s in l['spans'] if s['size'] >= 9.4]
        base = max(big) if big else None
        for s in l['spans']:
            t = s['text'].strip()
            if DIGITS.match(t) and s['size'] <= 8.6 and base is not None and s['origin'][1] < base - 1.0:
                calls.append((int(t), pno, round(s['origin'][1], 1)))
    for i, l in enumerate(fn_lines):
        first = l['spans'][0]
        t = first['text'].strip()
        if DIGITS.match(t) and first['size'] <= 8.0:
            markers.append((int(t), pno, round(first['origin'][1], 1)))
        elif i == 0:
            conts.append(pno)
    last_text = max((l['bbox'][3] for l in text_lines), default=None)
    fn_top = min((l['bbox'][1] for l in fn_lines), default=None)
    if last_text is not None:
        gaps.append((pno, round((fn_top if fn_top is not None else H - 62.4) - last_text, 1), fn_top is not None))
    pages_text.append(' '.join(s['text'] for l in body for s in l['spans']))

N = max([c[0] for c in calls] + [m[0] for m in markers] + [0])
cmap = collections.defaultdict(list); mmap = collections.defaultdict(list)
for n, p, y in calls: cmap[n].append(p)
for n, p, y in markers: mmap[n].append(p)
problems, violations = [], []
for n in range(1, N + 1):
    if len(cmap[n]) != 1: problems.append(f'note {n}: {len(cmap[n])} calls found {cmap[n]}')
    if len(mmap[n]) != 1: problems.append(f'note {n}: {len(mmap[n])} note starts found {mmap[n]}')
    if len(cmap[n]) == 1 and len(mmap[n]) == 1 and cmap[n][0] != mmap[n][0]:
        violations.append({'note': n, 'call_page': cmap[n][0], 'note_page': mmap[n][0]})

# letters: source HTML vs PDF (footers excluded); digits ignored (calls and page numbers)
s = open(src, encoding='utf-8').read()
s = re.sub(r'<(style|title|script)[^>]*>.*?</\1>', ' ', s, flags=re.S)
s = html.unescape(re.sub(r'<[^>]+>', ' ', s)).replace('­', '')
a = collections.Counter(c for c in s if c.isalpha())
b = collections.Counter(c for c in ' '.join(pages_text) if c.isalpha())
missing, extra = a - b, b - a

big_gaps = [g for g in gaps[:-1] if g[1] > 30]
report = {
    'pdf': pdf, 'pages': len(doc), 'notes': N, 'calls_found': len(calls), 'note_starts_found': len(markers),
    'violations': violations, 'problems': problems, 'continued_on_pages': conts,
    'gaps_over_30pt': big_gaps, 'max_gap': max((g[1] for g in gaps[:-1]), default=0),
    'letters_source': sum(a.values()), 'letters_pdf': sum(b.values()),
    'letters_missing': dict(missing.most_common(10)), 'letters_extra': dict(extra.most_common(10)),
}
if out_json: json.dump(report, open(out_json, 'w'), ensure_ascii=False, indent=1)
if '--summary' in sys.argv:
    name = pdf.rsplit('/', 1)[-1]
    print(f"{name}: {report['pages']} pages, {N} notes, {len(violations)} starting after their call page, "
          f"{len(problems)} not found; split notes continue on pages {conts or 'none'}")
    for v in violations: print(f"  note {v['note']}: call on page {v['call_page']}, starts on page {v['note_page']}")
    for p in problems: print('  ' + p)
    sys.exit(1 if violations or problems else 0)
print(json.dumps(report, ensure_ascii=False, indent=1))
