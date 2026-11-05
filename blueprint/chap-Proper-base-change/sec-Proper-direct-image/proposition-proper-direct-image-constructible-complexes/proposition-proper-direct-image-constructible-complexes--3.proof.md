+++
kind = "proof"
of = "proposition-proper-direct-image-constructible-complexes--3"
order = 425007
uses = ["proposition-proper-direct-image-constructible-complexes--2", "lemma-integral-models", "lemma-change-coefficients-direct-image", "corollary-coefficient-heart-b"]
+++
Equip $E$ with the norm induced by its embedding in
$\overline{\mathbf Q}_\ell$. The results
`AlgebraicGeometry.ProEtale.CondensedRing.ContinuousMapRingObj.finiteTypeDirectImage_single_boundedAbove`
and
`AlgebraicGeometry.ProEtale.CondensedRing.ContinuousMapRingObj.finiteTypeDirectImage_single_constructible`
give an upper bound and constructible cohomology for the direct image of each
constructible $E$-sheaf in degree zero. Their coefficient argument uses an
integral model [lemma-integral-models], exact inversion of $\ell$, and the
comparison of direct image with change of coefficients
[lemma-change-coefficients-direct-image].

The direct image is left t-exact. Thus each of these degree-zero sheaves has
bounded constructible direct image, and finite truncation dévissage gives the
claim for every $K\in\Dbc(X,E)$. The target is triangulated, as in
[corollary-coefficient-heart-b].
