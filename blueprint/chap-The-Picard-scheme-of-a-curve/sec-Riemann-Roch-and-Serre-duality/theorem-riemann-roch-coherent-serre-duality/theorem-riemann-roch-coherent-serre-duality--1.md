+++
id = "theorem-riemann-roch-coherent-serre-duality--1"
kind = "theorem"
title = "Riemann–Roch and coherent Serre duality (1)"
name_showing = false
order = 1525001
aliases = ["bp-r475-1"]
lean = ["AlgebraicGeometry.Scheme.Modules.eulerChar_eq_degree_add"]
uses = []
+++
Let $C$ be a smooth proper curve over a field $k$ such that
$k\to H^0(C,\mathcal O_C)$ is an isomorphism, and put
$g=h^1(C,\mathcal O_C)$. For an $\mathcal O_C$-module $\mathcal M$,
use the cohomological definition
$\deg\mathcal M=\chi(C,\mathcal M)-\chi(C,\mathcal O_C)$. Then

$$
\chi(C,\mathcal M)=\deg\mathcal M+1-g.
$$

For arbitrary $\mathcal M$, the Euler characteristic here uses the
finitely supported alternating sum of $h^q(C,\mathcal M)$, with
$h^q=0$ for an infinite-dimensional cohomology group and the sum set to
zero if infinitely many terms are nonzero. For an invertible sheaf
$\mathcal L$, cohomology is finite-dimensional and vanishes above degree
one; the cohomological degree agrees with the divisor degree, so this
is the usual Riemann–Roch formula.
