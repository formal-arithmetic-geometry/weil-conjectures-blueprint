#!/usr/bin/env python3
"""Put the refinement of one chapter of blueprint-layer-2.tex under the sketch nodes of blueprint/.

Usage: scripts/layer2bp.py <layer-2 tex> <blueprint dir> <blueprint.toml> <chapter>

blueprint-layer-2.tex refines DerivedCategoryAndSixFunctorsChoice_readable.tex:
each declaration of the notes (a "reference block", \\BPSource ... \\BPEndSource)
is split into clauses, theorem-like environments bp<kind> labelled bp-r<NNN>-<k>.
The declaration is a sketch node of blueprint/ (the block's \\label is its id);
its clauses become detail nodes under it:

- the sketch node <id>.md moves to <id>/_section.md, a directory of its own;
- clause k is <id>/<id>--<k>.md, of the clause's kind, titled by the clause's
  title or, for an unnamed clause, by the sketch's title and its number
  (name_showing = false), with alias bp-r<NNN>-<k>;
- text in the block between clauses (shared context, the statement's opening
  words) is a hidden node <id>--text-<k> in place.

A block without a \\label is matched with the sketch node of the chapter that has
no block, in order.  Chapters are the tex's \\section's, numbered from 1.  The
text is converted as scripts/tex2bp.py converts it; a reference inside maths
becomes the number the website gives the node.
"""
import json
import os
import re
import subprocess
import sys
import tomllib

L2, BP, TOMLF, CHAP = sys.argv[1], sys.argv[2], sys.argv[3], int(sys.argv[4])
HERE = os.path.dirname(os.path.abspath(__file__))

# The conversion machinery of tex2bp.py, read over the layer-2 tex (its labels,
# headings and equation numbers are those of the notes).
src = open(os.path.join(HERE, 'tex2bp.py'), encoding='utf-8').read()
src = src[:src.index('\nrun()\n')]
sys.argv = ['tex2bp.py', L2, '/dev/null', TOMLF, '1', '1']
G = {'__name__': 'tex2bp', '__file__': os.path.join(HERE, 'tex2bp.py')}
exec(compile(src, 'tex2bp.py', 'exec'), G)
BODY, LABEL, to_markdown, problems = G['BODY'], G['LABEL'], G['to_markdown'], G['problems']

KIND = {'bptheorem': 'theorem', 'bplemma': 'lemma', 'bpproposition': 'proposition',
        'bpcorollary': 'corollary', 'bpdefinition': 'definition', 'bpremark': 'remark',
        'bpexample': 'example', 'bpquestion': 'question', 'bpconvention': 'definition'}
STMT = {'theorem', 'lemma', 'proposition', 'corollary', 'definition', 'remark', 'example', 'question'}


def front(path):
    t = open(path, encoding='utf-8').read()
    m = re.match(r'\+\+\+\n(.*?)\n\+\+\+\n?(.*)', t, re.S)
    return tomllib.loads(m.group(1)), m.group(2), t


# the blueprint's nodes
nodes = {}
for dp, dn, fn in os.walk(BP):
    for f in fn:
        if f.endswith('.md'):
            fm, body, _ = front(os.path.join(dp, f))
            if fm.get('id'):
                nodes[fm['id']] = (os.path.join(dp, f), fm, body)

# the chapter's region of the tex
secs = [m.start() for m in re.finditer(r'\\section\*?\{', BODY)]
region = BODY[secs[CHAP - 1]:secs[CHAP] if CHAP < len(secs) else len(BODY)]
chap_title = re.match(r'\\section\*?\{', region)
chap_id = next(k for k, (p, fm, b) in nodes.items() if fm['kind'] in ('chapter', 'appendix')
               and LABEL.get(re.search(r'\\label\{([^}]*)\}', region).group(1), ('', ''))[1] == k)
chap_dir = os.path.dirname(nodes[chap_id][0])
sketches = sorted([k for k, (p, fm, b) in nodes.items() if fm['kind'] in STMT and p.startswith(chap_dir + '/')
                   and not os.path.basename(os.path.dirname(p)) == k], key=lambda k: nodes[k][1]['order'])

blocks = list(re.finditer(r'\\BPSource\{([^}]*)\}\{(\d+)\}\{(\d+)\}\{([^}]*)\}(.*?)\\BPEndSource\{\2\}', region, re.S))
clause_re = re.compile(r'\\begin\{(bp[a-z]+)\}(?:\[([^\]]*)\])?\s*\\label\{(bp-r\d+-\d+)\}(.*?)\\end\{\1\}', re.S)

# block -> sketch id: its \label, else the unmatched sketch nodes in order
labelled = {}
for b in blocks:
    m = re.match(r'\s*(?:\\leavevmode\s*)?\\label\{([^}]*)\}', b.group(5))
    first = re.search(r'\\label\{([^}]*)\}', b.group(5)).group(1)
    labelled[b.group(2)] = first if not first.startswith('bp-r') else None
free = iter([k for k in sketches if k not in set(labelled.values())])
assign = {}
for b in blocks:
    assign[b.group(2)] = labelled[b.group(2)] or next(free)
missing = [k for k in sketches if k not in assign.values()]
if missing:
    problems.append(f'sketch nodes with no block: {missing}')

# Labels of the clauses name their detail nodes; a sketch's label names the sketch.
for b in blocks:
    sid = assign[b.group(2)]
    LABEL[sid] = ('node', sid)
    for c in clause_re.finditer(b.group(5)):
        LABEL[c.group(3)] = ('node', f'{sid}--{int(c.group(3).split("-")[-1])}')


def words(s):
    s = re.sub(r'\$[^$]*\$|\\\[.*?\\\]|\\begin\{[a-z*]+\}|\\end\{[a-z*]+\}|\\[a-zA-Z]+|\[[^\]]*\]', ' ', s, flags=re.S)
    return set(re.findall(r'[A-Za-z]{4,}', s.lower()))


def toml_str(s):
    return json.dumps(s, ensure_ascii=False)


def write(path, fields, body):
    lines = ['+++']
    for k, v in fields:
        if isinstance(v, bool):
            lines.append(f'{k} = {"true" if v else "false"}')
        elif isinstance(v, int):
            lines.append(f'{k} = {v}')
        elif isinstance(v, list):
            lines.append(f'{k} = [' + ', '.join(toml_str(x) for x in v) + ']')
        else:
            lines.append(f'{k} = {toml_str(v)}')
    lines.append('+++')
    os.makedirs(os.path.dirname(path), exist_ok=True)
    open(path, 'w', encoding='utf-8').write('\n'.join(lines) + '\n' + body.rstrip() + '\n')


report = []
written = []
for b in blocks:
    sid = assign[b.group(2)]
    path, fm, sbody = nodes[sid]
    if fm['kind'] != b.group(1).lower():
        problems.append(f'{sid}: the block is a {b.group(1)}, the node a {fm["kind"]}')
    content = b.group(5)
    # move the sketch into a directory of its own
    d = os.path.join(os.path.dirname(path), sid)
    if os.path.basename(path) != '_section.md':
        os.makedirs(d, exist_ok=True)
        subprocess.run(['git', 'mv', path, os.path.join(d, '_section.md')], check=True)
    base = int(fm['order']) * 1000
    pieces, pos = [], 0
    for c in clause_re.finditer(content):
        pieces.append(('text', content[pos:c.start()]))
        pieces.append(('clause', c))
        pos = c.end()
    pieces.append(('text', content[pos:]))
    k_text, order, clause_words = 0, base, set()
    for kind, x in pieces:
        if kind == 'text':
            t = re.sub(r'\\label\{[^}]*\}|\\leavevmode|\\begin\{enumerate\}(\[[^\]]*\])?|\\end\{enumerate\}|'
                       r'\\begin\{itemize\}|\\end\{itemize\}|\\item(\[[^\]]*\])?', ' ', x)
            if not t.strip():
                continue
            k_text += 1
            order += 1
            write(os.path.join(d, f'{sid}--text-{k_text}.md'),
                  [('id', f'{sid}--text-{k_text}'), ('kind', 'hidden'), ('title', fm.get('title', sid)), ('order', order)],
                  to_markdown(t.strip()))
            clause_words |= words(t)
            continue
        env, title, lab, body = x.groups()
        k = int(lab.split('-')[-1])
        order += 1
        fields = [('id', f'{sid}--{k}'), ('kind', KIND[env])]
        if title and not re.fullmatch(r'Source clause \d+', title.strip()):
            fields.append(('title', G['heading_title'](title)))
        else:
            fields += [('title', f'{fm.get("title", sid)} ({k})'), ('name_showing', False)]
        fields += [('order', order), ('aliases', [lab])]
        write(os.path.join(d, f'{sid}--{k}.md'), fields, to_markdown(body.strip()))
        written.append(f'{sid}--{k}')
        clause_words |= words(body)
    # does the sketch say what its clauses say?
    sw = words(open(os.path.join(d, '_section.md')).read().split('+++', 2)[2])
    lost = sw - clause_words
    if len(lost) > max(3, len(sw) // 6):
        report.append(f'{sid}: words of the sketch not in its clauses: {sorted(lost)[:15]}')

# references inside maths: the website's number of the node (as documentOutline numbers them)
outline = {}
for k, (p, fm, b) in list(nodes.items()):
    pass
allnodes = {}
for dp, dn, fn in os.walk(BP):
    for f in fn:
        if f.endswith('.md'):
            p = os.path.join(dp, f)
            fm, body, t = front(p)
            if fm.get('id') and fm['kind'] not in ('hidden', 'proof', 'reference'):
                parent_dir = os.path.dirname(dp) if f == '_section.md' else dp
                allnodes[fm['id']] = (parent_dir, int(fm['order']), dp if f == '_section.md' else None)
dir_id = {v[2]: k for k, v in allnodes.items() if v[2]}
kids = {}
for nid, (parent, o, _) in allnodes.items():
    kids.setdefault(dir_id.get(parent), []).append((o, nid))
number = {}


def walk_numbers(pid, prefix):
    for i, (_, nid) in enumerate(sorted(kids.get(pid, [])), 1):
        number[nid] = f'{prefix}{i}'
        walk_numbers(nid, number[nid] + '.')


walk_numbers(None, '')
for nid in written:
    sid = nid.rsplit('--', 1)[0]
    p = os.path.join(os.path.dirname(nodes[sid][0]), sid, f'{nid}.md')
    t = open(p, encoding='utf-8').read()
    if '\x04' in t:
        open(p, 'w', encoding='utf-8').write(re.sub('\x04([^\x04]*)\x04', lambda m: number.get(m.group(1), m.group(1)), t))
for d in list(os.walk(BP)):
    pass

print(f'chapter {CHAP} ({chap_id}): {len(blocks)} blocks, {len(written)} clauses')
for r in report:
    print('CHECK', r)
for p in problems:
    print('PROBLEM', p)
