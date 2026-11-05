+++
kind = "proof"
of = "proposition-proper-direct-image-constructible-complexes--9"
order = 425019
uses = ["theorem-bounded-below-cohomology-comparison", "proposition-comparison-morphism-inverse-image"]
+++
Choose bounded constructible étale models $K_0$ and $M_0$. Since $A$ is a field,
$M_0$ has finite Tor amplitude, so $K_0\otimes^{\mathbf L}_A p^*M_0$ is bounded
below. The finite-coefficient étale projection formula gives an isomorphism.
The comparison of direct image and tensor product with $\nu^*$ carries this map
to the pro-étale projection map. Transport along the two chosen étale-origin
isomorphisms concludes.

The intermediate statements are
`AlgebraicGeometry.Etale.DerivedCategory.finiteTorAmplitude_of_boundedConstructible_of_field`,
`AlgebraicGeometry.Etale.isIso_rightDerivedLowerStarProjectionMap_of_finite` and
`AlgebraicGeometry.ProEtale.isIso_rightDerivedLowerStarProjectionMap_app_app_leftDerived`.
