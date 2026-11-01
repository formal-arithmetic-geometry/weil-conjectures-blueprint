+++
id = "det-def-sfb-base-change-morphism-comparison"
kind = "definition"
title = "The pullback comparison of a commutative square"
lean = ["AlgebraicGeometry.ProEtale.CondensedRing.boundedConstructiblePullbackSquareComparison"]
order = 2731
uses = ["def-sfb-dc-upper-star", "def-sfb-dc-upper-star-comp", "det-def-sfb-dc-setting"]
+++
Work in the setting of [det-def-sfb-dc-setting] with a commutative condensed ring $\Lambda$, and
let
$$
\begin{array}{ccc}
X' & \xrightarrow{\;g'\;} & X\\
{\scriptstyle f'}\downarrow & & \downarrow{\scriptstyle f}\\
Y' & \xrightarrow{\;g\;} & Y
\end{array}
\qquad f\circ g'=g\circ f'
$$
be a commutative square of the setting. Write $c_{a,b}\colon L(b\circ a)^*\xrightarrow{\sim}La^*\circ Lb^*$
for the composition isomorphisms of the restricted pullbacks on $D_{\mathrm{cons}}$
([def-sfb-dc-upper-star], [def-sfb-dc-upper-star-comp]). The *pullback comparison* of the square is
the natural isomorphism of functors $D_{\mathrm{cons}}(Y,\Lambda)\to D_{\mathrm{cons}}(X',\Lambda)$
$$
\theta_{sq}\colon Lf'^*\circ Lg^*\xrightarrow{\ c_{f',g}^{-1}\ }L(g\circ f')^*=L(f\circ g')^*\xrightarrow{\ c_{g',f}\ }Lg'^*\circ Lf^* .
$$
The middle equality uses only $g\circ f'=f\circ g'$. As a composite of natural isomorphisms,
$\theta_{sq}$ is a natural isomorphism.
