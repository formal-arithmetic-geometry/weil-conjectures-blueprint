+++
id = "def-sfb-finite-derived-lower-shriek-compactification"
kind = "definition"
title = "Derived lower shriek along a compactification"
order = 2519
uses = ["def-weil-extension-by-zero", "def-sfb-finite-lower-star", "lem-sfb-finite-extension-by-zero-exact", "sk-def-nagata-sketch-data", "det-def-sfb-derived-categories"]
lean = ["AlgebraicGeometry.ProEtale.rightDerivedLowerShriekOfCompactification"]
+++
Let $\mathcal A$ be a Grothendieck abelian category and let
$c=(X\xrightarrow{i}\bar X\xrightarrow{g}Y)$ be a compactification of $f$
[sk-def-nagata-sketch-data]. The *derived lower shriek along $c$* is

$$
Rf_!^c:=R(g_*)\circ D(i_!)\colon D(X_{\mathrm{proét}},\mathcal A)\to D(Y_{\mathrm{proét}},\mathcal A),
$$

where $D(i_!)$ applies the exact extension by zero $i_!$
([def-weil-extension-by-zero], [lem-sfb-finite-extension-by-zero-exact]) levelwise,
and $R(g_*)$ is the right derived functor [det-def-sfb-derived-categories] of the pushforward
$g_*$ of [def-sfb-finite-lower-star].
