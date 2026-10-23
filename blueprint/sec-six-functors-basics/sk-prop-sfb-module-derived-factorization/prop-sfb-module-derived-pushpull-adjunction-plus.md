+++
id = "prop-sfb-module-derived-pushpull-adjunction-plus"
kind = "proposition"
title = "Bounded below adjunction $D^+(f^*)\\dashv R^+f_*$"
order = 2557
uses = ["sk-def-sfb-module-derived-pushpull", "det-prop-sfb-module-pullback-exact-main", "det-def-sfb-derived-categories"]
lean = ["AlgebraicGeometry.ProEtale.CondensedRing.derivedUpperStarLowerStarAdjunctionPlus"]
+++
Let $\Lambda$ be a commutative condensed ring and $f\colon X\to Y$ a morphism of
schemes. On the bounded below derived categories, the functor $D^+(f^*)$ induced by
the exact pullback $f^*$ of module objects ([det-prop-sfb-module-pullback-exact-main]) is
left adjoint to the right derived pushforward $R^+f_*$
([sk-def-sfb-module-derived-pushpull]):

$$
D^+(f^*)\dashv R^+f_*\colon D^+(\Mod_{\Lambda_X})\to D^+(\Mod_{\Lambda_Y}).
$$
