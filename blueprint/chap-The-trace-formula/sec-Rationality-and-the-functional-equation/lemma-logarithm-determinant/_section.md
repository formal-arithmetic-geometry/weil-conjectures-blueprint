+++
id = "lemma-logarithm-determinant"
kind = "lemma"
title = "Logarithm of a determinant"
order = 1034
lean = ["LinearMap.inv_charpolyRev_eq_exp", "LinearMap.logOf_charpolyRev", "LinearMap.inv_alternatingCharpolyRevProd_eq_exp"]
+++
Let $L$ be a field of characteristic zero. For an endomorphism $v$ of
a finite-dimensional $L$-vector space $V$ we have

$$
\det(1-Tv\mid V)^{-1}
=\exp\left(\sum_{m\geq1}
\operatorname{Tr}(v^m\mid V)\frac{T^m}{m}\right)
\quad\text{in }1+TL[[T]].
\tag{12.5}
$$

For an endomorphism $v$ of a perfect complex $P$ in $D(L)$, put

$$
\det(1-Tv\mid P)
:=\prod_i\det(1-Tv\mid H^i(P))^{(-1)^i}.
$$

Then (12.5) holds for $P$, with
$\operatorname{Tr}(v^m\mid V)$ replaced by the categorical trace
$\operatorname{tr}_L(v^m\mid P)$.
