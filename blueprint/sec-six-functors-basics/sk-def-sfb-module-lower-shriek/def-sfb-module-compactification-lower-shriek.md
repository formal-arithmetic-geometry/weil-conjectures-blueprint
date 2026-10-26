+++
id = "def-sfb-module-compactification-lower-shriek"
kind = "definition"
title = "Lower shriek of module objects for a compactification"
order = 2521
uses = ["def-sfb-module-open-lower-shriek", "def-sfb-module-lower-star", "sk-def-nagata-sketch-data"]
lean = ["AlgebraicGeometry.ProEtale.CondensedRing.compactificationLowerShriek"]
+++
Let $\Lambda$ be a commutative condensed ring, $f\colon X\to Y$ a morphism of schemes
and $c=(X\xrightarrow{i}\bar X\xrightarrow{g}Y)$ a compactification of $f$
([sk-def-nagata-sketch-data]): $f=g\circ i$, $i$ an open immersion, $g$ proper. The
*lower shriek attached to $c$* is

$$
f^c_!:=g_*\circ i_!\colon\Mod_{\Lambda_X}\to\Mod_{\Lambda_Y},
$$

the extension by zero along $i$ ([def-sfb-module-open-lower-shriek]) followed by the
pushforward along $g$ ([def-sfb-module-lower-star]).
