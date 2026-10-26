+++
id = "lem-sfb-finite-monoidal-adjunction"
kind = "lemma"
title = "$g^*\\dashv g_*$ is a monoidal adjunction"
order = 889
uses = ["def-sfb-finite-lower-star-lax-monoidal", "def-sfb-finite-upper-lower-star-adjunction", "def-sfb-finite-upper-star-monoidal"]
lean = ["AlgebraicGeometry.ProEtale.oplaxMonoidal_upperStar", "AlgebraicGeometry.ProEtale.isMonoidal_upperStarLowerStarAdjunction"]
+++
Let $\mathcal A$ and $g$ be as in [def-sfb-finite-lower-star-lax-monoidal]. Give $g_*$ the lax
monoidal structure of [def-sfb-finite-lower-star-lax-monoidal] and $g^*$ the oplax monoidal
structure mate to it under the adjunction $g^*\dashv g_*$ of
[def-sfb-finite-upper-lower-star-adjunction] (it is the strong monoidal structure of
[def-sfb-finite-upper-star-monoidal] when tensoring in $\mathcal A$ commutes with filtered
colimits). Then the adjunction $g^*\dashv g_*$ is monoidal: its unit and counit are
monoidal natural transformations.
