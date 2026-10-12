+++
id = "def-sfb-push-hom"
kind = "definition"
title = "Underived (Push)"
order = 1718
uses = ["sk-def-sfb-coefficient-change", "sk-def-sfb-module-pushforward-pullback", "sk-def-sfb-change-of-scalars", "def-sfb-mate-push-hom", "def-sfb-comap-lower-star-iso"]
lean = ["AlgebraicGeometry.ProEtale.CondensedRing.pushHom"]
+++
For a morphism $a\colon\Lambda\to\Lambda'$ of commutative condensed rings
([sk-def-sfb-coefficient-change]) and a morphism of schemes $f\colon X\to Y$, the underived
*(Push)* comparison is the natural transformation

$$
\operatorname{Ext}_{a_Y}\circ f_*\longrightarrow f_*\circ\operatorname{Ext}_{a_X}\colon
\Mod_{\Lambda_X}\longrightarrow\Mod_{\Lambda'_Y},
$$

with $f_*$ the pushforward of module objects ([sk-def-sfb-module-pushforward-pullback]): the mate
([def-sfb-mate-push-hom]) of the isomorphism of [def-sfb-comap-lower-star-iso] along
$\operatorname{Ext}_{a_X}\dashv\operatorname{Res}_{a_X}$ and
$\operatorname{Ext}_{a_Y}\dashv\operatorname{Res}_{a_Y}$ ([sk-def-sfb-change-of-scalars]).
