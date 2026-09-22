+++
id = "sbc-def-milnor-tube"
kind = "definition"
title = "Milnor tube"
order = 5229
lean = ["AlgebraicGeometry.milnorTube"]
uses = ["sbc-def-strict-localization"]
+++
Let $f:X\to S$ be a morphism of schemes, $\bar x$ a geometric point of $X$,
$\bar s=f(\bar x)$ its image, and $\bar t\to S_{(\bar s)}$ a geometric point
of the strict localization $S_{(\bar s)}$ [sbc-def-strict-localization]. The
*variety of vanishing cycles (Milnor tube)* of $f$ at $\bar x$ is
$$
F_{\bar x,\bar t}=\bar t\times_{S_{(\bar s)}}X_{(\bar x)}.
$$

Unresolved dependencies: def:weil-pbc-scheme-conventions
