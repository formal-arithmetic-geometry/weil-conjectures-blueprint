+++
id = "lem-weil-pbc-geometric-point-field-extension"
kind = "lemma"
title = "Extension of separably closed geometric point fields"
uses = ["def-pc-scheme", "def-pc-separably-closed", "def-weil-pbc-geometric-stalks"]
lean = ["AlgebraicGeometry.Scheme.isIso_pointSmallEtalePrecomp_sheafFiber"]
order = 1803
+++
Let $S$ be a scheme [def-pc-scheme], $k$ and $l$ separably closed fields [def-pc-separably-closed], $s:\operatorname{Spec}k\to S$ a morphism of schemes and $a:\operatorname{Spec}l\to\operatorname{Spec}k$ any morphism of schemes. For an abelian sheaf $F$ on the small etale site of $S$, precomposition of pointed etale lifts by $a$ induces a canonical map $F_s\to F_{s\circ a}$ of geometric stalks [def-weil-pbc-geometric-stalks], natural in $F$. This map is an isomorphism. There is no algebraicity assumption on $l/k$.
