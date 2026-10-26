+++
id = "thm-a1-affine-curve-upper"
kind = "theorem"
title = "Affine compact-support upper bound"
lean = ["AlgebraicGeometry.hasWeightsAtMostOver_compactlySupportedCohomology_of_isAffine_of_isLisse"]
order = 4043
uses = ["def-weil-open-closed-recollement", "def-weil-ordinary-compact-cohomology", "def-weil-punctual-weights", "lem-a1-affine-hc0", "lem-a1-affine-hc2-pure", "lem-a1-curve-hc2-bound", "lem-a1-extension-bounds", "lem-a1-finite-boundary-cohomology", "lem-a1-finite-boundary-weights", "lem-a1-finite-map-curve", "lem-a1-reduction-composition", "lem-a1-reduction-lisse-pure", "lem-a1-subquotient-extension-bounds", "lem-a1-unramified-at-infinity", "lem-a1-weight-bound-constant-extension", "lem-wf-boundary-semicontinuity", "lem-zl-affine-curve-range", "prop-a1-curve-boundary-sequence", "prop-sf-open-closed-triangle-all-stages", "thm-a1-line-middle-extension-upper"]
+++
Let $C_0$ be a smooth geometrically connected affine curve and let
$\mathcal F$ be a lisse Weil sheaf that is punctually $\iota$-pure of
weight $w$. Then every
compactly supported cohomology group
$H_c^i(C,\mathcal F)$ has weights at most $w+i$. More precisely,
$H_c^0(C,\mathcal F)=0$, $H_c^2(C,\mathcal F)$ is $\iota$-pure of
weight $w+2$, and $H_c^i(C,\mathcal F)=0$ for $i\notin\{0,1,2\}$.
