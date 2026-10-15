+++
id = "lem-sfb-pullback-from-point-comp-monoidal"
kind = "lemma"
title = "$f^*\\circ p_Y^*\\cong p_X^*$ is monoidal"
order = 1557
uses = ["def-sfb-pullback-from-point-comp-iso", "sk-def-sfb-finite-pushforward-pullback", "sk-def-sfb-sheaf-tensor"]
lean = ["AlgebraicGeometry.ProEtale.isMonoidal_upperStarFromPointComp"]
+++
The natural isomorphism $f^*\circ p_Y^*\cong p_X^*$ of
[def-sfb-pullback-from-point-comp-iso] is monoidal. That is, it is compatible
with the unit and tensor comparison isomorphisms of the strong monoidal
functors $f^*\circ p_Y^*$ and $p_X^*$, for the tensor products of
[sk-def-sfb-sheaf-tensor].
