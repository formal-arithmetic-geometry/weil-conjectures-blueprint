+++
id = "def-sfb-derived-comap-lower-star-iso"
kind = "definition"
title = "Derived restriction of scalars commutes with $Rf_*$"
order = 1740
uses = ["sk-def-sfb-coefficient-change", "sk-def-sfb-module-derived-pushpull", "sk-def-sfb-derived-categories"]
lean = ["AlgebraicGeometry.ProEtale.CondensedRing.derivedComapLowerStarIso"]
+++
Let $a\colon\Lambda\to\Lambda'$ be a morphism of commutative condensed rings such that for every
scheme $X$ the extension of scalars $\operatorname{Ext}_{a_X}$ preserves finite limits
($\Lambda'_X$ flat over $\Lambda_X$; [sk-def-sfb-coefficient-change]), and let
$f\colon X\to Y$ be a morphism of schemes. With $Rf_*$ the derived pushforward of module objects
([sk-def-sfb-module-derived-pushpull]) there is a natural isomorphism

$$
D(\operatorname{Res}_{a_Y})\circ Rf_*\;\cong\;Rf_*\circ D(\operatorname{Res}_{a_X})\colon
D(\Mod_{\Lambda'_X})\longrightarrow D(\Mod_{\Lambda_Y}).
$$
