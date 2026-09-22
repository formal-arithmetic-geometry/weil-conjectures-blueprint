+++
id = "lem-sc-C1"
kind = "lemma"
title = "C1: vanishing above degree two"
order = 4542
lean = ["AlgebraicGeometry.Curve.C1_constant"]
uses = ["def-weil-pbc-eight-curve-assertions", "lem-sc-cohomological-dimension"]
+++
Let $k$ be algebraically closed, let $C$ be a smooth separated curve over
$k$, and let $n$ be a prime. Then the constant sheaf $\mathbf F_n$ satisfies
$\mathcal C_1(C,\mathbf F_n)$ of [def-weil-pbc-eight-curve-assertions]: $H^q(C_{\Et},\mathbf F_n)=0$ for every
$q>2$.

## Proof

The sheaf $\mathbf F_n$ is torsion; the assertion is
[lem-sc-cohomological-dimension] applied to it.

Unresolved dependencies: def:weil-pbc-etale-sheaves, def:sc-curves
