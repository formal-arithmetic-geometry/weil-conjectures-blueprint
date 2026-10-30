+++
id = "sk-d-real-detweights"
kind = "corollary"
title = "Determinant weights"
order = 655
lean = ["AlgebraicGeometry.WeilGroup.HasDetWeight"]
uses = ["sk-d-real-weil", "sk-r-real-linear", "sk-p-real-rankone", "sk-cor-wrp-rankone-pure"]
tags = ["sketch"]
+++
Let $\mathcal V$ be a nonzero lisse Weil sheaf of rank $r$ on a smooth
geometrically connected curve. Its determinant has finite geometric
monodromy and is punctually pure. Define

$$
\operatorname{dw}_\iota(\mathcal V)
=\frac{\lambda_\iota(\det\rho(s))}{r}.
$$

Here $\rho$ is the representation of $W(U_0)$ corresponding to
$\mathcal V$ and $s$ is a lift of degree one. This number is independent of $s$ and of a finite coefficient model, and
$\det\mathcal V$ is pure of weight $r\operatorname{dw}_\iota(\mathcal V)$.
This applies in particular to every irreducible constituent of
$\mathcal V$ and of every tensor or exterior construction on
$\mathcal V$, since these are again nonzero lisse Weil sheaves on the
curve.

*Complement.* For a lisse Weil sheaf, its constituent determinant weights are
the numbers $\operatorname{dw}_\iota(V_a)$ of its irreducible constituents
$V_a$; the rank-counted list repeats $\operatorname{dw}_\iota(V_a)$ exactly
$\operatorname{rank}V_a$ times ([def-mg-determinantal-weight-multiset]).
