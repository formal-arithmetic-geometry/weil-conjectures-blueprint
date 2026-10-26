+++
id = "lem-sfb-coefficient-pushforward-square"
kind = "lemma"
title = "Coefficient changes commute with $\\eta_f$"
order = 2552
uses = ["def-sfb-coefficient-map", "det-def-sfb-coefficient-morphisms", "sk-def-sfb-finite-pushforward-pullback"]
lean = ["AlgebraicGeometry.ProEtale.condensedPushforwardHom_comp_map_coefficientMap"]
+++
Let $a\colon\Lambda\to\Lambda'$ be a morphism of condensed abelian groups (in particular of
condensed rings), $f\colon X\to Y$ a morphism of schemes, and
$\eta_f\colon\Lambda_Y\to f_*\Lambda_X$, $\eta'_f\colon\Lambda'_Y\to f_*\Lambda'_X$ the
coefficient morphisms of [det-def-sfb-coefficient-morphisms], with $f_*$ the pushforward of
abelian sheaves ([sk-def-sfb-finite-pushforward-pullback]). Then

$$
f_*a_X\circ\eta_f=\eta'_f\circ a_Y\colon\Lambda_Y\longrightarrow f_*\Lambda'_X ,
$$

with $a_X$, $a_Y$ the coefficient changes of [def-sfb-coefficient-map].
