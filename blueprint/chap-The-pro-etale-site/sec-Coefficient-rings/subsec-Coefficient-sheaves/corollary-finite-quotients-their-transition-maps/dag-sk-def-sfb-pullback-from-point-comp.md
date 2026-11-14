+++
id = "dag-sk-def-sfb-pullback-from-point-comp"
kind = "dag-definition"
title = "$f^*\\circ p_Y^*\\cong p_X^*$"
name_showing = false
order = 181504
tags = ["sheaf-dag"]
split_from = "corollary-finite-quotients-their-transition-maps--3"
dag_id = "sk-def-sfb-pullback-from-point-comp"
dag_kind = "definition"
dag_status = "split"
serial = false
dag_lean = ["AlgebraicGeometry.ProEtale.upperStarFromPointComp", "AlgebraicGeometry.ProEtale.isMonoidal_upperStarFromPointComp"]
uses = ["dag-def-sfb-finite-upper-star"]
+++
Let $f\colon X\to Y$ be a morphism of schemes. Let $f^*$ be the pullback of
abelian pro-étale sheaves along $f$, and let
$p_X^*=\pi_X^*\circ p^*$, $p_Y^*=\pi_Y^*\circ p^*$ be the inverse images from
the point ([dag-det-pe-topos-functoriality-inverse-image],
`sk-def-sfb-pullback-from-point`). Since $\Spec\Z$ is terminal,
$\pi_Y\circ f=\pi_X$. The natural isomorphism
$$
f^*\circ p_Y^*=f^*\pi_Y^*p^*\ \cong\ (\pi_Y\circ f)^*p^*=\pi_X^*p^*=p_X^*
$$
is $p^*$ composed with the inverse of the composition isomorphism
$(\pi_Y\circ f)^*\cong f^*\circ\pi_Y^*$ of
[dag-det-pe-topos-functoriality-inverse-image], followed by the identification
$(\pi_Y\circ f)^*=\pi_X^*$.

It is a monoidal natural isomorphism for the strong monoidal structures of
$f^*\circ p_Y^*$ and $p_X^*$ and the tensor products of
`sk-def-sfb-sheaf-tensor`.

(SHEAF DAG node `sk-def-sfb-pullback-from-point-comp`; machine-alignment layer.) Split from [corollary-finite-quotients-their-transition-maps--3]. DAG kind: definition. DAG status: split. Statement dependencies not drawn: `def-sfb-upper-star-from-point`, `det-def-sfb-ring-object`, `det-def-sfb-ring-object-rings`, `lem-sfb-finite-upper-star-braided`, `lem-weil-pbc-sheaf-tensor-closed`, `sk-def-sfb-ring-object`.
