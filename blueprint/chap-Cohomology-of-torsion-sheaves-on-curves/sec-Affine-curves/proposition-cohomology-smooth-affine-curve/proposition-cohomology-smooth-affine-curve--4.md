+++
id = "proposition-cohomology-smooth-affine-curve--4"
kind = "proposition"
title = "Invariance under algebraically closed extension"
name_showing = false
order = 1579004
aliases = ["bp-r493-4"]
lean = ["AlgebraicGeometry.IsConnectedCurve.bijective_fieldExtensionCohomologyMap_of_isAffine"]
uses = ["definition-small-pro-etale-site", "proposition-comparison-morphism-inverse-image", "definition-underived-base-change-map"]
+++
Let $k'/k$ be an extension of algebraically closed fields, let $U/k$ be
a smooth affine connected curve, and let $n\geq1$ be invertible in $k$.
For every $q\geq0$, pullback induces an isomorphism

$$
H^q(U,\mathbf Z/n)\longrightarrow H^q(U_{k'},\mathbf Z/n).
$$

Choosing a primitive $n$th root of unity in $k$ and its image in $k'$
identifies these maps with the pullback maps for $\mu_n$.
