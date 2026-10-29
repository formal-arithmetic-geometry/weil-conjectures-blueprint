+++
id = "lem-sfb-pullback-from-point-comp-monoidal"
kind = "lemma"
title = "$f^*\\circ p_Y^*\\cong p_X^*$ is monoidal"
order = 1287
uses = ["def-sfb-pullback-from-point-comp-iso", "def-sfb-finite-upper-star-monoidal", "lem-weil-pbc-sheaf-tensor-closed"]
lean = ["AlgebraicGeometry.ProEtale.isMonoidal_upperStarFromPointComp"]
+++
The natural isomorphism $f^*\circ p_Y^*\cong p_X^*$ of
[def-sfb-pullback-from-point-comp-iso] is monoidal. That is, it is compatible
with the unit and tensor comparison isomorphisms of the strong monoidal
functors $f^*\circ p_Y^*$ and $p_X^*$ (with the strong monoidal structure of
[def-sfb-finite-upper-star-monoidal] on $f^*$), for the tensor products of
[lem-weil-pbc-sheaf-tensor-closed].
