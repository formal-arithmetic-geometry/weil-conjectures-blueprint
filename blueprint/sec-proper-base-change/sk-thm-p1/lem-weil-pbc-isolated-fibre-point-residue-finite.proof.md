+++
kind = "proof"
of = "lem-weil-pbc-isolated-fibre-point-residue-finite"
uses = ["def-weil-finite-type-morphism"]
+++
Apply Mathlib Scheme.Hom.quasiFiniteAt_iff_isOpen_singleton_asFiber (Mathlib/AlgebraicGeometry/Morphisms/QuasiFinite.lean:395) to the isolated fibre point. Since f is locally of finite type, its stalk map at x is quasi-finite. No change of the scheme or the point is necessary. (`AlgebraicGeometry.Scheme.Hom.fiber` ([Mathlib source](https://github.com/leanprover-community/mathlib4/blob/master/Mathlib/AlgebraicGeometry/Fiber.lean)), [def-weil-finite-type-morphism]).

The quotient map from the stalk at x to its residue field is surjective (Scheme.residue_surjective), hence finite (RingHom.Finite.of_surjective) and quasi-finite (RingHom.QuasiFinite.of_finite). Compose it with the quasi-finite stalk map. Scheme.residue_residueFieldMap identifies this composition with the residue-field map composed with the quotient from the base stalk. RingHom.QuasiFinite.of_comp therefore makes the residue-field map itself quasi-finite. These are direct applications of Mathlib/RingTheory/RingHom/QuasiFinite.lean:37,42,51 and Mathlib/AlgebraicGeometry/ResidueField.lean:80,128. (`AlgebraicGeometry.Scheme.residueField` ([Mathlib source](https://github.com/leanprover-community/mathlib4/blob/master/Mathlib/AlgebraicGeometry/ResidueField.lean))).

Install the algebra structure induced by the residue-field map, as in the statement. Its quasi-finiteness is the result of step 2. Apply Module.Finite.of_quasiFinite (Mathlib/RingTheory/QuasiFinite/Basic.lean:141): the base residue field is a field, hence Artinian. Module.Finite over a field is FiniteDimensional, giving precisely the required extension. (`Algebra` ([Mathlib source](https://github.com/leanprover-community/mathlib4/blob/master/Mathlib/Algebra/Algebra/Defs.lean))).
