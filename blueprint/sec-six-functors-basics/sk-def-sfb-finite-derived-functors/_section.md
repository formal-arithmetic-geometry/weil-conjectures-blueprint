+++
id = "sk-def-sfb-finite-derived-functors"
kind = "definition"
title = "Derived pushforward and pullback (finite coefficients)"
order = 1684
uses = ["sk-def-sfb-derived-categories", "sk-def-sfb-finite-lower-shriek"]
lean = ["AlgebraicGeometry.ProEtale.leftDerivedUpperStarIsoMapDerivedCategory", "AlgebraicGeometry.ProEtale.derivedUpperStarLowerStarAdjunction", "AlgebraicGeometry.ProEtale.derivedUpperStarLowerStarAdjunctionPlus", "AlgebraicGeometry.ProEtale.derivedOpenImmersionLowerShriekUpperStarAdjunction", "AlgebraicGeometry.ProEtale.derivedOpenImmersionLowerShriekUpperStarAdjunctionPlus"]
tags = ["sketch"]
+++
Let $\mathcal A$ be a Grothendieck abelian category and $g\colon Z\to Y$ a morphism of
schemes. Write $D(X_{\mathrm{proét}},\mathcal A)=D(\Sh(X_{\mathrm{proét}},\mathcal A))$ and
$D^+(X_{\mathrm{proét}},\mathcal A)$ for its bounded below part, and use the derived functors
of [sk-def-sfb-derived-categories]. With $g_*$, $g^*$ as in
[sk-def-sfb-finite-pushforward-pullback], define

$$
Rg_*:=R(g_*)\colon D(Z_{\mathrm{proét}},\mathcal A)\to D(Y_{\mathrm{proét}},\mathcal A),
$$

computed on K-injective resolutions, and its bounded below version
$R^+g_*\colon D^+(Z_{\mathrm{proét}},\mathcal A)\to D^+(Y_{\mathrm{proét}},\mathcal A)$,
computed on injective resolutions.

Assume moreover that $\mathcal A$ is closed symmetric monoidal with additive tensor
product and has functorial flat resolutions. Define

$$
Lg^*:=L(g^*)\colon D(Y_{\mathrm{proét}},\mathcal A)\to D(Z_{\mathrm{proét}},\mathcal A),
$$

computed on K-flat resolutions. Then:

1. $Lg^*\cong D(g^*)$, the functor induced levelwise by the exact functor $g^*$.
2. $Lg^*\dashv Rg_*$, and on bounded below categories $D^+(g^*)\dashv R^+g_*$.
3. For an open immersion $j$, the exact functors $j_!$ and $j^*$
   ([sk-def-sfb-finite-lower-shriek]) induce an adjunction $D(j_!)\dashv D(j^*)$, and
   likewise $D^+(j_!)\dashv D^+(j^*)$.
