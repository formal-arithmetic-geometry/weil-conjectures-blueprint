#!/usr/bin/env python3
"""Check, independently of tex2bp.py, that the blueprint reads as the tex does.

Both sides become a stream of plain words: the tex with its maths, labels,
references and commands removed; the blueprint in the website's document
order (doc.json from dump-doc.mjs), headings' titles and every body.  The two
streams are aligned chapter by chapter.  Reported:

  * text that is in one and not the other, or out of order (diff opcodes);
  * every node whose words sit, in the tex, under other headings than the
    ones the website puts it under.

Usage:
  blueprint build -o snap.json
  node scripts/tex2bp_doc.mjs .lake/packages/blueprint/web/model.js snap.json doc.json
  python3 scripts/tex2bp_check.py <tex> doc.json <first-tex-line> <last-tex-line>

The tex lines are the imported range, from the abstract to the line before the
first chapter not imported.  Expected differences: a part's title (no node),
and the words of the first heading after a part, which the site reads before
the part's text.
"""
import difflib
import json
import re
import sys
import unicodedata

TEX, DOC, FIRST, LAST = sys.argv[1], sys.argv[2], int(sys.argv[3]), int(sys.argv[4])
lines = open(TEX, encoding='utf-8').read().split('\n')

ROMAN = {'iii', 'vii', 'viii', 'xii'}


def words_of(text):
    text = unicodedata.normalize('NFD', text)
    text = ''.join(c for c in text if not unicodedata.combining(c)).lower()
    return [w for w in re.findall(r'[a-z]+', text) if len(w) >= 3 and w not in ROMAN]


# ------------------------------------------------------------------ the tex

def blank(s):
    """Same length, newlines kept: so positions still give line numbers."""
    return re.sub(r'[^\n]', ' ', s)


def tex_plain(src):
    src = '\n'.join(re.sub(r'(?<!\\)%.*', '', ln) for ln in src.split('\n'))
    # maths, every kind
    src = re.sub(r'\\begin\{(equation|align|gather|multline|CD)\*?\}.*?\\end\{\1\*?\}', lambda m: blank(m.group(0)), src, flags=re.S)
    src = re.sub(r'\$\$.*?\$\$|(?<!\\)\\\[.*?\\\]|\\\(.*?\\\)', lambda m: blank(m.group(0)), src, flags=re.S)
    src = re.sub(r'(?<!\\)\$(?:\\.|[^$\\])*\$', lambda m: blank(m.group(0)), src, flags=re.S)
    # what names a place, not prose
    src = re.sub(r'\\(label|ref|eqref|cref|Cref|url)\{[^}]*\}', lambda m: blank(m.group(0)), src)
    src = re.sub(r'\\cite(\[[^\]]*\])?\{[^}]*\}', lambda m: blank(m.group(0)) if not m.group(1) else ' ' * 6 + m.group(1)[1:-1] + blank(m.group(0)[len(m.group(1)) + 6:]), src)
    src = re.sub(r'\\stacks+\{[^}]*\}(\{[^}]*\})*', lambda m: 'Stacks' + blank(m.group(0)[6:]), src)
    src = re.sub(r'\\href\{[^}]*\}', lambda m: blank(m.group(0)), src)
    src = re.sub(r'\\(begin|end)\{[^}]*\}(\[[^\]\n]*\])?', lambda m: blank(m.group(0)), src)
    src = re.sub(r"\\['`\"^~=.vcuH]\{?([A-Za-z])\}?", lambda m: m.group(1).ljust(len(m.group(0))), src)
    src = re.sub(r'\\[A-Za-z]+\*?', lambda m: blank(m.group(0)), src)
    return src


src = '\n'.join(lines)
plain = tex_plain(src)
line_start = [0]
for ln in plain.split('\n'):
    line_start.append(line_start[-1] + len(ln) + 1)


def line_of(pos):
    lo, hi = 0, len(line_start) - 1
    while lo < hi:
        mid = (lo + hi + 1) // 2
        if line_start[mid] <= pos:
            lo = mid
        else:
            hi = mid - 1
    return lo + 1


def tex_accents(t):
    return re.sub(r"\\['`\"^~=.vcuH]\{?([A-Za-z])\}?", r'\1', t)


# the headings of the tex, by line, and what each line is under
HEAD = re.compile(r'\\(part|section|subsection|subsubsection)\*?\{(.*)\}\s*$')
heads_at = {}
cur = []
part_text = False
under = {}
for i, ln in enumerate(lines, 1):
    m = HEAD.match(ln)
    if m:
        level = ['part', 'section', 'subsection', 'subsubsection'].index(m.group(1))
        title = re.sub(r'\\texorpdfstring\{((?:[^{}]|\{[^{}]*\})*)\}\{[^{}]*\}', r'\1', m.group(2))
        if level == 0:
            part_text = True
            cur = []
        else:
            part_text = False
            cur = cur[:level - 1] + [' '.join(words_of(tex_accents(title)))]
        heads_at[i] = (level, title)
    under[i] = ('PART',) if part_text else tuple(cur)

# a part's text is meant to open the chapter after it
next_chapter = None
for i in range(len(lines), 0, -1):
    m = HEAD.match(lines[i - 1])
    if m and m.group(1) == 'section':
        title = re.sub(r'\\texorpdfstring\{((?:[^{}]|\{[^{}]*\})*)\}\{[^{}]*\}', r'\1', m.group(2))
        next_chapter = (' '.join(words_of(tex_accents(title))),)
    if under.get(i) == ('PART',):
        under[i] = next_chapter

tex_words = []          # (word, line)
for m in re.finditer(r'\S+', plain):
    for w in words_of(m.group(0)):
        tex_words.append((w, line_of(m.start())))

# ----------------------------------------------------------- the blueprint

rows = json.load(open(DOC, encoding='utf-8'))
by_id = {r['id']: r for r in rows}
HEADING = {'chapter', 'section', 'subsection'}


def md_plain(body):
    body = re.sub(r'\$\$.*?\$\$|\\\[.*?\\\]', ' ', body, flags=re.S)
    body = re.sub(r'(?<!\\)\$(?:\\.|[^$\\])*\$', ' ', body, flags=re.S)
    body = re.sub(r'\]\([^)]*\)', ']', body)                       # link targets
    body = re.sub(r'\[([A-Za-z0-9][\w.~/-]*)\]', ' ', body)          # [slug]
    body = re.sub(r'\[([A-Za-z0-9][\w.~/-]*), ', '[', body)          # [ref, locator]
    body = re.sub(r'^\*\*Convention\.\*\* ', '', body)
    body = re.sub(r'^#+ Proof\.?$', ' ', body, flags=re.M)
    return body


md_words = []           # (word, row index)
for k, r in enumerate(rows):
    if r['kind'] == 'reference':
        continue
    text = (r['title'] + ' ') if r['kind'] in HEADING else ''
    text += md_plain(r['body'])
    for w in words_of(text):
        md_words.append((w, k))


def heads_of(r):
    return tuple(' '.join(words_of(by_id[h]['title'])) for h in r['heads'])


# ------------------------------------------------------------- alignment

tw = [w for w, _ in tex_words if FIRST <= _ <= LAST]
tl = [l for _, l in tex_words if FIRST <= l <= LAST]
mw = [w for w, _ in md_words]
mk = [k for _, k in md_words]
print(f'tex words {len(tw)}, blueprint words {len(mw)}')
sm = difflib.SequenceMatcher(None, tw, mw, autojunk=False)
ops = sm.get_opcodes()
equal = sum(i2 - i1 for t, i1, i2, j1, j2 in ops if t == 'equal')
print(f'aligned {equal} words ({100 * equal / max(1, len(tw)):.2f}% of the tex)')
print('\n== differences longer than 3 words')
for t, i1, i2, j1, j2 in ops:
    if t == 'equal' or max(i2 - i1, j2 - j1) <= 3:
        continue
    where_t = f'tex {tl[i1]}-{tl[i2 - 1]}' if i2 > i1 else f'tex at {tl[min(i1, len(tl) - 1)]}'
    nodes = sorted({rows[k]['id'] for k in mk[j1:j2]}) if j2 > j1 else [rows[mk[min(j1, len(mk) - 1)]]['id']]
    print(f'{t:8} {where_t:18} tex: {" ".join(tw[i1:i2][:12])!r:60} bp: {" ".join(mw[j1:j2][:12])!r} {nodes[:3]}')

# ------------------------------------------------------------- placement
print('\n== nodes under other headings than in the tex')
lines_of_row = {}
for t, i1, i2, j1, j2 in ops:
    if t != 'equal':
        continue
    for d in range(i2 - i1):
        lines_of_row.setdefault(mk[j1 + d], []).append(tl[i1 + d])
# every 8 words of the tex, where they first start
grams = {}
for i in range(len(tw) - 7):
    grams.setdefault(tuple(tw[i:i + 8]), []).append(tl[i])
located = {}
bad = 0
for k, r in enumerate(rows):
    if r['kind'] in HEADING or r['kind'] == 'reference':
        continue
    # where its text is in the tex: its first eight words, found anywhere
    ws = words_of(md_plain(r['body']))
    at = None
    near = sorted(lines_of_row.get(k, []))
    near = near[len(near) // 2] if near else None
    for s0 in range(0, max(1, len(ws) - 7)):
        hits = grams.get(tuple(ws[s0:s0 + 8]))
        if hits:
            # the same words twice in the tex: the one the alignment chose
            at = min(hits, key=lambda h: abs(h - near)) if near else hits[0]
            break
    if at is None:
        ls = sorted(lines_of_row.get(k, []))
        if not ls:
            if ws:
                print(f'  not found in the tex: {r["id"]}')
            continue
        at = ls[len(ls) // 2]
    located[r['id']] = at
    want = under.get(at)
    got = heads_of(r)
    if r['kind'] == 'proof':
        got = got + ('proof of ' + r['of'],)
        want = want + ('proof of ' + r['of'],)
    if want != got:
        bad += 1
        print(f'  {r["id"]} ({r["kind"]}): its text is at tex line {at}, under {want}; the site puts it under {got}')
print(f'{bad} misplaced')

# reading order: the site's order of nodes against their places in the tex
print('\n== nodes read in another order than in the tex')
seq = [(r['id'], located[r['id']]) for r in rows if r['id'] in located]
worse = 0
for (a, la), (b, lb) in zip(seq, seq[1:]):
    if lb < la:
        worse += 1
        print(f'  {b} (tex line {lb}) is read after {a} (tex line {la})')
print(f'{worse} out of order')

# the headings: same titles, same nesting, same order
print('\n== headings')
tex_heads = [(lvl, ' '.join(words_of(tex_accents(t)))) for i, (lvl, t) in sorted(heads_at.items()) if FIRST <= i <= LAST and lvl > 0]
bp_heads = [(['chapter', 'section', 'subsection'].index(r['kind']) + 1, ' '.join(words_of(r['title']))) for r in rows if r['kind'] in HEADING]
print('same headings in the same order and nesting' if tex_heads == bp_heads else 'HEADINGS DIFFER')
if tex_heads != bp_heads:
    for a, b in zip(tex_heads, bp_heads):
        if a != b:
            print('  tex', a, ' bp', b)
            break
if tex_heads != bp_heads:
    print(f'  {len(tex_heads)} tex headings, {len(bp_heads)} on the site')
    for op in difflib.SequenceMatcher(None, tex_heads, bp_heads, autojunk=False).get_opcodes():
        if op[0] != 'equal':
            print('  ', op[0], tex_heads[op[1]:op[2]], bp_heads[op[3]:op[4]])
