+++
id = "def-sfb-finite-derived-lower-shriek-plus"
kind = "definition"
title = "Derived lower shriek on $D^+$"
order = 1671
uses = ["def-sfb-finite-extension-by-zero", "def-sfb-finite-lower-star", "lem-sfb-finite-extension-by-zero-exact", "sk-def-nagata-sketch-data", "sk-def-sfb-derived-categories"]
lean = ["AlgebraicGeometry.ProEtale.rightDerivedLowerShriekPlus"]
+++
Let $f\colon X\to Y$ admit a compactification [sk-def-nagata-sketch-data], with chosen
compactification $X\xrightarrow{i}\bar X\xrightarrow{g}Y$. On the bounded below derived
categories, the *derived lower shriek* is

$$
Rf_!^+:=R^+(g_*)\circ D^+(i_!)\colon D^+(X_{\mathrm{proét}},\mathcal A)\to D^+(Y_{\mathrm{proét}},\mathcal A),
$$

with $D^+(i_!)$ induced levelwise by the exact $i_!$
([def-sfb-finite-extension-by-zero], [lem-sfb-finite-extension-by-zero-exact]) and
$R^+(g_*)$ the bounded below right derived functor [sk-def-sfb-derived-categories] of the
pushforward of [def-sfb-finite-lower-star].
