+++
id = "prop-sfb-module-left-derived-upper-star-iso"
kind = "proposition"
title = "$Lf^*$ is $L(\\operatorname{Ext}_{\\alpha_f})\\circ D(\\operatorname{mapMod}(f^*))$"
order = 2554
uses = ["sk-def-sfb-module-derived-pushpull", "def-sfb-module-upper-star", "lem-sfb-module-mapmod-pullback-kflat", "det-def-sfb-derived-extension-of-scalars"]
lean = ["AlgebraicGeometry.ProEtale.CondensedRing.leftDerivedUpperStarIso"]
+++
Let $\Lambda$ be a commutative condensed ring and $f\colon X\to Y$ a morphism of
schemes. The derived pullback of module objects
([sk-def-sfb-module-derived-pushpull]) is the levelwise transport
$D(\operatorname{mapMod}(f^*_{\Ab}))\colon D(\Mod_{\Lambda_Y})\to
D(\Mod_{f^*\Lambda_Y})$ followed by the derived extension of scalars along $\alpha_f$
([det-def-sfb-derived-extension-of-scalars]): there is a natural isomorphism

$$
Lf^*\cong L(\operatorname{Ext}_{\alpha_f})\circ D(\operatorname{mapMod}(f^*_{\Ab})),
\qquad Lf^*M\cong\Lambda_X\otimes^{\mathrm L}_{f^*\Lambda_Y}f^*_{\Ab}M .
$$
