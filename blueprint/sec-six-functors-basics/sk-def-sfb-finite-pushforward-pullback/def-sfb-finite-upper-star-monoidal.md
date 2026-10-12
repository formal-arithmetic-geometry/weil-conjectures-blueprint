+++
id = "def-sfb-finite-upper-star-monoidal"
kind = "definition"
title = "Strong monoidal structure on $g^*$"
order = 1463
uses = ["def-sfb-finite-lower-star-lax-monoidal", "def-sfb-finite-upper-lower-star-adjunction", "lem-sfb-finite-upper-star-tensor", "lem-sfb-finite-upper-star-unit"]
lean = ["AlgebraicGeometry.ProEtale.monoidal_upperStar"]
+++
Let $\mathcal A$ and $g$ be as in [lem-sfb-finite-upper-star-unit]. The *monoidal
structure* on $g^*$ is the oplax monoidal structure mate, under $g^*\dashv g_*$
([def-sfb-finite-upper-lower-star-adjunction]), of the lax structure of
[def-sfb-finite-lower-star-lax-monoidal]. Its structure maps are invertible by
[lem-sfb-finite-upper-star-unit] and [lem-sfb-finite-upper-star-tensor], so $g^*$ is a
strong monoidal functor.
