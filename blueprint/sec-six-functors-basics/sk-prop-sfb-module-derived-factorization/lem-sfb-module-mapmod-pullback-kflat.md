+++
id = "lem-sfb-module-mapmod-pullback-kflat"
kind = "lemma"
title = "Transport along the pullback preserves K-flat complexes"
order = 1704
uses = ["sk-def-sfb-finite-pushforward-pullback", "sk-def-sfb-transport", "sk-prop-sfb-module-category", "sk-def-sfb-derived-categories"]
lean = ["AlgebraicGeometry.ProEtale.CondensedRing.preservesKFlatComplexes_mapMod_upperStar"]
+++
Let $\Lambda$ be a commutative condensed ring and $f\colon X\to Y$ a morphism of
schemes. The transport
$\operatorname{mapMod}(f^*_{\Ab})\colon\Mod_{\Lambda_Y}\to\Mod_{f^*\Lambda_Y}$ along
the strong monoidal pullback of abelian sheaves ([sk-def-sfb-transport],
[sk-def-sfb-finite-pushforward-pullback]) sends K-flat complexes ([sk-def-sfb-derived-categories]) of
$\Lambda_Y$-modules to K-flat complexes of $f^*\Lambda_Y$-modules, for the relative
tensor products of [sk-prop-sfb-module-category].
