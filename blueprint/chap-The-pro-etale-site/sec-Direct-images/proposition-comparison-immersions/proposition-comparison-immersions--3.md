+++
id = "proposition-comparison-immersions--3"
kind = "proposition"
title = "Comparison of inverse images"
name_showing = false
order = 139003
aliases = ["bp-r040-3"]
lean = ["AlgebraicGeometry.ProEtale.mapDerivedCategoryComparisonUpperStarCompUpperStarIso"]
uses = ["definition-small-pro-etale-site", "proposition-comparison-morphism-inverse-image", "proposition-topos-functoriality"]
+++
The comparison of localization triangles is bypassed by the Lean proof;
the inverse-image comparison it uses holds for every morphism of schemes.

Let $A$ be a Grothendieck abelian category and $g:Y\to X$ a morphism
of schemes. There is a canonical isomorphism

$$
g_{\mathrm{pro}\acute{e}t}^*\nu_X^*\simeq\nu_Y^*g_{\acute{e}t}^*
\quad\text{of functors }D(X_{\acute{e}t},A)\to D(Y_{\mathrm{pro}\acute{e}t},A).
$$

The derived categories here are unbounded. For a closed immersion
$i:Z\hookrightarrow X$, this gives the inverse-image comparison in (2).
The direct-image comparison in (2) is the specialization of
[theorem-comparison-direct-images] to $i$.
