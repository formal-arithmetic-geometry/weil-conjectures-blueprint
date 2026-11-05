#!/usr/bin/env python3
"""Bring a new version of the readable tex onto blueprint/, keeping what was added since the import.

Usage: scripts/retex.py <tex> <layer-2 tex> <blueprint dir> <blueprint.toml> <out dir>

The blueprint is built afresh in <out dir>, which is then put in place of
<blueprint dir> by hand (rsync -a --delete <out>/ blueprint/):

1. scripts/tex2bp.py converts the whole tex (chapters 1-25), as for the import;
2. what was added to the blueprint after the import is carried over, node by
   node (matched by id, or through RENAMED): `lean`, `uses`, `aliases`,
   `hide_content`, the kind `appendix` or `matter` of a chapter, and its part
   (`refines`, `serial`; the part-* directories are kept, with their text).  The references/ directory
   is kept as it is;
3. scripts/layer2bp.py puts the clauses of the layer-2 tex under the sketch
   nodes again (chapters 2-25).  The layer-2 tex may lag behind the tex: it
   is read with the tex's heading titles and equation tags (matched by
   label), RENAMED
   applied to its labels, and a split declaration's block split as well.

Run on the tex the blueprint was made from, it gives the blueprint back.
"""
import json
import os
import re
import shutil
import subprocess
import sys
import tempfile
import tomllib

TEX, L2, BP, TOMLF, OUT = sys.argv[1:6]
HERE = os.path.dirname(os.path.abspath(__file__))

# Ids changed by the tex: a heading retitled (its id is the slug of its
# title), a declaration relabelled.  The node keeps its old id as an alias.
RENAMED = {
    # November 2026: "Deligne's theorem" is "the Deligne--Laumon theorem"
    'sec-Delignes-theorem': 'sec-The-Deligne-Laumon-theorem',
    'sec-Delignes-theorem-2': 'sec-The-Deligne-Laumon-theorem-2',
    'chap-Delignes-theorem-for-curves': 'chap-The-Deligne-Laumon-theorem-for-curves',
    'chap-Delignes-theorem-in-general': 'chap-The-Deligne-Laumon-theorem-in-general',
    'sec-Proof-of-Delignes-theorem': 'sec-Proof-of-the-Deligne-Laumon-theorem',
    # November 2026: remarks stated as results, with proofs
    'remark-cohomology-modules-underlying-abelian': 'lemma-cohomology-modules-underlying-abelian',
    'remark-finiteness-small-etale-topoi': 'lemma-finiteness-small-etale-topoi',
    'remark-results-from-etale-theory': 'theorem-results-from-etale-theory',
}
# A declaration the tex has split into several: its parts, each with the
# attributes it takes of the old node (the first part also its id, as an
# alias), and the clauses of the old node's
# layer-2 block that each part takes.  `uses` are those of the old node that
# the part's Lean names depend on (the facts of the site branch).
SPLIT = {
    'remark-henselian-pairs-facts': {
        'theorem-gabber-affine-proper-base-change': {
            'lean': ['AlgebraicGeometry.Etale.bijective_cohomologyMap_of_henselianRing'],
            'uses': None,                     # all of the old node's
            'clauses': [1],
        },
        'theorem-finite-etale-covers-proper-henselian': {
            'lean': ['AlgebraicGeometry.Scheme.isEquivalence_pullback_finiteEtale_of_henselianRing',
                     'AlgebraicGeometry.Etale.bijective_cohomologyMap_one_constantSheaf_of_henselianRing'],
            'uses': ['definition-ind-etale-pro-etale-weakly', 'proposition-etale-implications',
                     'definition-small-pro-etale-site', 'proposition-comparison-morphism-inverse-image',
                     'definition-compactification-refinement', 'lemma-schematic-closure-uniqueness',
                     'lemma-uniqueness-maps-dense-open', 'theorem-chow-s-lemma-projective-form'],
            'clauses': [2, 3],
        },
    },
}
CARRIED = ('lean', 'uses', 'aliases')


def parse(path):
    t = open(path, encoding='utf-8').read()
    m = re.match(r'\+\+\+\n(.*?)\n\+\+\+\n?(.*)', t, re.S)
    return tomllib.loads(m.group(1)), m.group(1), m.group(2)


def key_of(path, fm):
    if fm.get('kind') == 'proof':
        n = re.fullmatch(r'proof/.*/(\d+)', fm.get('id', ''))
        return ('proof', fm['of'], int(n.group(1)) if n else 1)
    if fm.get('id'):
        return fm['id']
    if os.path.basename(path) == '_section.md':
        return os.path.basename(os.path.dirname(path))
    return path


def toml_list(xs):
    return '[' + ', '.join('"' + x.replace('\\', '\\\\').replace('"', '\\"') + '"' for x in xs) + ']'


# ------------------------------------------------------------------ 1. convert

tmp = tempfile.mkdtemp()
conv = os.path.join(tmp, 'conv')
r = subprocess.run([sys.executable, os.path.join(HERE, 'tex2bp.py'), TEX, conv, TOMLF, '1', '25'],
                   capture_output=True, text=True)
print(r.stdout.strip())
if r.returncode:
    sys.exit(r.stderr)

# ------------------------------------------------------------------ 2. carry over

old = {}            # key -> fm, for the blueprint's nodes that are not layer-2 nodes
for dp, dn, fn in os.walk(BP):
    for f in fn:
        p = os.path.join(dp, f)
        if not f.endswith('.md') or os.path.relpath(p, BP).startswith('references' + os.sep):
            continue
        fm, _, _ = parse(p)
        k = key_of(p, fm)
        if '--' in str(k):
            continue                      # a clause, its proof or text: layer2bp writes them
        old[k] = fm

part_of = {}        # new id of a part -> the old id it was split from
for o, parts in SPLIT.items():
    for n in parts:
        part_of[n] = o
back = {v: k for k, v in RENAMED.items()}


conv_ids = set()
for dp, dn, fn in os.walk(conv):
    for f in fn:
        fm, _, _ = parse(os.path.join(dp, f))
        conv_ids.add(key_of(os.path.join(dp, f), fm))


def renamed(i):
    n = RENAMED.get(i, i)
    return n if n in conv_ids and i not in conv_ids else i


def remap_uses(uses, body):
    out = []
    for u in uses:
        if u in SPLIT and u not in conv_ids:
            parts = list(SPLIT[u])
            cited = [n for n in parts if f'[{n}]' in body]
            new = cited or parts
        else:
            new = [renamed(u)]
        out += [n for n in new if n not in out]
    return out


if os.path.exists(OUT):
    shutil.rmtree(OUT)
shutil.copytree(os.path.join(BP, 'references'), os.path.join(OUT, 'references'))
carried, fresh = 0, []
for dp, dn, fn in os.walk(conv):
    for f in fn:
        src = os.path.join(dp, f)
        fm, front, body = parse(src)
        k = key_of(src, fm)
        if isinstance(k, tuple):
            ok = (k[0], back.get(k[1], k[1]), k[2])
        else:
            ok = back.get(k, k)
        prev = old.get(k)
        via_old = prev is None and ok in old       # renamed by the tex just now
        if via_old:
            prev = old[ok]
        lines = front.split('\n')
        extra = {}
        if prev is not None:
            carried += 1
            # a chapter made an appendix, or front matter, keeps that kind
            if prev.get('kind') in ('appendix', 'matter') and fm['kind'] == 'chapter':
                lines = [f'kind = "{prev["kind"]}"' if x == 'kind = "chapter"' else x for x in lines]
            for a in CARRIED:
                if a in prev:
                    extra[a] = list(prev[a])
            if via_old and isinstance(ok, str) and ok not in extra.get('aliases', []):
                extra['aliases'] = extra.get('aliases', []) + [ok]
        elif k in part_of:
            o = part_of[k]
            spec = SPLIT[o][k]
            extra['lean'] = spec['lean']
            extra['uses'] = list(old[o].get('uses', [])) if spec['uses'] is None else spec['uses']
            if k == next(iter(SPLIT[o])):
                extra['aliases'] = [o]        # the first part keeps the old id
        else:
            fresh.append(k)
        if 'uses' in extra:
            extra['uses'] = remap_uses(extra['uses'], body)
        for a in CARRIED:
            if a in extra:
                lines.append(f'{a} = {toml_list(extra[a])}')
        # a chapter's part and letter (#206)
        if prev is not None:
            for a in ('refines', 'serial'):
                if prev.get(a) is not None:
                    lines.append(f'{a} = {json.dumps(prev[a], ensure_ascii=False)}')
        # a heading whose content the website leaves off its parent's page
        if prev is not None and prev.get('hide_content') is not None:
            v = prev['hide_content']
            lines.append(f'hide_content = {"true" if v is True else "false" if v is False else json.dumps(v)}')
        dst = os.path.join(OUT, os.path.relpath(src, conv))
        os.makedirs(os.path.dirname(dst), exist_ok=True)
        open(dst, 'w', encoding='utf-8').write('+++\n' + '\n'.join(lines) + '\n+++\n' + body)
print(f'{carried} nodes carried over; new: {fresh}')

# The parts (#206): each part-* directory of the blueprint is kept, and the
# opening text of the part, which the conversion puts into the part's first
# chapter, is moved into it; the part comes just before that text.
for d in sorted(x for x in os.listdir(BP) if x.startswith('part-')):
    src, dst = os.path.join(BP, d), os.path.join(OUT, d)
    os.makedirs(dst, exist_ok=True)
    first = None
    for f in sorted(os.listdir(src)):
        if f == '_section.md':
            continue
        hits = [os.path.join(dp, f) for dp, dn, fn in os.walk(OUT) if f in fn and not dp.startswith(dst)]
        if len(hits) == 1:
            shutil.move(hits[0], os.path.join(dst, f))
        else:
            print(f'PROBLEM: the text {f} of {d} is converted {len(hits)} times; kept as it was')
            shutil.copy(os.path.join(src, f), os.path.join(dst, f))
        o = parse(os.path.join(dst, f))[0].get('order')
        if o is not None:
            first = o if first is None else min(first, o)
    t = open(os.path.join(src, '_section.md'), encoding='utf-8').read()
    if first is not None:
        t = re.sub(r'^order = .*$', f'order = {first - 0.5}', t, count=1, flags=re.M)
    open(os.path.join(dst, '_section.md'), 'w', encoding='utf-8').write(t)

# ------------------------------------------------------------------ 3. layer 2

l2 = open(L2, encoding='utf-8').read()
# headings as the tex titles them, matched by their labels
head_re = re.compile(r'(\\(?:sub)*section\*?\{)((?:[^{}]|\{[^{}]*\})*)(\}\s*\\label\{([^}]*)\})')
title_of = {m.group(4): m.group(2) for m in head_re.finditer(open(TEX, encoding='utf-8').read())}
l2 = head_re.sub(lambda m: m.group(1) + title_of.get(m.group(4), m.group(2)) + m.group(3), l2)
# an equation the tex tags itself, (C) for (E.11), is tagged so in layer 2 too
eq_re = re.compile(r'\\begin\{equation\}(.*?)\\end\{equation\}', re.S)
lab_re = re.compile(r'\\label\{([^}]*)\}')
tag_re = re.compile(r'\\tag\{(?:[^{}]|\{[^{}]*\})*\}')
tags = {}
for m in eq_re.finditer(open(TEX, encoding='utf-8').read()):
    lab, tag = lab_re.search(m.group(1)), tag_re.search(m.group(1))
    if lab and tag:
        tags[lab.group(1)] = tag.group(0)
l2 = eq_re.sub(lambda m: m.group(0) if tag_re.search(m.group(1)) or not lab_re.search(m.group(1))
               or lab_re.search(m.group(1)).group(1) not in tags
               else m.group(0).replace('\\end{equation}', ' ' + tags[lab_re.search(m.group(1)).group(1)] + '\n\\end{equation}'), l2)
present = set()
for dp, dn, fn in os.walk(OUT):
    for f in fn:
        fm, _, _ = parse(os.path.join(dp, f))
        if fm.get('id'):
            present.add(fm['id'])
KIND_WORD = {'lemma': 'Lemma', 'theorem': 'Theorem', 'proposition': 'Proposition', 'remark': 'Remark',
             'corollary': 'Corollary', 'definition': 'Definition', 'example': 'Example'}
for o, n in RENAMED.items():
    if n not in present or o in present or not n.split('-')[0] in KIND_WORD:
        continue
    word = KIND_WORD[n.split('-')[0]]
    l2 = re.sub(r'\\BPSource\{\w+\}(\{\d+\}\{\d+\}\{[^}]*\}\s*\\label\{' + re.escape(o) + r'\})',
                lambda m: '\\BPSource{' + word + '}' + m.group(1), l2)
    l2 = re.sub(r'Remark(~\\ref\{' + re.escape(o) + r'\})', lambda m: word + m.group(1), l2)
    l2 = l2.replace('{' + o + '}', '{' + n + '}')
block_re = re.compile(r'\\BPSource\{(\w+)\}\{(\d+)\}\{(\d+)\}\{([^}]*)\}(.*?)\\BPEndSource\{\2\}', re.S)
for o, parts in SPLIT.items():
    if o in present or not all(n in present for n in parts):
        continue
    m = next(b for b in block_re.finditer(l2) if re.search(r'\\label\{' + re.escape(o) + r'\}', b.group(5)))
    clause = {int(c.group(1)): c.group(0) for c in
              re.finditer(r'\\begin\{(?:bp[a-z]+)\}(?:\[[^\]]*\])?\s*\\label\{bp-r' + m.group(2) + r'-(\d+)\}.*?\\end\{bp[a-z]+\}', m.group(5), re.S)}
    new = []
    for j, (n, spec) in enumerate(parts.items()):
        no = m.group(2) if j == 0 else str(int(m.group(2)) * 1000 + j)    # block numbers are unique
        new.append(f'\\BPSource{{{KIND_WORD[n.split("-")[0]]}}}{{{no}}}{{{len(spec["clauses"])}}}{{{m.group(4)}}}\n\n'
                   f'\\label{{{n}}}\n\n' + '\n\n'.join(clause[c] for c in spec['clauses']) + f'\n\n\\BPEndSource{{{no}}}')
    l2 = l2[:m.start()] + '\n\n'.join(new) + l2[m.end():]
    # a citation of an item of the old node cites the part that took it
    items = {'i': list(parts)[0], 'ii': list(parts)[-1]}
    l2 = re.sub(r'Remark~\\ref\{' + re.escape(o) + r'\}\((i|ii)\)',
                lambda mm: KIND_WORD[items[mm.group(1)].split('-')[0]] + '~\\ref{' + items[mm.group(1)] + '}', l2)
    l2 = re.sub(r'\\ref\{' + re.escape(o) + r'\}', '\\\\ref{' + list(parts)[0] + '}', l2)
l2path = os.path.join(tmp, 'layer-2.tex')
open(l2path, 'w', encoding='utf-8').write(l2)
r = subprocess.run([sys.executable, os.path.join(HERE, 'layer2bp.py'), l2path, OUT, TOMLF, '2-25'],
                   capture_output=True, text=True)
print(r.stdout.strip())
if r.returncode:
    sys.exit(r.stderr)
shutil.rmtree(tmp)
