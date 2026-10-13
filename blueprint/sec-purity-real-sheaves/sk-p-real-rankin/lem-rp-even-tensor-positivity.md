+++
id = "lem-rp-even-tensor-positivity"
kind = "lemma"
title = "Even tensor powers of a real sheaf are positive"
order = 3005
uses = ["def-real-weil-representation-operations", "def-weil-pbc-scheme-conventions", "def-wf-iota-real", "def-wf-weil-category", "p-linear-spectra"]
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
