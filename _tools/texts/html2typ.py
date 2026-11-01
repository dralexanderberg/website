"""Convert a manuscript HTML (endnote version, in src/) into a Typst document with footnotes.

Usage: python html2typ.py SOURCE.html OUT.typ DOC LABEL   (normally called by build.sh)
DOC is identity | lw | psych (selects the spacing rules of that text's CSS); LABEL is the footer.
The HTML keeps the notes as an endnote list (<ol class="notes">, calls <sup class="fnref">);
every note becomes a Typst footnote at its call. Typst splits long footnotes across pages and
keeps each note's start on the page of its call.
"""
import html, re, sys
from html.parser import HTMLParser

src, out, doc, label = sys.argv[1:5]
raw = open(src, encoding='utf-8').read()
assert doc in ('identity', 'lw', 'psych')

# ---------------------------------------------------------------- tiny DOM
class Node:
    def __init__(self, tag, attrs=None, parent=None):
        self.tag, self.attrs, self.parent, self.children = tag, dict(attrs or {}), parent, []
    def cls(self): return self.attrs.get('class', '').split()
    def __repr__(self): return f'<{self.tag} {self.attrs}>'

VOID = {'br', 'meta', 'img', 'hr', 'link', 'wbr'}
class Builder(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.root = Node('#root'); self.cur = self.root
    def handle_starttag(self, tag, attrs):
        n = Node(tag, attrs, self.cur); self.cur.children.append(n)
        if tag not in VOID: self.cur = n
    def handle_startendtag(self, tag, attrs):
        self.cur.children.append(Node(tag, attrs, self.cur))
    def handle_endtag(self, tag):
        n = self.cur
        while n is not self.root and n.tag != tag: n = n.parent
        if n is not self.root: self.cur = n.parent
    def handle_data(self, data):
        self.cur.children.append(data)

b = Builder(); b.feed(raw)
def find(node, pred):
    for c in node.children:
        if isinstance(c, Node):
            if pred(c): return c
            r = find(c, pred)
            if r: return r
title = ''.join(x for x in find(b.root, lambda n: n.tag == 'title').children if isinstance(x, str)).strip()
body = find(b.root, lambda n: n.tag == 'body')

# ---------------------------------------------------------------- notes
notes = {}
ol = find(body, lambda n: n.tag == 'ol' and 'notes' in n.cls())
for li in ol.children:
    if isinstance(li, Node) and li.tag == 'li':
        num = int(li.attrs['id'][1:])
        kids = list(li.children)
        assert isinstance(kids[0], Node) and kids[0].tag == 'a' and 'back' in kids[0].cls()
        notes[num] = kids[1:]
body.children = [c for c in body.children
                 if not (isinstance(c, Node) and (c is ol or (c.tag == 'h3' and ''.join(
                     x for x in c.children if isinstance(x, str)).strip() in ('Notes', 'Anmerkungen'))))]

# ---------------------------------------------------------------- inline conversion
MONTHS = ('January|February|March|April|May|June|July|August|September|October|November|December|'
          'Januar|Februar|März|Juni|Juli|Oktober|Dezember')
def lit(s):
    s = s.replace('\u00ad', '')                      # soft hyphens: Typst hyphenates itself
    s = re.sub(r'[ \t\r\n\f]+', ' ', s)              # HTML whitespace collapsing (keeps NBSP)
    # keep together: initials and surname (G. E. Moore), day and month, p./pp./S. and the number
    s = re.sub(r'\b([A-Z]\.) (?=[A-Z])', '\\1\u00a0', s)
    s = re.sub(rf'\b(\d{{1,2}}\.?) (?=(?:{MONTHS})\b)', '\\1\u00a0', s)
    s = re.sub(r'\b(pp?\.|S\.) (?=\d)', '\\1\u00a0', s)
    return '#"' + s.replace('\\', '\\\\').replace('"', '\\"') + '"' if s else ''

used_notes = []
def inline(nodes):
    parts = []
    for c in nodes:
        if isinstance(c, str):
            parts.append(lit(c)); continue
        t, k = c.tag, c.cls()
        if t == 'i': parts.append('#text(style: "italic")[' + inline(c.children) + ']')
        elif t == 'b': parts.append('#text(weight: "bold")[' + inline(c.children) + ']')
        elif t == 'br': parts.append('#linebreak()')
        elif t == 'a' and 'href' in c.attrs:
            url = c.attrs['href'].replace('\\', '\\\\').replace('"', '\\"')
            label_txt = ''.join(x for x in c.children if isinstance(x, str))
            if label_txt == c.attrs['href'] and label_txt.startswith('https://doi.org/') and len(c.children) == 1:
                parts.append(f'#link("{url}")[#"https://doi.org/"#box[' + lit(label_txt[16:]) + ']]')
            else:
                parts.append(f'#link("{url}")[' + inline(c.children) + ']')
        elif t == 'span' and 'pg' in k:
            txt = ''.join(x for x in c.children if isinstance(x, str))
            parts.append('#pg(' + lit(txt)[1:] + ')')
        elif t == 'span' and 'gr' in k:
            parts.append('#greek[' + inline(c.children) + ']')
        elif t == 'sup' and 'fnref' in k:
            num = int(c.attrs['id'][1:])
            used_notes.append(num)
            parts.append('#footnote[' + inline(strip_edges(notes[num])) + ']')
        elif t == 'span':
            parts.append(inline(c.children))
        else:
            raise SystemExit(f'unhandled inline <{t} {c.attrs}>')
    return ''.join(parts)

def strip_edges(nodes):
    """Drop leading/trailing whitespace of a block's inline content (HTML block semantics)."""
    nodes = list(nodes)
    while nodes and isinstance(nodes[0], str) and not nodes[0].strip(): nodes.pop(0)
    while nodes and isinstance(nodes[-1], str) and not nodes[-1].strip(): nodes.pop()
    if nodes and isinstance(nodes[0], str): nodes[0] = nodes[0].lstrip(' \t\r\n')
    if nodes and isinstance(nodes[-1], str): nodes[-1] = nodes[-1].rstrip(' \t\r\n')
    return nodes

def para_content(p): return inline(strip_edges(p.children))
def elems(node): return [c for c in node.children if isinstance(c, Node)]

# ---------------------------------------------------------------- block conversion
INDENT = '15.4pt'          # 1.4em of 11pt
out_blocks = []
def emit(s): out_blocks.append(s)

def body_par(p, indent):
    amount = INDENT if indent else '0pt'
    if 'closing' in p.cls():
        emit('#block(above: 14pt, below: 0pt, width: 100%)[#align(center)[' + para_content(p) + ']]')
    else:
        emit(f'#par(first-line-indent: (amount: {amount}, all: true))[' + para_content(p) + ']')

def blockquote(bq):
    ps = [para_content(p) for p in elems(bq) if p.tag == 'p']
    assert ps, 'empty blockquote'
    inner = '\n\n'.join(ps)
    emit('#quoteblock[\n' + inner + '\n]')

def main_block(m):
    prev = None
    for c in elems(m):
        if c.tag == 'p':
            if doc == 'lw':
                indent = 'noindent' not in c.cls()
            else:
                indent = prev is not None and prev.tag == 'p'
            body_par(c, indent)
        elif c.tag == 'h2':
            emit('#heading(level: 2)[' + para_content(c) + ']')
        elif c.tag == 'blockquote':
            blockquote(c)
        else:
            raise SystemExit(f'unhandled in main: <{c.tag} {c.attrs}>')
        prev = c

for c in elems(body):
    k = c.cls()
    if c.tag == 'div' and 'notice' in k:
        emit('#notice[\n' + '\n\n'.join(para_content(p) for p in elems(c)) + '\n]')
    elif c.tag == 'h1':
        emit('#heading(level: 1)[' + para_content(c) + ']')
    elif c.tag == 'p' and 'author' in k:
        emit('#author[' + para_content(c) + ']')
    elif c.tag == 'p' and 'abstract' in k:
        emit('#abstract-p[' + para_content(c) + ']')
    elif c.tag == 'p' and 'keywords' in k:
        emit('#keywords[' + para_content(c) + ']')
    elif c.tag == 'div' and 'abstract' in k:
        emit('#abstract-div[\n' + '\n\n'.join(para_content(p) for p in elems(c)) + '\n]')
    elif c.tag == 'p' and 'epigraph' in k:
        emit('#epigraph[' + para_content(c) + ']')
    elif c.tag == 'main':
        main_block(c)
    elif c.tag == 'h3':
        emit('#heading(level: 2, supplement: [h3])[' + para_content(c) + ']')
    elif c.tag == 'div' and ({'refs', 'abbr', 'sigla'} & set(k)):
        for i, p in enumerate(elems(c)):
            fn = 'refsrc' if 'src' in p.cls() else 'ref'
            sticky = 'true' if i == 0 else 'false'
            emit(f'#{fn}(sticky: {sticky})[' + para_content(p) + ']')
    else:
        raise SystemExit(f'unhandled top-level <{c.tag} {c.attrs}>')

assert used_notes == list(range(1, len(notes) + 1)), ('note order', used_notes[:5], len(notes))

# ---------------------------------------------------------------- document setup
lang = 'de' if doc == 'psych' else 'en'
author_below = '16pt' if doc == 'identity' else '4pt'
title_below = '6pt' if doc == 'identity' else '14pt'
if doc == 'psych':
    epigraph = '#let epigraph(body) = block(below: 16pt, width: 100%)[#set text(size: 10pt, ..lh(1.45)); #set par(justify: false, first-line-indent: 0pt); #align(right, body)]'
else:
    epigraph = '#let epigraph(body) = block(below: 18pt, inset: (left: 22pt))[#set text(size: 10pt, ..lh(1.45)); #set par(first-line-indent: 0pt); #body]'

def q(s): return '"' + s.replace('\\', '\\\\').replace('"', '\\"') + '"'

head = f'''// generated by html2typ.py from {src.split('/')[-1]} – do not edit by hand; edit the HTML and run build.sh
#set document(title: {q(title)}, author: "Alexander Berg")
#set page(paper: "a4", margin: (top: 24mm, left: 24mm, right: 24mm, bottom: 22mm),
  footer-descent: 40%,
  footer: context align(center, text(size: 7.5pt, fill: rgb("#555555"), top-edge: "cap-height", bottom-edge: "baseline")[
    #{q(label + ' · ')}#counter(page).display()#"/"#counter(page).final().first()]))
// Each line box is as tall as the CSS line height (glyph box 0.8em/-0.2em plus half the leading
// above and below), and leading is 0: paragraph and block spacing then equal the CSS margins.
#let lh(x) = (top-edge: 0.8em + (x - 1) / 2 * 1em, bottom-edge: -0.2em - (x - 1) / 2 * 1em)
#set text(font: ("P052", "FreeSerif"), size: 11pt, lang: "{lang}", hyphenate: true, fill: rgb("#111111"), ..lh(1.5))
#set par(justify: true, leading: 0pt, spacing: 0pt, first-line-indent: (amount: {INDENT}, all: true))
#set super(typographic: false, size: 0.7em, baseline: -0.38em)
#show super: set text(top-edge: "x-height", bottom-edge: "baseline")   // calls never enlarge a line
#show link: it => text(fill: rgb("#1b2638"), underline(offset: 1.5pt, stroke: 0.4pt, it))

// footnotes: 9 pt, leading 1.4, rule above the footnote area, number as a small superscript
#set footnote(numbering: "1")
#set footnote.entry(separator: block(width: 100%, inset: (bottom: 5pt), line(length: 100%, stroke: 0.5pt + rgb("#999999"))),
  clearance: 10pt, gap: 0pt, indent: 0pt)
// Notes may split after any line (no widow/orphan penalty inside a note): a note then starts on
// its call's page instead of dragging the call's line, and a white gap, onto the next page.
#show footnote.entry: it => {{
  set text(size: 9pt, ..lh(1.4), costs: (widow: 0%, orphan: 0%))
  set par(leading: 0pt, justify: true, first-line-indent: 0pt, spacing: 0pt, hanging-indent: 0pt)
  let num = numbering(it.note.numbering, ..counter(footnote).at(it.note.location()))
  [#super(size: 0.75em, baseline: -0.33em)[#num]#h(0.3em)#it.note.body]
}}

#let pg(n) = box(text(size: 0.72em, fill: rgb("#777777"), tracking: 0.02em, style: "normal", n) + h(0.15em))
#let greek(body) = text(font: "FreeSerif", size: 1.06em, lang: "el", top-edge: "cap-height", bottom-edge: "baseline", body)
#let notice(body) = block(width: 100%, stroke: 0.6pt + rgb("#888888"), inset: (x: 9pt, y: 7pt), below: 20pt)[
  #set text(size: 9pt, ..lh(1.4)); #set par(spacing: 4pt, first-line-indent: 0pt); #body]
#show heading.where(level: 1): it => block(above: 0pt, below: {title_below}, sticky: true)[
  #set text(size: 17pt, weight: "bold", ..lh(1.25)); #set par(justify: false, first-line-indent: 0pt); #it.body]
#show heading.where(level: 2): it => if it.supplement == [h3] {{
  v(22pt, weak: true)
  block(above: 0pt, below: 8pt, sticky: true)[#set par(first-line-indent: 0pt); #text(size: 11pt, weight: "bold", ..lh(1.5), it.body)]
}} else {{
  v(16pt, weak: true)
  block(above: 0pt, below: 8pt, sticky: true, width: 100%)[#set par(first-line-indent: 0pt); #align(center, text(size: 11pt, weight: "bold", ..lh(1.5), it.body))]
}}
#let author(body) = block(below: {author_below})[#set par(first-line-indent: 0pt); #text(size: 12pt, body)]
#let abstract-p(body) = block(below: 6pt)[#set text(size: 9.5pt, ..lh(1.45)); #set par(first-line-indent: 0pt); #body]
#let keywords(body) = block(below: 18pt)[#set text(size: 9.5pt, ..lh(1.5)); #set par(first-line-indent: 0pt); #body]
#let abstract-div(body) = block(below: 18pt)[#set text(size: 9.5pt, lang: "en", ..lh(1.45)); #set par(spacing: 3pt, first-line-indent: 0pt); #body]
{epigraph}
// Block quotes are ordinary paragraphs indented on every line (no block container): a note
// called in a quote's last line then moves with that line, exactly like in body paragraphs.
#let quoteblock(body) = {{
  v(9pt, weak: true)
  set text(size: 10pt, ..lh(1.45))
  set par(spacing: 4pt, first-line-indent: (amount: 22pt, all: true), hanging-indent: 22pt)
  body
  v(9pt, weak: true)
}}
#let ref(sticky: false, body) = block(above: 0pt, below: 3pt, sticky: sticky)[#set text(size: 9.5pt, ..lh(1.45)); #par(justify: false, hanging-indent: 15.2pt, first-line-indent: 0pt, body)]
#let refsrc(sticky: false, body) = block(above: 0pt, below: 6pt, sticky: sticky)[#set text(size: 9.5pt, ..lh(1.45)); #par(justify: false, first-line-indent: 0pt, body)]

'''
GERMAN_PHRASES = {'lw': ['Zeit der Unkultur. Ludwig Wittgenstein im Österreich der Zwischenkriegszeit']}
for ph in GERMAN_PHRASES.get(doc, []):
    lit_ph = lit(ph)
    hits = sum(b_.count(lit_ph) for b_ in out_blocks)
    assert hits >= 1, ph
    out_blocks = [b_.replace(lit_ph, '#text(lang: "de")[' + lit_ph + ']') for b_ in out_blocks]
if doc == 'psych':   # the footnote section no longer exists
    out_blocks = [s.replace('#" Die Fußnoten erscheinen hier als Anmerkungen am Ende."', '') for s in out_blocks]
    out_blocks = [s.replace(' Die Fußnoten erscheinen hier als Anmerkungen am Ende.', '') for s in out_blocks]
open(out, 'w', encoding='utf-8').write(head + '\n\n'.join(out_blocks) + '\n')
print(out, 'notes:', len(notes), 'blocks:', len(out_blocks))
