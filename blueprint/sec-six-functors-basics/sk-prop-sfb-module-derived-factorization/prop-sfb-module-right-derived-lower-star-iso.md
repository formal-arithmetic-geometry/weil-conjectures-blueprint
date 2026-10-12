+++
id = "prop-sfb-module-right-derived-lower-star-iso"
kind = "proposition"
title = "$Rf_*$ is $D(\\operatorname{Res}_{\\eta_f})\\circ R\\operatorname{mapMod}(f_*)$"
order = 1688
uses = ["sk-def-sfb-module-derived-pushpull", "def-sfb-module-lower-star", "sk-def-sfb-change-of-scalars", "sk-def-sfb-derived-categories"]
lean = ["AlgebraicGeometry.ProEtale.CondensedRing.rightDerivedLowerStarIso"]
+++
Let $\Lambda$ be a commutative condensed ring and $f\colon X\to Y$ a morphism of
schemes. The derived pushforward of module objects
([sk-def-sfb-module-derived-pushpull]) is the total right derived functor of
$\operatorname{mapMod}(f^{\Ab}_*)\colon\Mod_{\Lambda_X}\to\Mod_{f^{\Ab}_*\Lambda_X}$
followed by the levelwise restriction of scalars along $\eta_f$: there is a natural
isomorphism

$$
Rf_*\cong D(\operatorname{Res}_{\eta_f})\circ R\operatorname{mapMod}(f^{\Ab}_*)\colon
D(\Mod_{\Lambda_X})\to D(\Mod_{\Lambda_Y}).
$$
