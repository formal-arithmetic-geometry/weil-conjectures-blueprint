+++
id = "def-zla-recip-charpoly"
kind = "definition"
title = "Reciprocal characteristic polynomial"
order = 989
+++
For a finite-dimensional $E$-vector space $V$ and
$u\in\operatorname{End}_E(V)$, define

$$
P_{V,u}(T)=\det(1-Tu\mid V)\in E[T].
$$

After scalar extension to an algebraic closure $\Omega/E$, write

$$
P_{V,u}(T)=\prod_{j=1}^{\dim_EV}(1-\alpha_jT).
$$

The multiset $\{\alpha_j\}$, with algebraic multiplicities, is the multiset of
*reciprocal roots* of $P_{V,u}$; it is the eigenvalue multiset of $u$.
If $u$ is invertible then every $\alpha_j\neq0$, $\deg P_{V,u}=\dim_EV$, and
the leading coefficient is
$[T^{\dim V}]P_{V,u}=(-1)^{\dim V}\det(u)$.
