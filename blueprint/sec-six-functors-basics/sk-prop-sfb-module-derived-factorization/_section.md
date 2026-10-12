+++
id = "sk-prop-sfb-module-derived-factorization"
kind = "proposition"
title = "Factorizations and levelwise descriptions of the derived functors"
order = 1699
uses = ["sk-def-sfb-module-derived-pushpull", "sk-def-sfb-module-lower-shriek", "sk-def-sfb-derived-extension-of-scalars"]
lean = ["AlgebraicGeometry.ProEtale.CondensedRing.preservesKFlatComplexes_mapMod_upperStar", "AlgebraicGeometry.ProEtale.CondensedRing.rightDerivedLowerStarIso", "AlgebraicGeometry.ProEtale.CondensedRing.leftDerivedUpperStarIso", "AlgebraicGeometry.ProEtale.CondensedRing.leftDerivedUpperStarIsoMapDerivedCategory", "AlgebraicGeometry.ProEtale.CondensedRing.leftDerivedUpperStarComp", "AlgebraicGeometry.ProEtale.CondensedRing.derivedUpperStarLowerStarAdjunctionPlus", "AlgebraicGeometry.ProEtale.CondensedRing.derivedOpenImmersionLowerShriekUpperStarAdjunction", "AlgebraicGeometry.ProEtale.CondensedRing.derivedOpenImmersionLowerShriekUpperStarAdjunctionPlus"]
tags = ["sketch"]
+++
Let $\Lambda$ be a commutative condensed ring and $f\colon X\to Y$ a morphism of
schemes, with $Rf_*$, $R^+f_*$ and $Lf^*$ as in [sk-def-sfb-module-derived-pushpull].
Write $D(F)$, $D^+(F)$ for the functor induced levelwise on derived categories by an
exact functor $F$ ([sk-def-sfb-derived-categories]).

1. The derived pushforward factors as
   $$
   Rf_*\cong D(\operatorname{Res}_{\eta_f})\circ R\operatorname{mapMod}(f^{\Ab}_*),
   $$
   with $R\operatorname{mapMod}(f^{\Ab}_*)\colon D(\Mod_{\Lambda_X})\to
   D(\Mod_{f^{\Ab}_*\Lambda_X})$ ([sk-def-sfb-change-of-scalars],
   [sk-def-sfb-transport]).
2. The transport $\operatorname{mapMod}(f^*_{\Ab})\colon\Mod_{\Lambda_Y}\to
   \Mod_{f^*\Lambda_Y}$ sends K-flat complexes to K-flat complexes, and the derived
   pullback factors as
   $$
   Lf^*\cong L(\operatorname{Ext}_{\alpha_f})\circ D(\operatorname{mapMod}(f^*_{\Ab})),
   \qquad\text{i.e.}\qquad
   Lf^*M\cong\Lambda_X\otimes^{\mathrm L}_{f^*\Lambda_Y}f^*_{\Ab}M,
   $$
   with the derived extension of scalars of
   [sk-def-sfb-derived-extension-of-scalars]; this is the pullback of
   Bhatt–Scholze, Remark 6.8.15.
3. The derived pullback is levelwise: $Lf^*\cong D(f^*)$.
4. For $g\colon Y\to Z$ there is a composition isomorphism
   $L(g\circ f)^*\cong Lf^*\circ Lg^*$.
5. On bounded below derived categories, $D^+(f^*)\dashv R^+f_*$.
6. For an open immersion $j\colon U\to X$, the extension by zero $j_!$ of
   [sk-def-sfb-module-lower-shriek] is derived levelwise, and
   $D(j_!)\dashv D(j^*)$ and $D^+(j_!)\dashv D^+(j^*)$.

In layer (A) the choice "derived functor of the composite" versus "composite of
derived functors" is invisible, the pullback being exact for formal reasons. On module
objects $Lf^*$ is defined through K-flat resolutions, and that it is levelwise is a
consequence of $\alpha_f$ being invertible, which does not enter the definition.
