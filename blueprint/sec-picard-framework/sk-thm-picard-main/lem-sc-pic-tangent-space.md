+++
id = "lem-sc-pic-tangent-space"
kind = "lemma"
title = "The tangent space of the Picard scheme"
order = 832
uses = ["def-pc-geometrically-irreducible", "def-pc-smooth-projective-curve", "def-sc-picard-functor", "lem-sc-cech-spectral", "thm-pc-picard-representable"]
lean = ["AlgebraicGeometry.nonempty_tangentSpaceAt_linearEquiv_H_one"]
+++
Let $k$ be a separably closed field and $C$ a scheme over $k$ which
is smooth of relative dimension $1$, proper and geometrically integral
over $k$ (for instance a geometrically integral smooth projective curve).
Let $J$ be a group scheme over $k$ representing the degree-zero part
$\operatorname{Pic}^0_{C/k}$ of the Picard functor
$\operatorname{Pic}_{C/k}$, with the group structure induced by that of
$\operatorname{Pic}^0_{C/k}$. Then the tangent space of $J$ at the unit is
isomorphic to $H^1(C,\mathcal O_C)$ as a $k$-vector space.
