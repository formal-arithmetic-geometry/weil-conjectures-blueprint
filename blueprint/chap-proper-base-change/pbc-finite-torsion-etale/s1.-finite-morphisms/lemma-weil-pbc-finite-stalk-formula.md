+++
id = "lemma-weil-pbc-finite-stalk-formula"
kind = "lemma"
title = "Geometric stalk formula for finite direct image"
order = 1539
lean = ["AlgebraicGeometry.Etale.lowerStarSheafFiberIsoPi", "AlgebraicGeometry.Etale.stalkRestrict"]
uses = ["def-weil-pbc-cartesian-square", "def-weil-pbc-geometric-fibre", "lemma-weil-pbc-geometric-stalk-conservative"]
+++
Let $h:W\to V$ be finite and let $\bar v:\operatorname{Spec}\Omega\to V$ be a geometric
point with $\Omega$ algebraically closed. For every sheaf $F$ on $W_{\mathrm{et}}$ there
is a canonical bijection

$$
(h_*F)_{\bar v}\;\cong\;
\prod_{\bar w\,|\,\bar v}F_{\bar w},
$$

where the index runs over the finite geometric fibre of $h$ over $\bar v$ and the
$\bar w$-th component is restriction of stalks.

## Proof

The formalisation avoids the strict henselisation: it works with the category of
*split neighbourhoods* of $\bar v$ (pointed etale neighbourhoods $(U,\bar u)$ together
with a decomposition of $W\times_VU$ into pairwise disjoint clopen pieces indexed by the
geometric points $\bar w$ over $\bar v$, the $\bar w$-th piece containing $(\bar u,\bar w)$), shows
that these are cofinal among all pointed etale neighbourhoods (Stacks 00UJ applied to an affine
chart), that the $\bar w$-th pieces are cofinal among the pointed etale neighbourhoods of
$\bar w$ (an etale-local section lemma for finite algebras with a unique point), and that a
sheaf sends the disjoint clopen cover into a product; finite products commute with the
filtered colimit since the coefficients satisfy AB5. The restriction to geometric points
with algebraically closed residue field suffices for all uses, since these already form a
conservative family (Lemma [lemma-weil-pbc-geometric-stalk-conservative]).
