+++
id = "prop-sfb-module-left-derived-upper-star-comp"
kind = "proposition"
title = "Composition isomorphism of derived pullbacks of module objects"
order = 2556
uses = ["sk-def-sfb-module-derived-pushpull", "def-sfb-module-upper-star-comp"]
lean = ["AlgebraicGeometry.ProEtale.CondensedRing.leftDerivedUpperStarComp"]
+++
Let $\Lambda$ be a commutative condensed ring and $f\colon X\to Y$, $g\colon Y\to Z$
morphisms of schemes. There is a natural isomorphism

$$
L(g\circ f)^*\cong Lf^*\circ Lg^*\colon D(\Mod_{\Lambda_Z})\to D(\Mod_{\Lambda_X})
$$

of derived pullbacks ([sk-def-sfb-module-derived-pushpull]), induced by the underived
composition isomorphism $(g\circ f)^*\cong f^*\circ g^*$ of
[def-sfb-module-upper-star-comp].
