+++
id = "det-def-sfb-coefficient-comparisons"
kind = "definition"
title = "Comparison maps for a change of coefficients"
order = 2401
uses = ["det-def-sfb-coefficient-change", "det-def-sfb-module-derived-lower-shriek"]
lean = ["CategoryTheory.Mod.comapMapModComapIso", "CategoryTheory.Mod.comapMapModComapIso_hom_app_hom", "CategoryTheory.Adjunction.pullIsoOfComapIso", "CategoryTheory.Adjunction.pushHomOfComapIso", "CategoryTheory.Mod.extendScalarsComapIsoOfIsIso", "CategoryTheory.Functor.ProjectionFormula.mapModLeftComapIso", "AlgebraicGeometry.ProEtale.CondensedRing.comapLowerStarIso", "AlgebraicGeometry.ProEtale.CondensedRing.pullIso", "AlgebraicGeometry.ProEtale.CondensedRing.pushHom", "AlgebraicGeometry.ProEtale.CondensedRing.comapUpperStarIso", "AlgebraicGeometry.ProEtale.CondensedRing.derivedComapUpperStarIso", "AlgebraicGeometry.ProEtale.CondensedRing.preservesHomology_extendScalars_coefficientMap", "AlgebraicGeometry.ProEtale.CondensedRing.preservesKInjectiveComplexes_comap_coefficientMap", "AlgebraicGeometry.ProEtale.CondensedRing.derivedComapLowerStarIso", "AlgebraicGeometry.ProEtale.CondensedRing.derivedPullIso", "AlgebraicGeometry.ProEtale.CondensedRing.derivedPushHom", "AlgebraicGeometry.ProEtale.CondensedRing.comapOpenImmersionLowerShriekIso", "AlgebraicGeometry.ProEtale.CondensedRing.openImmersionShriekIso", "AlgebraicGeometry.ProEtale.CondensedRing.derivedOpenImmersionShriekIso", "AlgebraicGeometry.ProEtale.CondensedRing.derivedLowerShriekHom", "AlgebraicGeometry.ProEtale.CondensedRing.isIso_derivedLowerShriekHom"]
+++
Let $a\colon\Lambda\to\Lambda'$ be a morphism of commutative condensed rings, with coefficient
changes $a_X\colon\Lambda_X\to\Lambda'_X$ and derived extensions of scalars
$T^X=L(\operatorname{Ext}_{a_X})$ ([det-def-sfb-coefficient-change]). For a morphism of schemes
$f\colon X\to Y$ write $f^*$, $f_*$ for the pullback and pushforward of module objects over
$\Lambda$ resp. $\Lambda'$ ([det-def-sfb-module-pushforward-pullback]), $Lf^*$, $Rf_*$ for their
derived functors ([det-def-sfb-module-derived-pushpull]), $j_!$ for the extension by zero along
an open immersion $j\colon U\to X$ ([det-def-sfb-module-lower-shriek]), and, when $f$ admits a
compactification, $Rf_!=R(g_*)\circ D(i_!)$ for the chosen compactification $f=g\circ i$
($i$ an open immersion, $g$ proper; [det-def-sfb-module-derived-lower-shriek]). Restriction and
extension of scalars $\operatorname{Res}$, $\operatorname{Ext}$ are those of
[det-def-sfb-change-of-scalars].

The *comparison maps* between the change of coefficients and the six functors are the following
natural transformations; all of them are produced formally, as conjugates and mates, from the
fact that restriction of scalars commutes with pushforward,
$\operatorname{Res}_{a_Y}\circ f_*\cong f_*\circ\operatorname{Res}_{a_X}$, and with pullback,
$\operatorname{Res}_{a_X}\circ f^*\cong f^*\circ\operatorname{Res}_{a_Y}$.

- **Extension by zero.** For every open immersion $j\colon U\to X$, an isomorphism
  $\operatorname{Ext}_{a_X}\circ j_!\cong j_!\circ\operatorname{Ext}_{a_U}$ and an isomorphism
  $T^X\circ D(j_!)\cong D(j_!)\circ T^U$ of functors
  $D(\Mod_{\Lambda_U})\to D(\Mod_{\Lambda'_X})$ on the unbounded derived categories.

Assume moreover that $a$ is *flat*: for every scheme $X$ the extension of scalars
$\operatorname{Ext}_{a_X}=\Lambda'_X\otimes_{\Lambda_X}-$ is exact, i.e. $\Lambda'_X$ is flat
over $\Lambda_X$. Then:

- **(Pull)** an isomorphism $T^X\circ Lf^*\cong Lf^*\circ T^Y$ of functors
  $D(\Mod_{\Lambda_Y})\to D(\Mod_{\Lambda'_X})$, on the unbounded derived categories;
- **(Push)** a natural transformation $T^Y\circ Rf_*\to Rf_*\circ T^X$ of functors
  $D(\Mod_{\Lambda_X})\to D(\Mod_{\Lambda'_Y})$, not an isomorphism in general;
- **(Shriek)** for $f$ admitting a compactification, a natural transformation
  $T^Y\circ Rf_!\to Rf_!\circ T^X$, namely (Push) for the proper part $g$ followed by the
  extension-by-zero isomorphism for the open part $i$; it is an isomorphism whenever (Push) for
  $g$ is an isomorphism.

The underived analogues $\operatorname{Ext}_{a_X}\circ f^*\cong f^*\circ\operatorname{Ext}_{a_Y}$
and $\operatorname{Ext}_{a_Y}\circ f_*\to f_*\circ\operatorname{Ext}_{a_X}$ exist without the
flatness assumption.
