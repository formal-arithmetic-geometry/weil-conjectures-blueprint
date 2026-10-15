+++
id = "lem-weil-pbc-etale-module-pullback-forget-naturality"
kind = "lemma"
title = "Naturality of etale module pullback under forgetting coefficients"
uses = ["def-pc-scheme", "def-weil-pbc-etale-sheaves", "def-weil-pbc-inverse-image"]
lean = ["AlgebraicGeometry.Etale.exists_upperStar_forget₂_natIso"]
+++
Let X and Y be schemes [def-pc-scheme], f:X→Y a morphism, and Λ a commutative ring. In the categories of constant-coefficient module sheaves [def-weil-pbc-etale-sheaves] and abelian sheaves `CategoryTheory.Sheaf` ([Mathlib source](https://github.com/leanprover-community/mathlib4/blob/master/Mathlib/CategoryTheory/Sites/Sheaf.lean)), let U_X and U_Y forget the module structure. There is a natural isomorphism f⁻¹_Mod ⋙ U_X ≅ U_Y ⋙ f⁻¹_Ab, where inverse image is [def-weil-pbc-inverse-image]. In particular its components commute with every module-sheaf morphism C→F. No finite coefficient, torsion, properness, or henselian hypothesis is required. Unlike an independent choice of objectwise isomorphisms, this single functor isomorphism supplies the commuting square needed on cohomology.
