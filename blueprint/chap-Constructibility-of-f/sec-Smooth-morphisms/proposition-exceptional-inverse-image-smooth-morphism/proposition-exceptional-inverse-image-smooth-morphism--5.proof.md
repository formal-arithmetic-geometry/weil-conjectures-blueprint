+++
kind = "proof"
of = "proposition-exceptional-inverse-image-smooth-morphism--5"
order = 561012
uses = ["proposition-exceptional-inverse-image-smooth-morphism--1"]
+++
The chart argument proves invertibility of the canonical tensor maps at the
same time as the rank-one shape. Factor through the locus where the exponent
of $A$ is invertible and use
[proposition-exceptional-inverse-image-smooth-morphism--1] on an open cover.
The lemma `AlgebraicGeometry.Etale.isIso_dualizingComplexTensorMap_of_jointlySurjective`
descends the isomorphism from that cover. Compose back with the open
immersion into $S$. This is the last clause of
`AlgebraicGeometry.Etale.exists_dualizingComplex_iso_and_tensor`.

Finally use the symmetry of the derived tensor product. This last step is
packaged by
`AlgebraicGeometry.Etale.nonempty_iso_derivedTensor_leftDerivedUpperStar_obj_dualizingComplex`.
