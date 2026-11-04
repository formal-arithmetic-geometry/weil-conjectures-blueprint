#!/usr/bin/env python3
"""The citations between declarations of DerivedCategoryAndSixFunctorsChoice_readable.tex.

Usage: scripts/tex_citations.py <tex> <out.json>

Reads the tex on its own, independently of blueprint/, and records for every
theorem-like environment the declarations its statement cites and those its
proofs cite.  A citation is a \\ref or an \\eqref.  A label resolves to the
declaration it stands in: its own \\label, a \\label on an item or an equation
inside its statement, or one inside one of its proofs.  A label standing in
running text (an equation in prose, a heading) names no declaration.  A proof
proves the statement before it, or the one its title names ("Proof of
Theorem~\\ref{x}"), as scripts/tex2bp.py reads it.
"""
import json
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from tex2bp_titles import UNLABELLED  # noqa: E402

DECL = ['theorem', 'lemma', 'proposition', 'corollary', 'definition', 'remark', 'question', 'example']
TEX, OUT = sys.argv[1], sys.argv[2]


def strip_comments(src):
    out = []
    for line in src.split('\n'):
        m = re.search(r'(?<!\\)%', line)
        if m:
            if not line[:m.start()].strip():
                continue
            line = line[:m.start()]
        out.append(line)
    return '\n'.join(out)


src = strip_comments(open(TEX, encoding='utf-8').read())
BODY = src[src.index('\\begin{document}'):src.index('\\end{document}')]
BODY = BODY[:BODY.index('\\begin{thebibliography}')] if '\\begin{thebibliography}' in BODY else BODY

# The environments in tex order: statements, proofs, conventions.
env_re = re.compile(r'\\begin\{(' + '|'.join(DECL + ['proof', 'convention']) + r')\}')
units = []          # dicts: kind, id (statements), of (proofs), start, end, text
pos = 0
last_decl = None
problems = []
while True:
    m = env_re.search(BODY, pos)
    if not m:
        break
    env = m.group(1)
    end = BODY.index('\\end{' + env + '}', m.end())
    content = BODY[m.end():end]
    opt = None
    om = re.match(r'\s*\[', content)
    if om:
        depth, j = 0, om.end() - 1
        while True:
            c = content[j]
            if c == '[':
                depth += 1
            elif c == ']':
                depth -= 1
                if depth == 0:
                    break
            j += 1
        opt, content = content[om.end():j], content[j + 1:]
    # the text between this environment and the previous one is running text
    if env == 'proof':
        named = re.search(r'\\ref\{([^}]*)\}', opt or '')
        of = named.group(1) if named else last_decl
        if of is None:
            problems.append('a proof after no statement: ' + content[:80])
        units.append(dict(kind='proof', of=of, start=m.start(), end=end, text=content))
        last_decl = None if not named else last_decl
    elif env == 'convention':
        units.append(dict(kind='convention', start=m.start(), end=end, text=content))
        last_decl = None
    else:
        lab = re.match(r'\s*\\label\{([^}]*)\}', content)
        if lab:
            did = lab.group(1)
        else:
            key = next((k for k in UNLABELLED if content.strip().startswith(k)), None)
            did = UNLABELLED[key][0] if key else None
            if did is None:
                problems.append(f'{env} without a label: {content.strip()[:80]}')
        units.append(dict(kind=env, id=did, start=m.start(), end=end, text=content))
        last_decl = did
    pos = end

# Every label: the declaration it stands in, or None for running text.
label_owner = {}
for u in units:
    owner = u.get('id') if u['kind'] in DECL else u.get('of') if u['kind'] == 'proof' else None
    for lm in re.finditer(r'\\label\{([^}]*)\}', u['text']):
        label_owner[lm.group(1)] = owner
    if u['kind'] in DECL and u.get('id'):
        label_owner[u['id']] = u['id']
for lm in re.finditer(r'\\label\{([^}]*)\}', BODY):
    label_owner.setdefault(lm.group(1), None)

kind_of = {u['id']: u['kind'] for u in units if u['kind'] in DECL and u.get('id')}
order = {u['id']: i for i, u in enumerate(u for u in units if u['kind'] in DECL and u.get('id'))}
ref_re = re.compile(r'\\(ref|eqref)\{([^}]*)\}')


def cited(text, self_id):
    out = {}
    for m in ref_re.finditer(text):
        for lab in m.group(2).split(','):
            lab = lab.strip()
            if lab not in label_owner:
                problems.append(f'reference to an unknown label {lab}')
                continue
            tgt = label_owner[lab]
            if tgt is None or tgt == self_id:
                continue
            s = max(text.rfind('. ', 0, m.start()), text.rfind('\n\n', 0, m.start())) + 1
            e = text.find('. ', m.end())
            snippet = re.sub(r'\s+', ' ', text[s:(len(text) if e < 0 else e + 1)]).strip()[:300]
            out.setdefault(tgt, []).append({'label': lab, 'cmd': m.group(1), 'context': snippet})
    return out


decls = {}
for u in units:
    if u['kind'] in DECL and u.get('id'):
        decls[u['id']] = dict(kind=u['kind'], order=order[u['id']], statement=cited(u['text'], u['id']), proofs=[])
for u in units:
    if u['kind'] == 'proof' and u.get('of') in decls:
        decls[u['of']]['proofs'].append(cited(u['text'], u['of']))
    elif u['kind'] == 'proof':
        problems.append(f'a proof of {u.get("of")}, which is no declaration')

json.dump({'declarations': decls, 'problems': problems}, open(OUT, 'w'), indent=1, ensure_ascii=False)
n_st = sum(len(d['statement']) for d in decls.values())
n_pf = sum(len(p) for d in decls.values() for p in d['proofs'])
print(f'{len(decls)} declarations, {sum(len(d["proofs"]) for d in decls.values())} proofs; '
      f'cited declarations: {n_st} from statements, {n_pf} from proofs; {len(problems)} problems')
for p in problems[:20]:
    print('PROBLEM', p)
