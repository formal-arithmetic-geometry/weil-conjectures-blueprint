+++
id = "prop-sfb-module-left-derived-upper-star-levelwise"
kind = "proposition"
title = "The derived pullback of module objects is levelwise"
order = 1329
uses = ["det-def-sfb-module-derived-pushpull", "det-prop-sfb-module-pullback-exact-main", "det-def-sfb-derived-categories"]
lean = ["AlgebraicGeometry.ProEtale.CondensedRing.leftDerivedUpperStarIsoMapDerivedCategory"]
+++
Let $\Lambda$ be a commutative condensed ring and $f\colon X\to Y$ a morphism of
schemes. The total left derived functor $Lf^*$ of the pullback of module objects
([det-def-sfb-module-derived-pushpull]), computed via K-flat resolutions, is
canonically isomorphic to the functor $D(f^*)$ obtained by applying the exact functor
$f^*$ ([det-prop-sfb-module-pullback-exact-main]) levelwise:

$$
Lf^*\cong D(f^*)\colon D(\Mod_{\Lambda_Y})\to D(\Mod_{\Lambda_X}).
$$
