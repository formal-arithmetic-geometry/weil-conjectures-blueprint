+++
kind = "proof"
of = "lem-weil-pbc-free-etale-module-shriek-comparison"
uses = ["def-weil-pbc-etale-sum-extension"]
+++
The free-forgetful adjunction for ModuleCat, whiskered over the site, and ulift Yoneda identify presheaf maps from the free representable with sections of F on W. Compose with sheafificationAdjunction to obtain the natural equivalence Hom(P_W,F) ≃ F(W). This is sectionEquiv in Lean. (`PresheafOfModules.freeYonedaEquiv` ([Mathlib source](https://github.com/leanprover-community/mathlib4/blob/master/Mathlib/Algebra/Category/ModuleCat/Presheaf/Generator.lean)), `PresheafOfModules.sheafification` ([Mathlib source](https://github.com/leanprover-community/mathlib4/blob/master/Mathlib/Algebra/Category/ModuleCat/Presheaf/Sheafification.lean))).

The etale extension-by-zero/pullback adjunction, followed by upperStarIsoLocalizationRestriction, identifies Hom(j_! constant Λ,F) with Hom(constant Λ,F restricted to W). The constant-sheaf adjunction evaluates at the terminal etale W-object (W,id). The restriction there is F evaluated at the localization image of (W,id), canonically isomorphic to W. Finally linear maps Λ → F(W) are identified with F(W) by evaluation at 1. This is shriekSectionEquiv in Lean. ([def-weil-pbc-etale-sum-extension], `CategoryTheory.constantSheaf` ([Mathlib source](https://github.com/leanprover-community/mathlib4/blob/master/Mathlib/CategoryTheory/Sites/ConstantSheaf.lean))).

Both equivalences commute with postcomposition. For the second, use naturality of the pullback/restriction comparison, naturality of the constant-sheaf adjunction, and naturality of F→G along the inverse of the localization-terminal isomorphism. Combine the equivalences and apply Coyoneda.ext to obtain the isomorphism.
