+++
id = "sk-prop-sf-comp-coherence"
kind = "proposition"
title = "Construction and independence of $Rf_!$"
order = 1813
uses = ["sk-def-sf-operations", "sk-prop-nagata-sketch-comp-category", "sk-thm-properbasechange", "sk-def-localizing-closure"]
lean = ["AlgebraicGeometry.Etale.rightDerivedLowerShriekOfCompactificationPlusComparison", "AlgebraicGeometry.Etale.rightDerivedLowerShriekOfCompactificationPlusComparison_id", "AlgebraicGeometry.Etale.rightDerivedLowerShriekOfCompactificationPlusComparison_comp"]
tags = ["sketch"]
+++
Let $\Lambda$ be admissible and let $f:X\to Y$ be separated of finite type,
with compactification $f=p\circ j$ ($j:X\to\overline X$ a quasi-compact open
immersion, $p:\overline X\to Y$ proper). The functor

$$
Rf_!=Rp_*\circ j_!:\Loc(\Dctf(X,\Lambda))\to\Loc(\Dctf(Y,\Lambda))
$$

is exact, preserves direct sums, and maps $\Dctf(X,\Lambda)$ into
$\Dctf(Y,\Lambda)$. Two compactifications give canonically isomorphic
functors, and these isomorphisms satisfy the cocycle condition.
