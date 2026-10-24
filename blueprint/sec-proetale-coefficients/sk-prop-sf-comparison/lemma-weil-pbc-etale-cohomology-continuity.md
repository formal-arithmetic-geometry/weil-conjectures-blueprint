+++
id = "lemma-weil-pbc-etale-cohomology-continuity"
kind = "lemma"
title = "Etale cohomology continuity"
lean = ["AlgebraicGeometry.Etale.isZero_rightDerived_sectionsFunctor_upperStar_of_isLimit", "AlgebraicGeometry.Etale.cohomologyMap_isColimit_of_isLimit"]
order = 1025
uses = ["def-weil-pbc-etale-sheaves", "def-weil-pbc-scheme-conventions", "lem-weil-pbc-etale-section-continuity", "lem-weil-pbc-hypercover-refinement", "lemma-weil-pbc-fibre-product-limit", "lemma-weil-pbc-finite-hypercover-descent", "thm-weil-pbc-hypercover-cohomology"]
+++
Let $(X_i)_{i\in I}$ be a cofiltered inverse system of quasi-compact
quasi-separated schemes [def-weil-pbc-scheme-conventions] with affine
transition maps and limit $X$. Let $F_i$ be an abelian etale sheaf
[def-weil-pbc-etale-sheaves] on $X_i$, and write $F_j$ and $F$ for its
pullbacks to later stages and to $X$. Then

$$
 \varinjlim_{j\geq i}H^q(X_j,F_j)
 \xrightarrow{\sim}H^q(X,F)
 \qquad(q\geq0).
$$
