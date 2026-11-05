#!/usr/bin/env python3
"""Import chapters of DerivedCategoryAndSixFunctorsChoice_readable.tex into blueprint/.

Usage: scripts/tex2bp.py <tex> <out-dir> <blueprint.toml> <first-chapter> <last-chapter>

Unnamed declarations take their titles from scripts/tex2bp_titles.py.

Chapters are the tex's \\section's, numbered from 1.  Each \\section is a node
of kind chapter, each \\subsection a section, each \\subsubsection a
subsection, one directory each with its _section.md.  Each theorem-like
environment is a node whose id is its \\label, its proof a separate
<label>.proof.md.  Text outside declarations is a hidden node.
"""
import os
import re
import sys
import tomllib
import unicodedata

TEX, OUT, TOML, FIRST, LAST = sys.argv[1], sys.argv[2], sys.argv[3], int(sys.argv[4]), int(sys.argv[5])

DECL_KIND = {
    'theorem': 'theorem', 'lemma': 'lemma', 'proposition': 'proposition',
    'corollary': 'corollary', 'definition': 'definition', 'remark': 'remark',
    'question': 'question', 'example': 'example',
}
# The kinds a proof may be of (the tool's `proof` kind).
PROVABLE = {'definition', 'theorem', 'proposition', 'lemma', 'corollary', 'remark', 'example'}
# Conventions are text, set as hidden nodes.
HIDDEN_ENVS = {'convention'}

CITE = {
    'Weil49': 'weil49', 'DeligneWeilI': 'deligne74', 'DeligneWeilII': 'deligne80',
    'BBD': 'bbd82', 'Humphreys': 'humphreys72', 'Laumon': 'laumon87', 'BS': 'bhatt-scholze15',
    'Ekedahl': 'ekedahl90', 'SGA4': 'sga4', 'SGA5': 'sga5', 'SGA4half': 'sga4-5',
    'SGA7II': 'sga7-2', 'IllusieNearby': 'illusie94', 'Varshavsky': 'varshavsky05',
    'ConradNagata': 'conrad07', 'MilneAV': 'milne-av', 'MilneJV': 'milne-jv', 'Stacks': 'stacks',
    'Hasse': 'hasse36', 'WeilCourbes': 'weil48-courbes', 'WeilAV': 'weil48-av', 'Deuring': 'deuring41',
    'Deninger': 'deninger22', 'WeilBlueprint': 'weil-blueprint', 'Rankin': 'rankin39',
    'KatzLaumon': 'katz88', 'KiehlWeissauer': 'kiehl-weissauer01',
}

# Titles for declarations the tex leaves unnamed (marked name_showing = false).
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from tex2bp_titles import GENERATED_TITLES, UNLABELLED  # noqa: E402

problems = []


def problem(msg):
    problems.append(msg)


# --------------------------------------------------------------------------- reading

def strip_comments(src):
    out = []
    for line in src.split('\n'):
        m = re.search(r'(?<!\\)%', line)
        if m:
            if not line[:m.start()].strip():
                continue          # a comment line vanishes, newline and all
            line = line[:m.start()]
        out.append(line)
    return '\n'.join(out)


raw = open(TEX, encoding='utf-8').read()
src = strip_comments(raw)
body_start = src.index('\\begin{document}') + len('\\begin{document}')
body_end = src.index('\\end{document}')
BODY = src[body_start:body_end]


def braced(s, i):
    """s[i] == '{': return (content, index after the closing brace)."""
    assert s[i] == '{', (s[i:i + 40])
    depth = 0
    j = i
    while j < len(s):
        c = s[j]
        if c == '\\':
            j += 2
            continue
        if c == '{':
            depth += 1
        elif c == '}':
            depth -= 1
            if depth == 0:
                return s[i + 1:j], j + 1
        j += 1
    raise ValueError('unbalanced braces at ' + s[i:i + 60])


def bracketed(s, i):
    """s[i] == '[': return (content, index after the matching ']'), braces respected."""
    assert s[i] == '['
    depth = 0
    j = i
    while j < len(s):
        c = s[j]
        if c == '\\':
            j += 2
            continue
        if c == '{':
            depth += 1
        elif c == '}':
            depth -= 1
        elif c == ']' and depth == 0:
            return s[i + 1:j], j + 1
        j += 1
    raise ValueError('unbalanced brackets')


def skip_ws(s, i):
    while i < len(s) and s[i] in ' \t\n':
        i += 1
    return i


# --------------------------------------------------------------------------- macros

def tex_macros():
    """The 0-argument \\newcommand's of the preamble."""
    pre = src[:body_start]
    out = {}
    for m in re.finditer(r'\\newcommand\{(\\[A-Za-z]+)\}(\[\d\])?', pre):
        if m.group(2):
            continue
        val, _ = braced(pre, m.end())
        out[m.group(1)] = val
    return out


with open(TOML, 'rb') as fh:
    KATEX = tomllib.load(fh).get('katex', {}).get('macros', {})
EXPAND = {}
for name, val in tex_macros().items():
    if KATEX.get(name, '').replace(' ', '') != val.replace(' ', ''):
        EXPAND[name] = val


def expand_macros(math):
    for _ in range(3):
        before = math
        for name, val in EXPAND.items():
            math = re.sub(re.escape(name) + r'(?![A-Za-z])\s*(?=([A-Za-z])?)',
                          lambda m: (' ' if val[:1].isalpha() and re.search(r'\\[A-Za-z]+$', m.string[:m.start()]) else '')
                          + val + (' ' if m.group(1) and re.search(r'(\\[A-Za-z]+|[A-Za-z])$', val) else ''),
                          math)
        if math == before:
            break
    return math


# --------------------------------------------------------------------------- ids

ACCENTS = {"'": '\u0301', '`': '\u0300', '"': '\u0308', '^': '\u0302', '~': '\u0303',
           'v': '\u030c', 'c': '\u0327', 'u': '\u0306', '=': '\u0304', 'H': '\u030b'}


def accents(s):
    def rep(m):
        acc, letter = m.group(1), m.group(2) or m.group(3)
        if letter == '\\i':
            letter = 'i'
        return unicodedata.normalize('NFC', letter + ACCENTS[acc])
    s = re.sub(r"\\([`'\"^~=])\s*(?:\{(\\i|[A-Za-z])\}|([A-Za-z]))", rep, s)
    s = re.sub(r"\\([vcuH])(?:\{(\\i|[A-Za-z])\}|\s+([A-Za-z]))", rep, s)
    s = s.replace('\\ss{}', 'ß').replace('\\o{}', 'ø')
    return s


def heading_title(t):
    t = re.sub(r'\\texorpdfstring\{((?:[^{}]|\{[^{}]*\})*)\}\{[^{}]*\}', r'\1', t)
    t = accents(t)
    t = t.replace('---', '—').replace('--', '–').replace('~', ' ')
    return t.strip()


def heading_slug(t):
    t = re.sub(r'\\texorpdfstring\{(?:[^{}]|\{[^{}]*\})*\}\{([^{}]*)\}', r'\1', t)
    t = accents(t).replace('ℓ', 'ell').replace('--', '-')
    t = unicodedata.normalize('NFKD', t)
    t = ''.join(c for c in t if not unicodedata.combining(c))
    t = re.sub(r"[^A-Za-z0-9\s-]", '', t)
    return re.sub(r'[\s-]+', '-', t.strip()).strip('-')


PREFIX = {'section': 'chap', 'subsection': 'sec', 'subsubsection': 'subsec'}
KIND = {'section': 'chapter', 'subsection': 'section', 'subsubsection': 'subsection'}
ROMAN = ['I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII']

# --------------------------------------------------------------------------- pass 1: labels

HEAD_RE = re.compile(r'\\(part|section|subsection|subsubsection)\*?\{')
HEADING_IDS = []    # in document order, ids made unique by a suffix
LABEL = {}          # tex label -> ('node', id) | ('eq', '2.3') | ('part', 'I')
APPENDIX_CHAPTERS = set()   # the ids of the \\section's after \\appendix
EQ_ENVS = {'equation', 'align', 'gather', 'multline'}


def pass1():
    sec = 0
    appendix = False
    part = 0
    eq = 0
    ids = {}
    pos = 0
    tokens = re.compile(r'\\(part|section|subsection|subsubsection)\*?\{|\\appendix\b|'
                        r'\\begin\{(equation|align|gather|multline)\}|\\label\{([^}]*)\}|'
                        r'\\begin\{(' + '|'.join(list(DECL_KIND) + list(HIDDEN_ENVS)) + r')\}')
    pending = None      # what the next \label names
    current = None      # the innermost heading
    for m in tokens.finditer(BODY):
        if m.group(1):
            kind = m.group(1)
            title, end = braced(BODY, m.end() - 1)
            if kind == 'part':
                part += 1
                pending = ('part', ROMAN[part - 1])
                continue
            if kind == 'section':
                sec += 1
                eq = 0
            hid = PREFIX[kind] + '-' + heading_slug(title)
            k = 2
            while hid + ('' if k == 2 else f'-{k - 1}') in ids:
                k += 1
            hid = hid + ('' if k == 2 else f'-{k - 1}')
            ids[hid] = title
            HEADING_IDS.append(hid)
            if kind == 'section' and appendix:
                APPENDIX_CHAPTERS.add(hid)
            pending = ('node', hid)
            current = hid
        elif m.group(0) == '\\appendix':
            appendix = True
            sec = 0
        elif m.group(2):
            env = m.group(2)
            content_end = BODY.index('\\end{' + env + '}', m.end())
            content = BODY[m.end():content_end]
            secno = chr(ord('A') + sec - 1) if appendix else str(sec)
            if env == 'equation':
                tag = re.search(r'\\tag\{((?:[^{}]|\{[^{}]*\})*)\}', content)
                if not tag:
                    eq += 1     # an equation with a \tag of its own is not numbered
                for lm in re.finditer(r'\\label\{([^}]*)\}', content):
                    LABEL[lm.group(1)] = ('eq', tag.group(1) if tag else f'{secno}.{eq}')
            else:
                for line in re.split(r'\\\\', content):
                    if re.search(r'\\(nonumber|notag|tag)\b', line):
                        continue
                    eq += 1
                    for lm in re.finditer(r'\\label\{([^}]*)\}', line):
                        LABEL[lm.group(1)] = ('eq', f'{secno}.{eq}')
            pending = None
        elif m.group(3) is not None:
            lab = m.group(3)
            if lab in LABEL:
                continue                     # an equation's, done above
            if pending is None:
                # a label standing in the text names the heading it is under
                LABEL[lab] = ('node', current)
                continue
            LABEL[lab] = pending if pending[0] != 'decl' else ('node', lab)
            if pending[0] == 'decl':
                pending = None   # several labels after a heading all name it
        elif m.group(4):
            pending = ('decl', None)


pass1()


def secnum_of_appendix(n):
    return n


# --------------------------------------------------------------------------- prose

class Shield:
    def __init__(self):
        self.store = []

    def put(self, text):
        self.store.append(text)
        return f'\x00{len(self.store) - 1}\x00'

    def restore(self, s):
        for _ in range(4):
            s = re.sub(r'\x00(\d+)\x00', lambda m: self.store[int(m.group(1))], s)
        return s


def ref_text(lab):
    t = LABEL.get(lab)
    if t is None:
        problem(f'\\ref to unknown label {lab}')
        return lab
    if t[0] == 'node':
        return f'[{t[1]}]'
    if t[0] == 'eq':
        return f'({t[1]})'
    if t[0] == 'part':
        return t[1]
    raise AssertionError


def math_ref(lab):
    t = LABEL.get(lab)
    if t is None:
        problem(f'\\ref to unknown label {lab} inside maths')
        return lab
    if t[0] == 'node':
        return f'\x04{t[1]}\x04'
    return t[1]


def convert_math(m, display, eqno=None):
    m = expand_macros(m)
    # KaTeX has no \lhook: the long hooked arrow is its \hookrightarrow
    m = re.sub(r'\\lhook\s*\\joinrel\s*\\(?:long)?rightarrow', r'\\hookrightarrow', m)
    # nor \ensuremath: maths inside a tag's text is written $…$
    m = re.sub(r'\\ensuremath\{([^{}]*)\}', r'$\1$', m)
    m = re.sub(r'\\label\{[^}]*\}\s*', '', m)
    # Maths cannot hold a link: an equation is its number, a statement or a
    # section the number the website gives it, filled in once every file is
    # written (`number_math_refs`).
    m = re.sub(r'\\eqref\{([^}]*)\}', lambda x: ref_text(x.group(1)).replace('[', '').replace(']', ''), m)
    m = re.sub(r'\\ref\{([^}]*)\}', lambda x: math_ref(x.group(1)), m)
    if re.search(r'\\cite\b', m):
        problem('citation inside maths: ' + m[:80])
    m = re.sub(r"\\'\s*e", r"\\acute{e}", m) if not re.search(r'\\text', m) else m
    if display:
        lines = [ln.strip() for ln in m.strip().split('\n')]
        inner = '\n'.join(ln for ln in lines if ln)
        if eqno:
            inner += f'\n\\tag{{{eqno}}}'
        return '$$\n' + inner + '\n$$'
    return '$' + m.strip() + '$' if m.strip() == m else '$' + m.strip() + '$'


def shield_math(s, sh):
    """Replace the maths of `s` by placeholders. Display maths keeps a marker
    so that lists and paragraphs can set it on lines of its own."""
    out = []
    i = 0
    n = len(s)
    while i < n:
        c = s[i]
        if s.startswith('\\begin{', i):
            env = re.match(r'\\begin\{([a-zA-Z*]+)\}', s[i:]).group(1)
            if env in ('equation', 'equation*', 'align', 'align*', 'gather', 'gather*', 'multline'):
                end = s.index('\\end{' + env + '}', i)
                content = s[i + len(env) + 8:end]
                eqno = None
                if env == 'equation':
                    lab = re.search(r'\\label\{([^}]*)\}', content)
                    if re.search(r'\\tag\b', content):
                        pass                     # its own tag, kept
                    elif lab:
                        eqno = LABEL[lab.group(1)][1]
                    else:
                        problem('unlabelled numbered equation: ' + content[:60])
                elif not env.endswith('*'):
                    rows = re.split(r'(\\\\)', content)
                    for r in range(0, len(rows), 2):
                        if re.search(r'\\(nonumber|notag|tag)\b', rows[r]):
                            continue
                        lab = re.search(r'\\label\{([^}]*)\}', rows[r])
                        if lab:
                            rows[r] = rows[r] + f'\\tag{{{LABEL[lab.group(1)][1]}}}'
                        else:
                            problem(f'numbered {env} line without a label: tag not written')
                    content = ''.join(rows)
                if env == 'align':
                    # KaTeX takes a tag per row in `align`, not in `aligned`
                    content = '\\begin{align}' + content + '\\end{align}'
                elif env.startswith('align'):
                    content = '\\begin{aligned}' + content + '\\end{aligned}'
                elif env.startswith('gather'):
                    content = '\\begin{gathered}' + content + '\\end{gathered}'
                out.append('\x01' + sh.put(convert_math(content, True, eqno)) + '\x01')
                i = end + len(env) + 6
                continue
        if s.startswith('\\[', i):
            end = s.index('\\]', i)
            out.append('\x01' + sh.put(convert_math(s[i + 2:end], True)) + '\x01')
            i = end + 2
            continue
        if s.startswith('$$', i):
            end = s.index('$$', i + 2)
            out.append('\x01' + sh.put(convert_math(s[i + 2:end], True)) + '\x01')
            i = end + 2
            continue
        if s.startswith('\\(', i):
            end = s.index('\\)', i)
            out.append(sh.put(convert_math(s[i + 2:end], False)))
            i = end + 2
            continue
        if c == '\\' and i + 1 < n:
            out.append(s[i:i + 2])
            i += 2
            continue
        if c == '$':
            j = i + 1
            while j < n and s[j] != '$':
                j += 2 if s[j] == '\\' else 1
            out.append(sh.put(convert_math(s[i + 1:j], False)))
            i = j + 1
            continue
        out.append(c)
        i += 1
    return ''.join(out)


def replace_cmd(s, name, fn, nargs=1, opt=False):
    """Replace \\name[opt]{a}{b}... by fn(opt, a, b, ...), innermost first."""
    pat = re.compile(r'\\' + name + r'(?![A-Za-z])\s*')
    while True:
        m = None
        for cand in pat.finditer(s):
            m = cand            # the last one: inner commands come later in the text
        if not m:
            return s
        i = m.end()
        o = None
        if opt and i < len(s) and s[i] == '[':
            o, i = bracketed(s, i)
        args = []
        for _ in range(nargs):
            i = skip_ws(s, i)
            if i < len(s) and s[i] == '{':
                a, i = braced(s, i)
            else:                # a single token argument
                a, i = s[i], i + 1
            args.append(a)
        s = s[:m.start()] + fn(o, *args) + s[i:]


# The tex is an article: its \\section is a chapter of the blueprint (an
# appendix after \\appendix), its \\subsection a section and its
# \\subsubsection a subsection.  The prose names them by the tex's words, which
# are moved up a level here.
IN_APPENDIX = False     # whether the text converted is in an appendix chapter
ID_RE = r'\[((?:chap|sec|subsec)-[^\]\s]+)\]'
NAMED_RE = re.compile(r'\b((?:[Ss]ub)?[Ss]ections?|[Cc]hapters?|[Aa]ppendix|[Aa]ppendices)(\s+)'
                      rf'({ID_RE}(?:\s*(?:–|,|, and|and|or)\s*{ID_RE})*)')
# "this section" of a sheaf is not one of these
HERE_RE = re.compile(r'\b(?:(?:[Tt]hroughout|[Ii]n|(?<!extension )of|[Tt]o|[Aa]t|[Ff]rom|[Bb]y)\s+(?:this|that)'
                     r'|(?<![A-Za-z] )This'
                     r'|(?:start|beginning|end|opening|rest)\s+of\s+the'
                     r'|the\s+(?:next|previous|preceding|following|last|later)(?:\s+(?:two|three|four))?'
                     r'|this\s+(?=sub))'
                     r'\s+((?:sub)*sections?)\b'
                     r'|\bthe\s+((?:sub)*section)\s+opening\b')


def structure_word(level, plural, upper, appendix):
    """The blueprint's word for a heading: `level` 0 is a chapter (an appendix
    if `appendix`), 1 a section, 2 a subsection."""
    w = ['appendix' if appendix else 'chapter', 'section', 'subsection'][level]
    if plural:
        w = 'appendices' if w == 'appendix' else w + 's'
    return w[0].upper() + w[1:] if upper else w


def structure_words(s):
    """The word before a reference to a heading names that heading's kind, and
    "this section", "the next subsection", ... are a level up from the tex's."""
    def named(m):
        ids = re.findall(ID_RE, m.group(3))
        kinds = {(i.split('-')[0], i in APPENDIX_CHAPTERS) for i in ids}
        if len(kinds) != 1:
            problem(f'one word for headings of different kinds: {m.group(0)}')
            return m.group(0)
        prefix, appendix = kinds.pop()
        w = m.group(1)
        new = structure_word(['chap', 'sec', 'subsec'].index(prefix),
                             w.lower() in ('sections', 'subsections', 'chapters', 'appendices'),
                             w[0].isupper(), appendix)
        return new + m.group(2) + m.group(3)

    def here(m):
        g = 1 if m.group(1) else 2
        w = m.group(g)
        new = structure_word(w.count('sub'), w.endswith('s'), False, IN_APPENDIX)
        return m.group(0)[:m.start(g) - m.start()] + new + m.group(0)[m.end(g) - m.start():]
    s = NAMED_RE.sub(named, s)
    return HERE_RE.sub(here, s)


def stacks_link(tag):
    return f'[{tag}](https://stacks.math.columbia.edu/tag/{tag})'


def inline(s, sh):
    """Prose commands to Markdown; `s` has its maths shielded."""
    s = accents(s)
    # references
    s = re.sub(r'\\S\\S\s*~?\s*\\ref\{([^}]*)\}', lambda m: 'Sections ' + ref_text(m.group(1)), s)
    s = re.sub(r'\\S\s*~?\s*\\ref\{([^}]*)\}', lambda m: 'Section ' + ref_text(m.group(1)), s)
    s = re.sub(r'\\(?:eqref)\{([^}]*)\}', lambda m: ref_text(m.group(1)), s)
    s = re.sub(r'\\(?:ref|cref|Cref|autoref)\{([^}]*)\}', lambda m: ref_text(m.group(1)), s)

    def cite(o, keys):
        ids = []
        for k in keys.split(','):
            k = k.strip()
            if k not in CITE:
                problem('unknown citation ' + k)
            ids.append(CITE.get(k, k))
        if o is not None:
            if len(ids) != 1:
                problem('locator on several citations')
            return sh.put(f'[{ids[0]}, {inline(o, sh)}]')
        return ', '.join(sh.put(f'[{i}]') for i in ids)
    s = replace_cmd(s, 'cite', cite, 1, opt=True)
    s = replace_cmd(s, 'stacks', lambda o, t: sh.put('[Stacks, ' + stacks_link(t) + ']'), 1)
    s = replace_cmd(s, 'stackss', lambda o, a, b: sh.put('[Stacks, ' + stacks_link(a) + ', ' + stacks_link(b) + ']'), 2)
    s = replace_cmd(s, 'stacksss', lambda o, a, b, c: sh.put('[Stacks, ' + ', '.join(map(stacks_link, (a, b, c))) + ']'), 3)
    s = replace_cmd(s, 'href', lambda o, u, t: sh.put(f'[{t}]({u})'), 2)
    s = replace_cmd(s, 'url', lambda o, u: sh.put(f'<{u}>'), 1)
    # fonts
    s = replace_cmd(s, 'emph', lambda o, a: f'*{a.strip()}*')
    s = replace_cmd(s, 'textit', lambda o, a: f'*{a.strip()}*')
    s = replace_cmd(s, 'textbf', lambda o, a: f'**{a.strip()}**')
    for c in ('textnormal', 'textrm', 'text', 'mbox', 'textsf', 'textsc'):
        s = replace_cmd(s, c, lambda o, a: a)
    s = replace_cmd(s, 'footnote', lambda o, a: f' ({a.strip()})')
    s = re.sub(r'\\paragraph\*?\s*\{([^{}]*)\}\s*', lambda m: f'**{m.group(1).strip()}** ', s)
    s = re.sub(r'\\label\{[^}]*\}\s*', '', s)
    s = re.sub(r'\\addcontentsline\{[^}]*\}\{[^}]*\}\{[^}]*\}\s*', '', s)
    s = replace_cmd(s, 'texorpdfstring', lambda o, a, b: a, 2)
    # spacing and the rest
    s = re.sub(r'\\(leavevmode|noindent|medskip|smallskip|bigskip|hfill|centering|small|footnotesize|clearpage|newpage|phantomsection)\b\s*', '', s)
    s = re.sub(r'\\par\b\s*', '\n\n', s)
    s = s.replace('\\S', '§')
    s = re.sub(r'\\ldots\b|\\dots\b', '...', s)
    s = s.replace('---', '—').replace('--', '–')
    s = s.replace('``', '“').replace("''", '”')
    s = re.sub(r'(?<!\\)~', ' ', s)
    s = re.sub(r'\\[,;!]', '', s)
    s = structure_words(s)
    s = s.replace('\\ ', ' ').replace('\\@', '')
    for a, b in (('\\%', '%'), ('\\&', '&'), ('\\_', '\\_'), ('\\#', '#'), ('\\$', '\\$'), ('\\{', '{'), ('\\}', '}')):
        s = s.replace(a, b)
    s = re.sub(r'(?<![\\{]){}', '', s)
    left = re.findall(r'\\[A-Za-z]+', s)
    for c in left:
        problem('command left in prose: ' + c)
    return s


def enumerate_template(opt):
    """The `label=` of an enumerate's options, or None."""
    m = re.search(r'label\s*=\s*', opt)
    if not m:
        problem('enumerate option ' + opt)
        return None
    depth, i = 0, m.end()
    for j in range(m.end(), len(opt)):
        c = opt[j]
        if c == '{':
            depth += 1
        elif c == '}':
            depth -= 1
        elif c == ',' and depth == 0:
            return opt[i:j].strip()
    return opt[i:].strip()


def item_label(template, n):
    roman = ['i', 'ii', 'iii', 'iv', 'v', 'vi', 'vii', 'viii', 'ix', 'x', 'xi', 'xii']
    out = (template.replace('\\arabic*', str(n)).replace('\\alph*', chr(ord('a') + n - 1))
           .replace('\\Alph*', chr(ord('A') + n - 1)).replace('\\roman*', roman[n - 1])
           .replace('\\Roman*', roman[n - 1].upper()))
    if '*' in out:
        problem('enumerate label ' + template)
    return out


def convert_table(content, sh):
    content = re.sub(r'\\(toprule|midrule|bottomrule|hline)\b', '', content)
    rows = [r.strip() for r in re.split(r'\\\\', content) if r.strip()]
    cells = [[inline(c.strip(), sh).replace('\n', ' ') for c in r.split('&')] for r in rows]
    width = max(len(r) for r in cells)
    lines = ['| ' + ' | '.join(cells[0]) + ' |', '|' + (sh.put('---') + '|') * width]
    for r in cells[1:]:
        lines.append('| ' + ' | '.join(r) + ' |')
    return '\n\n' + '\n'.join(lines) + '\n\n'


def environments(s, sh):
    """Lists, tables, centre and quote, innermost first."""
    pat = re.compile(r'\\begin\{(itemize|enumerate|center|tabular|quote)\}')
    while True:
        ms = list(pat.finditer(s))
        # the innermost: a begin with no begin of the same family before its end
        target = None
        for m in ms:
            env = m.group(1)
            end = s.index('\\end{' + env + '}', m.end())
            if not pat.search(s, m.end(), end):
                target = (m, env, end)
                break
        if not target:
            return s
        m, env, end = target
        content = s[m.end():end]
        after = end + len('\\end{' + env + '}')
        if env == 'tabular':
            _, k = braced(content, 0)          # the column specification
            rep = convert_table(content[k:], sh)
        elif env == 'center':
            rep = '\n\n' + content.strip() + '\n\n'
        elif env == 'quote':
            rep = '\n\n' + '\n'.join('> ' + ln for ln in content.strip().split('\n')) + '\n\n'
        else:
            opt = None
            c = content
            if c.startswith('['):
                opt, k = bracketed(c, 0)
                c = c[k:]
            items = re.split(r'\\item\b\s*', c)
            if items[0].strip():
                problem('text before first \\item: ' + items[0][:60])
            items = items[1:]
            out = []
            for k, it in enumerate(items):
                label = None
                if it.startswith('['):
                    label, j = bracketed(it, 0)
                    it = it[j:]
                template = enumerate_template(sh.restore(opt)) if opt else None
                if env == 'itemize':
                    marker = '- '
                    lead = '' if label is None else label + ' '
                elif template and template != r'\arabic*.':
                    # the label as the tex sets it, "(a)", "(ii)", "$(C_{3})$"
                    marker = '- '
                    lead = sh.put(item_label(template, k + 1)) + ' '
                else:
                    marker = f'{k + 1}. '
                    lead = ''
                pad = ' ' * len(marker)
                text = it.strip()
                # an item is one block: blank lines inside become single newlines
                text = re.sub(r'\n\s*\n', '\n', text)
                text = text.replace('\x01', '\n')
                lines = [ln.strip() for ln in text.split('\n') if ln.strip()]
                block = marker + lead + lines[0] + ''.join('\n' + pad + ln for ln in lines[1:])
                out.append(block)
            rep = '\n\n' + '\n'.join(out) + '\n\n'
            rep = rep.replace('\x02', '\n')
        s = s[:m.start()] + rep.replace('\n', '\x02') + s[after:]


def to_markdown(tex):
    sh = Shield()
    # a source line that Markdown would read as a list item or a heading
    tex = re.sub(r'\n[ \t]*(?=(?:\d+\.|[-+*#>])[ \t])', ' ', tex)
    s = shield_math(tex, sh)
    s = environments(s, sh)
    s = s.replace('\x02', '\n')
    s = inline(s, sh)
    # display maths on lines of its own, as a block between paragraphs
    s = re.sub(r'[ \t]*\x01(\x00\d+\x00)\x01[ \t]*', lambda m: '\n\n' + m.group(1) + '\n\n', s)
    lines = [ln.rstrip() for ln in s.split('\n')]
    out = []
    in_list = False
    for ln in lines:
        stripped = ln.strip()
        if re.match(r'(\d+\. |- )', ln):
            in_list = True
        elif not stripped:
            pass
        elif not ln.startswith(' '):
            in_list = False
        if in_list and ln.startswith(' '):
            out.append(ln)                       # an item's continuation
        else:
            out.append(stripped)
    s = '\n'.join(out)
    # inside a list item display maths stays in the item, without blank lines
    s = re.sub(r'\n\n( +)(\x00\d+\x00)\n\n', lambda m: '\n' + m.group(1) + m.group(2) + '\n', s)
    s = re.sub(r'\n{3,}', '\n\n', s).strip()
    s = sh.restore(s)
    # indent the lines of display maths inside list items
    s = fix_list_math(s)
    return s


def fix_list_math(s):
    out = []
    pad = None
    inside = False
    for ln in s.split('\n'):
        m = re.match(r'(\d+\. |- )', ln)
        if m:
            pad = ' ' * len(m.group(1))
        elif not ln.strip():
            pad = None
        if ln.lstrip() == '$$' and pad is not None:
            inside = not inside
            out.append(pad + '$$')
            continue
        if inside and pad is not None:
            out.append(pad + ln.strip())
            continue
        out.append(ln)
    return '\n'.join(out)


# --------------------------------------------------------------------------- pass 2: nodes

def toml_str(s):
    return '"' + s.replace('\\', '\\\\').replace('"', '\\"') + '"'


def write(path, front, body):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    lines = ['+++']
    for k, v in front:
        if isinstance(v, bool):
            lines.append(f'{k} = {"true" if v else "false"}')
        elif isinstance(v, int):
            lines.append(f'{k} = {v}')
        else:
            lines.append(f'{k} = {toml_str(v)}')
    lines.append('+++')
    text = '\n'.join(lines) + '\n' + (body.strip() + '\n' if body.strip() else '')
    with open(path, 'w', encoding='utf-8') as fh:
        fh.write(text)
    written.append(path)


written = []
order = 0


def next_order():
    global order
    order += 1
    return order


def chapter_spans():
    """(start, end) of each \\section in BODY, and the text before the first."""
    starts = [m.start() for m in re.finditer(r'\\section\*?\{', BODY)]
    ends = starts[1:] + [len(BODY)]
    return list(zip(starts, ends))


def run():
    spans = chapter_spans()
    a = spans[FIRST - 1][0]
    b = spans[LAST - 1][1]
    region = BODY[a:b]
    global REGION_START
    REGION_START = a
    # stop at the appendix, a part or the bibliography that ends the last chapter
    pre = BODY[:a]
    if FIRST == 1:
        abs_m = re.search(r'\\begin\{abstract\}(.*?)\\end\{abstract\}', pre, re.S)
        if abs_m:
            write(os.path.join(OUT, 'prose-00-01.md'),
                  [('id', 'prose-00-01'), ('kind', 'hidden'), ('title', 'Abstract'), ('order', next_order())],
                  to_markdown(abs_m.group(1)))
    walk(region, FIRST)


TOKEN = re.compile(r'\\(part|section|subsection|subsubsection)\*?\{|'
                   r'\\begin\{(' + '|'.join(list(DECL_KIND) + list(HIDDEN_ENVS) + ['proof']) + r')\}|'
                   r'\\begin\{thebibliography\}|\\appendix\b')


def heading_index(pos_in_region):
    return sum(1 for _ in re.finditer(r'\\(section|subsection|subsubsection)\*?\{', BODY[:REGION_START + pos_in_region]))


def walk(region, chapno):
    global IN_APPENDIX
    chapno -= 1
    path = []                 # [(level, id, title, dir)]
    prose_count = {}
    part_no = sum(1 for _ in re.finditer(r'\\part\{', BODY[:BODY.index(region)]))
    in_part = None            # the part whose opening text we are in
    appendix_no = None        # after \appendix: the number of the appendix chapter
    pos = 0
    last_decl = None
    decl_dir = {}             # statement id -> the directory it is written in
    decl_kind = {}
    proof_count = {}

    def here_dir():
        return path[-1][3] if path else OUT

    def flush(text, nxt):
        nonlocal in_part, appendix_no
        if not text.strip():
            return
        if in_part:
            key = 'PA' if appendix_no is not None else 'P' + str(in_part)
            title = in_part_title
        else:
            # appendix chapters are lettered, as in the tex
            key = chr(ord('A') + appendix_no - 1) if appendix_no else f'{chapno:02d}'
            title = path[-1][2] if path else 'Text'
        n = prose_count.get(key, 0) + 1
        prose_count[key] = n
        pid = f'prose-{key}-{n:02d}'
        # A part's opening text introduces the chapters after it: it opens
        # the next chapter, on that chapter's page, before the chapter's own
        # opening lines.  It is read in tex order, so its `order` is already
        # the chapter's first.
        if in_part:
            if not (nxt and nxt.group(1) == 'section'):
                problem(f'the text of part {in_part} is followed by no chapter')
                where = OUT
            else:
                where = os.path.join(OUT, HEADING_IDS[heading_index(nxt.start())])
        else:
            where = here_dir()
        write(os.path.join(where, pid + '.md'),
              [('id', pid), ('kind', 'hidden'), ('title', title + ' \x03'), ('order', next_order())],
              to_markdown(text))

    in_part_title = None
    while True:
        m = TOKEN.search(region, pos)
        text = region[pos:m.start()] if m else region[pos:]
        flush(text, m)
        if not m:
            break
        if m.group(0).startswith('\\begin{thebibliography}'):
            break
        if m.group(0) == '\\appendix':
            appendix_no = 0
            IN_APPENDIX = True
            pos = m.end()
            continue
        if m.group(1):
            kind = m.group(1)
            title_tex, end = braced(region, m.end() - 1)
            lab = re.match(r'\s*\\label\{([^}]*)\}', region[end:])
            if lab:
                end += lab.end()
                more = re.match(r'(\s*\\label\{[^}]*\})+', region[end:])
                if more:
                    end += more.end()
            pos = end
            if kind == 'part':
                part_no += 1
                in_part = part_no
                in_part_title = heading_title(title_tex)
                continue
            in_part = None
            if kind == 'section':
                chapno += 1
                if appendix_no is not None:
                    appendix_no += 1
            level = ['section', 'subsection', 'subsubsection'].index(kind)
            path[:] = path[:level]
            hid = HEADING_IDS[heading_index(m.start())]
            if lab and LABEL.get(lab.group(1)) != ('node', hid):
                problem(f'label {lab.group(1)} maps to {LABEL.get(lab.group(1))}, heading is {hid}')
            d = os.path.join(here_dir(), hid)
            title = heading_title(title_tex)
            path.append((level, hid, title, d))
            last_decl = None
            write(os.path.join(d, '_section.md'),
                  [('id', hid), ('kind', KIND[kind]), ('title', title), ('order', next_order())], '')
            continue
        env = m.group(2)
        i = m.end()
        opt = None
        if i < len(region) and region[i] == '[':
            opt, i = bracketed(region, i)
        end = region.index('\\end{' + env + '}', i)
        content = region[i:end]
        pos = end + len('\\end{' + env + '}')
        lab = re.match(r'\s*\\label\{([^}]*)\}', content)
        if lab:
            content = content[lab.end():]
        if env == 'proof':
            # "Proof of Theorem~\ref{x}" proves x wherever it stands; any
            # other proof proves the statement before it, even with text
            # between them, which is a hidden node of its own.
            named = re.search(r'\\ref\{([^}]*)\}', opt or '')
            title = None
            if named:
                t = LABEL.get(named.group(1))
                did = t[1] if t and t[0] == 'node' else None
                if did not in decl_dir:
                    problem(f'a proof of {named.group(1)}, which is not imported: ' + content[:80])
                    continue
            elif last_decl is not None:
                did = last_decl[0]
                title = heading_title(opt) if opt else None
            else:
                problem('a proof after no statement: ' + content[:80])
                continue
            if decl_kind[did] not in PROVABLE:
                problem(f'a proof of the {decl_kind[did]} {did}, which a proof cannot be of')
                continue
            n = proof_count.get(did, 0) + 1
            proof_count[did] = n
            front = [('kind', 'proof'), ('of', did)]
            if n > 1:
                front.insert(0, ('id', f'proof/{did}/{n}'))
            if title:
                front.append(('title', title))
            # A proof is read where the tex has it: in the section it stands
            # in, at its place among that section's entries, so text between
            # a statement and its proof, or a proof given sections later
            # ("Proof of Theorem~\ref{x}"), reads as in the tex.
            front.append(('order', next_order()))
            name = did + ('.proof.md' if n == 1 else f'.proof-{n}.md')
            write(os.path.join(here_dir(), name), front, to_markdown(content))
            last_decl = None
            continue
        if lab:
            did = lab.group(1)
        else:
            key = next((k for k in UNLABELLED if content.strip().startswith(k)), None)
            if key is None:
                problem(f'{env} without a label: {content.strip()[:300]}')
                continue
            did, gen_title = UNLABELLED[key]
            GENERATED_TITLES[did] = gen_title
        if env in HIDDEN_ENVS:
            title = heading_title(opt) if opt else env.capitalize()
            write(os.path.join(here_dir(), did + '.md'),
                  [('id', did), ('kind', 'hidden'), ('title', title), ('order', next_order())],
                  f'**{env.capitalize()}{" (" + inline(heading_title(opt), Shield()) + ")" if opt else ""}.** ' + to_markdown(content))
            last_decl = None
            continue
        front = [('id', did), ('kind', DECL_KIND[env])]
        if opt:
            front.append(('title', heading_title(opt)))
        else:
            gen = GENERATED_TITLES.get(did)
            if gen is None:
                problem(f'no title for unnamed {env} {did}: {content.strip()[:300]}')
                gen = did
            front.append(('title', gen))
            front.append(('name_showing', False))
        front.append(('order', next_order()))
        write(os.path.join(here_dir(), did + '.md'), front, to_markdown(content))
        decl_dir[did] = here_dir()
        decl_kind[did] = DECL_KIND[env]
        last_decl = (did, pos)


run()

# "(k)" on the titles of headings with several prose nodes
by_title = {}
for p in written:
    t = open(p, encoding='utf-8').read()
    m = re.search(r'^title = "(.*) \x03"$', t, re.M)
    if m:
        by_title.setdefault((os.path.dirname(p), m.group(1)), []).append(p)
for (d, title), paths in by_title.items():
    paths.sort(key=lambda p: int(re.search(r'^order = (\d+)', open(p, encoding='utf-8').read(), re.M).group(1)))
    for k, p in enumerate(paths, 1):
        t = open(p, encoding='utf-8').read()
        new = title if len(paths) == 1 else f'{title} ({k})'
        t = t.replace(f'title = "{title} \x03"', f'title = "{new}"', 1)
        open(p, 'w', encoding='utf-8').write(t)

def number_math_refs():
    """The website's number of every node written (as `documentOutline`
    numbers them: chapters, sections and statements, counted per parent in
    `order`, text and proofs left out), put in place of the references inside
    maths."""
    nodes = {}
    for p in written:
        t = open(p, encoding='utf-8').read()
        front = t.split('+++')[1]
        kind = re.search(r'^kind = "([^"]*)"', front, re.M).group(1)
        idm = re.search(r'^id = "([^"]*)"', front, re.M)
        orderm = re.search(r'^order = (\d+)', front, re.M)
        if kind in ('hidden', 'proof') or not idm:
            continue
        d = os.path.dirname(p)
        parent = os.path.dirname(d) if p.endswith('_section.md') else d
        nodes[idm.group(1)] = (parent, int(orderm.group(1)), d if p.endswith('_section.md') else None)
    dir_id = {v[2]: k for k, v in nodes.items() if v[2]}
    kids = {}
    for nid, (parent, o, _) in nodes.items():
        kids.setdefault(dir_id.get(parent), []).append((o, nid))
    number = {}

    def walk_numbers(pid, prefix):
        for k, (_, nid) in enumerate(sorted(kids.get(pid, [])), 1):
            number[nid] = f'{prefix}{k}'
            walk_numbers(nid, number[nid] + '.')
    walk_numbers(None, '')
    for p in written:
        t = open(p, encoding='utf-8').read()
        if '\x04' not in t:
            continue
        def num(m):
            if m.group(1) not in number:
                problem(f'a reference inside maths to {m.group(1)}, which is not imported')
                return m.group(1)
            return number[m.group(1)]
        open(p, 'w', encoding='utf-8').write(re.sub('\x04([^\x04]*)\x04', num, t))


number_math_refs()

print(f'{len(written)} files written, last order {order}')
for p in problems:
    print('PROBLEM', p)
