+++
kind  = "proof"
of    = "sk-thm-tracetodeterminant"
uses = ["sk-cor-tf-point-counting", "sk-def-zeta", "sk-prop-logdet"]
+++
By [sk-cor-tf-point-counting] the point counts are alternating traces,
$N_n=\sum_i(-1)^{i}\Tr(F_{i,\ell}^{n}\mid V_{i,\ell})$. Substituting into the
exponential definition of [sk-def-zeta] and exchanging the finite $i$-sum
with the power series,

$$
\log Z(X_0,T)=\sum_{n\ge1}\Bigl(\sum_i(-1)^{i}\Tr(F_{i,\ell}^{n}\mid
V_{i,\ell})\Bigr)\frac{T^{n}}{n}
=\sum_i(-1)^{i}\sum_{n\ge1}\Tr(F_{i,\ell}^{n})\frac{T^{n}}{n}.
$$

By [sk-prop-logdet] the inner series is $-\log P_{i,\ell}(T)$, so
$\log Z=\sum_i(-1)^{i+1}\log P_{i,\ell} =\log\prod_iP_{i,\ell}^{(-1)^{i+1}}$. Exponentiating gives the identity; it
lies in $\Ql(T)$ because the right side is a finite product of rational
functions with constant term $1$, and in $\Ql[[T]]$ because the left side is.
