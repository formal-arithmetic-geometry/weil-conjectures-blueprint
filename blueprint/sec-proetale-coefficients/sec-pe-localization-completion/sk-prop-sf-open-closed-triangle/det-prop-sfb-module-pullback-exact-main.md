+++
id = "det-prop-sfb-module-pullback-exact-main"
kind = "proposition"
title = "Exactness of $f^*$ on module objects"
lean = ["AlgebraicGeometry.ProEtale.CondensedRing.upperStar_additive", "AlgebraicGeometry.ProEtale.CondensedRing.preservesFiniteLimits_upperStar", "AlgebraicGeometry.ProEtale.CondensedRing.preservesFiniteColimits_upperStar", "AlgebraicGeometry.ProEtale.CondensedRing.preservesHomology_upperStar", "CategoryTheory.Functor.preservesFiniteLimits_mapMod", "CategoryTheory.Functor.preservesFiniteColimits_mapMod", "CategoryTheory.Mod.extendScalarsIsoComapInv"]
order = 1212
uses = ["det-prop-sfb-module-pullback-exact-lifted", "def-sfb-module-upper-star", "def-sfb-modobj-transport", "def-sfb-modobj-extension-along-iso", "lem-sfb-alpha-iso", "lem-sfb-finite-upper-star-exact"]
+++
Let $\Lambda$ be a commutative condensed ring and $f\colon X\to Y$ any morphism of schemes. The
pullback of module objects
$$
f^*=\operatorname{Ext}_{\alpha_f}\circ\operatorname{mapMod}(f^*_{\Ab})\colon\Mod_{\Lambda_Y}\to\Mod_{\Lambda_X}
$$
of [def-sfb-module-upper-star] is exact: it is additive and preserves finite limits and finite
colimits. More precisely, both $\operatorname{mapMod}(f^*_{\Ab})\colon\Mod_{\Lambda_Y}\to\Mod_{f^*\Lambda_Y}$
and $\operatorname{Ext}_{\alpha_f}\colon\Mod_{f^*\Lambda_Y}\to\Mod_{\Lambda_X}$ are exact.
