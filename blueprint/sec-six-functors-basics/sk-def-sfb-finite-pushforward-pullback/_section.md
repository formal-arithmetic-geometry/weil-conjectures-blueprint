+++
id = "sk-def-sfb-finite-pushforward-pullback"
kind = "definition"
title = "Pushforward and pullback along base change (finite coefficients)"
order = 1453
uses = ["def-weil-pbc-proetale-site", "sk-def-sfb-sheaf-tensor"]
lean = ["AlgebraicGeometry.ProEtale.lowerStar", "AlgebraicGeometry.ProEtale.upperStar", "AlgebraicGeometry.ProEtale.upperStarLowerStarAdjunction", "AlgebraicGeometry.ProEtale.preservesFiniteLimits_upperStar", "AlgebraicGeometry.ProEtale.lowerStarId", "AlgebraicGeometry.ProEtale.lowerStarComp", "AlgebraicGeometry.ProEtale.upperStarComp", "AlgebraicGeometry.ProEtale.laxMonoidal_lowerStar", "AlgebraicGeometry.ProEtale.laxBraided_lowerStar", "AlgebraicGeometry.ProEtale.isIso_η_upperStar", "AlgebraicGeometry.ProEtale.isIso_δ_upperStar", "AlgebraicGeometry.ProEtale.monoidal_upperStar", "AlgebraicGeometry.ProEtale.laxBraided_upperStar", "AlgebraicGeometry.ProEtale.isMonoidal_upperStarLowerStarAdjunction"]
tags = ["sketch"]
+++
Let $\mathcal A$ be a Grothendieck abelian category and let $g\colon Z\to Y$ be an
*arbitrary* morphism of schemes. Base change $V\mapsto V\times_YZ$ is a continuous
functor $Y_{\mathrm{proét}}\to Z_{\mathrm{proét}}$ between the small pro-étale sites
[def-weil-pbc-proetale-site]. Define functors between the categories of
$\mathcal A$-valued sheaves

$$
g_*\colon\Sh(Z_{\mathrm{proét}},\mathcal A)\to\Sh(Y_{\mathrm{proét}},\mathcal A),
\qquad (g_*G)(V):=G(V\times_YZ),
$$

$$
g^*\colon\Sh(Y_{\mathrm{proét}},\mathcal A)\to\Sh(Z_{\mathrm{proét}},\mathcal A),
\qquad g^*:=\operatorname{sheafify}\circ\operatorname{Lan}_{(\text{base change})^{\mathrm{op}}},
$$

that is, $g^*$ is the left Kan extension of the underlying presheaf along the opposite
of base change, followed by sheafification. Then:

1. $g^*$ is left adjoint to $g_*$.
2. $g^*$ is exact.
3. There are identity isomorphisms $(\mathrm{id}_Y)_*\cong\mathrm{id}$, and for
   $h_1\colon T\to S$ and $h_2\colon S\to R$ there are composition isomorphisms
   $(h_2)_*\circ(h_1)_*\cong(h_2\circ h_1)_*$ and
   $(h_2\circ h_1)^*\cong h_1^*\circ h_2^*$, the second being the conjugate of the first
   under the adjunctions of 1.
4. If $\mathcal A$ is moreover closed symmetric monoidal and the sheaf categories carry
   the tensor product of [sk-def-sfb-sheaf-tensor], then $g_*$ is lax symmetric monoidal,
   $g^*$ is strong symmetric monoidal, and $g^*\dashv g_*$ is a monoidal adjunction.
