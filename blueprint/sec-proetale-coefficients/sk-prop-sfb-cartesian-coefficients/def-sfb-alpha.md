+++
id = "def-sfb-alpha"
kind = "definition"
title = "The coefficient morphism $\\alpha_f$"
order = 1220
uses = ["def-sfb-pullback-from-point-comp-iso", "det-def-sfb-pulled-back-coefficients"]
lean = ["AlgebraicGeometry.ProEtale.condensedPullbackHom"]
+++
Let $\Lambda$ be a condensed ring and $f\colon X\to Y$ a morphism of schemes.
Then
$$
\alpha_f\colon f^*\Lambda_Y=f^*p_Y^*\Lambda\longrightarrow p_X^*\Lambda=\Lambda_X
$$
is the component at $\Lambda$ of the natural isomorphism
$f^*\circ p_Y^*\cong p_X^*$ of [def-sfb-pullback-from-point-comp-iso]. Here
$\Lambda_X$ and $\Lambda_Y$ are as in [det-def-sfb-pulled-back-coefficients].
