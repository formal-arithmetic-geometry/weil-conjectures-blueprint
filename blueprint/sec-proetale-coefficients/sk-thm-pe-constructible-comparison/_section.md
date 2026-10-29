+++
id = "sk-thm-pe-constructible-comparison"
kind = "theorem"
title = "Constructible comparison"
order = 1262
lean = ["AlgebraicGeometry.ProEtale.IsConstructible", "AlgebraicGeometry.ProEtale.isConstructible_comparisonUpperStar_obj", "AlgebraicGeometry.ProEtale.isConstructible_iff_exists_isConstructibleSheaf_iso_comparisonUpperStar_obj", "AlgebraicGeometry.ProEtale.full_comparisonUpperStar", "AlgebraicGeometry.ProEtale.faithful_comparisonUpperStar", "AlgebraicGeometry.ProEtale.DerivedCategory.boundedConstructible", "AlgebraicGeometry.ProEtale.bijective_comparisonUpperStar_mapDerivedCategory_map", "AlgebraicGeometry.ProEtale.openImmersionLowerShriekComparisonUpperStarIso"]
uses = ["sk-prop-pe-finite-local-systems", "sk-cor-pe-classical-derived", "sk-thm-pe-direct-image-comparison", "sk-prop-sf-open-closed-triangle", "sk-def-sfb-constructible"]
tags = ["sketch"]
+++
For a discrete Noetherian ring $\Lambda$, a $\Lambda_X$-module on $X_{\Proet}$ is
constructible in the sense of [sk-def-sfb-constructible] exactly when a finite
partition of $X$ into constructible locally closed strata makes it locally
constant with finitely generated stalks on each stratum.

Let $X$ be quasi-compact and quasi-separated. For a discrete Noetherian ring
$\Lambda$, every constructible pro-étale $\Lambda_X$-module sheaf is classical.
The functor $\nu_X^*$ gives an equivalence from constructible étale sheaves of
$\Lambda$-modules to $\operatorname{Cons}(X,\Lambda)$, and an equivalence
$D^b_c(X_{\Et},\Lambda)\to\Dbc(X,\Lambda)$ of bounded constructible derived
categories.
