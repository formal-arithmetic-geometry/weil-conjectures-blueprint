+++
kind  = "proof"
of    = "thm-weil-pbc-integral-truncations"
+++
Take the reduction tower and its local models. By
[prop-weil-pbc-levelwise-truncations] (whose Tor-compatibility condition (1)
holds here by the hypothesis of the statement), $\tau^{\le m}K_\bullet$ is an adic tower
which is uniformly bounded constructible and has compatible etale-origin
witnesses, so by the reconstruction lemma for uniform towers its derived
limit $\tau^{\le m}K$ is derived $I$-complete, has no cohomology outside the
model interval, and satisfies the reduction isomorphisms of (i) by the
finite-reduction reconstruction lemma; the same holds for
$\tau^{\ge m+1}K$. Hence both objects lie in $\Dbc(T_{\Proet},A)$ of
[def-weil-pbc-bounded-constructible-complete]. The cohomology formulas of
(ii) follow from (i) and the cohomology formulas of
[prop-weil-pbc-levelwise-truncations] (iii) at the reduction level, together
with the long exact cohomology sequence of the triangle of (iii) (the end
terms of the triangle are the two objects just constructed, with the
vanishing cohomology of (ii)); the functoriality and additivity are those of
the levelwise truncations and of the functor $\Rlim$. Since a truncation
triangle is characterized by the vanishing properties of its end terms, the
constructed truncations are the canonical truncations of the ambient
category. For (iii), the levelwise truncation triangles form a compatible
family under the normalization isomorphisms of
[prop-weil-pbc-levelwise-truncations] (i) (both the triangles and the
isomorphisms being canonical), hence a triangle in
$D(\operatorname{Tow}_A(T))$, whose image under the triangulated functor
$\Rlim$ is the displayed triangle; its functoriality is inherited from the
levelwise functoriality.
