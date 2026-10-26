+++
id = "def-sfb-finite-shriek-adjunction-compactification"
kind = "definition"
title = "The étale adjunction $Rf_!^c\\dashv Rf^!_c$"
lean = ["AlgebraicGeometry.Etale.rightDerivedUpperShriekOfCompactificationAdjunction"]
order = 2509
uses = ["def-weil-pbc-projection-compactification", "def-weil-pbc-extension-by-zero", "def-sfb-finite-upper-shriek-compactification", "thm-sfb-finite-proper-pushforward-left-adjoint"]
+++
Let $\Lambda$ be a finite ring and $c=(X\xrightarrow{i}\bar X\xrightarrow{g}Y)$ a
compactification of $f$. On the étale sites, the derived lower shriek
$Rf_!^c=Rg_*\circ D(i_!)$ of [def-weil-pbc-projection-compactification] is left adjoint to
$Rf^!_c$ of [def-sfb-finite-upper-shriek-compactification]:

$$
Rf_!^c\;\dashv\;Rf^!_c,
$$

the composite of the adjunction $D(i_!)\dashv D(i^*)$ for the exact extension by zero of
[def-weil-pbc-extension-by-zero] and the adjunction $Rg_*\dashv Rg^!$ of
[thm-sfb-finite-proper-pushforward-left-adjoint].
