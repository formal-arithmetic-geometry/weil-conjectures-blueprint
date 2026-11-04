+++
id = "lemma-finite-quasi-finite-direct-images"
kind = "lemma"
title = "Finite and quasi-finite direct images"
order = 1315
lean = ["AlgebraicGeometry.isZero_higherLowerShriek_of_quasiFinite", "AlgebraicGeometry.WeilSheaf.isZero_higherLowerShriek_and_isMixedOfWeightsAtMost_of_quasiFinite", "AlgebraicGeometry.HasDirectImageWeightBound.of_locallyQuasiFinite", "AlgebraicGeometry.WeilSheaf.IsMixedOfWeightsAtMost.higherLowerShriek_zero_of_quasiFinite", "AlgebraicGeometry.WeilSheaf.HasWeightsAtMost.higherLowerShriek_zero_of_quasiFinite", "AlgebraicGeometry.WeilSheaf.IsPunctuallyPureOfWeight.higherLowerShriek_zero_of_quasiFinite"]
uses = ["definition-ind-etale-pro-etale-weakly", "definition-small-pro-etale-site", "proposition-topos-functoriality", "definition-weights", "definition-compactification-refinement", "lemma-schematic-closure-uniqueness", "proposition-compactifying-union-two-opens", "lemma-affine-covers-dense-intersection"]
+++
Let $g:Z_0\to Y_0$ be separated and quasi-finite. Then $Rg_!$ is
exact on sheaves and carries mixed sheaves of weights at most $w$ to
mixed sheaves of weights at most $w$. It also carries
$D_{\leq w}(Z_0)$ into $D_{\leq w}(Y_0)$.
For a finite map, direct image carries a pure sheaf of weight $w$
to a pure sheaf of weight $w$.
