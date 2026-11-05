+++
kind = "proof"
of = "proposition-proper-direct-image-constructible-complexes--11"
order = 425023
uses = ["lemma-change-coefficients-direct-image", "proposition-six-operations-change-coefficients", "proposition-proper-direct-image-constructible-complexes--10"]
+++
Extension of scalars along $\mathcal O_E\to E$ is exact and commutes with
pullback and tensor product. Its direct-image comparison is invertible on
$K_0$ and on $K_0\otimes^{\mathbf L}_{\mathcal O_E}p^*M_0$, since both are
bounded below and $p$ is quasi-compact and quasi-separated
[lemma-change-coefficients-direct-image]. These comparisons respect the
adjunction counits and hence carry the integral projection map to the rational
one. Applying extension of scalars to the assumed isomorphism proves the claim.

The proof uses
`AlgebraicGeometry.ProEtale.CondensedRing.isIso_derivedPushHom_app_padicIntegers_of_isGE`
at those two objects and
`AlgebraicGeometry.ProEtale.CondensedRing.isIso_projectionMap_app_app_extendScalars_of_isIso`.
For the proper constructible case the integral hypothesis is supplied by
[proposition-proper-direct-image-constructible-complexes--10].
