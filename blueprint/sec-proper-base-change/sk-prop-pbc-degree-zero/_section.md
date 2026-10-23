+++
id = "sk-prop-pbc-degree-zero"
kind = "proposition"
title = "Proper base change in degree zero"
order = 1553
lean = ["AlgebraicGeometry.Etale.isIso_baseChangeMap_of_isProper", "AlgebraicGeometry.Etale.bijective_stalkToFibreSections_of_isProper"]
uses = ["sk-def-exchange", "sk-thm-pbc-henselian-h0"]
tags = ["sketch"]
+++
In degree zero, proper base change holds for every étale sheaf of abelian
groups or of $\Lambda$-modules, with no torsion hypothesis.

For a cartesian square as in [sk-def-exchange] with $f$ proper, and for every
étale sheaf $F$ of abelian groups or of $\Lambda$-modules on $X$, the map

$$
\Ex^0_{\square,F}:g^{-1}f_*F\xrightarrow{\ \sim\ }f'_*g'^{-1}F
$$

is an isomorphism of sheaves on $Y'_{\Et}$. Moreover, for a geometric
point $\bar y:\operatorname{Spec}\Omega\to Y$, restriction identifies

$$
(f_*F)_{\bar y}\xrightarrow{\ \sim\ }\Gamma(X_{\bar y},F|_{X_{\bar y}}).
$$
