+++
id = "def-sfb-finite-derived-adjunction-plus"
kind = "definition"
title = "The derived adjunction on $D^+$"
order = 1661
uses = ["def-sfb-finite-derived-pullback-iso", "def-sfb-finite-upper-lower-star-adjunction", "lem-sfb-finite-upper-star-exact", "sk-def-sfb-derived-categories"]
lean = ["AlgebraicGeometry.ProEtale.derivedUpperStarLowerStarAdjunctionPlus"]
+++
Let $\mathcal A$ be as in [def-sfb-finite-derived-pullback-iso] and $g\colon Z\to Y$ a
morphism. On the bounded below derived categories, the functor $D^+(g^*)$ induced by the
exact $g^*$ ([lem-sfb-finite-upper-star-exact]) is left adjoint to the right derived functor
$R^+g_*$, computed on injective resolutions:

$$
D^+(g^*)\dashv R^+g_*,
$$

induced by $g^*\dashv g_*$ ([def-sfb-finite-upper-lower-star-adjunction]).
