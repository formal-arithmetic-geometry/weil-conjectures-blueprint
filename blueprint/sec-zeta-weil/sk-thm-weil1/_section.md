+++
id = "sk-thm-weil1"
kind = "theorem"
title = "Weil conjectures I: rationality and Euler product"
order = 3231
lean = ["AlgebraicGeometry.Scheme.zetaSeries_rational", "AlgebraicGeometry.Scheme.Hom.zetaSeries_eq_tprod"]
uses = ["sk-def-zeta", "sk-thm-rationality"]
tags = ["sketch"]
+++
Let $X_0$ be a scheme of finite type (quasi-compact and locally of finite
type) over $\Fq$. Then there are $A,B\in\Z[T]$ with $B(0)=1$ and
$B(T)\,Z(X_0,T)=A(T)$ in $\Q[[T]]$; in particular
$Z(X_0,T)\in1+T\Z[[T]]\cap\Q(T)$. Moreover
$Z(X_0,T)=\prod_{x\in|X_0|}(1-T^{\deg(x)})^{-1}$ in $\Q[[T]]$, the product
over the closed points of $X_0$.
