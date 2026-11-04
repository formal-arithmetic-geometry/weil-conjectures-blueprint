+++
id = "lemma-change-coefficients-compact-support"
kind = "lemma"
title = "Change of coefficients for compactly supported direct image"
order = 631
lean = ["AlgebraicGeometry.ProEtale.isIso_rightDerivedLowerShriekOfCompactificationExtendScalarsMap_app", "AlgebraicGeometry.ProEtale.CondensedRing.boundedConstructibleLowerShriekExtendScalarsIso"]
uses = ["definition-ind-etale-pro-etale-weakly", "lemma-stability", "definition-small-pro-etale-site", "proposition-topos-functoriality", "proposition-comparison-morphism-inverse-image", "definition-constructible-sheaves", "definition-lisse-sheaves", "lemma-proper-direct-image-unbounded-complexes", "lemma-extension-scalars-preserves-dctf", "definition-sp-scalar-extension"]
+++
For each map $\Lambda\to\Lambda'$ listed above, every separated morphism
$f:X\to Y$ of finite type and every $K\in D^b_{\mathrm{ctf}}(X,\Lambda)$, the map
$(Rf_!K)_{\Lambda'}\to Rf_!(K_{\Lambda'})$ of
Definition [definition-change-of-coefficients-maps](5) is an isomorphism,
and it does not depend on the compactification.
