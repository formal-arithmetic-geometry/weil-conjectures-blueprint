#!/usr/bin/env python3
"""Put the refinement of one chapter of blueprint-layer-2.tex under the sketch nodes of blueprint/.

Usage: scripts/layer2bp.py <layer-2 tex> <blueprint dir> <blueprint.toml> <chapters>

<chapters> is a number or a range, "2" or "2-25".

blueprint-layer-2.tex refines DerivedCategoryAndSixFunctorsChoice_readable.tex:
each declaration of the notes (a "reference block", \\BPSource ... \\BPEndSource)
is split into clauses, theorem-like environments bp<kind> labelled bp-r<NNN>-<k>.
The declaration is a sketch node of blueprint/ (the block's \\label is its id);
its clauses become detail nodes under it:

- the sketch node <id>.md moves to <id>/_section.md, a directory of its own;
- clause k is <id>/<id>--<k>.md, of the clause's kind, titled by the clause's
  title or, for an unnamed clause, by the sketch's title and its number
  (name_showing = false), with alias bp-r<NNN>-<k>;
- a proof in the block ("Justification of clause~\\ref{bp-r…}", or one after a
  clause) is the proof of that clause, <id>/<id>--<k>.proof.md;
- a "Dependencies:" line after a clause gives its `uses` (on its proof when it
  has one), leaving out every arrow with a definition at either end;
- text in the block between clauses (shared context, the statement's opening
  words) is a hidden node <id>--text-<k> in place;
- a block whose label is a text node of the blueprint (a convention) is left
  as it is: text has no detail nodes.

A block without a \\label is matched with the sketch nodes of its chapter that
have no block, in order, which must be of the block's kind.  Chapters are the tex's \\section's, numbered from 1.  The
text is converted as scripts/tex2bp.py converts it; a reference inside maths
becomes the number the website gives the node.
"""
import json
import os
import re
import subprocess
import sys
import tomllib

L2, BP, TOMLF, CHAPS = sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4]
lo, _, hi = CHAPS.partition('-')
CHAPTERS = list(range(int(lo), int(hi or lo) + 1))
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

secs = [m.start() for m in re.finditer(r'\\section\*?\{', BODY)]
clause_re = re.compile(r'\\begin\{(bp[a-z]+)\}(?:\[([^\]]*)\])?\s*\\label\{(bp-r\d+-\d+)\}(.*?)\\end\{\1\}', re.S)
proof_re = re.compile(r'\\begin\{proof\}(?:\[([^\]]*)\])?(.*?)\\end\{proof\}', re.S)
deps_re = re.compile(r'\\noindent\{\\small\\textit\{Dependencies:\}(.*?)\}\\par', re.S)
block_re = re.compile(r'\\BPSource\{([^}]*)\}\{(\d+)\}\{(\d+)\}\{((?:[^{}]|\{(?:[^{}]|\{[^{}]*\})*\})*)\}(.*?)\\BPEndSource\{\2\}', re.S)


def chapter(c):
    """(chapter id, its directory, its blocks, its sketch ids in order)."""
    region = BODY[secs[c - 1]:secs[c] if c < len(secs) else len(BODY)]
    head = LABEL.get(re.search(r'\\label\{([^}]*)\}', region).group(1), ('', ''))[1]
    cdir = os.path.dirname(nodes[head][0])
    sk = sorted([k for k, (p, fm, b) in nodes.items() if fm['kind'] in STMT and '--' not in k
                 and os.path.relpath(p, cdir).split(os.sep)[0] != '..'
                 and (os.path.basename(p) != '_section.md' or os.path.basename(os.path.dirname(p)) == k)],
                key=lambda k: nodes[k][1]['order'])
    return head, cdir, list(block_re.finditer(region)), sk


# Every block of the document, matched with its node, before any chapter is
# written: clauses cite clauses of other chapters.
plan = {}          # chapter -> [(block, sketch id or None)]
for c in range(1, len(secs) + 1):
    head, cdir, blocks, sk = chapter(c)
    lab = {}
    for b in blocks:
        first = re.search(r'\\label\{([^}]*)\}', b.group(5)).group(1)
        lab[b.group(2)] = None if first.startswith('bp-r') else first
    free = [k for k in sk if k not in set(lab.values())]
    rows = []
    for b in blocks:
        sid = lab[b.group(2)]
        if sid is None:
            sid = free.pop(0) if free else None
            if sid and nodes[sid][1]['kind'] != b.group(1).lower():
                problems.append(f'block {b.group(2)} ({b.group(1)}) matched by position with {sid}, a {nodes[sid][1]["kind"]}')
        rows.append((b, sid))
    if free and c in CHAPTERS:
        problems.append(f'chapter {c}: sketch nodes with no block: {free}')
    plan[c] = (head, cdir, rows)
    for b, sid in rows:
        if sid and sid in nodes and nodes[sid][1]['kind'] in STMT:
            LABEL[sid] = ('node', sid)
            for cm in clause_re.finditer(b.group(5)):
                LABEL[cm.group(3)] = ('node', f'{sid}--{int(cm.group(3).split("-")[-1])}')
kind_of = {}
for c, (head, cdir, rows) in plan.items():
    for b, sid in rows:
        if sid and sid in nodes and nodes[sid][1]['kind'] in STMT:
            for cm in clause_re.finditer(b.group(5)):
                kind_of[f'{sid}--{int(cm.group(3).split("-")[-1])}'] = KIND[cm.group(1)]
for k, (p, fm, b) in nodes.items():
    kind_of.setdefault(k, fm['kind'])


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
    # The conversion makes `--` an en dash, also inside the `[id]` of a link to a
    # clause; put the id back where it names a node.
    body = re.sub(r'\[([^\]\s]*–[^\]\s]*)\]',
                  lambda m: '[' + m.group(1).replace('–', '--') + ']'
                  if m.group(1).replace('–', '--') in kind_of else m.group(0), body)
    os.makedirs(os.path.dirname(path), exist_ok=True)
    open(path, 'w', encoding='utf-8').write('\n'.join(lines) + '\n' + body.rstrip() + '\n')


def ref_ids(tex):
    out = []
    for lab in re.findall(r'\\ref\{([^}]*)\}', tex):
        t = LABEL.get(lab)
        if t and t[0] == 'node' and t[1] not in out:
            out.append(t[1])
    return out


report, written, skipped, arrows = [], [], [], []
for CHAP in CHAPTERS:
    head, cdir, rows = plan[CHAP]
    G['IN_APPENDIX'] = head in G['APPENDIX_CHAPTERS']     # what "this section" becomes
    n_clauses = 0
    for b, sid in rows:
        if sid is None or nodes.get(sid, (0, {'kind': None}))[1]['kind'] not in STMT:
            skipped.append(f'chapter {CHAP}, block {b.group(2)} ({b.group(1)}): {sid or "no node"} is no statement of the blueprint')
            continue
        path, fm, sbody = nodes[sid]
        if fm['kind'] != b.group(1).lower():
            problems.append(f'{sid}: the block is a {b.group(1)}, the node a {fm["kind"]}')
        content = b.group(5)
        d = os.path.join(os.path.dirname(path), sid) if os.path.basename(path) != '_section.md' else os.path.dirname(path)
        if os.path.basename(path) != '_section.md':
            os.makedirs(d, exist_ok=True)
            os.replace(path, os.path.join(d, '_section.md'))
        base = int(fm['order']) * 1000
        # the pieces of the block in order: clauses, proofs, dependency lines, text
        marks = [(m.start(), m.end(), 'clause', m) for m in clause_re.finditer(content)]
        marks += [(m.start(), m.end(), 'proof', m) for m in proof_re.finditer(content)]
        marks += [(m.start(), m.end(), 'deps', m) for m in deps_re.finditer(content)]
        marks.sort(key=lambda x: x[0])
        pieces, pos = [], 0
        for s0, e0, kind, m in marks:
            if s0 < pos:
                continue                      # inside a clause (a proof cannot be)
            pieces.append(('text', content[pos:s0]))
            pieces.append((kind, m))
            pos = e0
        pieces.append(('text', content[pos:]))
        k_text, order, clause_words, last = 0, base, set(), None
        n_proof = {}
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
            if kind == 'deps':
                if last is None:
                    problems.append(f'{sid}: a dependency line before any clause')
                    continue
                for tgt in ref_ids(x.group(1)):
                    if tgt != last:
                        arrows.append((last, tgt))
                continue
            if kind == 'proof':
                title, body = x.group(1) or '', x.group(2)
                named = re.search(r'\\ref\{(bp-r\d+-\d+)\}', title)
                of = LABEL[named.group(1)][1] if named and named.group(1) in LABEL else last
                if of is None:
                    problems.append(f'{sid}: a proof before any clause')
                    continue
                n_proof[of] = n_proof.get(of, 0) + 1
                order += 1
                k = n_proof[of]
                fields = ([('id', f'proof/{of}/{k}')] if k > 1 else []) + [('kind', 'proof'), ('of', of)]
                if title and not named:
                    fields.append(('title', G['heading_title'](title)))
                fields.append(('order', order))
                write(os.path.join(d, f'{of}.proof.md' if k == 1 else f'{of}.proof-{k}.md'), fields, to_markdown(body.strip()))
                continue
            env, title, lab, body = x.groups()
            k = int(lab.split('-')[-1])
            order += 1
            cid = f'{sid}--{k}'
            fields = [('id', cid), ('kind', KIND[env])]
            if title and not re.fullmatch(r'Source clause \d+', title.strip()):
                fields.append(('title', G['heading_title'](title)))
            else:
                fields += [('title', f'{fm.get("title", sid)} ({k})'), ('name_showing', False)]
            fields += [('order', order), ('aliases', [lab])]
            write(os.path.join(d, f'{cid}.md'), fields, to_markdown(body.strip()))
            written.append(cid)
            n_clauses += 1
            last = cid
            clause_words |= words(body)
        sw = words(open(os.path.join(d, '_section.md')).read().split('+++', 2)[2])
        lost = sw - clause_words
        if len(lost) > max(3, len(sw) // 6):
            report.append(f'{sid}: words of the sketch not in its clauses: {sorted(lost)[:15]}')
    print(f'chapter {CHAP} ({head}): {len(rows)} blocks, {n_clauses} clauses')

# Dependency lines: `uses`, on the clause's proof when it has one; no arrow
# with a definition at either end.
by_src = {}
for a, t in arrows:
    if kind_of.get(a) == 'definition' or kind_of.get(t) == 'definition':
        continue
    by_src.setdefault(a, [])
    if t not in by_src[a]:
        by_src[a].append(t)
for a, ts in by_src.items():
    sid = a.rsplit('--', 1)[0]
    d = os.path.join(os.path.dirname(nodes[sid][0]), sid) if os.path.basename(nodes[sid][0]) != '_section.md' else os.path.dirname(nodes[sid][0])
    p = os.path.join(d, f'{a}.proof.md')
    if not os.path.exists(p):
        p = os.path.join(d, f'{a}.md')
    t = open(p, encoding='utf-8').read()
    i = t.index('+++', 3)
    t = t[:i] + 'uses = [' + ', '.join(toml_str(x) for x in ts) + ']\n' + t[i:]
    open(p, 'w', encoding='utf-8').write(t)
print(f'{sum(len(v) for v in by_src.values())} dependency arrows from {len(by_src)} clauses '
      f'({len(arrows)} listed, with definitions left out)')

# References inside maths are left as \x04id\x04: their numbers are the website's,
# which depend on the tool's numbering; they are filled in afterwards.
left = []
for dp, dn, fn in os.walk(BP):
    for f in fn:
        p = os.path.join(dp, f)
        if f.endswith('.md') and '\x04' in open(p, encoding='utf-8').read():
            left.append(os.path.relpath(p, BP))
if left:
    print(f'{len(left)} files hold references inside maths still to number: {left[:5]}')
for x in skipped:
    print('SKIPPED', x)
for r in report:
    print('CHECK', r)
for p in problems:
    print('PROBLEM', p)
