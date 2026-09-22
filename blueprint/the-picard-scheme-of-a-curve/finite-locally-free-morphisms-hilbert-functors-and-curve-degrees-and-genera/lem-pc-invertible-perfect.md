+++
id = "lem-pc-invertible-perfect"
kind = "lemma"
title = "Invertible modules are perfect"
order = 4277
lean = ["AlgebraicGeometry.isPerfect_of_invertible"]
uses = ["def-pc-perfect-complex", "def-pc-derived-category"]
+++
Let $X$ be a scheme and $\mathcal{M}$ an invertible $\mathcal{O}_X$-module.
Then $\mathcal{M}$, viewed as a complex in degree $0$, is perfect
[def-pc-perfect-complex].

## Proof

An invertible module is locally free of rank one: Zariski-locally
$\mathcal{M}\cong\mathcal{O}_X$, hence the bounded complex $\mathcal{M}$ in
degree $0$ is locally isomorphic to the free module $\mathcal{O}_X$ in
degree zero, which is a bounded complex of finite projective modules.

Unresolved dependencies: def:sc-invertible-module
