+++
id = "k1-constant-mod-sheaf-prime-coefficient-identification"
kind = "lemma"
title = "Prime coefficient constant sheaf identification"
uses = ["def-sc-constant-sheaves"]
lean = ["AlgebraicGeometry.IsCurve.constantModSheaf_iso_constantSheaf"]
source = "Mathlib/LinearAlgebra/Quotient/Basic.lean and lean/WeilConjectures/SixFunctors/Etale/SmoothBaseChange/Defs.lean, Submodule.quotEquivOfEqBot; Etale.constantModSheaf; CategoryTheory.constantSheaf.mapIso"
+++
Let U be a scheme and r a prime. Put R=ULift(Z/rZ). The constant R-module sheaf with value R/(r), denoted Etale.constantModSheaf R U r, is isomorphic to the constant R-module sheaf with value R `CategoryTheory.constantSheaf` ([Mathlib source](https://github.com/leanprover-community/mathlib4/blob/master/Mathlib/CategoryTheory/Sites/ConstantSheaf.lean)), [def-sc-constant-sheaves]. This asserts existence of a sheaf isomorphism, not literal equality of the two sheaf objects.
