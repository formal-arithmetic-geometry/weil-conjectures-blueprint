+++
id = "sk-prop-logdet"
kind = "section"
title = "Logarithm of the Frobenius determinant"
order = 2391
uses = ["sk-def-frobmod", "sk-p-linear-triangular"]
lean = ["LinearMap.inv_charpolyRev_eq_exp"]
+++
*Proposition (sketch).*

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

## Proof

Over the algebraically closed field $\Qlb$ put $F$ in upper triangular form
with diagonal $(\lambda_1,\dots,\lambda_m)$. Then
$\Tr(F^{n}\mid V)=\sum_j\lambda_j^{n}$ and
$\det(1-TF\mid V)=\prod_j(1-\lambda_jT)$. The formal logarithm is additive on
$1+T\Qlb[[T]]$ (compare derivatives), and
$\log(1-\lambda T)=-\sum_{n\ge1}\lambda^{n}T^{n}/n$; summing over the finite
index range gives the identity. Exponentiating, and using that the formal
exponential and logarithm are mutually inverse between $T\Qlb[[T]]$ and
$1+T\Qlb[[T]]$, gives the second form. No semisimplicity is used: the
computation is triangular and therefore valid for arbitrary $F$.
