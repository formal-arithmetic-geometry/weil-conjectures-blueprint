+++
id = "def-sfb-finite-shriek-adjunction-compactification"
kind = "definition"
title = "The adjunction $Rf_!^c\\dashv Rf^!_c$"
order = 1675
uses = ["def-sfb-finite-derived-extension-by-zero-adjunction", "def-sfb-finite-derived-lower-shriek-compactification", "def-sfb-finite-derived-pullback-iso", "def-sfb-finite-upper-shriek-compactification", "thm-sfb-finite-proper-pushforward-left-adjoint"]
lean = ["AlgebraicGeometry.ProEtale.rightDerivedUpperShriekOfCompactificationAdjunction"]
+++
Let $\mathcal A$ be as in [def-sfb-finite-derived-pullback-iso] and let
$c=(X\xrightarrow{i}\bar X\xrightarrow{g}Y)$ be a compactification of $f$. Then
$Rf_!^c$ of [def-sfb-finite-derived-lower-shriek-compactification] is left adjoint to
$Rf^!_c$ of [def-sfb-finite-upper-shriek-compactification]:

$$
Rf_!^c=Rg_*\circ D(i_!)\;\dashv\;D(i^*)\circ Rg^!=Rf^!_c,
$$

the composite of the adjunction $D(i_!)\dashv D(i^*)$ of
[def-sfb-finite-derived-extension-by-zero-adjunction] and the adjunction $Rg_*\dashv Rg^!$
of [thm-sfb-finite-proper-pushforward-left-adjoint].
