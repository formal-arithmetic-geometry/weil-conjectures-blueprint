+++
id = "def-sfb-module-derived-lower-shriek-compactification"
kind = "definition"
title = "Derived lower shriek of module objects for a compactification"
order = 2561
uses = ["def-sfb-module-open-lower-shriek", "sk-def-sfb-module-derived-pushpull", "det-def-sfb-derived-categories", "sk-def-nagata-sketch-data"]
lean = ["AlgebraicGeometry.ProEtale.CondensedRing.rightDerivedLowerShriekOfCompactification"]
+++
Let $\Lambda$ be a commutative condensed ring and
$c=(X\xrightarrow{i}\bar X\xrightarrow{g}Y)$ a compactification of a morphism
$f\colon X\to Y$ ([sk-def-nagata-sketch-data]). The *derived lower shriek attached to
$c$* is

$$
Rf^c_!:=Rg_*\circ D(i_!)\colon D(\Mod_{\Lambda_X})\to D(\Mod_{\Lambda_Y}),
$$

the functor induced on derived categories by the exact extension by zero $i_!$
([def-sfb-module-open-lower-shriek]) applied levelwise ([det-def-sfb-derived-categories]), followed by the total right
derived pushforward $Rg_*$ ([sk-def-sfb-module-derived-pushpull]). It is not the
total right derived functor of $g_*\circ i_!$.
