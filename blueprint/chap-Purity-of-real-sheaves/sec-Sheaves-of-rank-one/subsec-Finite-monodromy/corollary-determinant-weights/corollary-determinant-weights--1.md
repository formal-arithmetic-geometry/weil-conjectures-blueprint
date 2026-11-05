+++
id = "corollary-determinant-weights--1"
kind = "corollary"
title = "Finite geometric determinant and determinant weight"
name_showing = false
order = 1111001
aliases = ["bp-r341-1"]
lean = ["AlgebraicGeometry.WeilGroup.IsLisse.hasFiniteGeometricDet", "AlgebraicGeometry.WeilGroup.IsLisse.hasDetWeight"]
uses = ["situation-weil", "definition-weil-representation", "definition-determinant-weight", "definition-weights"]
+++
Let $U_0/k_0$ be a smooth geometrically connected curve, with the
coefficients and Weil group of Convention [situation-weil]. In the Lean
formulation, the degree-zero subgroup is assumed to be identified with
$\pi_1(U)$ compatibly with Frobenius. Let $\rho$ be a lisse
$\overline{\mathbf Q}_\ell$-representation of $W(U_0)$ on a
finite-dimensional space $V$, put $r=\dim V$, and let $s$ be the chosen
degree-one lift.

The set $\det\rho(\pi_1(U))$ is finite. Moreover, for every closed point
$x$ of $U_0$,

$$
\frac{2\log|\iota(\det\rho(\operatorname{Frob}_x))|}{\log q_x}
=r\,\frac{\lambda_\iota(\det\rho(s))}{r}.
$$

The quotient on the right is interpreted as zero when $r=0$; in this
case $\det\rho$ is the trivial character. For $r>0$, the formula says
that the determinant line is punctually $\iota$-pure of weight
$r\operatorname{dw}_\iota(\mathcal V)$, where $\mathcal V$ is the sheaf
corresponding to $\rho$.
