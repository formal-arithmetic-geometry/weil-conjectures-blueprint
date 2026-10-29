+++
id = "sk-prop-sf-comp-coherence"
kind = "proposition"
title = "Construction and independence of $Rf_!$"
order = 2499
uses = ["sk-def-localizing-closure", "sk-def-nagata-sketch-data"]
lean = ["AlgebraicGeometry.Etale.rightDerivedLowerShriekOfCompactificationPlusComparison", "AlgebraicGeometry.Etale.rightDerivedLowerShriekOfCompactificationPlusComparison_id", "AlgebraicGeometry.Etale.rightDerivedLowerShriekOfCompactificationPlusComparison_comp"]
tags = ["sketch"]
+++
Let $\Lambda$ be admissible and let $f:X\to Y$ be separated of finite type,
with compactification $f=p\circ j$ ([sk-def-nagata-sketch-data],
[sk-rem-compactifications]: $j:X\to\overline X$ a quasi-compact open
immersion, $p:\overline X\to Y$ proper). The functor

$$
Rf_!=Rp_*\circ j_!:\Loc(\Dctf(X,\Lambda))\to\Loc(\Dctf(Y,\Lambda))
$$

([sk-def-localizing-closure]) is exact, preserves direct sums, and maps
$\Dctf(X,\Lambda)$ into $\Dctf(Y,\Lambda)$. Two compactifications give
canonically isomorphic functors, and these isomorphisms satisfy the cocycle
condition.

Here *canonical* has the following meaning. If $j:X\to Z$ is an open
immersion, then $j_!$ is left adjoint to $j^*$ on the pro-étale derived
categories. Hence a map out of $j_!K$ is determined by its restriction to $X$.
All comparison maps between compactifications restrict to the identity on $X$,
and this property determines them uniquely.
