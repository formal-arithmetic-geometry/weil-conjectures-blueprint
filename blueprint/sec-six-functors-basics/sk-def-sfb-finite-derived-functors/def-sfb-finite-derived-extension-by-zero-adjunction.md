+++
id = "def-sfb-finite-derived-extension-by-zero-adjunction"
kind = "definition"
title = "The derived adjunction $D(j_!)\\dashv D(j^*)$"
order = 1649
uses = ["def-sfb-finite-derived-pullback-iso", "def-sfb-finite-extension-by-zero-adjunction", "lem-sfb-finite-extension-by-zero-exact", "lem-sfb-finite-upper-star-exact", "sk-def-sfb-derived-categories"]
lean = ["AlgebraicGeometry.ProEtale.derivedOpenImmersionLowerShriekUpperStarAdjunction"]
+++
Let $\mathcal A$ be as in [def-sfb-finite-derived-pullback-iso] and $j\colon U\to X$ an
open immersion. The functors $j_!$ and $j^*$ are exact
([lem-sfb-finite-extension-by-zero-exact], [lem-sfb-finite-upper-star-exact]), so they
induce functors $D(j_!)$ and $D(j^*)$ on the unbounded derived categories by applying them
levelwise. The adjunction $j_!\dashv j^*$ of [def-sfb-finite-extension-by-zero-adjunction]
induces an adjunction

$$
D(j_!)\dashv D(j^*).
$$
