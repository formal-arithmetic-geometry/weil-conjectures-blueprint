+++
id = "def-sc-hilbert-degree"
kind = "definition"
title = "The Hilbert degree of an ample line bundle"
lean = ["AlgebraicGeometry.Scheme.Hom.degree", "AlgebraicGeometry.Scheme.Hom.degree_eq_sum", "AlgebraicGeometry.Scheme.Hom.exists_polynomial_degree_eq_factorial_mul_coeff"]
order = 465
uses = ["def-sc-ample"]
+++
Let $X$ be a scheme over a field $k$ and $\mathcal M$ an
$\mathcal O_X$-module. Let $g$ be the Krull dimension of the
underlying topological space of $X$ (read as $g=0$ if $X$ is empty or
infinite-dimensional). The *degree* of $X$ with respect to $\mathcal M$
is the $g$-th forward difference at $0$ of the Hilbert function
$m\mapsto\chi(X,\mathcal M^{\otimes m})$:

$$
\deg_{\mathcal M}(X):=\sum_{i=0}^{g}(-1)^{g-i}\binom gi\,
\chi(X,\mathcal M^{\otimes i}).
$$

When $X$ is proper and $\mathcal M$ is an ample invertible module, the
Hilbert function is a numerical polynomial of degree at most $g$
([lem-sc-hilbert-polynomial]), and $\deg_{\mathcal M}(X)$ is $g!$
times its coefficient of $m^g$.
