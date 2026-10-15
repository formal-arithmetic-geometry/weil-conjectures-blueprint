+++
id = "lem-weil-pbc-module-directed-colimit-underlying-sets"
kind = "lemma"
title = "The underlying sheaf of sets of a directed colimit of sheaves of modules is the colimit of the underlying sheaves of sets"
lean = ["SheafOfModules.underlying_directed_colimit_isColimit"]
+++
Let $X$ be a topological space, $\mathcal O_X$ a sheaf of rings on $X$ and $\Mod(\mathcal O_X)$ the category of sheaves of $\mathcal O_X$-modules `SheafOfModules` ([Mathlib source](https://github.com/leanprover-community/mathlib4/blob/master/Mathlib/Algebra/Category/ModuleCat/Sheaf.lean)). Let $I$ be a directed set and $(\mathcal F_i,\varphi_{i'i})_{i\le i'}$ a system of $\mathcal O_X$-modules over $I$ with a colimit $(\mathcal F,(c_i)_i)$ in $\Mod(\mathcal O_X)$ `CategoryTheory.Limits.colimit` ([Mathlib source](https://github.com/leanprover-community/mathlib4/blob/master/Mathlib/CategoryTheory/Limits/HasLimits.lean)). Then the underlying sheaf of sets of $\mathcal F$, with the maps of sheaves of sets underlying the $c_i$, is a colimit of the system of underlying sheaves of sets of the $\mathcal F_i$ in the category of sheaves of sets on $X$.
