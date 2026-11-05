+++
id = "proposition-comparison-morphism-inverse-image"
kind = "proposition"
title = "The comparison morphism and its inverse image"
order = 112
lean = ["AlgebraicGeometry.Scheme.toProEt", "AlgebraicGeometry.ProEtale.comparisonLowerStar", "AlgebraicGeometry.ProEtale.isColimit_comparisonUpperStar_mapCocone"]
+++
Inclusion of étale objects defines a morphism of topoi

$$
\nu_X:X_{\mathrm{pro}\acute{e}t}\longrightarrow X_{\acute{e}t}.
$$

Its direct image $\nu_{X,*}:\Sh(X_{\mathrm{pro}\acute{e}t})\to\Sh(X_{\acute{e}t})$ is
restriction to the étale subsite. Its inverse image
$\nu_X^*:\Sh(X_{\acute{e}t})\to\Sh(X_{\mathrm{pro}\acute{e}t})$ is exact and has the
description

$$
(\nu_X^*F)(h:V\to X)
=\Gamma(V_{\acute{e}t},h_{\acute{e}t}^*F),
\tag{2.5}
$$

where $h_{\acute{e}t}^*:\Sh(X_{\acute{e}t})\to\Sh(V_{\acute{e}t})$ is the étale inverse
image along the weakly étale map $h$. Both functors carry
sheaves of $\Lambda$-modules to sheaves of $\Lambda$-modules, so they
restrict to functors between $\operatorname{Mod}(X_{\acute{e}t},\Lambda)$ and
$\operatorname{Mod}(X_{\mathrm{pro}\acute{e}t},\Lambda)$.
In particular, for $U=\varprojlim_iU_i$ as above, we have

$$
(\nu_X^*F)(U)=\varinjlim_i F(U_i).
\tag{2.6}
$$
