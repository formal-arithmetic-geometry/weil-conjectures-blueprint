+++
id = "lem-kun-0f0g"
kind = "lemma"
title = "Projection formula for proper morphisms"
lean = ["AlgebraicGeometry.Etale.isIso_rightDerivedLowerStarProjectionMap_of_isProper"]
order = 3143
uses = ["def-kun-cd", "def-kun-projection-formula-map", "def-kun-truncations", "def-weil-pbc-direct-image", "def-weil-pbc-inverse-image", "def-weil-pbc-scheme-conventions", "lem-kun-0f10", "lem-kun-0f11", "lem-kun-bounded-flat-replacement", "lem-kun-complex-colimit-hocolim", "lem-kun-derived-tensor-direct-sums", "lem-kun-derived-tensor-triangulated", "lem-kun-hocolim-truncations"]
+++
Let $f:X\to Y$ be a
proper morphism and
$\Lambda$ a torsion ring. For $E\in D(X_{\Et},\Lambda)$ and
$K\in D(Y_{\Et},\Lambda)$, the canonical projection-formula morphism

$$
\mathrm{PF}_f(E,K):\quad
Rf_*E\kunotimes{\Lambda}K\longrightarrow
Rf_*(E\kunotimes{\Lambda}f^{-1}K)
$$

of [def-kun-projection-formula-map] is an isomorphism.
