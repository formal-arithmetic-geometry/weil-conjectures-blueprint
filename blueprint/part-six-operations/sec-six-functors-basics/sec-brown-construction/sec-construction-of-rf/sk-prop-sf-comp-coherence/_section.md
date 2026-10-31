+++
id = "sk-prop-sf-comp-coherence"
kind = "proposition"
title = "Construction and independence of $Rf_!$"
order = 300
lean = ["AlgebraicGeometry.Etale.rightDerivedLowerShriekOfCompactificationPlusComparison", "AlgebraicGeometry.Etale.rightDerivedLowerShriekOfCompactificationPlusComparison_id", "AlgebraicGeometry.Etale.rightDerivedLowerShriekOfCompactificationPlusComparison_comp"]
uses = ["sk-def-localizing-closure", "sk-def-nagata-sketch-data"]
tags = ["sketch"]
+++
Let $\Lambda$ be admissible and let $f:X\to Y$ be separated of finite
type, with compactification
$f=p\circ j$ as above. The functor

$$
Rf_!=Rp_*\circ j_!:\Loc(D^b_{\mathrm{ctf}}(X,\Lambda))\to\Loc(D^b_{\mathrm{ctf}}(Y,\Lambda))
$$

is exact, preserves direct sums, and maps $D^b_{\mathrm{ctf}}(X,\Lambda)$ into
$D^b_{\mathrm{ctf}}(Y,\Lambda)$. Two compactifications give canonically isomorphic
functors, and these isomorphisms satisfy the cocycle condition.
