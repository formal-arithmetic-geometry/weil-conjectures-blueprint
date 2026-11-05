+++
id = "corollary-determinant-weights--1"
kind = "corollary"
title = "Finite geometric determinant and determinant weight"
order = 1114001
aliases = ["bp-r341-1"]
lean = ["AlgebraicGeometry.WeilGroup.IsLisse.hasDetWeight", "AlgebraicGeometry.WeilGroup.IsLisse.hasFiniteGeometricDet"]
uses = ["definition-determinant-weight--1"]
+++
Let $U_0/k_0$ be a smooth geometrically connected curve, with the
coefficients and Weil group of Convention [sec-Weil-sheaves-and-weights]. Let $\rho$ be a lisse
$\overline{\mathbf Q}_\ell$-representation of $W(U_0)$ on a
finite-dimensional space $V$, put $r=\dim V$, and let $s$ be the chosen
degree-one lift.

The set $\det\rho(\pi_1(U))$ is finite. Moreover, for every closed point
$x$ of $U_0$,

$$
\frac{2\log|\iota(\det\rho(\operatorname{Frob}_x))|}{\log q_x}
=\lambda_\iota(\det\rho(s)).
$$

When $r=0$, $\det\rho$ is the trivial character and both sides vanish. For
$r>0$, since $\operatorname{dw}_\iota(\mathcal V)=\lambda_\iota(\det\rho(s))/r$
(Definition [definition-determinant-weight]), the formula says that the
determinant line is punctually $\iota$-pure of weight
$r\operatorname{dw}_\iota(\mathcal V)$, where $\mathcal V$ is the sheaf
corresponding to $\rho$.
