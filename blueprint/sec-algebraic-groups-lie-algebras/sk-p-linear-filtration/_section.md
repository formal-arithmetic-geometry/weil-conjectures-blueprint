+++
id = "sk-p-linear-filtration"
kind = "section"
title = "Characteristic polynomials along a filtration"
order = 2548
uses = ["sk-d-linear"]
lean = ["LinearMap.charpoly_eq_charpoly_restrict_mul_charpoly_mapQ", "Module.End.hasEigenvalue_of_subquotient"]
+++
*Proposition (sketch).*

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

## Proof

Let $R$ be the base ring ($R=k$ for the first assertion) and $T$ an
indeterminate. Since $V/S$ is free, a basis of $S$ together with lifts of a
basis of $V/S$ is a basis of $V$. In it the matrix of $f$ is block upper
triangular, with diagonal blocks the matrices of $f$ on $S$ and on $V/S$;
so the matrix of $T-f$ over $R[T]$ is block upper triangular with
diagonal blocks those of $T-f$ on $S$ and on $V/S$, and its determinant is
the product of the two block determinants. This is the displayed formula.

For the second assertion (over the field $k$, where all subspaces and
quotients are free), let $f$ act on $S/U\ne0$ by the scalar $c$ and put
$B=f-c$, which preserves $U$ and $S$. Applying the factorization to $B$
along $S\subseteq V$, and then to $B|_S$ along $U\subseteq S$, gives
$$
\det(B\mid V)=\det(B\mid U)\,\det(B\mid S/U)\,\det(B\mid V/S).
$$
The middle factor is the determinant of the zero map on a space of
positive dimension, hence zero, so $\det(f-c\operatorname{id}_V)=0$ and $c$
is an eigenvalue of $f$ on $V$.
