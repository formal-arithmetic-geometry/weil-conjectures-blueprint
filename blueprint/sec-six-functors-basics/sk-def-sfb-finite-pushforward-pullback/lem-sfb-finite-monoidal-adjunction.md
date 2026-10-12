+++
id = "lem-sfb-finite-monoidal-adjunction"
kind = "lemma"
title = "$g^*\\dashv g_*$ is a monoidal adjunction"
order = 1503
uses = ["def-sfb-finite-lower-star-lax-monoidal", "def-sfb-finite-upper-lower-star-adjunction", "def-sfb-finite-upper-star-monoidal"]
lean = ["AlgebraicGeometry.ProEtale.isMonoidal_upperStarLowerStarAdjunction"]
+++
With the structures of [def-sfb-finite-upper-star-monoidal] on $g^*$ and
[def-sfb-finite-lower-star-lax-monoidal] on $g_*$, the adjunction $g^*\dashv g_*$ of
[def-sfb-finite-upper-lower-star-adjunction] is monoidal: its unit and counit are
monoidal natural transformations.
