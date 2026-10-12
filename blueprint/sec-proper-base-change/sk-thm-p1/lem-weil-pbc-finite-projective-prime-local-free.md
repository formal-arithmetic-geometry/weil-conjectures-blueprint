+++
id = "lem-weil-pbc-finite-projective-prime-local-free"
kind = "lemma"
title = "A finite projective module is free after localizing away from each prime"
lean = ["Module.exists_localizationAway_equiv_finsupp_of_finite_projective"]
source = "literature/stacks-project/algebra.tex, Lemma Tag 00NX (lemma-finite-projective, line 19027), implication (3)\\Rightarrow(7): the finite locally free standard-open neighbourhood of each prime"
+++
Let $A$ be a commutative ring and $M$ a finite projective $A$-module, i.e. $M$ is finitely generated `Module.Finite` ([Mathlib source](https://github.com/leanprover-community/mathlib4/blob/master/Mathlib/RingTheory/Finiteness/Defs.lean)) and projective `Module.Projective` ([Mathlib source](https://github.com/leanprover-community/mathlib4/blob/master/Mathlib/Algebra/Module/Projective.lean)). For every prime ideal $\mathfrak p\subset A$ there exists an element $f\in A\setminus\mathfrak p$ such that the localization $M_f$ `LocalizedModule.Away` ([Mathlib source](https://github.com/leanprover-community/mathlib4/blob/master/Mathlib/Algebra/Module/LocalizedModule/Basic.lean)) is a finite free $A_f$-module, i.e. $M_f\cong A_f^{\oplus r}$ as $A_f$-modules for some integer $r\ge0$.
