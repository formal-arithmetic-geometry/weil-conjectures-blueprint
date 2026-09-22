+++
id = "lem-sc-C6"
kind = "lemma"
title = "C6: invariance under algebraically closed extension"
order = 4547
lean = ["AlgebraicGeometry.Curve.C6_constant"]
uses = ["def-weil-pbc-eight-curve-assertions", "thm-sc-constant-invariance"]
+++
Let $k\subseteq k'$ be algebraically closed, let $C$ be a smooth separated
curve over $k$, and let $r$ be prime to $\operatorname{char}k$. Then the
constant sheaf $\mathbf F_r$ satisfies $\mathcal C_6(C,\mathbf F_r)$ of [def-weil-pbc-eight-curve-assertions]: the
pullback maps $\rho^q_{k'/k}(C,\mathbf F_r)$ are isomorphisms for every
$q\geq0$.

## Proof

This is the invariance part of [thm-sc-constant-invariance] (applied to
$n=r$); the maps are the pullback maps of the curve-calculation chapter and
agree with those fixed in the eight-assertion definition.

Unresolved dependencies: def:sc-field-extension, def:sc-curves
