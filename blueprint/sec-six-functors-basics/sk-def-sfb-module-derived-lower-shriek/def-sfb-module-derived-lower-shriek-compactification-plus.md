+++
id = "def-sfb-module-derived-lower-shriek-compactification-plus"
kind = "definition"
title = "Bounded below derived lower shriek for a compactification"
order = 2543
uses = ["def-sfb-module-open-lower-shriek", "sk-def-sfb-module-derived-pushpull", "det-def-sfb-derived-categories", "sk-def-nagata-sketch-data"]
lean = ["AlgebraicGeometry.ProEtale.CondensedRing.rightDerivedLowerShriekOfCompactificationPlus"]
+++
Let $\Lambda$ be a commutative condensed ring and
$c=(X\xrightarrow{i}\bar X\xrightarrow{g}Y)$ a compactification of a morphism
$f\colon X\to Y$ ([sk-def-nagata-sketch-data]). On the bounded below derived
categories the derived lower shriek attached to $c$ is

$$
R^+f^c_!:=R^+g_*\circ D^+(i_!)\colon D^+(\Mod_{\Lambda_X})\to D^+(\Mod_{\Lambda_Y}),
$$

with $D^+(i_!)$ the levelwise functor ([det-def-sfb-derived-categories]) of the exact extension by zero
([def-sfb-module-open-lower-shriek]) and $R^+g_*$ the right derived pushforward on
bounded below derived categories ([sk-def-sfb-module-derived-pushpull]).
