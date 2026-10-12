+++
id = "lem-zl-affine-curve-hc2-purity"
kind = "lemma"
title = "Purity of the top affine-curve factor"
order = 3178
lean = ["AlgebraicGeometry.isPureOfWeightOver_compactlySupportedCohomology_two_of_isAffine"]
uses = ["def-weil-frobenius-module-weights", "def-weil-ordinary-compact-cohomology", "def-weil-punctual-weights", "lem-a1-affine-hc2-pure"]
+++
Let $C_0$ be a smooth affine curve over $k_0=\mathbf F_q$ (an affine
$k_0$-scheme, smooth of relative dimension one) and let $\mathcal E$ be
a lisse Weil sheaf on $C_0$, punctually $\iota$-pure of weight zero.
Then $H_c^2(C,\mathcal E)$ is $\iota$-pure of weight two over $k_0$:
every Frobenius eigenvalue on it has $\iota$-modulus $q$.
