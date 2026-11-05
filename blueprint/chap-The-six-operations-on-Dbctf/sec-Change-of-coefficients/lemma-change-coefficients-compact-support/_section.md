+++
id = "lemma-change-coefficients-compact-support"
kind = "lemma"
title = "Change of coefficients for compactly supported direct image"
order = 638
lean = ["AlgebraicGeometry.ProEtale.isIso_rightDerivedLowerShriekOfCompactificationExtendScalarsMap_app", "AlgebraicGeometry.ProEtale.CondensedRing.BoundedConstructibleCoefficientChange.squareCompatible_lowerShriekOfCompactificationIso"]
uses = ["lemma-stability", "proposition-comparison-morphism-inverse-image", "definition-constructible-sheaves", "definition-lisse-sheaves", "definition-sp-scalar-extension", "lemma-schematic-closure-uniqueness"]
+++
For each map $\Lambda\to\Lambda'$ listed above, every separated morphism
$f:X\to Y$ of finite type and every $K\in D^b_{\mathrm{ctf}}(X,\Lambda)$, the map
$(Rf_!K)_{\Lambda'}\to Rf_!(K_{\Lambda'})$ of
Definition [definition-change-of-coefficients-maps](5) is an isomorphism,
and it does not depend on the compactification.
