+++
id = "lem-sfb-module-mapmod-pullback-kflat"
kind = "lemma"
title = "Transport along the pullback preserves K-flat complexes"
order = 2533
uses = ["sk-def-sfb-finite-pushforward-pullback", "det-def-sfb-transport", "det-prop-sfb-module-category", "det-def-sfb-derived-categories"]
lean = ["AlgebraicGeometry.ProEtale.CondensedRing.preservesKFlatComplexes_mapMod_upperStar"]
+++
Let $\Lambda$ be a commutative condensed ring and $f\colon X\to Y$ a morphism of
schemes. The transport
$\operatorname{mapMod}(f^*_{\Ab})\colon\Mod_{\Lambda_Y}\to\Mod_{f^*\Lambda_Y}$ along
the strong monoidal pullback of abelian sheaves ([det-def-sfb-transport],
[sk-def-sfb-finite-pushforward-pullback]) sends K-flat complexes ([det-def-sfb-derived-categories]) of
$\Lambda_Y$-modules to K-flat complexes of $f^*\Lambda_Y$-modules, for the relative
tensor products of [det-prop-sfb-module-category].
