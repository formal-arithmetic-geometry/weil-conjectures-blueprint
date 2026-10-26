+++
id = "def-sfb-finite-lower-shriek"
kind = "definition"
title = "Lower shriek $f_!$"
order = 2490
uses = ["def-sfb-finite-lower-shriek-compactification", "sk-def-nagata-sketch-data"]
lean = ["AlgebraicGeometry.ProEtale.lowerShriek"]
+++
Let $f\colon X\to Y$ be a morphism that admits a compactification
[sk-def-nagata-sketch-data], and fix a choice $c(f)=(X\xrightarrow{i}\bar X\xrightarrow{g}Y)$
of one. The *lower shriek* of $f$ is

$$
f_!:=f_!^{c(f)}=g_*\circ i_!
$$

in the sense of [def-sfb-finite-lower-shriek-compactification].
