+++
id = "sk-def-sfb-finite-lower-shriek"
kind = "definition"
title = "Extension by zero and lower shriek (finite coefficients)"
order = 1653
uses = ["def-weil-pbc-proetale-site", "sk-def-nagata-sketch-data", "sk-def-sfb-finite-pushforward-pullback"]
lean = ["AlgebraicGeometry.ProEtale.openImmersionLowerShriek", "AlgebraicGeometry.ProEtale.openImmersionLowerShriekUpperStarAdjunction", "AlgebraicGeometry.ProEtale.preservesFiniteLimits_openImmersionLowerShriek", "AlgebraicGeometry.ProEtale.fullyFaithfulOpenImmersionLowerShriek", "AlgebraicGeometry.ProEtale.Compactification.lowerShriek", "AlgebraicGeometry.ProEtale.lowerShriek", "AlgebraicGeometry.ProEtale.lowerShriekToLowerStar", "AlgebraicGeometry.ProEtale.isIso_lowerShriekToLowerStar"]
tags = ["sketch"]
+++
Let $\mathcal A$ be a Grothendieck abelian category.

For an open immersion $j\colon U\to X$, the *extension by zero*
$j_!\colon\Sh(U_{\mathrm{proét}},\mathcal A)\to\Sh(X_{\mathrm{proét}},\mathcal A)$ is
sheafification composed with the left Kan extension along the opposite of the
localization functor $U_{\mathrm{proét}}\to X_{\mathrm{proét}}$,
$(T\to U)\mapsto(T\to U\to X)$. It is left adjoint to the pullback $j^*$ of
[sk-def-sfb-finite-pushforward-pullback], exact, and fully faithful.

For a compactification $c=(X\xrightarrow{i}\bar X\xrightarrow{g}Y)$ of $f\colon X\to Y$
[sk-def-nagata-sketch-data], put $f_!^c:=g_*\circ i_!$. For $f$ admitting a
compactification, the *lower shriek* is $f_!:=f_!^c$ for a chosen compactification $c$
of $f$. There is a canonical natural transformation $f_!\to f_*$, and it is an
isomorphism when $f$ is proper.
