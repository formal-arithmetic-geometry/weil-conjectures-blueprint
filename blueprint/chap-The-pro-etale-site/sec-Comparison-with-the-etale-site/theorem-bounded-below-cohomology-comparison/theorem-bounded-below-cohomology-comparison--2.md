+++
id = "theorem-bounded-below-cohomology-comparison--2"
kind = "theorem"
title = "Bounded-below cohomology comparison (2)"
name_showing = false
order = 123002
aliases = ["bp-r035-2"]
lean = ["AlgebraicGeometry.ProEtale.bijective_comparisonUpperStar_mapDerivedCategory_map"]
uses = ["definition-small-pro-etale-site", "proposition-comparison-morphism-inverse-image"]
+++
Let $X$ be a scheme and $\mathcal A$ a Grothendieck abelian category
with a closed symmetric monoidal structure whose tensor product is additive
in each variable, and with functorial flat resolutions. For
$K,M\in D(X_{\acute{e}t},\mathcal A)$ with $M$ bounded below, the map

$$
\operatorname{Hom}(K,M)\longrightarrow
\operatorname{Hom}(\nu_X^*K,\nu_X^*M),\qquad f\longmapsto\nu_X^*f,
$$

is bijective. No boundedness assumption on $K$ is needed. Consequently
$\nu_X^*:D^+(X_{\acute{e}t},\mathcal A)\to
D^+(X_{\mathrm{pro}\acute{e}t},\mathcal A)$ is fully faithful, in particular
for $\mathcal A=\operatorname{Mod}(\Lambda)$ and a discrete commutative
ring $\Lambda$.
