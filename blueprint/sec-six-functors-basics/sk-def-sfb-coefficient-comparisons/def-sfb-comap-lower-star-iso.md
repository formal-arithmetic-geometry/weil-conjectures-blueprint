+++
id = "def-sfb-comap-lower-star-iso"
kind = "definition"
title = "Restriction of scalars commutes with $f_*$"
order = 1733
uses = ["sk-def-sfb-coefficient-change", "sk-def-sfb-module-pushforward-pullback", "sk-def-sfb-change-of-scalars"]
lean = ["AlgebraicGeometry.ProEtale.CondensedRing.comapLowerStarIso"]
+++
Let $a\colon\Lambda\to\Lambda'$ be a morphism of commutative condensed rings with coefficient
changes $a_X$ ([sk-def-sfb-coefficient-change]), and $f\colon X\to Y$ a morphism of schemes.
With $f_*$ the pushforward of module objects ([sk-def-sfb-module-pushforward-pullback]), there
is a natural isomorphism

$$
\operatorname{Res}_{a_Y}\circ f_*\;\cong\;f_*\circ\operatorname{Res}_{a_X}\colon
\Mod_{\Lambda'_X}\longrightarrow\Mod_{\Lambda_Y},
$$

under which both sides are $\mathrm{mapMod}(f_*)$ followed by the restriction of scalars along
$\eta'_f\circ a_Y=f_*a_X\circ\eta_f\colon\Lambda_Y\to f_*\Lambda'_X$.
