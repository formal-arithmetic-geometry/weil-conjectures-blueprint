+++
id = "det-def-sfb-pullback-from-point-comp"
kind = "definition"
title = "$f^*\\circ p_Y^*\\cong p_X^*$"
order = 1183
uses = ["def-sfb-finite-upper-star", "def-sfb-finite-upper-star-comp", "def-sfb-finite-upper-star-monoidal", "det-def-sfb-pullback-from-point", "lem-weil-pbc-sheaf-tensor-closed"]
lean = ["AlgebraicGeometry.ProEtale.upperStarFromPointComp", "AlgebraicGeometry.ProEtale.isMonoidal_upperStarFromPointComp"]
+++
Let $f\colon X\to Y$ be a morphism of schemes. Let $f^*$ be the pullback of
abelian pro-étale sheaves along $f$, and let
$p_X^*=\pi_X^*\circ p^*$, $p_Y^*=\pi_Y^*\circ p^*$ be the inverse images from
the point ([def-sfb-finite-upper-star],
[det-def-sfb-pullback-from-point]). Since $\Spec\Z$ is terminal,
$\pi_Y\circ f=\pi_X$. The natural isomorphism
$$
f^*\circ p_Y^*=f^*\pi_Y^*p^*\ \cong\ (\pi_Y\circ f)^*p^*=\pi_X^*p^*=p_X^*
$$
is $p^*$ composed with the inverse of the composition isomorphism
$(\pi_Y\circ f)^*\cong f^*\circ\pi_Y^*$ of
[def-sfb-finite-upper-star-comp], followed by the identification
$(\pi_Y\circ f)^*=\pi_X^*$.

It is a monoidal natural isomorphism for the strong monoidal structures of
$f^*\circ p_Y^*$ and $p_X^*$ ([def-sfb-finite-upper-star-monoidal],
[det-def-sfb-pullback-from-point]) and the tensor products of
[lem-weil-pbc-sheaf-tensor-closed].
