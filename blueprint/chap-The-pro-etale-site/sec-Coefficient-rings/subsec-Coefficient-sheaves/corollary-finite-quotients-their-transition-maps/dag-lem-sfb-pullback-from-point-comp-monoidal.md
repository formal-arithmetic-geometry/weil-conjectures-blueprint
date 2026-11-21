+++
id = "dag-lem-sfb-pullback-from-point-comp-monoidal"
kind = "dag-lemma"
title = "$f^*\\circ p_Y^*\\cong p_X^*$ is monoidal"
name_showing = false
order = 181503
tags = ["sheaf-dag"]
split_from = "corollary-finite-quotients-their-transition-maps--3"
dag_id = "lem-sfb-pullback-from-point-comp-monoidal"
dag_kind = "statement"
dag_status = "split"
serial = false
dag_lean = ["AlgebraicGeometry.ProEtale.isMonoidal_upperStarFromPointComp"]
uses = ["dag-def-sfb-finite-upper-star", "dag-def-sfb-pullback-from-point-comp-iso"]
+++
The natural isomorphism $f^*\circ p_Y^*\cong p_X^*$ of
[dag-def-sfb-pullback-from-point-comp-iso] is monoidal. That is, it is compatible
with the unit and tensor comparison isomorphisms of the strong monoidal
functors $f^*\circ p_Y^*$ and $p_X^*$, for the tensor products of
`sk-def-sfb-sheaf-tensor`.

(SHEAF DAG node `lem-sfb-pullback-from-point-comp-monoidal`; machine-alignment layer.) Split from [corollary-finite-quotients-their-transition-maps--3]. DAG kind: statement. DAG status: split. Statement dependencies not drawn: `def-sfb-upper-star-from-point`, `det-def-sfb-ring-object`, `det-def-sfb-ring-object-rings`, `lem-sfb-finite-upper-star-braided`, `lem-weil-pbc-sheaf-tensor-closed`, `sk-def-sfb-ring-object`.
