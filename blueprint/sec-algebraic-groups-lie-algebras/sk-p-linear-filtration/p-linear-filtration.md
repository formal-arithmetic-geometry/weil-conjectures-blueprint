+++
id = "p-linear-filtration"
kind = "theorem"
title = "Characteristic polynomials along a filtration"
order = 2889
tags = ["latex:proposition"]
lean = ["LinearMap.charpoly_eq_charpoly_restrict_mul_charpoly_mapQ", "Module.End.hasEigenvalue_of_subquotient"]
+++
Let $f$ be an endomorphism of a finite-dimensional
$k$-space $V$ and let $S\subseteq V$ be an $f$-stable subspace. Then the
characteristic polynomials satisfy

$$
\det(T-f\mid V)=\det(T-f\mid S)\,\det(T-f\mid V/S)
$$

(more generally this holds over a commutative ring, for a finite free
module $V$ and an $f$-stable submodule $S$ with $S$ and $V/S$ finite
free). Moreover, if $U\subsetneq S\subseteq V$ are $f$-stable subspaces
and $f$ acts on the nonzero subquotient $S/U$ as a scalar $c$, then $c$
is an eigenvalue of $f$ on $V$.
