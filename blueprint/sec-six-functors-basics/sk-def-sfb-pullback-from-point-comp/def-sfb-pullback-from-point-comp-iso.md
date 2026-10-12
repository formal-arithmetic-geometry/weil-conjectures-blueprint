+++
id = "def-sfb-pullback-from-point-comp-iso"
kind = "definition"
title = "The comparison $f^*\\circ p_Y^*\\cong p_X^*$"
order = 1552
uses = ["def-sfb-upper-star-from-point", "sk-def-sfb-finite-pushforward-pullback"]
lean = ["AlgebraicGeometry.ProEtale.upperStarFromPointComp"]
+++
Let $f\colon X\to Y$ be a morphism of schemes, and let $p_X^*$, $p_Y^*$ be as
in [def-sfb-upper-star-from-point]. The natural isomorphism
$$
f^*\circ p_Y^*\ \cong\ p_X^*
$$
of functors $\Sh(*_{\mathrm{proét}},\Ab)\to\Sh(X_{\mathrm{proét}},\Ab)$ is
defined as the composite
$$
f^*\circ\pi_Y^*\circ p^*\ \cong\ (\pi_Y\circ f)^*\circ p^*=\pi_X^*\circ p^*.
$$
The first step is the inverse of the composition isomorphism
$(\pi_Y\circ f)^*\cong f^*\circ\pi_Y^*$ of
[sk-def-sfb-finite-pushforward-pullback], whiskered by $p^*$. The equality
holds because $\pi_Y\circ f=\pi_X$, as $\Spec\Z$ is terminal.
