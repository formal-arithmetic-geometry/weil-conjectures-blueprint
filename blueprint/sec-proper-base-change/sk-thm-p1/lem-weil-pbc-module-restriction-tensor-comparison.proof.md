+++
kind = "proof"
of = "lem-weil-pbc-module-restriction-tensor-comparison"
uses = ["def-pur-sheaf-tensor-product"]
+++
Construct the comparison by the sheafification universal property: restriction of the sectionwise tensor presheaf is the tensor presheaf of the restrictions, and restriction commutes with sheafification by the restriction/direct-image adjunction. The universal maps agree on pure tensors, giving the displayed formula. (`AlgebraicGeometry.Scheme.Modules.restrictFunctor, AlgebraicGeometry.Scheme.Modules.restrictAdjunction, AlgebraicGeometry.Scheme.Modules.instIsLeftAdjointRestrictFunctor, AlgebraicGeometry.Scheme.Modules.isQuasicoherent_restrictFunctor` ([Mathlib source](https://github.com/leanprover-community/mathlib4/blob/master/Mathlib/AlgebraicGeometry/Modules/Sheaf.lean)), [def-pur-sheaf-tensor-product], `PresheafOfModules.sheafification` ([Mathlib source](https://github.com/leanprover-community/mathlib4/blob/master/Mathlib/Algebra/Category/ModuleCat/Presheaf/Sheafification.lean))).
