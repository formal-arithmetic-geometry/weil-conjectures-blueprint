+++
id = "def-weil-open-immersion"
kind = "definition"
title = "Open immersion of schemes"
order = 12
uses = ["def-pc-scheme"]
lean = ["AlgebraicGeometry.IsOpenImmersion"]
tags = ["mathlib", "stacks-01HE"]
+++
A morphism of schemes $f:X\to Y$ [def-pc-scheme] is an *open immersion* if $f$ is a homeomorphism of the underlying space of $X$ onto an open subset $U$ of $Y$ and the induced map $f^{-1}\mathcal O_Y\to\mathcal O_X$ is an isomorphism of sheaves of rings; equivalently, $f$ induces an isomorphism of $X$ with the open subscheme $(U,\mathcal O_Y|_U)$ of $Y$.
