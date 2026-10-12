+++
id = "def-sfb-pull-iso"
kind = "definition"
title = "Underived (Pull)"
order = 1730
uses = ["sk-def-sfb-coefficient-change", "sk-def-sfb-module-pushforward-pullback", "sk-def-sfb-change-of-scalars", "def-sfb-conjugate-pull-iso", "def-sfb-comap-lower-star-iso"]
lean = ["AlgebraicGeometry.ProEtale.CondensedRing.pullIso"]
+++
For a morphism $a\colon\Lambda\to\Lambda'$ of commutative condensed rings
([sk-def-sfb-coefficient-change]) and a morphism of schemes $f\colon X\to Y$, the underived
*(Pull)* comparison is the natural isomorphism

$$
\operatorname{Ext}_{a_X}\circ f^*\;\cong\;f^*\circ\operatorname{Ext}_{a_Y}\colon
\Mod_{\Lambda_Y}\longrightarrow\Mod_{\Lambda'_X},
$$

with $f^*$ the pullback of module objects ([sk-def-sfb-module-pushforward-pullback]), defined as
the conjugate of the isomorphism of [def-sfb-comap-lower-star-iso] along the adjunctions
$f^*\dashv f_*$ (over $\Lambda$ and over $\Lambda'$) and
$\operatorname{Ext}\dashv\operatorname{Res}$ ([sk-def-sfb-change-of-scalars]), in the sense of
[def-sfb-conjugate-pull-iso].
