+++
id = "sk-thm-trace-transport"
kind = "theorem"
title = "Transport of the trace formula to the non-finite stages"
order = 2394
uses = ["sk-d-setup", "sk-d-six", "sk-d-trace", "sk-d-weil", "sk-def-sf-weil-complexes", "sk-i-curve-zero", "sk-p-trace-coeff", "sk-prop-cd", "sk-prop-logdet", "sk-prop-trace-adic", "sk-thm-sf-ctf-stability", "sk-thm-trace-formula"]
lean = ["AlgebraicGeometry.ProEtale.hasProd_inv_alternatingCharpolyRevProd"]
tags = ["sketch"]
+++
Let the coefficient ring range over the three non-finite stages

$$
\Lambda\in\{\mathcal O_E,\ E,\ \overline{\mathbf Q}_\ell\},
$$

the $\mathcal O_E$-stage being the normalized systems of
finite-level objects, the $E$-stage its
rationalization, and the $\overline{\mathbf Q}_\ell$-stage the colimit over
finite $E/\mathbf Q_\ell$. Let $X_0/\mathbf F_q$ be separated of finite
type and let $K$ be a Weil datum with coefficients in
$\Lambda$, that is, a Weil pair at the stage $\Lambda$ in the all-stage
sense of [sk-def-sf-weil-complexes]: at $\mathcal O_E$ a normalized system
of finite-level Weil pairs ([sk-d-weil]) whose transitions commute with the
$\varphi_n$ (a compatible tower of Weil pairs as in
[sk-prop-trace-adic](ii)), and at $E$ and $\overline{\mathbf Q}_\ell$ its
rationalization and colimit. Then:

1. **(a)** *Trace identity.* The identity of
[sk-thm-trace-formula] holds for every $m\ge1$ with $A$ replaced by
$\Lambda$, with compact cohomology and
ordinary traces taken at the stage $\Lambda$.
1. **(b)** *Euler-product form.* Let
$\Lambda\in\{E,\overline{\mathbf Q}_\ell\}$, write $e_x$ for the degree of
a closed point $x\in|X_0|$, and put
$$
L(X_0,K,T)=\prod_{x\in|X_0|}
\det\bigl(1-T^{e_x}F_x\mid K_{\bar x}\bigr)^{-1}
\in1+T\Lambda[[T]],
$$
a locally finite product. For a complex, the stalk determinant denotes
the alternating product of the determinants on its cohomology. Then
$$
L(X_0,K,T)=\prod_{i}
\det\bigl(1-TF\mid H_c^i(X,K)\bigr)^{(-1)^{i+1}}
$$
as formal power series, the product being finite; if $X_0$ is a curve and $K$ is a sheaf in degree zero, it
runs over $0\le i\le2$. Any field embedding
$\iota:\overline{\mathbf Q}_\ell\to\mathbf C$ carries the identity to one
in $\mathbf C[[T]]$.
