+++
id = "def-sfb-finite-lower-shriek-compactification"
kind = "definition"
title = "Lower shriek along a compactification"
order = 1603
uses = ["def-sfb-finite-extension-by-zero", "def-sfb-finite-lower-star", "sk-def-nagata-sketch-data"]
lean = ["AlgebraicGeometry.ProEtale.Compactification.lowerShriek"]
+++
Let $\mathcal A$ be a Grothendieck abelian category and let
$c=(X\xrightarrow{i}\bar X\xrightarrow{g}Y)$ be a compactification of $f\colon X\to Y$
[sk-def-nagata-sketch-data]: $i$ is an open immersion, $g$ is proper and $f=g\circ i$.
The *lower shriek along $c$* is

$$
f_!^c:=g_*\circ i_!\colon\Sh(X_{\mathrm{proét}},\mathcal A)\to\Sh(Y_{\mathrm{proét}},\mathcal A),
$$

with $i_!$ the extension by zero of [def-sfb-finite-extension-by-zero] and $g_*$ the
pushforward of [def-sfb-finite-lower-star].
