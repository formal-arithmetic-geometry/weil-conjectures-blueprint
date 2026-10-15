+++
id = "lem-weil-pbc-etale-constant-ring-module-equivalence"
kind = "lemma"
title = "Constant-coefficient etale sheaves and modules over the constant ring sheaf are equivalent"
uses = ["def-weil-pbc-etale-site"]
lean = ["AlgebraicGeometry.Scheme.etaleConstantModuleFunctor_isEquivalence"]
+++
Let Y be a scheme with its small etale site [def-weil-pbc-etale-site], and let $\Lambda$ be a commutative ring in Type (u+1). Let R be the constant ring sheaf associated to $\Lambda$ `CategoryTheory.constantSheaf` ([Mathlib source](https://github.com/leanprover-community/mathlib4/blob/master/Mathlib/CategoryTheory/Sites/ConstantSheaf.lean)). Extending the scalar action by module sheafification `CategoryTheory.presheafToSheaf` ([Mathlib source](https://github.com/leanprover-community/mathlib4/blob/master/Mathlib/CategoryTheory/Sites/Sheafification.lean)) gives an equivalence from the category of sheaves valued in $\Lambda$-modules to the category of sheaves of R-modules `SheafOfModules` ([Mathlib source](https://github.com/leanprover-community/mathlib4/blob/master/Mathlib/Algebra/Category/ModuleCat/Sheaf.lean)). This extension keeps the underlying abelian presheaf `CategoryTheory.Sheaf` ([Mathlib source](https://github.com/leanprover-community/mathlib4/blob/master/Mathlib/CategoryTheory/Sites/Sheaf.lean)) unchanged. An inverse restricts scalars along the constant-ring presheaf sheafification map. No nonzero-ring or nonempty-scheme hypothesis is imposed.
