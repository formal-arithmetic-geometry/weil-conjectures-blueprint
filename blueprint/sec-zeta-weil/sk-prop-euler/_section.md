+++
id = "sk-prop-euler"
kind = "section"
title = "Closed-point Euler product and integrality"
order = 2876
lean = ["AlgebraicGeometry.Scheme.Hom.pointCount_eq_sum", "AlgebraicGeometry.Scheme.Hom.zetaSeries_eq_tprod", "AlgebraicGeometry.Scheme.Hom.exists_int_zetaSeries"]
uses = ["sk-def-zeta"]
+++
*Proposition (sketch).*

Let $Y_0$ be a finite-type $\Fq$-scheme, $|Y_0|$ its closed points and
$c_r=\#\{y\in|Y_0|:\deg(y)=r\}$. Then

$$
\#Y_0(\Fqn)=\sum_{r\mid n}r\,c_r
\qquad\text{and}\qquad
Z(Y_0,T)=\prod_{y\in|Y_0|}\bigl(1-T^{\deg(y)}\bigr)^{-1}\in1+T\Z[[T]].
$$

The product is coefficientwise locally finite: modulo $T^{m+1}$ only closed
points of degree $\le m$ occur.

## Proof

The points of $Y_0(\Fqn)$ are the closed points of degree $r\mid n$, each
contributing $r$ points (the $\deg(y)$ embeddings of $\kappa(y)$ into
$\Fqn$); this is the geometric-Frobenius orbit decomposition and gives the
first identity. Taking $\log$ of the product and expanding each factor,
$\log\prod_y(1-T^{\deg y})^{-1}=\sum_y\sum_{m\ge1}T^{m\deg y}/m =\sum_{n\ge1}\bigl(\sum_{r\mid n}rc_r\bigr)T^{n}/n =\sum_{n\ge1}N_nT^{n}/n$, which is $\log Z$ by [sk-def-zeta].
Integrality is inherited from the exponential definition, and only finitely
many closed points of degree $\le m$ exist because $Y_0$ is of finite type
over a finite field.

Uses: [sk-def-zeta]
