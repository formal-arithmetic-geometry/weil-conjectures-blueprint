+++
id = "def-sfb-derived-pull-iso"
kind = "definition"
title = "(Pull)"
order = 1724
uses = ["sk-def-sfb-coefficient-change", "sk-def-sfb-module-derived-pushpull", "sk-def-sfb-derived-extension-of-scalars", "def-sfb-conjugate-pull-iso", "def-sfb-derived-comap-lower-star-iso"]
lean = ["AlgebraicGeometry.ProEtale.CondensedRing.derivedPullIso"]
+++
Let $a\colon\Lambda\to\Lambda'$ be a morphism of commutative condensed rings such that for every
scheme $X$ the extension of scalars $\operatorname{Ext}_{a_X}$ preserves finite limits, with
derived extensions of scalars $T^X$ ([sk-def-sfb-coefficient-change]), and let
$f\colon X\to Y$ be a morphism of schemes. The comparison *(Pull)* is the natural isomorphism

$$
T^X\circ Lf^*\;\cong\;Lf^*\circ T^Y\colon D(\Mod_{\Lambda_Y})\longrightarrow
D(\Mod_{\Lambda'_X})
$$

on the unbounded derived categories, with $Lf^*$ the derived pullback of module objects
([sk-def-sfb-module-derived-pushpull]): the conjugate ([def-sfb-conjugate-pull-iso]) of the
isomorphism of [def-sfb-derived-comap-lower-star-iso] along the derived adjunctions
$Lf^*\dashv Rf_*$ (over $\Lambda$ and over $\Lambda'$) and $T\dashv D(\operatorname{Res})$
([sk-def-sfb-derived-extension-of-scalars]).
