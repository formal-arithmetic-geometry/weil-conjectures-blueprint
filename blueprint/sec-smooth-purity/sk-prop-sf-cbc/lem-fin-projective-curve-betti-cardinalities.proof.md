+++
kind  = "proof"
of    = "lem-fin-projective-curve-betti-cardinalities"
+++
A smooth geometric fibre is regular. Its finitely many irreducible
components are disjoint, since a regular local ring is a domain.
Thus its connected components are integral smooth proper curves.
By [lem-sc-global-functions], each contributes one copy of
$\kappa(\bar s)$ to $H^0(\mathcal O)$, and by
[def-sc-genus] its genus is its $H^1(\mathcal O)$ dimension.
Cohomology on a finite disjoint union is the direct sum of the
component cohomologies, so

$$
c_s=h^0(X_{\bar s},\mathcal O),\qquad
g_s=h^1(X_{\bar s},\mathcal O).
$$

Smoothness includes flatness by [def-sbc-smooth-morphisms];
apply [lem-fin-projective-flat-coherent-ranks] to
$\mathcal G=\mathcal O_X$. It proves constructibility of both
functions, without assuming all components have the same genus.
The twist trivialization of [def-sc-mu-trivialization] and the
curve computation [thm-sc-proper-cohomology] give ranks
$1,2g(D),1$ in degrees $0,1,2$ on each component.
Vanishing above degree two is
[lem-sc-cohomological-dimension]. Sum over components and
take cardinalities to obtain the formula and its constructibility.
