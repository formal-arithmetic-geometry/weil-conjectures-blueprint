+++
id = "prop-sfb-module-derived-open-adjunction"
kind = "proposition"
title = "Derived adjunction $D(j_!)\\dashv D(j^*)$ on module objects"
order = 1332
uses = ["def-sfb-module-open-lower-shriek", "def-sfb-module-open-lower-shriek-adjunction", "det-prop-sfb-module-pullback-exact-main", "det-def-sfb-derived-categories"]
lean = ["AlgebraicGeometry.ProEtale.CondensedRing.derivedOpenImmersionLowerShriekUpperStarAdjunction"]
+++
Let $\Lambda$ be a commutative condensed ring and $j\colon U\to X$ an open immersion.
The extension by zero $j_!$ of module objects ([def-sfb-module-open-lower-shriek]) and
the pullback $j^*$ are exact ([det-prop-sfb-module-pullback-exact-main]), and the functors
they induce levelwise on the unbounded derived categories are adjoint:

$$
D(j_!)\dashv D(j^*)\colon D(\Mod_{\Lambda_X})\to D(\Mod_{\Lambda_U}).
$$
