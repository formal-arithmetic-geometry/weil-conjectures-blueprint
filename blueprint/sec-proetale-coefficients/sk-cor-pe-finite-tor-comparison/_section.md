+++
id = "sk-cor-pe-finite-tor-comparison"
kind = "corollary"
title = "Finite Tor amplitude under comparison"
order = 1266
lean = ["AlgebraicGeometry.ProEtale.DerivedCategory.torAmplitudeIn_mapDerivedCategory_iff", "AlgebraicGeometry.ProEtale.DerivedCategory.constructibleFiniteTor_mapDerivedCategory", "DerivedCategory.torAmplitudeIn_mapDerivedCategory_obj_iff", "AlgebraicGeometry.ProEtale.preservesFlat_comparisonUpperStar"]
uses = ["sk-thm-pe-constructible-comparison"]
tags = ["sketch"]
+++
For a qcqs scheme $X$ and a discrete Noetherian ring $\Lambda$, the equivalence
$\nu_X^*\colon D^b_c(X_{\Et},\Lambda)\to\Dbc(X,\Lambda)$ of
[sk-thm-pe-constructible-comparison] restricts to

$$
\Dctf(X,\Lambda)\simeq D^b_{\mathrm{ctf}}(X_{\Et},\Lambda).
$$

In particular the corollary applies to every finite commutative $\ell$-primary
ring $A$, regular or not.
