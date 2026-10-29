+++
id = "sk-thm-sf-pf-proetale"
kind = "theorem"
title = "Projection formula: the pro-étale realization"
lean = ["AlgebraicGeometry.ProEtale.hasProjectionFormula_of_constructibleFiniteTor"]
order = 3456
uses = ["sk-thm-sf-pf-adic", "sk-prop-sf-comparison", "sk-thm-sf-pf-field", "sk-prop-scalar-six"]
tags = ["sketch"]
+++
Let $A$ be a finite admissible coefficient ring and let $K,L$ be the
pro-étale realizations $\nu^*K_{\mathrm{\acute et}}$, $\nu^*L_{\mathrm{\acute et}}$ of
bounded constructible finite-Tor complexes on the small étale sites
([sk-prop-sf-comparison]). Then $\operatorname{PF}_{f,K,L}$ is an
isomorphism in $D^+(Y_{\Proet},A)$.

For $\Lambda=\mathcal O_E,E,\Qlb$ there is no étale realization to transport:
the projection formula holds directly on the condensed categories of
$X_{\mathrm{pro\acute et}}$ by [sk-thm-sf-pf-adic] and [sk-thm-sf-pf-field].
