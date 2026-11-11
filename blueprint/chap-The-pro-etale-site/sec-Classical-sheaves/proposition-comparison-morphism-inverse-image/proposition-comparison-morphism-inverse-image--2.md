+++
id = "proposition-comparison-morphism-inverse-image--2"
kind = "proposition"
title = "The comparison morphism and its inverse image (2)"
name_showing = false
order = 112003
aliases = ["bp-r031-2"]
lean = ["AlgebraicGeometry.ProEtale.comparisonAdjunction", "AlgebraicGeometry.ProEtale.comparisonUpperStar", "AlgebraicGeometry.ProEtale.preservesFiniteColimits_comparisonUpperStar", "AlgebraicGeometry.ProEtale.preservesFiniteLimits_comparisonUpperStar"]
uses = ["definition-small-pro-etale-site--1", "proposition-comparison-morphism-inverse-image--1"]
+++
Its inverse image
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
