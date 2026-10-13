+++
id = "sk-prop-logdet"
kind = "proposition"
title = "Logarithm of the Frobenius determinant"
order = 2735
uses = ["sk-def-frobmod", "sk-p-linear-triangular"]
lean = ["LinearMap.inv_charpolyRev_eq_exp"]
tags = ["sketch"]
+++
Let $K$ be a field of characteristic zero, $V$ a finite-dimensional
$K$-vector space and $F$ a $K$-linear endomorphism of $V$ (not necessarily
invertible). Regard the polynomial $\det(1-TF\mid V)$, whose constant term
is $1$, as a formal power series. Then in $K[[T]]$

$$
\det(1-TF\mid V)^{-1}
=\exp\Bigl(\sum_{n\ge1}\Tr(F^{n}\mid V)\frac{T^{n}}{n}\Bigr),
\qquad\text{equivalently}\qquad
\log\det(1-TF\mid V)=-\sum_{n\ge1}\Tr(F^{n}\mid V)\frac{T^{n}}{n}.
$$

In particular, for a Frobenius module $(V,F)$ (the case $K=\Qlb$),
$\exp\bigl(\operatorname{tr}_F(T)\bigr)=\det(1-TF\mid V)^{-1}$ and
$\log\det(1-TF\mid V)=-\operatorname{tr}_F(T)$ in $\Qlb[[T]]$.
