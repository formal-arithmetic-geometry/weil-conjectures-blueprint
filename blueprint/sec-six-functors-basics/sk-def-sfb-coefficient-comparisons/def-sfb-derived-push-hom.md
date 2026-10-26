+++
id = "def-sfb-derived-push-hom"
kind = "definition"
title = "(Push)"
order = 2597
uses = ["sk-def-sfb-coefficient-change", "sk-def-sfb-module-derived-pushpull", "det-def-sfb-derived-extension-of-scalars", "def-sfb-mate-push-hom", "def-sfb-derived-comap-lower-star-iso"]
lean = ["AlgebraicGeometry.ProEtale.CondensedRing.derivedPushHom"]
+++
Let $a\colon\Lambda\to\Lambda'$ be a morphism of commutative condensed rings such that for every
scheme $X$ the extension of scalars $\operatorname{Ext}_{a_X}$ preserves finite limits, with
derived extensions of scalars $T^X$ ([sk-def-sfb-coefficient-change]), and let
$f\colon X\to Y$ be a morphism of schemes. The comparison *(Push)* is the natural transformation

$$
T^Y\circ Rf_*\longrightarrow Rf_*\circ T^X\colon D(\Mod_{\Lambda_X})\longrightarrow
D(\Mod_{\Lambda'_Y}),
$$

with $Rf_*$ the derived pushforward of module objects ([sk-def-sfb-module-derived-pushpull]):
the mate ([def-sfb-mate-push-hom]) of the isomorphism of [def-sfb-derived-comap-lower-star-iso]
along the adjunctions $T^X\dashv D(\operatorname{Res}_{a_X})$ and
$T^Y\dashv D(\operatorname{Res}_{a_Y})$ ([det-def-sfb-derived-extension-of-scalars]). It is not
an isomorphism in general.
