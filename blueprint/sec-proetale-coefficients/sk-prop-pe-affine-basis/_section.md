+++
id = "sk-prop-pe-affine-basis"
kind = "proposition"
title = "Pro-étale affines form a basis"
order = 921
lean = ["AlgebraicGeometry.Scheme.AffineProEt", "AlgebraicGeometry.Scheme.AffineProEt.isCoverDense_toProEt", "AlgebraicGeometry.Scheme.AffineProEt.isEquivalence_sheafPushforwardContinuous_toProEt"]
uses = ["sk-def-pe-site", "sk-def-pe-morphisms", "sk-thm-pe-indetale-refinement"]
tags = ["sketch"]
+++
Every object of $X_{\mathrm{proét}}$ [sk-def-pe-site] has a pro-étale covering by pro-étale
affines over $X$ [sk-def-pe-morphisms]. These form a full subsite whose category of sheaves
is equivalent to $\Sh(X_{\mathrm{proét}})$.
