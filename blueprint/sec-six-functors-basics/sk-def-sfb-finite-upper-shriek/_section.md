+++
id = "sk-def-sfb-finite-upper-shriek"
kind = "definition"
title = "Exceptional pullback $Rf^!$ (finite coefficients)"
order = 1658
uses = ["sk-def-nagata-sketch-data", "sk-def-sfb-finite-derived-lower-shriek"]
lean = ["AlgebraicGeometry.ProEtale.isLeftAdjoint_rightDerivedLowerStar_of_isProper", "AlgebraicGeometry.ProEtale.rightDerivedUpperShriekOfCompactification", "AlgebraicGeometry.ProEtale.rightDerivedUpperShriek", "AlgebraicGeometry.ProEtale.rightDerivedUpperShriekOfCompactificationAdjunction", "AlgebraicGeometry.ProEtale.rightDerivedUpperShriekAdjunction", "AlgebraicGeometry.ProEtale.isLeftAdjoint_rightDerivedLowerShriek", "AlgebraicGeometry.ProEtale.plus_rightDerivedUpperShriek_obj", "AlgebraicGeometry.ProEtale.rightDerivedUpperShriekPlus", "AlgebraicGeometry.ProEtale.rightDerivedUpperShriekPlusAdjunction"]
tags = ["sketch"]
+++
Let $\mathcal A$ be a Grothendieck abelian category. For a proper morphism $g$, the derived
pushforward $Rg_*$ of [sk-def-sfb-finite-derived-functors] on unbounded derived categories
has a right adjoint; fix one and call it $Rg^!$.

Let $f\colon X\to Y$ admit a compactification [sk-def-nagata-sketch-data], with chosen
compactification $X\xrightarrow{i}\bar X\xrightarrow{g}Y$ as in
[sk-def-sfb-finite-derived-lower-shriek]. The *exceptional pullback* is

$$
Rf^!:=D(i^*)\circ Rg^!\colon D(Y_{\mathrm{proét}},\mathcal A)\to D(X_{\mathrm{proét}},\mathcal A),
$$

with $D(i^*)$ induced levelwise by the exact pullback $i^*$
([sk-def-sfb-finite-pushforward-pullback]). The functor $Rg^!$ enters only through the
adjunction $Rg_*\dashv Rg^!$.

Assume moreover that $\mathcal A$ satisfies the monoidal hypotheses of
[sk-def-sfb-finite-derived-functors]. Then:

1. $Rf_!\dashv Rf^!$, the composite of the adjunctions $D(i_!)\dashv D(i^*)$ and
   $Rg_*\dashv Rg^!$. In particular $Rf_!$ ([sk-def-sfb-finite-derived-lower-shriek]) is
   a left adjoint; this is a theorem, not an assumption.
2. Suppose that $Rg_*$ has finite cohomological amplitude. Then $Rf^!$ preserves bounded
   below objects, so it restricts to $Rf^{!,+}\colon D^+(Y_{\mathrm{proét}},\mathcal A)\to
   D^+(X_{\mathrm{proét}},\mathcal A)$, and the adjunction restricts to
   $Rf_!^+\dashv Rf^{!,+}$.
