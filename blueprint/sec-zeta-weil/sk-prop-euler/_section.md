+++
id = "sk-prop-euler"
kind = "proposition"
title = "Closed-point Euler product and integrality"
order = 3180
lean = ["AlgebraicGeometry.Scheme.Hom.pointCount_eq_sum", "AlgebraicGeometry.Scheme.Hom.zetaSeries_eq_tprod", "AlgebraicGeometry.Scheme.Hom.exists_int_zetaSeries"]
uses = ["sk-def-zeta"]
tags = ["sketch"]
+++
Let $Y_0$ be a finite-type $\Fq$-scheme, $|Y_0|$ its closed points and
$c_r=\#\{y\in|Y_0|:\deg(y)=r\}$. Then

$$
\#Y_0(\Fqn)=\sum_{r\mid n}r\,c_r
\qquad\text{and}\qquad
Z(Y_0,T)=\prod_{y\in|Y_0|}\bigl(1-T^{\deg(y)}\bigr)^{-1}\in1+T\Z[[T]].
$$

The product is coefficientwise locally finite: modulo $T^{m+1}$ only closed
points of degree $\le m$ occur.
