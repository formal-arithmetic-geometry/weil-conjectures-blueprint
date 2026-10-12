+++
kind = "proof"
of = "lem-weil-pbc-finite-constant-set-sections-cover"
uses = ["def-weil-pbc-etale-sheaves", "def-weil-pbc-scheme-conventions"]
+++
For (1), specialize the proved finite-family lifting theorem in ConstantSheafSections to Type-valued sheaves and the given localized etale site. Its proof intersects the finitely many covering image sieves. For (2), specialize the proved injectivity theorem to the same topology. It uses local injectivity of the unit and the identity restriction maps of the constant presheaf. ([def-weil-pbc-scheme-conventions], `CategoryTheory.Sheaf` ([Mathlib source](https://github.com/leanprover-community/mathlib4/blob/master/Mathlib/CategoryTheory/Sites/Sheaf.lean)), [def-weil-pbc-etale-sheaves], `CategoryTheory.constantSheaf` ([Mathlib source](https://github.com/leanprover-community/mathlib4/blob/master/Mathlib/CategoryTheory/Sites/ConstantSheaf.lean)), `CategoryTheory.presheafToSheaf` ([Mathlib source](https://github.com/leanprover-community/mathlib4/blob/master/Mathlib/CategoryTheory/Sites/Sheafification.lean))).
