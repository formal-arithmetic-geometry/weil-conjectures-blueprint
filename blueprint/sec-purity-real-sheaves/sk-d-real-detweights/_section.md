+++
id = "sk-d-real-detweights"
kind = "corollary"
title = "Determinant weights"
order = 3858
uses = ["sk-cor-wrp-rankone-pure", "sk-d-weights", "sk-p-real-rankone"]
lean = ["AlgebraicGeometry.WeilGroup.HasDetWeight"]
tags = ["sketch"]
+++
Let $\mathcal V$ be a nonzero lisse Weil sheaf of rank $r$ on a smooth
geometrically connected curve. Its determinant has finite geometric
image and is punctually pure. Define

$$
 \operatorname{dw}_\iota(\mathcal V)
   =\frac{\lambda_\iota(\det\rho(s))}{r}.
$$

This number is independent of $s$ and of a finite coefficient model, and
$\det\mathcal V$ is pure of weight $r\operatorname{dw}_\iota(\mathcal V)$.
In particular every irreducible constituent, including every constituent
of a tensor or exterior construction, satisfies the finite geometric
determinant condition used in [sec-algebraic-groups-lie-algebras].

*Complement.* For a lisse Weil sheaf, its constituent determinant weights are
the numbers $\operatorname{dw}_\iota(V_a)$ of its irreducible constituents
$V_a$; the rank-counted list repeats $\operatorname{dw}_\iota(V_a)$ exactly
$\operatorname{rank}V_a$ times ([def-mg-determinantal-weight-multiset]). For
these constituents $\operatorname{dw}_\iota$ agrees with the determinant
weight $\operatorname{dw}_{\lambda_\iota}$ of [sk-d-weights]
([lem-rp-determinant-weights-agree]).
