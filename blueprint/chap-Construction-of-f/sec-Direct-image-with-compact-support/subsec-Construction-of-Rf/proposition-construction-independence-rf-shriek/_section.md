+++
id = "proposition-construction-independence-rf-shriek"
kind = "proposition"
title = "Construction and independence of $Rf_!$"
order = 512
lean = ["AlgebraicGeometry.ProEtale.DerivedCategory.localizingConstructibleFiniteTor_lowerShriek", "AlgebraicGeometry.ProEtale.CondensedRing.lowerShriek_continuousMapRingObj", "AlgebraicGeometry.ProEtale.CondensedRing.lowerShriek_padicIntegersRingObj", "AlgebraicGeometry.ProEtale.CondensedRing.lowerShriek_padicAlgClRingObj", "AlgebraicGeometry.Etale.rightDerivedLowerShriekOfCompactificationPlusComparison", "AlgebraicGeometry.Etale.rightDerivedLowerShriekOfCompactificationPlusComparison_id", "AlgebraicGeometry.Etale.rightDerivedLowerShriekOfCompactificationPlusComparison_comp"]
uses = ["definition-ind-etale-pro-etale-weakly", "lemma-stability", "definition-small-pro-etale-site", "proposition-topos-functoriality", "example-locally-constant-functions-w-local", "proposition-comparison-morphism-inverse-image", "proposition-pro-etale-site-separably-closed", "lemma-inverse-image-coefficient-sheaves", "definition-constructible-sheaves", "lemma-constructible-sheaves", "definition-localizing-subcategory", "lemma-inverse-image-tensor-product", "definition-compactification-refinement"]
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
