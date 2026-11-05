+++
id = "proposition-integral-tate-module--4"
kind = "proposition"
title = "The integral Tate module (4)"
name_showing = false
order = 1509004
aliases = ["bp-r471-4"]
lean = ["AlgebraicGeometry.IsAbelianVariety.geometricPointsAddEquiv", "AlgebraicGeometry.bijective_toUnit_comp_torsionSubgroupScheme"]
uses = ["definition-abelian-variety"]
+++
The full equivariance assertion for the Tate-module projections is
bypassed by the Lean route, which uses the following statements on
points.

Let $A$ be a group scheme over a field $k$. For every
$\sigma\in\operatorname{Gal}(\bar k/k)$, precomposition with
$\operatorname{Spec}\sigma$ gives a group automorphism

$$
A(\bar k)\longrightarrow A(\bar k),\qquad
P\longmapsto P\circ\operatorname{Spec}\sigma.
$$

If $A$ is an abelian variety over an algebraically closed field $k$
of characteristic $p$, $m>0$ and $p\nmid m$, then for every
algebraically closed extension $k'/k$ the canonical map

$$
A[m](k)\longrightarrow A[m](k')
$$

is a bijection.
