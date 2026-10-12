+++
id = "sk-def-sfb-pullback-from-point-comp"
kind = "definition"
title = "$f^*\\circ p_Y^*\\cong p_X^*$"
order = 1500
uses = ["sk-def-sfb-pullback-from-point"]
lean = ["AlgebraicGeometry.ProEtale.upperStarFromPointComp", "AlgebraicGeometry.ProEtale.isMonoidal_upperStarFromPointComp"]
tags = ["sketch"]
+++
Let $f\colon X\to Y$ be a morphism of schemes. Let $f^*$ be the pullback of
abelian pro-étale sheaves along $f$, and let
$p_X^*=\pi_X^*\circ p^*$, $p_Y^*=\pi_Y^*\circ p^*$ be the inverse images from
the point ([sk-def-sfb-finite-pushforward-pullback],
[sk-def-sfb-pullback-from-point]). Since $\Spec\Z$ is terminal,
$\pi_Y\circ f=\pi_X$. The natural isomorphism
$$
f^*\circ p_Y^*=f^*\pi_Y^*p^*\ \cong\ (\pi_Y\circ f)^*p^*=\pi_X^*p^*=p_X^*
$$
is $p^*$ composed with the inverse of the composition isomorphism
$(\pi_Y\circ f)^*\cong f^*\circ\pi_Y^*$ of
[sk-def-sfb-finite-pushforward-pullback], followed by the identification
$(\pi_Y\circ f)^*=\pi_X^*$.

It is a monoidal natural isomorphism for the strong monoidal structures of
$f^*\circ p_Y^*$ and $p_X^*$ and the tensor products of
[sk-def-sfb-sheaf-tensor].
