+++
id = "sk-prop-pbc-degree-zero"
kind = "proposition"
title = "Proper base change in degree zero"
order = 184
lean = ["AlgebraicGeometry.Etale.isIso_baseChangeMap_of_isProper", "AlgebraicGeometry.Etale.bijective_stalkToFibreSections_of_isProper"]
uses = ["sk-def-exchange", "sk-thm-pbc-henselian-h0"]
tags = ["sketch"]
+++
For (4.1) with $f$ proper, and for every étale sheaf of
sets $F$ on $X$, the map

$$
g^*f_*F\xrightarrow{\sim} f'_*g'^*F
$$

is an isomorphism. Moreover, for a
geometric point $\bar y:\operatorname{Spec}\Omega\to Y$, restriction identifies

$$
(f_*F)_{\bar y}\xrightarrow{\sim}
\Gamma(X_{\bar y},F|_{X_{\bar y}}).
\tag{4.5}
$$
