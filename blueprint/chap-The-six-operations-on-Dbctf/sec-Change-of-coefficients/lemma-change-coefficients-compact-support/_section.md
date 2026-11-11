+++
id = "lemma-change-coefficients-compact-support"
kind = "lemma"
title = "Change of coefficients for compactly supported direct image"
order = 638
lean = ["AlgebraicGeometry.ProEtale.isIso_rightDerivedLowerShriekOfCompactificationExtendScalarsMap_app", "AlgebraicGeometry.ProEtale.CondensedRing.BoundedConstructibleCoefficientChange.squareCompatible_lowerShriekOfCompactificationIso"]
uses = ["definition-ind-etale-pro-etale-weakly", "lemma-stability", "definition-small-pro-etale-site", "proposition-topos-functoriality", "example-locally-constant-functions-w-local", "proposition-comparison-morphism-inverse-image", "proposition-pro-etale-site-separably-closed", "lemma-inverse-image-coefficient-sheaves", "definition-constructible-sheaves", "lemma-constructible-sheaves", "lemma-descent-finite-coefficient-field", "lemma-integral-models", "lemma-inverse-image-tensor-product", "proposition-six-operations-dctf", "definition-change-of-coefficients-maps", "proposition-sp-unique-adjoint", "definition-sp-scalar-extension", "definition-compactification-refinement", "lemma-schematic-closure-uniqueness", "proposition-compactifying-union-two-opens", "lemma-affine-covers-dense-intersection"]
+++
For each map $\Lambda\to\Lambda'$ listed above, every separated morphism
$f:X\to Y$ of finite type and every $K\in D^b_{\mathrm{ctf}}(X,\Lambda)$, the map
$(Rf_!K)_{\Lambda'}\to Rf_!(K_{\Lambda'})$ of
Definition [definition-change-of-coefficients-maps](5) is an isomorphism,
and it does not depend on the compactification.
