+++
id = "sk-lem-nagata-density-normalization"
kind = "lemma"
title = "Passing to the schematic closure"
order = 814
lean = ["AlgebraicGeometry.ProEtale.CondensedRing.isIso_boundedConstructibleOpenImmersionLowerShriekRefinement", "AlgebraicGeometry.ProEtale.CondensedRing.isIso_boundedConstructibleOpenImmersionLowerShriekRefinementPushforward", "AlgebraicGeometry.ProEtale.CondensedRing.isIso_boundedConstructibleOpenImmersionLowerShriekRefinementPushforward_padicAlgCl", "AlgebraicGeometry.ProEtale.CondensedRing.boundedConstructibleLowerShriekRefinementIso"]
uses = ["sk-def-nagata-sketch-data", "sk-lem-nagata-sketch-closure", "sk-prop-sf-open-closed-triangle"]
tags = ["sketch"]
+++
Let $X\xrightarrow{j}\overline X\xrightarrow{p}S$ be any
compactification with $\overline X$ Noetherian, and let
$i:Z\hookrightarrow\overline X$ be the
schematic closure of $X$, with $j_Z:X\hookrightarrow Z$ the induced
open immersion. For a condensed coefficient ring $\Lambda$, we use the
pullbacks of its coefficient sheaf to these schemes as coefficients. For every
$K\in D(X_{\mathrm{pro}\acute{e}t},\Lambda_X)$ there are canonical identifications

$$
j_!K\simeq i_*j_{Z,!}K,\qquad
Rp_*j_!K\simeq R(p\circ i)_*j_{Z,!}K.
$$
