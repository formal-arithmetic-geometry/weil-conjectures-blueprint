+++
id = "sk-prop-sfb-module-pullback-exact"
kind = "proposition"
title = "The pullback of module objects is exact"
order = 1688
uses = ["sk-def-sfb-module-pushforward-pullback"]
lean = ["AlgebraicGeometry.ProEtale.CondensedRing.preservesFiniteColimits_upperStar", "AlgebraicGeometry.ProEtale.CondensedRing.preservesFiniteLimits_upperStar", "AlgebraicGeometry.ProEtale.CondensedRing.preservesHomology_upperStar"]
tags = ["sketch"]
+++
Let $\Lambda$ be a commutative condensed ring and $f\colon X\to Y$ any morphism of
schemes. The pullback of module objects
$f^*\colon\Mod_{\Lambda_Y}\to\Mod_{\Lambda_X}$
([sk-def-sfb-module-pushforward-pullback]) is exact: it preserves finite colimits
and finite limits.
