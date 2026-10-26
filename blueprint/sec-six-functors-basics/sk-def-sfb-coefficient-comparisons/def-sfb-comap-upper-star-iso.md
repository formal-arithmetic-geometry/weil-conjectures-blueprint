+++
id = "def-sfb-comap-upper-star-iso"
kind = "definition"
title = "Restriction of scalars commutes with $f^*$"
order = 2591
uses = ["sk-def-sfb-coefficient-change", "det-def-sfb-module-pushforward-pullback", "det-def-sfb-change-of-scalars"]
lean = ["AlgebraicGeometry.ProEtale.CondensedRing.comapUpperStarIso"]
+++
Let $a\colon\Lambda\to\Lambda'$ be a morphism of commutative condensed rings
([sk-def-sfb-coefficient-change]). For every morphism of schemes $f\colon X\to Y$ there is a
natural isomorphism

$$
\operatorname{Res}_{a_X}\circ f^*\;\cong\;f^*\circ\operatorname{Res}_{a_Y}\colon
\Mod_{\Lambda'_Y}\longrightarrow\Mod_{\Lambda_X},
$$

with $f^*$ the pullback of module objects ([det-def-sfb-module-pushforward-pullback]).
