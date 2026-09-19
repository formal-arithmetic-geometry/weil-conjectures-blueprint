+++
id = "def-zla-weight-stratum"
kind = "definition"
title = "Weight stratum of a rational polynomial"
order = 1021
+++
Let $R\in\mathbf Q[T]$ satisfy $R(0)=1$. Since $R(0)\neq0$, no irreducible
factor of $R$ is a scalar multiple of $T$, so $R$ has a factorization

$$
R=\prod_{j}F_j^{m_j},
\qquad
F_j\in\mathbf Q[T]\text{ irreducible},\quad F_j(0)=1,
$$

with the $F_j$ pairwise distinct and $m_j\geq1$, and this normalized
irreducible factorization is unique. For a real number $w$, the
*weight-$w$ stratum* of $R$ is

$$
R_w(T)=\prod_{j\in J_w}F_j(T)^{m_j},
\qquad
J_w=\{j:|z|=q^{-w/2}\text{ for every complex root }z\text{ of }F_j\},
$$

the product of those normalized irreducible rational factors of $R$ all of
whose complex roots have absolute value $q^{-w/2}$, taken with the
multiplicities they have in $R$.
