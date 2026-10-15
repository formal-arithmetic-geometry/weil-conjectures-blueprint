+++
id = "lem-weil-pbc-finite-etale-graph-base-change"
kind = "lemma"
title = "Product projections and clopen graph images commute with base change"
uses = ["def-pc-scheme"]
lean = ["AlgebraicGeometry.Scheme.finiteEtale_graph_base_change"]
+++
Let $p:U\to Y$, $q:V\to Y$, and $i:Y_0\to Y$ be morphisms of schemes [def-pc-scheme], with $q$ finite etale `CategoryTheory.MorphismProperty.Over, CategoryTheory.MorphismProperty.Over.pullback` ([Mathlib source](https://github.com/leanprover-community/mathlib4/blob/master/Mathlib/CategoryTheory/MorphismProperty/Comma.lean)). Form $U_0=U\times_Y Y_0$, $V_0=V\times_Y Y_0$, $P=V\times_Y U$, and $P_0=V_0\times_{Y_0}U_0$ `CategoryTheory.Limits.pullback` ([Mathlib source](https://github.com/leanprover-community/mathlib4/blob/master/Mathlib/CategoryTheory/Limits/Shapes/Pullback/HasPullback.lean)). Write $t:U_0\to U$, $j:P_0\to P$ for the canonical maps and $r:P\to U$, $r_0:P_0\to U_0$ for the projections. Then the square with maps $(j,r_0,r,t)$ is cartesian. For every $a:U\to V$ over $Y$, let $a_0:U_0\to V_0$ be its base change. The image of the graph of $a_0$ is exactly $j^{-1}$ of the image of the graph of $a$.
