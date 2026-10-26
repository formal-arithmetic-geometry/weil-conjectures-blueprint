+++
id = "sk-prop-pe-comparison-morphism"
kind = "proposition"
title = "The comparison morphism and its inverse image"
order = 956
lean = ["AlgebraicGeometry.Scheme.toProEt", "AlgebraicGeometry.ProEtale.comparisonLowerStar", "AlgebraicGeometry.ProEtale.comparisonUpperStar", "AlgebraicGeometry.ProEtale.comparisonAdjunction", "AlgebraicGeometry.ProEtale.preservesFiniteLimits_comparisonUpperStar", "AlgebraicGeometry.ProEtale.preservesFiniteColimits_comparisonUpperStar", "AlgebraicGeometry.ProEtale.isColimit_comparisonUpperStar_mapCocone"]
uses = ["sk-def-pe-site", "sk-prop-pe-affine-basis", "sk-def-pe-classical-definition"]
tags = ["sketch"]
+++
Inclusion of étale objects defines a morphism of topoi

$$
\nu_X\colon X_{\Proet}\longrightarrow X_{\Et}.
$$

Its direct image $\nu_{X,*}\colon\Sh(X_{\Proet})\to\Sh(X_{\Et})$ is restriction
to the étale subsite. Its inverse image
$\nu_X^*\colon\Sh(X_{\Et})\to\Sh(X_{\Proet})$ is exact and has the description

$$
(\nu_X^*F)(h\colon V\to X)=\Gamma(V_{\Et},h_{\Et}^*F),
$$

where $h_{\Et}^*\colon\Sh(X_{\Et})\to\Sh(V_{\Et})$ is the étale inverse image
along the weakly étale map $h$. Both functors carry $\Lambda$-module sheaves to
$\Lambda$-module sheaves, so they restrict to functors between
$\Mod(X_{\Et},\Lambda)$ and $\Mod(X_{\Proet},\Lambda)$. For a pro-étale affine
presentation $U=\varprojlim_iU_i$ with $U_i$ affine and étale over $X$, this
gives

$$
(\nu_X^*F)(U)=\varinjlim_iF(U_i).
$$
