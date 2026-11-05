+++
kind = "proof"
of = "lemma-inverse-image-tensor-product--1"
order = 494003
uses = ["proposition-topos-functoriality", "lemma-inverse-image-coefficient-sheaves", "definition-lisse-sheaves"]
+++
The coefficient isomorphism of [lemma-inverse-image-coefficient-sheaves]
identifies pullback of module objects with the exact inverse image on
sheaves. Thus
$$
H^q(\mathbf Lf^*K)\simeq f^*H^q(K),
$$
as recorded by `AlgebraicGeometry.ProEtale.CondensedRing.leftDerivedUpperStarHomologyIso`.
The cohomological bounds of $K$ therefore also bound $\mathbf Lf^*K$.
Pull back a stratification for each $H^q(K)$ and its pro-étale covers.
Finite presentations pull back to finite presentations, so the cohomology
sheaves remain constructible. This is
`AlgebraicGeometry.ProEtale.CondensedRing.IsConstructibleModuleObject.upperStar`.
