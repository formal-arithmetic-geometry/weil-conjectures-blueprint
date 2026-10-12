+++
id = "sk-def-sfb-module-derived-lower-shriek"
kind = "definition"
title = "Derived lower shriek of module objects"
order = 1695
uses = ["sk-def-sfb-module-lower-shriek", "sk-def-sfb-module-derived-pushpull", "sk-def-nagata-sketch-data"]
lean = ["AlgebraicGeometry.ProEtale.CondensedRing.rightDerivedLowerShriekOfCompactification", "AlgebraicGeometry.ProEtale.CondensedRing.rightDerivedLowerShriekOfCompactificationPlus", "AlgebraicGeometry.ProEtale.CondensedRing.rightDerivedLowerShriekOfCompactificationPlusCompatibility", "AlgebraicGeometry.ProEtale.CondensedRing.rightDerivedLowerShriek", "AlgebraicGeometry.ProEtale.CondensedRing.rightDerivedLowerShriekPlus", "AlgebraicGeometry.ProEtale.CondensedRing.rightDerivedLowerShriekPlusCompatibility"]
tags = ["sketch"]
+++
Let $\Lambda$ be a commutative condensed ring and $f\colon X\to Y$ a morphism of
schemes. For a compactification $c=(X\xrightarrow{i}\bar X\xrightarrow{g}Y)$ of $f$
([sk-def-nagata-sketch-data]) the *derived lower shriek attached to $c$* is the
composite of derived functors

$$
Rf^c_!:=Rg_*\circ D(i_!)\colon D(\Mod_{\Lambda_X})\to D(\Mod_{\Lambda_Y}),
\qquad
R^+f^c_!:=R^+g_*\circ D^+(i_!)\colon D^+(\Mod_{\Lambda_X})\to D^+(\Mod_{\Lambda_Y}),
$$

where $D(i_!)$, $D^+(i_!)$ apply the exact extension by zero of module objects
([sk-def-sfb-module-lower-shriek]) levelwise ([sk-def-sfb-derived-categories]) and $Rg_*$, $R^+g_*$ are the derived
pushforwards of [sk-def-sfb-module-derived-pushpull]. For $f$ admitting a
compactification, $Rf_!:=Rf^c_!$ and $R^+f_!:=R^+f^c_!$ for the chosen
compactification $c$ of $f$. The bounded below functors are the restrictions of the
unbounded ones: $R^+f^c_!$ agrees with $Rf^c_!$ on $D^+(\Mod_{\Lambda_X})$.

Here, and only here, the derived functor is a composite of derived functors rather
than the derived functor of the composite: $Rf^c_!$ is *not* the total right derived
functor of $f^c_!=g_*\circ i_!$. The extension by zero $i_!$ does not send injective
modules to $g_*$-acyclic ones, so $R(g_*\circ i_!)$ is the wrong functor, although its
$H^0$ is $f^c_!$.
