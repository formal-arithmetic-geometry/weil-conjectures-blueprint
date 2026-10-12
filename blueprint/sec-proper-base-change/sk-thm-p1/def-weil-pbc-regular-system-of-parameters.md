+++
id = "def-weil-pbc-regular-system-of-parameters"
kind = "definition"
title = "Regular system of parameters"
lean = ["IsLocalRing.IsRegularSystemOfParameters"]
source = "literature/stacks-project/algebra.tex, Definition Tag 00KU (definition-regular-local), clause (2)"
+++
Let $R$ be a commutative Noetherian local ring `IsNoetherianRing` ([Mathlib source](https://github.com/leanprover-community/mathlib4/blob/master/Mathlib/RingTheory/Noetherian/Defs.lean)) with maximal ideal $\mathfrak m$ and Krull dimension $d$ `ringKrullDim` ([Mathlib source](https://github.com/leanprover-community/mathlib4/blob/master/Mathlib/RingTheory/KrullDimension/Basic.lean)). An ordered finite list $t=(t_1,\ldots,t_r)$ is a regular system of parameters if $r=d$ and $(t_1,\ldots,t_r)=\mathfrak m$; thus $R$ is regular local in the sense of `IsRegularLocalRing, IsRegularRing` ([Mathlib source](https://github.com/leanprover-community/mathlib4/blob/master/Mathlib/RingTheory/RegularLocalRing/Defs.lean)). The empty list is permitted when $d=0$.
