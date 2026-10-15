+++
id = "def-weil-pbc-finite-etale-trace-splitting-data"
kind = "definition"
title = "Explicit splitting data, splitting presieve, and local sum"
uses = ["def-weil-pbc-etale-site", "def-weil-pbc-scheme-conventions"]
lean = ["AlgebraicGeometry.Etale.FiniteEtaleTraceSplitting"]
+++
Let $f:Y\to X$ be a morphism of schemes [def-weil-pbc-scheme-conventions] and $T\to X$ an object of the small etale site [def-weil-pbc-etale-site]. A splitting is a finite type $J$, schemes $V_j$, a clopen coproduct cofan $i_j:V_j\to T\times_XY$ `CategoryTheory.Limits.pullback` ([Mathlib source](https://github.com/leanprover-community/mathlib4/blob/master/Mathlib/CategoryTheory/Limits/Shapes/Pullback/HasPullback.lean)), `AlgebraicGeometry.IsOpenImmersion` ([Mathlib source](https://github.com/leanprover-community/mathlib4/blob/master/Mathlib/AlgebraicGeometry/OpenImmersion.lean)), `AlgebraicGeometry.IsClosedImmersion` ([Mathlib source](https://github.com/leanprover-community/mathlib4/blob/master/Mathlib/AlgebraicGeometry/Morphisms/ClosedImmersion.lean)), and inverse projections $t_j:T\to V_j$, with $t_ji_jp=1$ and $i_jpt_j=1$. The split presieve on $W$ consists of all arrows $T\to W$ with some such splitting. For etale $f$ the sheet section is $t_ji_j:T\to B_fT$, and for an abelian sheaf $F$ `CategoryTheory.Sheaf` ([Mathlib source](https://github.com/leanprover-community/mathlib4/blob/master/Mathlib/CategoryTheory/Sites/Sheaf.lean)) the splitting sum on $s\in F(B_fT)$ is $\sum_jF(t_ji_j)s$. Empty $J$ is allowed. All data are explicit constructor inputs.
