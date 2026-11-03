+++
id = "det-def-sfb-finite-derived-lower-shriek"
kind = "definition"
title = "Derived lower shriek and $R\\Gamma_c$ (finite coefficients)"
order = 2547
uses = ["def-weil-pbc-proetale-site", "sk-def-nagata-sketch-data", "det-def-sfb-finite-derived-functors"]
lean = ["AlgebraicGeometry.ProEtale.rightDerivedLowerShriekOfCompactification", "AlgebraicGeometry.ProEtale.rightDerivedLowerShriek", "AlgebraicGeometry.ProEtale.rightDerivedLowerShriekPlus", "AlgebraicGeometry.ProEtale.rightDerivedLowerShriekPlusCompatibility", "AlgebraicGeometry.ProEtale.rightDerivedGlobalSections", "AlgebraicGeometry.ProEtale.compactlySupportedGlobalSections"]
+++
Let $\mathcal A$ be a Grothendieck abelian category and let $f\colon X\to Y$ admit a
compactification [sk-def-nagata-sketch-data], with chosen compactification
$X\xrightarrow{i}\bar X\xrightarrow{g}Y$ as in [det-def-sfb-finite-lower-shriek]. The
*derived lower shriek* is

$$
Rf_!:=Rg_*\circ D(i_!)\colon D(X_{\mathrm{proét}},\mathcal A)\to D(Y_{\mathrm{proét}},\mathcal A),
$$

with $D(i_!)$ induced levelwise by the exact extension by zero
([det-def-sfb-finite-lower-shriek]) and $Rg_*$ the derived pushforward of
[det-def-sfb-finite-derived-functors]. Its bounded below version
$Rf_!^+:=R^+g_*\circ D^+(i_!)\colon D^+(X_{\mathrm{proét}},\mathcal A)\to D^+(Y_{\mathrm{proét}},\mathcal A)$
is the restriction of $Rf_!$: there is an isomorphism
$\iota\circ Rf_!^+\cong Rf_!\circ\iota$, with $\iota$ the inclusions $D^+\subseteq D$.

$Rf_!$ is in general *not* the right derived functor $R(f_!)=R(g_*\circ i_!)$ of the
lower shriek, although $H^0(Rf_!F)=f_!F$ for a sheaf $F$ placed in degree $0$.

The *compactly supported cohomology complex* is

$$
R\Gamma_c(X/Y,-):=R\Gamma(Y,-)\circ Rf_!\colon D(X_{\mathrm{proét}},\mathcal A)\to D(\mathcal A),
$$

where $R\Gamma(Y,-)=R\Gamma(Y_{\mathrm{proét}},-)$ is the right derived functor of global
sections.
