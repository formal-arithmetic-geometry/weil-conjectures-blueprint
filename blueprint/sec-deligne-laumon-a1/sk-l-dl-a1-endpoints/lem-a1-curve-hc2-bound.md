+++
id = "lem-a1-curve-hc2-bound"
kind = "lemma"
title = "Top compact-support bound on a curve"
order = 3979
uses = ["def-weil-ordinary-compact-cohomology", "def-weil-punctual-weights", "lem-a1-affine-hc2", "lem-a1-subquotient-extension-bounds", "lem-tw-tate-twist-weight-shift"]
lean = ["AlgebraicGeometry.WeilSheaf.hasWeightsAtMostOver_compactlySupportedCohomology_two"]
+++
If $C_0$ is a smooth affine curve over $k_0$ (affine and smooth of
relative dimension one, not necessarily connected) and $\mathcal F$ is a
lisse Weil sheaf on $C_0$,
punctually $\iota$-pure of weight $w$, then
$H_c^2(C,\mathcal F)$ has weights at most $w+2$.
