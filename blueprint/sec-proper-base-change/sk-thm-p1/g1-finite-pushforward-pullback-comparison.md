+++
id = "g1-finite-pushforward-pullback-comparison"
kind = "lemma"
title = "FinitePushforwardPullbackComparison"
uses = ["def-weil-pbc-cartesian-square", "def-weil-pbc-cohomology-pullback", "def-weil-pbc-constructible-torsion", "def-weil-pbc-curve-setting", "def-weil-pbc-primary-torsion"]
lean = ["AlgebraicGeometry.IsCurve.finite_pushforward_pullback_comparison"]
order = 1961
+++
Let $k$ be algebraically closed, $(X,F)$ a torsion curve coefficient pair [def-weil-pbc-curve-setting], $Y$ a curve over $k$, and $f:X\to Y$ a finite morphism over $k$. Let $A_X,A_Y$ be the abelian sheaves underlying $F$ and $f_*F$, each regarded as a sheaf of $\mathbb Z$-modules. In any cartesian square with upper arrow $b:X'\to X$, lower arrow $a:Y'\to Y$ and vertical arrows $f',f$ [def-weil-pbc-cartesian-square] (no condition on $Y'$), for every $q\ge0$ the pullback $H^q(Y,A_Y)\to H^q(Y',a^{-1}A_Y)$ along $a$ is bijective (respectively surjective) if and only if the pullback $H^q(X,A_X)\to H^q(X',b^{-1}A_X)$ along $b$ is bijective (respectively surjective) [def-weil-pbc-cohomology-pullback].
