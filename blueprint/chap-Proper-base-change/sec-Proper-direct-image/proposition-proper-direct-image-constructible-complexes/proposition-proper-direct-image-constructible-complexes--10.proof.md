+++
kind = "proof"
of = "proposition-proper-direct-image-constructible-complexes--10"
order = 425021
uses = ["proposition-proper-direct-image-constructible-complexes--2", "proposition-proper-direct-image-constructible-complexes--9", "lemma-integral-models", "lemma-reduction-derived-nakayama", "proposition-integral-constructibility-criterion", "lemma-change-coefficients-direct-image", "proposition-six-operations-change-coefficients"]
+++
The source and target of the projection formula map are bounded constructible:
use [proposition-proper-direct-image-constructible-complexes--2] and stability
under inverse image and tensor product [lemma-integral-models]. Derived
Nakayama [lemma-reduction-derived-nakayama] reduces invertibility to the first
derived reduction.

Extension of scalars to $\mathbf F_E$ carries the integral projection map to
the residue-field projection map: the pullback comparison is monoidal and the
direct-image comparison is invertible on the bounded-below complexes in
question. The equivalence with sheaves of $\mathbf F_E$-modules then identifies
it with the map of
[proposition-proper-direct-image-constructible-complexes--9]. That map is
invertible, so the integral map is invertible. Lean uses
`AlgebraicGeometry.ProEtale.CondensedRing.isIso_map_projectionMap_derivedExtendScalars_residueField`
and `AlgebraicGeometry.ProEtale.CondensedRing.isIso_projectionMap_residueField_of_moduleCat`
for these two comparisons, and
`AlgebraicGeometry.ProEtale.isIso_of_isIso_derivedReduction_map` to conclude.
