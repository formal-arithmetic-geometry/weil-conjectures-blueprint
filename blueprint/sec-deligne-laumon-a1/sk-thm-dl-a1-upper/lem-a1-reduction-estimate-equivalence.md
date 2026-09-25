+++
id = "lem-a1-reduction-estimate-equivalence"
kind = "lemma"
title = "The curve estimate is the line estimate for the transported datum"
order = 3067
uses = ["def-weil-ordinary-compact-cohomology", "def-weil-punctual-weights", "lem-a1-reduction-composition"]
+++
Let $C_0$ be a smooth geometrically connected affine curve, let
$C'_0$ be a smooth geometrically connected curve containing $C_0$
as a dense open with finite complement, let
$g:C'_0\to\mathbf A^1_{k_0}$ be a finite generically etale morphism,
let $j:C_0\hookrightarrow C'_0$, and let $\mathcal F$ be lisse and
punctually $\iota$-pure of weight $w$ on $C_0$. Put
$\mathcal K:=g_*j_!\mathcal F$. Then the estimate
$H_c^i(\mathbf A^1,\mathcal K)$ has weights at most $w+i$ for every
$i$ holds if and only if the same estimate holds for
$H_c^i(C,\mathcal F)$: the curve estimate is equivalent to the line
estimate for the transported datum.

## Proof

The degreewise identification is that of
[lem-a1-reduction-composition], an isomorphism of Frobenius
modules in every degree; isomorphic Frobenius modules have the same
eigenvalue multiset, so a weight bound holds for one of the two groups
if and only if it holds for the other.
