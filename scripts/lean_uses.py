#!/usr/bin/env python3
"""The arrows between declarations, from Lean: what `blueprint check --lean` expects.

Usage: scripts/lean_uses.py <lean-facts.json> <blueprint dir> [--write]

A uses B when a Lean name of A depends on a Lean name of B, as `blueprint
extract` records it (`deps`: the mapped constants reached from A's constant,
stopping at mapped ones).  What A's Lean statements need (`typeDeps`) goes on
A, what only their proofs need (`valueDeps`) on A's proof (its first proof
file), as `check --lean` holds statements and proofs against the two; with no
proof file, everything goes on A.

Every statement node is rewritten this way, and so are their proofs: a node
without Lean names gets no arrows, since Lean says nothing about it.  The
detail nodes of layer 2 (ids `<id>--<k>`, with no Lean names) keep the arrows
their "Dependencies:" lines give.  Without --write it only reports.
"""
import collections
import json
import os
import re
import sys
import tomllib

FACTS, BP = sys.argv[1], sys.argv[2]
WRITE = '--write' in sys.argv
STMT = {'theorem', 'lemma', 'proposition', 'corollary', 'definition', 'remark', 'example', 'question'}

decls = json.load(open(FACTS))['decls']

nodes, proofs = {}, collections.defaultdict(list)
for dp, dn, fn in os.walk(BP):
    for f in fn:
        if not f.endswith('.md'):
            continue
        p = os.path.join(dp, f)
        t = open(p, encoding='utf-8').read()
        m = re.match(r'\+\+\+\n(.*?)\n\+\+\+\n', t, re.S)
        fm = tomllib.loads(m.group(1))
        if fm.get('kind') == 'proof':
            proofs[fm['of']].append((fm.get('order', 0), p))
        elif fm.get('kind') in STMT and fm.get('id'):
            nodes[fm['id']] = (p, fm)

owners = collections.defaultdict(set)
for k, (p, fm) in nodes.items():
    for name in fm.get('lean', []):
        owners[name].add(k)

missing = sorted({n for k, (p, fm) in nodes.items() for n in fm.get('lean', []) if not decls.get(n, {}).get('exists')})
st, pf = collections.defaultdict(set), collections.defaultdict(set)
for k, (p, fm) in nodes.items():
    for name in fm.get('lean', []):
        d = decls.get(name) or {}
        if not d.get('exists'):
            continue
        ty = d.get('typeDeps')
        va = d.get('valueDeps')
        if ty is None or va is None:
            ty, va = d.get('deps', []), []
        for dep in ty:
            st[k] |= owners.get(dep, set()) - {k}
        for dep in va:
            pf[k] |= owners.get(dep, set()) - {k}
for k in list(pf):
    pf[k] -= st[k]
    if not proofs.get(k):
        st[k] |= pf.pop(k)

# cycles among the nodes (a statement and its proofs are one node)
g = collections.defaultdict(set)
for d in (st, pf):
    for a, bs in d.items():
        g[a] |= bs
sys.setrecursionlimit(100000)
idx, low, stack, on, comps, c = {}, {}, [], set(), [], [0]


def strong(v):
    idx[v] = low[v] = c[0]
    c[0] += 1
    stack.append(v)
    on.add(v)
    for w in g[v]:
        if w not in idx:
            strong(w)
            low[v] = min(low[v], low[w])
        elif w in on:
            low[v] = min(low[v], idx[w])
    if low[v] == idx[v]:
        comp = []
        while True:
            w = stack.pop()
            on.discard(w)
            comp.append(w)
            if w == v:
                break
        if len(comp) > 1:
            comps.append(comp)


for v in list(g):
    if v not in idx:
        strong(v)

n_arrows = sum(len(v) for v in st.values()) + sum(len(v) for v in pf.values())
print(f'{len(nodes)} statements, {sum(1 for k in nodes if nodes[k][1].get("lean"))} with Lean names; '
      f'{n_arrows} arrows ({sum(len(v) for v in st.values())} on statements, {sum(len(v) for v in pf.values())} on proofs)')
print(f'Lean names not in the facts or not declared: {len(missing)} {missing[:10]}')
print(f'cycles: {len(comps)}', [sorted(x) for x in comps][:10])
json.dump({'st': {k: sorted(v) for k, v in st.items() if v}, 'pf': {k: sorted(v) for k, v in pf.items() if v},
           'cycles': comps, 'missing': missing}, open(os.path.join(os.path.dirname(FACTS), 'lean-uses.json'), 'w'), indent=1)

if not WRITE:
    sys.exit()
order = {k: fm.get('order', 0) for k, (p, fm) in nodes.items()}


def set_uses(path, ids):
    t = open(path, encoding='utf-8').read()
    i = t.index('+++', 3)
    head = re.sub(r'^uses = \[.*\]\n', '', t[:i], count=1, flags=re.M)
    if ids:
        head += 'uses = [' + ', '.join(json.dumps(x) for x in sorted(ids, key=lambda x: order.get(x, 0))) + ']\n'
    if head != t[:i]:
        open(path, 'w', encoding='utf-8').write(head + t[i:])


for k, (p, fm) in nodes.items():
    if '--' in k:
        continue                  # layer-2 detail nodes keep their own arrows
    set_uses(p, st.get(k, set()))
    ps = sorted(proofs.get(k, []))
    for j, (_, pp) in enumerate(ps):
        set_uses(pp, pf.get(k, set()) if j == 0 else set())
print('written')
