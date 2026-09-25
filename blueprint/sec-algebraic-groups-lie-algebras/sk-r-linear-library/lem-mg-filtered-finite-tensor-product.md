+++
id = "lem-mg-filtered-finite-tensor-product"
kind = "lemma"
title = "Finite tensor products of filtered representations"
order = 2700
uses = ["def-mg-weil-composition-series", "lem-mg-filtered-tensor-product"]
+++
Let $V^{(a)}_\bullet$ be composition series for finite-dimensional Weil
representations $V^{(a)}$, with simple factors
$A^{(a)}_{i_a}$ ($1\le a\le k$). Then
$\bigotimes_{a=1}^{k}V^{(a)}$ has a finite Weil-stable filtration whose
nonzero successive quotients are

$$
\bigotimes_{a=1}^{k}A^{(a)}_{i_a},
$$

one for every tuple of indices.

## Proof

The input composition series are those of
[def-mg-weil-composition-series]. Induct on $k$. The case
$k=1$ is the given composition series.
For the induction step, apply
[lem-mg-filtered-tensor-product] to the already filtered tensor
$\bigotimes_{a<k}V^{(a)}$ and $V^{(k)}$, and refine each first-factor
quotient by its induction filtration. Pulling the resulting subspaces back
gives the asserted filtration; all maps are Weil-equivariant because the
input filtrations are Weil-stable.
