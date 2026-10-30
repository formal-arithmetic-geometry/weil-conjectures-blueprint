+++
id = "sk-prop-sf-comparison"
kind = "theorem"
title = "Bounded-below cohomology comparison"
order = 85
lean = ["AlgebraicGeometry.ProEtale.derivedComparisonAdjunction", "AlgebraicGeometry.ProEtale.isIso_derivedComparisonAdjunction_unit_app", "AlgebraicGeometry.ProEtale.bijective_comparisonUpperStar_mapDerivedCategory_map", "AlgebraicGeometry.ProEtale.comparisonLowerStarCompRightDerivedGlobalSectionsIso"]
tags = ["sketch"]
+++
For $K\in D^+(X_{\acute{e}t},\Lambda)$ the unit of the adjunction between
$\nu_X^*:D^+(X_{\acute{e}t},\Lambda)\to D^+(X_{\mathrm{pro}\acute{e}t},\Lambda)$ and
$R\nu_{X,*}$ is an isomorphism

$$
K\xrightarrow{\ \sim\ }R\nu_{X,*}\nu_X^*K.
\tag{2.7}
$$

Consequently $\nu_X^*:D^+(X_{\acute{e}t},\Lambda)\to D^+(X_{\mathrm{pro}\acute{e}t},\Lambda)$ is fully faithful,
and there is a canonical isomorphism

$$
R\Gamma(X_{\mathrm{pro}\acute{e}t},\nu_X^*K)
\simeq R\Gamma(X_{\acute{e}t},K).
$$
