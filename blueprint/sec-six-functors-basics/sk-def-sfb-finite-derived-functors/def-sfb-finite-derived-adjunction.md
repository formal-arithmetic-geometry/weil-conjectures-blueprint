+++
id = "def-sfb-finite-derived-adjunction"
kind = "definition"
title = "The derived adjunction $Lg^*\\dashv Rg_*$"
order = 1647
uses = ["def-sfb-finite-derived-pullback-iso", "def-sfb-finite-upper-lower-star-adjunction", "sk-def-sfb-derived-categories"]
lean = ["AlgebraicGeometry.ProEtale.derivedUpperStarLowerStarAdjunction"]
+++
Let $\mathcal A$ be as in [def-sfb-finite-derived-pullback-iso] and $g\colon Z\to Y$ a
morphism. The adjunction $g^*\dashv g_*$ of [def-sfb-finite-upper-lower-star-adjunction]
induces an adjunction

$$
Lg^*\dashv Rg_*
$$

between the total derived functors on the unbounded derived categories
[sk-def-sfb-derived-categories]: $Lg^*$ computed on K-flat resolutions of
$D(Y_{\mathrm{proét}},\mathcal A)$, $Rg_*$ on K-injective resolutions of
$D(Z_{\mathrm{proét}},\mathcal A)$.
