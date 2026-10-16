+++
id = "thm-zl-relative-line-stratification"
kind = "theorem"
title = "Stratification of a sheaf on a relative line"
lean = ["AlgebraicGeometry.WeilSheaf.exists_dense_isLisse_upperStar", "AlgebraicGeometry.WeilSheaf.HasRelativeLineStratification", "AlgebraicGeometry.WeilSheaf.IsPunctuallyPureOfWeight.hasRelativeLineStratification"]
order = 3191
uses = ["def-sbc-affine-space", "def-weil-pbc-constructible-complexes", "def-weil-pbc-scheme-conventions", "i-topology", "lem-zl-affine-partition", "pqf-def-quasifinite"]
+++
Let $Y_0$ be a separated finite-type $k_0$-scheme and let $\mathcal F$
be a constructible Weil sheaf on $\mathbf A^1_{Y_0}$ (in the
constructible conventions of [def-weil-pbc-constructible-complexes]).
There are finite stratifications of source and target such that
$\mathcal F$ is lisse on every source stratum and each induced map is
either separated quasi-finite or smooth with one-dimensional affine
geometric fibers.
