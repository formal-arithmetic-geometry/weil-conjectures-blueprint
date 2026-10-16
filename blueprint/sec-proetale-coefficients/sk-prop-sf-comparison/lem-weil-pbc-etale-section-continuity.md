+++
id = "lem-weil-pbc-etale-section-continuity"
kind = "lemma"
title = "Continuity of sections at an inverse limit"
lean = ["AlgebraicGeometry.Etale.unitComparison_app_surjective_of_isLimit", "AlgebraicGeometry.Etale.exists_unitComparison_app_eq_zero_of_isLimit", "AlgebraicGeometry.Etale.unitComparison_app_isColimit_of_isLimit"]
order = 959
uses = ["def-weil-pbc-etale-sheaves", "def-weil-pbc-inverse-image", "def-weil-pbc-scheme-conventions", "lem-weil-pbc-etale-finite-data-descent"]
+++
Let $X=\varprojlim_jX_j$ be as in the quasi-compact quasi-separated
[def-weil-pbc-scheme-conventions] setting above. Let $F_i$ be an abelian
etale sheaf on $X_i$, and let $F_j,F$ be its inverse images
[def-weil-pbc-inverse-image]. Then

$$
 \varinjlim_{j\geq i}F_j(X_j)\xrightarrow{\sim}F(X).
$$

The same formula holds on every etale finite-presentation object $W_j\to X_j$,
with $W=X\times_{X_j}W_j$.
