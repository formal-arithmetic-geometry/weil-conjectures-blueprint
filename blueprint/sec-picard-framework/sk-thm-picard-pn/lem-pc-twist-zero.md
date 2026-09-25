+++
id = "lem-pc-twist-zero"
kind = "lemma"
title = "The trivial twist"
order = 626
uses = ["def-pc-proj", "def-pc-projective-space-twist", "def-sc-invertible-module"]
+++
Let $A$ be a commutative ring, $n\ge0$ and
$P=\operatorname{Proj}(A[x_0,\ldots,x_n])$ with standard affine opens
$U_i=D_+(x_i)$ and bases $e_i^{(0)}$ of $\mathcal O_P(0)|_{U_i}$
([def-pc-projective-space-twist]). Then there is a canonical
isomorphism $\mathcal O_P(0)\to\mathcal O_P$ of
[def-sc-invertible-module] whose restriction to $U_i$ sends
$e_i^{(0)}$ to $1$.

## Proof

By [def-pc-projective-space-twist] the transition rule for $d=0$ is
$e_i^{(0)}=e_j^{(0)}$, so the isomorphisms
$\mathcal O_{U_i}e_i^{(0)}\to\mathcal O_{U_i}$, $e_i^{(0)}\mapsto1$,
agree on the overlaps. They glue to an isomorphism
$\mathcal O_P(0)\to\mathcal O_P$ because isomorphisms between
$\mathcal O_P$-modules agreeing on an open cover glue (the sheaf axiom
for $\mathcal O_P$, whose sections over the standard opens are the rings
of [def-pc-proj]), the glued map being an isomorphism since it is
one locally ([def-sc-invertible-module]).
