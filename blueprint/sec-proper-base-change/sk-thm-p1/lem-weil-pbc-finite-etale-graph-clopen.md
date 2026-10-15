+++
id = "lem-weil-pbc-finite-etale-graph-clopen"
kind = "lemma"
title = "Morphisms correspond to clopen graphs projecting isomorphically"
uses = ["def-pc-scheme"]
lean = ["AlgebraicGeometry.Scheme.finiteEtale_graph_clopen"]
+++
Let $p:U\to Y$ be a morphism of schemes [def-pc-scheme] and $q:V\to Y$ a finite etale morphism `CategoryTheory.MorphismProperty.Over, CategoryTheory.MorphismProperty.Over.pullback` ([Mathlib source](https://github.com/leanprover-community/mathlib4/blob/master/Mathlib/CategoryTheory/MorphismProperty/Comma.lean)). Put $P=V\times_Y U$ `CategoryTheory.Limits.pullback` ([Mathlib source](https://github.com/leanprover-community/mathlib4/blob/master/Mathlib/CategoryTheory/Limits/Shapes/Pullback/HasPullback.lean)) with projection $r:P\to U$. There exists a bijection from the set of morphisms $a:U\to V$ satisfying $q\circ a=p$ to the set of open subsets $W\subseteq P$ `AlgebraicGeometry.IsOpenImmersion` ([Mathlib source](https://github.com/leanprover-community/mathlib4/blob/master/Mathlib/AlgebraicGeometry/OpenImmersion.lean)) that are also closed and for which $r|_W$ is an isomorphism. The underlying subset assigned to $a$ is the image of its graph $(a,\mathrm{id}_U):U\to P$.
