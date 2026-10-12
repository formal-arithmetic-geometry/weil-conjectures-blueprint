+++
id = "def-sfb-derived-lower-shriek-hom"
kind = "definition"
title = "(Shriek)"
order = 1729
uses = ["sk-def-sfb-coefficient-change", "sk-def-sfb-module-derived-lower-shriek", "def-sfb-derived-push-hom", "def-sfb-derived-open-immersion-shriek-iso"]
lean = ["AlgebraicGeometry.ProEtale.CondensedRing.derivedLowerShriekHom"]
+++
Let $a\colon\Lambda\to\Lambda'$ be a morphism of commutative condensed rings such that for every
scheme $X$ the extension of scalars $\operatorname{Ext}_{a_X}$ preserves finite limits, with
derived extensions of scalars $T^X$ ([sk-def-sfb-coefficient-change]). Let $f\colon X\to Y$ be a
morphism of schemes admitting a compactification, with chosen compactification
$X\xrightarrow{i}Z\xrightarrow{g}Y$ ($i$ an open immersion, $g$ proper) and
$Rf_!=R(g_*)\circ D(i_!)$ ([sk-def-sfb-module-derived-lower-shriek]). The comparison
*(Shriek)* is the natural transformation

$$
T^Y\circ Rf_!=T^Y\circ R(g_*)\circ D(i_!)\xrightarrow{\ \mathrm{(Push)}_g\ }
R(g_*)\circ T^Z\circ D(i_!)\xrightarrow{\ \sim\ }R(g_*)\circ D(i_!)\circ T^X=Rf_!\circ T^X
$$

of functors $D(\Mod_{\Lambda_X})\to D(\Mod_{\Lambda'_Y})$: (Push) for $g$
([def-sfb-derived-push-hom]) followed by the extension-by-zero isomorphism for $i$
([def-sfb-derived-open-immersion-shriek-iso]).
