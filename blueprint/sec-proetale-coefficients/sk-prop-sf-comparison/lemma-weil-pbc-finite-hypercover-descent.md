+++
id = "lemma-weil-pbc-finite-hypercover-descent"
kind = "lemma"
title = "Finite etale hypercover skeleta descend"
order = 1024
lean = ["AlgebraicGeometry.finite_hypercover_descent", "AlgebraicGeometry.FiniteSplitEtaleHypercover.exists_truncated_refinement"]
uses = ["def-weil-pbc-finite-split-hypercover", "def-weil-pbc-scheme-conventions", "lem-weil-pbc-etale-finite-data-descent", "lemma-weil-pbc-fibre-product-limit"]
+++
Let $(X_i)$ be a cofiltered inverse system of quasi-compact quasi-separated
[def-weil-pbc-scheme-conventions] schemes with affine transition maps and
limit $X$. For each $r\geq0$, a truncation through degree $r$ of a split
etale hypercover finite in each degree
[def-weil-pbc-finite-split-hypercover], every morphism between two such
truncations, and every equality between such morphisms descend to one finite
stage $X_i$. The descended matching maps are covers at a sufficiently late
stage.
Moreover, for every $N\geq0$, every etale hypercover of $X$ admits a
refinement whose $N$-skeleton is split, has finitely many quasi-compact and
quasi-separated components in each degree, and is the pullback of an
$N$-truncated etale hypercover of some $X_j$.
