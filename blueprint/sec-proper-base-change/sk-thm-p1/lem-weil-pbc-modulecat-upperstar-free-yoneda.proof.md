+++
kind = "proof"
of = "lem-weil-pbc-modulecat-upperstar-free-yoneda"
uses = ["def-weil-pbc-inverse-image"]
+++
The upperStar/lowerStar adjunction followed by free-Yoneda evaluation identifies Hom(g^{-1}Lambda[W],F) with Hom(Lambda,(g_*F)(W)). By the definition of lowerStar this is Hom(Lambda,F(W times_X Y)), which is Hom(Lambda[W times_X Y],F). The equivalences are natural by homEquiv_naturality_right and freeYonedaHomEquiv_comp. Coyoneda.ext gives the isomorphism. This is the existing proved source-library definition at FreeLifting.lean:234-261. ([def-weil-pbc-inverse-image], `PresheafOfModules.freeYonedaEquiv` ([Mathlib source](https://github.com/leanprover-community/mathlib4/blob/master/Mathlib/Algebra/Category/ModuleCat/Presheaf/Generator.lean))).
