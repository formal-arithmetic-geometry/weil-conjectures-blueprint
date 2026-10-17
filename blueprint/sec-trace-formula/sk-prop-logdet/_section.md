+++
id = "sk-prop-logdet"
kind = "lemma"
title = "Logarithm of a determinant"
order = 2640
uses = ["sk-def-frobmod", "sk-p-linear-triangular", "sk-p-trace"]
lean = ["LinearMap.inv_charpolyRev_eq_exp"]
tags = ["sketch"]
+++
Let $L$ be a field of characteristic zero. For an endomorphism $v$ of
a finite-dimensional $L$-vector space $V$,

$$
 \det(1-Tv\mid V)^{-1}
  =\exp\left(\sum_{m\geq1}
       \operatorname{Tr}(v^m\mid V)\frac{T^m}{m}\right)
 \quad\text{in }1+TL[[T]].
 \tag{1}
$$

For an endomorphism $v$ of a perfect complex $P$ in $D(L)$, put

$$
 \det(1-Tv\mid P)
  :=\prod_i\det(1-Tv\mid H^i(P))^{(-1)^i}.
$$

Then (1) holds for $P$, with
$\operatorname{Tr}(v^m\mid V)$ replaced by the categorical trace
$\operatorname{tr}_L(v^m\mid P)$.

*Complement.* Equivalently, for $v$ on $V$ as above,

$$
\log\det(1-Tv\mid V)=-\sum_{m\ge1}\operatorname{Tr}(v^{m}\mid V)\frac{T^{m}}{m}
\quad\text{in }L[[T]].
$$

In particular, for a Frobenius module $(V,F)$ of [sk-def-frobmod] (the case
$L=\overline{\mathbf Q}_\ell$),
$\exp\bigl(\operatorname{tr}_F(T)\bigr)=\det(1-TF\mid V)^{-1}$ and
$\log\det(1-TF\mid V)=-\operatorname{tr}_F(T)$ in $\overline{\mathbf Q}_\ell[[T]]$.
