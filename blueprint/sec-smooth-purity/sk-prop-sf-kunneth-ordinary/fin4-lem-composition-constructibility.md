+++
id = "fin4-lem-composition-constructibility"
kind = "lemma"
title = "Constructibility composes"
order = 1679
uses = ["def-weil-pbc-constructible-complexes", "def-weil-pbc-direct-image", "def-weil-pbc-scheme-conventions", "lem-finrepair-composition-c", "lem-weil-pbc-grothendieck-spectral-sequence", "sbc-def-coefficient-conventions"]
+++
Let $f:U\to V$ and $g:V\to W$ be morphisms of
schemes of finite type over
$k$ such that the higher direct image functors $R^qf_*$ and $R^qg_*$
of [def-weil-pbc-direct-image] preserve
constructible
$\Lambda$-sheaves (the ring $\Lambda$ of
[sbc-def-coefficient-conventions]), and assume moreover that the
geometric fibres of $f$
and of $g$ have dimension at most $e$, resp. $c$, and that
$R^qf_*G=0$ for $q>2e$ and $R^qg_*H=0$ for $q>2c$ for the
constructible sheaves in question. Then $R^q(g\circ f)_*$ preserves
constructible $\Lambda$-sheaves, and $R^q(g\circ f)_*F=0$ for
$q>2(e+c)$: the bound $2\cdot(\text{fibre dimension})$ is additive
under composition.

## Proof

Constructibility follows from [lem-finrepair-composition-c].
For the bound, use the spectral sequence of
[lem-weil-pbc-grothendieck-spectral-sequence],
$E_2^{a,b}=R^ag_*R^bf_*F$.
It is zero outside $0\leq a\leq2c$, $0\leq b\leq2e$, by the
two assumed vanishing bounds, since each $R^bf_*F$ is constructible.
No term can contribute to total degree greater than $2(c+e)$.
The bounded first-quadrant filtration proves the asserted vanishing.
