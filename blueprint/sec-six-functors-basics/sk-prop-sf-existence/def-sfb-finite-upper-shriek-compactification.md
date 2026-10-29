+++
id = "def-sfb-finite-upper-shriek-compactification"
kind = "definition"
title = "Étale exceptional pullback along a compactification"
lean = ["AlgebraicGeometry.Etale.rightDerivedUpperShriekOfCompactification"]
order = 2550
uses = ["def-weil-pbc-inverse-image", "sk-def-nagata-sketch-data", "thm-sfb-finite-proper-pushforward-left-adjoint"]
+++
Let $\Lambda$ be a finite ring and $c=(X\xrightarrow{i}\bar X\xrightarrow{g}Y)$ a
compactification of $f$ [sk-def-nagata-sketch-data]. The *étale exceptional pullback along $c$* is

$$
Rf^!_c:=D(i^*)\circ Rg^!\colon D(Y_{\et},\Lambda)\to D(X_{\et},\Lambda),
$$

where $Rg^!$ is a chosen right adjoint of the étale $Rg_*$
([thm-sfb-finite-proper-pushforward-left-adjoint], $g$ being proper) and $D(i^*)$ applies the
exact étale pullback $i^*$ ([def-weil-pbc-inverse-image]) levelwise.
