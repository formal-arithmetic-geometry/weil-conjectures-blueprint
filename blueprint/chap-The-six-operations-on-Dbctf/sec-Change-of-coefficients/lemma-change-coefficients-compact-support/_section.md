+++
id = "lemma-change-coefficients-compact-support"
kind = "lemma"
title = "Change of coefficients for compactly supported direct image"
order = 637
lean = ["AlgebraicGeometry.ProEtale.CondensedRing.boundedConstructibleLowerShriekExtendScalarsIso", "AlgebraicGeometry.ProEtale.CondensedRing.boundedConstructibleLowerShriekToPadicAlgClIso", "AlgebraicGeometry.ProEtale.CondensedRing.etaleReductionLowerShriekIsoOfCompactification", "AlgebraicGeometry.ProEtale.CondensedRing.BoundedConstructibleCoefficientChange.squareCompatible_lowerShriekOfCompactificationIso"]
uses = ["definition-constructible-sheaves", "definition-sp-scalar-extension", "lemma-extension-scalars-preserves-dctf", "definition-change-of-coefficients-maps", "definition-compactification-refinement", "proposition-construction-independence-rf-shriek", "proposition-comparison-etale-derived-category"]
+++
For each map $\Lambda\to\Lambda'$ listed above, every separated morphism
$f:X\to Y$ of finite type and every $K\in D^b_{\mathrm{ctf}}(X,\Lambda)$, the map
$(Rf_!K)_{\Lambda'}\to Rf_!(K_{\Lambda'})$ of
Definition [definition-change-of-coefficients-maps](5) is an isomorphism,
and it does not depend on the compactification.
