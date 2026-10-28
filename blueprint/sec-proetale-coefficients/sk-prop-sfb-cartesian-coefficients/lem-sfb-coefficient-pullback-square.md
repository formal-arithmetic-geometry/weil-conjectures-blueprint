+++
id = "lem-sfb-coefficient-pullback-square"
kind = "lemma"
title = "Coefficient changes commute with $\\alpha_f$"
order = 1336
uses = ["def-sfb-coefficient-map", "det-def-sfb-coefficient-morphisms", "sk-def-sfb-finite-pushforward-pullback"]
lean = ["AlgebraicGeometry.ProEtale.map_coefficientMap_comp_condensedPullbackHom"]
+++
Let $a\colon\Lambda\to\Lambda'$ be a morphism of condensed abelian groups (in particular of
condensed rings), $f\colon X\to Y$ a morphism of schemes, and
$\alpha_f\colon f^*\Lambda_Y\to\Lambda_X$, $\alpha'_f\colon f^*\Lambda'_Y\to\Lambda'_X$ the
coefficient morphisms of [det-def-sfb-coefficient-morphisms], with $f^*$ the pullback of abelian
sheaves ([sk-def-sfb-finite-pushforward-pullback]). Then

$$
\alpha'_f\circ f^*a_Y=a_X\circ\alpha_f\colon f^*\Lambda_Y\longrightarrow\Lambda'_X ,
$$

with $a_X$, $a_Y$ the coefficient changes of [def-sfb-coefficient-map].
