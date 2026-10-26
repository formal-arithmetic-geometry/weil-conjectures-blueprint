+++
id = "sk-prop-sf-comparison"
kind = "theorem"
title = "Bounded-below cohomology comparison"
order = 973
uses = []
lean = ["AlgebraicGeometry.ProEtale.derivedComparisonAdjunction", "AlgebraicGeometry.ProEtale.isIso_derivedComparisonAdjunction_unit_app", "AlgebraicGeometry.ProEtale.bijective_comparisonUpperStar_mapDerivedCategory_map", "AlgebraicGeometry.ProEtale.comparisonLowerStarCompRightDerivedGlobalSectionsIso"]
tags = ["sketch"]
+++
Let $X$ be a scheme, $\Lambda$ a ring, and $\nu_X:X_{\mathrm{proét}}\to X_{\mathrm{ét}}$
the comparison morphism. For $K\in D^+(X_{\mathrm{ét}},\Lambda)$ the unit of the
adjunction between
$\nu_X^*:D^+(X_{\mathrm{ét}},\Lambda)\to D^+(X_{\mathrm{proét}},\Lambda)$ and
$R\nu_{X,*}$ is an isomorphism

$$
K\xrightarrow{\ \sim\ }R\nu_{X,*}\nu_X^*K\quad\text{in }D^+(X_{\mathrm{ét}},\Lambda).
$$

Consequently $\nu_X^*:D^+(X_{\mathrm{ét}},\Lambda)\to D^+(X_{\mathrm{proét}},\Lambda)$ is
fully faithful, and there is a canonical isomorphism in the derived category
of $\Lambda$-modules

$$
R\Gamma(X_{\mathrm{proét}},\nu_X^*K)\simeq R\Gamma(X_{\mathrm{ét}},K).
$$
