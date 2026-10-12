+++
id = "def-sfb-module-derived-lower-shriek-chosen"
kind = "definition"
title = "Derived lower shriek of module objects"
order = 1661
uses = ["def-sfb-module-derived-lower-shriek-compactification"]
lean = ["AlgebraicGeometry.ProEtale.CondensedRing.rightDerivedLowerShriek"]
+++
Let $\Lambda$ be a commutative condensed ring and $f\colon X\to Y$ a morphism of
schemes admitting a compactification. The *derived lower shriek*

$$
Rf_!\colon D(\Mod_{\Lambda_X})\to D(\Mod_{\Lambda_Y})
$$

is the functor $Rf^c_!=Rg_*\circ D(i_!)$ of
[def-sfb-module-derived-lower-shriek-compactification] for the chosen
compactification $c=(X\xrightarrow{i}\bar X\xrightarrow{g}Y)$ of $f$.
