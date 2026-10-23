+++
id = "def-sfb-finite-compactly-supported"
kind = "definition"
title = "Compactly supported cohomology complex $R\\Gamma_c$"
order = 2524
uses = ["def-sfb-finite-derived-global-sections", "def-sfb-finite-derived-lower-shriek"]
lean = ["AlgebraicGeometry.ProEtale.compactlySupportedGlobalSections"]
+++
For $f\colon X\to Y$ admitting a compactification, the *compactly supported cohomology
complex* is the composite

$$
R\Gamma_c(X/Y,-):=R\Gamma(Y,-)\circ Rf_!\colon D(X_{\mathrm{proét}},\mathcal A)\to D(\mathcal A)
$$

of the derived lower shriek of [def-sfb-finite-derived-lower-shriek] and the derived global
sections of [def-sfb-finite-derived-global-sections].
