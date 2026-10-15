+++
id = "def-weil-pbc-comm-algebra-sheaf"
kind = "definition"
title = "Sheaves of commutative algebras on a scheme and their underlying modules"
uses = ["def-pc-scheme"]
lean = ["AlgebraicGeometry.Scheme.CommAlgebraSheaf"]
+++
Let $X$ be a scheme [def-pc-scheme]. A sheaf of commutative $\mathcal O_X$-algebras is a sheaf $\mathcal A$ of commutative rings on the open-set site of $X$, together with a morphism of ring sheaves $\mathcal O_X\to\mathcal A$. Morphisms are ring-sheaf morphisms commuting with these structure morphisms; equivalently this category is the under category of $\mathcal O_X$ in sheaves of commutative rings. Its underlying $\mathcal O_X$-module `SheafOfModules` ([Mathlib source](https://github.com/leanprover-community/mathlib4/blob/master/Mathlib/Algebra/Category/ModuleCat/Sheaf.lean)) is $\mathcal A$, viewed as the rank-one module over itself and restricted along $\mathcal O_X\to\mathcal A$.
