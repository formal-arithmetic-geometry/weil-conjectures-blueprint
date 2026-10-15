+++
id = "sk-def-sfb-finite-pushforward-pullback"
kind = "proposition"
title = "The topos and its functoriality"
order = 704
uses = ["def-weil-pbc-proetale-site", "sk-def-sfb-sheaf-tensor", "sk-def-pe-site", "sk-lem-pe-weakly-etale-stability"]
lean = ["AlgebraicGeometry.ProEtale.lowerStar", "AlgebraicGeometry.ProEtale.upperStar", "AlgebraicGeometry.ProEtale.upperStarLowerStarAdjunction", "AlgebraicGeometry.ProEtale.preservesFiniteLimits_upperStar", "AlgebraicGeometry.ProEtale.lowerStarId", "AlgebraicGeometry.ProEtale.lowerStarComp", "AlgebraicGeometry.ProEtale.upperStarComp", "AlgebraicGeometry.ProEtale.laxMonoidal_lowerStar", "AlgebraicGeometry.ProEtale.laxBraided_lowerStar", "AlgebraicGeometry.ProEtale.isIso_η_upperStar", "AlgebraicGeometry.ProEtale.isIso_δ_upperStar", "AlgebraicGeometry.ProEtale.monoidal_upperStar", "AlgebraicGeometry.ProEtale.laxBraided_upperStar", "AlgebraicGeometry.ProEtale.isMonoidal_upperStarLowerStarAdjunction"]
tags = ["sketch"]
+++
The coverings of [sk-def-pe-site] define a subcanonical site. Its category of sheaves
$\Sh(X_{\mathrm{proét}})$ is a Grothendieck topos. Every scheme morphism $f\colon X\to Y$
induces a geometric morphism

$$
f_{\mathrm{proét}}\colon\Sh(X_{\mathrm{proét}})\longrightarrow\Sh(Y_{\mathrm{proét}}),
\qquad f^{-1}\dashv f_*.
$$

Here $f^{-1}\colon\Sh(Y_{\mathrm{proét}})\to\Sh(X_{\mathrm{proét}})$ preserves finite
limits and all colimits, and is exact on abelian sheaves. These morphisms are compatible
with composition.
