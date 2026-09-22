+++
id = "lem-fin-projective-curve-betti-cardinalities"
kind = "lemma"
title = "Betti cardinalities in a smooth projective curve family"
order = 5185
lean = ["AlgebraicGeometry.Etale.isConstructible_bettiCard_of_smoothProjective_curve"]
uses = ["def-sbc-smooth-morphisms", "lem-fin-projective-flat-coherent-ranks"]
+++
Let $S$ be Noetherian and let $f:X\to S$ be smooth
[def-sbc-smooth-morphisms] and projective, with geometric fibres of pure
dimension one. Fix a prime $\ell$ invertible on $S$. Write $c_s$ for the
number of connected components of the smooth proper curve $X_{\bar s}$, and
$g_s=\sum_Dg(D)$ for the sum of the genera over its connected components.
Then the étale cohomology cardinalities are
$$
|H^r(X_{\bar s},\mathbf F_\ell)|=
\begin{cases}
\ell^{c_s},&r=0,2,\\
\ell^{2g_s},&r=1,\\
1,&r>2,
\end{cases}
$$
and each of these functions of $s$ is constructible.

## Proof

A smooth geometric fibre is regular. Its finitely many irreducible
components are disjoint, since a regular local ring is a domain. Thus its
connected components are integral smooth proper curves. Each contributes one
copy of $\kappa(\bar s)$ to $H^0(\mathcal O)$, and its genus is its
$H^1(\mathcal O)$ dimension. Cohomology on a finite disjoint union is the
direct sum of the component cohomologies, so
$$
c_s=h^0(X_{\bar s},\mathcal O),\qquad g_s=h^1(X_{\bar s},\mathcal O).
$$

Smoothness includes flatness by [def-sbc-smooth-morphisms]; apply
[lem-fin-projective-flat-coherent-ranks] to
$\mathcal G=\mathcal O_X$. It proves constructibility of both functions,
without assuming all components have the same genus.

The twist trivialization by a primitive root of unity and the Kummer
computation on a proper curve give ranks $1,2g(D),1$ in degrees $0,1,2$ on
each component. Vanishing above degree two is the cohomological-dimension
bound for a smooth curve. Sum over components and take cardinalities to
obtain the formula and its constructibility.

Unresolved dependencies: def:pc-projective-morphism, def:sc-curves, def:sc-genus, def:weil-pbc-scheme-conventions, def:weil-pbc-etale-cohomology, lem:sc-global-functions, thm:sc-proper-cohomology, lem:sc-cohomological-dimension, def:sc-mu-trivialization
