+++
id = "lem-sfb-finite-upper-shriek-bounded-below"
kind = "lemma"
title = "$Rf^!$ preserves bounded below objects"
order = 1682
uses = ["def-sfb-finite-upper-shriek", "sk-def-sfb-derived-categories"]
lean = ["AlgebraicGeometry.ProEtale.plus_rightDerivedUpperShriek_obj"]
+++
Let $f\colon X\to Y$ admit a compactification, with chosen compactification
$X\xrightarrow{i}\bar X\xrightarrow{g}Y$, and suppose that $Rg_*$ has finite cohomological
amplitude: there is $d\ge0$ with $Rg_*(D^{\le0})\subseteq D^{\le d}$. If
$K\in D(Y_{\mathrm{proét}},\mathcal A)$ is bounded below, then so is $Rf^!K$
([def-sfb-finite-upper-shriek]). More precisely, $K\in D^{\ge n}$ implies
$Rf^!K\in D^{\ge n-d}$.
