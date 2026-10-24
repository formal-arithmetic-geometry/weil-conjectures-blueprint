+++
id = "sk-def-sfb-finite-pushforward-pullback"
kind = "proposition"
title = "The topos and its functoriality"
order = 910
uses = ["def-weil-pbc-proetale-site", "sk-def-pe-site", "sk-lem-pe-weakly-etale-stability"]
lean = ["AlgebraicGeometry.Scheme.ProEt.topology", "CategoryTheory.GrothendieckTopology.subcanonical_of_full_of_faithful", "AlgebraicGeometry.Scheme.ProEt.isContinuous_overPullback", "AlgebraicGeometry.ProEtale.lowerStar", "AlgebraicGeometry.ProEtale.upperStar", "AlgebraicGeometry.ProEtale.upperStarLowerStarAdjunction", "AlgebraicGeometry.ProEtale.preservesFiniteLimits_upperStar", "AlgebraicGeometry.ProEtale.preservesFiniteLimits_op_lan_overPullback_of_isGrothendieckAbelian", "AlgebraicGeometry.ProEtale.lowerStarId", "AlgebraicGeometry.ProEtale.upperStarId", "AlgebraicGeometry.ProEtale.lowerStarComp", "AlgebraicGeometry.ProEtale.upperStarComp", "AlgebraicGeometry.ProEtale.laxMonoidal_lowerStar", "AlgebraicGeometry.ProEtale.laxBraided_lowerStar", "AlgebraicGeometry.ProEtale.isIso_η_upperStar", "AlgebraicGeometry.ProEtale.isIso_δ_upperStar", "AlgebraicGeometry.ProEtale.monoidal_upperStar", "AlgebraicGeometry.ProEtale.laxBraided_upperStar", "AlgebraicGeometry.ProEtale.isMonoidal_upperStarLowerStarAdjunction"]
tags = ["sketch"]
+++
The coverings of [sk-def-pe-site] define a subcanonical site. Let $\mathcal A$ be a
Grothendieck abelian category whose morphism groups lie in the universe one above that of the
schemes. Every scheme morphism $f\colon X\to Y$ induces an adjunction

$$
f^*\colon\Sh(Y_{\mathrm{proét}},\mathcal A)\rightleftarrows\Sh(X_{\mathrm{proét}},\mathcal A)\colon f_*,
\qquad f^*\dashv f_*,
$$

where $f_*$ is restriction along base change, $(f_*G)(V)=G(V\times_YX)$, and $f^*$ is left Kan
extension followed by sheafification. Here $f^*$ preserves finite limits and all colimits, so
it is exact. These functors are compatible with identities and composition. If $\mathcal A$ is
moreover closed symmetric monoidal, with the tensor product of [lem-weil-pbc-sheaf-tensor-closed], then
$f_*$ is lax symmetric monoidal, $f^*$ is strong symmetric monoidal, and $f^*\dashv f_*$ is a
monoidal adjunction.
