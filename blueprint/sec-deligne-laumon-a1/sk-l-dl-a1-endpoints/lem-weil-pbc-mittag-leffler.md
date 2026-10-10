+++
id = "lem-weil-pbc-mittag-leffler"
kind = "lemma"
title = "Mittag--Leffler vanishing"
order = 2731
uses = ["def-weil-pbc-derived-inverse-limit", "prop-weil-pbc-roos-triangle"]
+++
A tower of finite abelian groups satisfies the Mittag--Leffler condition and
has $\varprojlim{}^1=0$. Consequently, for the derived inverse-limit
construction of [def-weil-pbc-derived-inverse-limit], the canonical Milnor
map is an isomorphism for such a tower.

## Proof

Descending chains of subgroups of a finite group stabilize, so the tower is
Mittag--Leffler and $\varprojlim{}^1=0$ by the product-cokernel description
of $\varprojlim{}^1$ (Stacks, Tag
[07KW](https://stacks.math.columbia.edu/tag/07KW): a Mittag--Leffler
system is right acyclic for $\lim$); the exact sequence of
[prop-weil-pbc-roos-triangle] then identifies the Milnor map (Stacks, Tag
[07KY](https://stacks.math.columbia.edu/tag/07KY)). Stacks states these
for towers of abelian groups; the argument applies verbatim to a tower of
finite abelian groups in the tower category over $T_{\Proet}$, finiteness
being what forces the Mittag--Leffler condition.
