+++
kind = "proof"
of = "lem-weil-pbc-killed-sheaf-module-lift"
uses = ["def-weil-pbc-etale-sheaves"]
+++
Evaluate the annihilation equation at every object and section. Use Mathlib AddCommGroup.zmodModule to equip each section group with its Z/n-module structure and ULift.module for lifted scalars. Additive restriction maps are linear by ZMod.map_smul. Functor laws follow from those of the original sheaf. This is valid also at n=0, n=1 and for the zero sheaf. (`CategoryTheory.Sheaf` ([Mathlib source](https://github.com/leanprover-community/mathlib4/blob/master/Mathlib/CategoryTheory/Sites/Sheaf.lean))).

The underlying abelian presheaf is definitionally the original presheaf. ModuleCat forgetting to abelian groups reflects limits, so Presheaf.isSheaf_of_isSheaf_comp proves the module presheaf is a sheaf. Iso.refl gives the claimed underlying-sheaf isomorphism. ([def-weil-pbc-etale-sheaves]).
