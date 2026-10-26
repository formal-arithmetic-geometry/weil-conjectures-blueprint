+++
id = "lem-rp-even-tensor-positivity"
kind = "lemma"
title = "Even tensor powers of a real sheaf are positive"
lean = ["AlgebraicGeometry.WeilGroup.IsReal.tensorPower", "AlgebraicGeometry.WeilGroup.IsReal.hasNonnegCoeffs_eulerFactor_tensorPower", "AlgebraicGeometry.WeilGroup.IsReal.hasNonnegCoeffs_eulerFactor_tprod_self"]
order = 3857
uses = ["def-real-weil-representation-operations", "def-weil-pbc-scheme-conventions", "def-weil-weil-sheaf-complex", "def-wf-iota-real", "p-linear-spectra", "sk-lem-coefficient-heart"]
+++
Let $\mathcal G_0$ be a lisse
$\iota$-real
Weil sheaf on a
separated finite-type
$k_0$-scheme. Then for every closed point $x$ and every
$k\ge1$, with $\mathcal G_0^{\otimes k}$ the $k$-fold tensor power of
[def-real-weil-representation-operations]:

**(i)** the local characteristic polynomial
$\iota\det(1-tF_x,\mathcal G^{\otimes k}_{0,\bar x})$ has real
coefficients;
**(ii)** if $k$ is even, the power series
$$
\iota\det(1-tF_x,\mathcal G^{\otimes k}_{0,\bar x})^{-1}
=\sum_{n\ge0}a_nt^n
$$
has all coefficients $a_n\ge0$, and its constant term is $1$.
