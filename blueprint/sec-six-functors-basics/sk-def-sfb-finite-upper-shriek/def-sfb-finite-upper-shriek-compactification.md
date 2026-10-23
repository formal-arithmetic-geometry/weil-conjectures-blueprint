+++
id = "def-sfb-finite-upper-shriek-compactification"
kind = "definition"
title = "Exceptional pullback along a compactification"
order = 2527
uses = ["def-sfb-finite-upper-star", "lem-sfb-finite-upper-star-exact", "sk-def-nagata-sketch-data", "thm-sfb-finite-proper-pushforward-left-adjoint"]
lean = ["AlgebraicGeometry.ProEtale.rightDerivedUpperShriekOfCompactification"]
+++
Let $\mathcal A$ be a Grothendieck abelian category and
$c=(X\xrightarrow{i}\bar X\xrightarrow{g}Y)$ a compactification of $f$
[sk-def-nagata-sketch-data]. The *exceptional pullback along $c$* is

$$
Rf^!_c:=D(i^*)\circ Rg^!\colon D(Y_{\mathrm{proét}},\mathcal A)\to D(X_{\mathrm{proét}},\mathcal A),
$$

where $Rg^!$ is a chosen right adjoint of $Rg_*$
([thm-sfb-finite-proper-pushforward-left-adjoint], $g$ being proper) and $D(i^*)$ applies
the exact pullback $i^*$ ([def-sfb-finite-upper-star], [lem-sfb-finite-upper-star-exact])
levelwise.
