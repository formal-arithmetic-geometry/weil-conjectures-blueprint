+++
kind = "proof"
of = "lem-weil-pbc-module-abelian-inverse-image-comparison"
uses = ["def-weil-pbc-direct-image", "def-weil-pbc-inverse-image"]
+++
Write the inverse image [def-weil-pbc-inverse-image] as left Kan extension followed by sheafification `CategoryTheory.presheafToSheaf` ([Mathlib source](https://github.com/leanprover-community/mathlib4/blob/master/Mathlib/CategoryTheory/Sites/Sheafification.lean)). The functor forgetting a module to its additive group preserves colimits and limits. Mathlib Functor.leftKanExtensionCompIsoOfPreserves and sheafComposeNatIso therefore give an isomorphism e from the abelian inverse image of the underlying sheaf to the underlying module inverse image.

Naturality of the sheafification unit and sheafComposeNatTrans_fac show that the composite of the abelian sheafification unit with e is the inverse Kan-extension comparison followed by the underlying module sheafification unit. The factorization leftKanExtensionCompIsoOfPreserves_inv_fac then shows that the abelian adjoint of e is the underlying module adjunction unit; direct image [def-weil-pbc-direct-image] commutes with forgetting because it is restriction of presheaves. Apply the injective adjunction hom equivalence: e is the displayed canonical map, so that map is an isomorphism. ([def-weil-pbc-inverse-image]).
