+++
id = "lem-sc-degree-2g1-very-ample"
kind = "lemma"
title = "Line bundles of large degree are very ample"
lean = ["AlgebraicGeometry.Scheme.isVeryAmple_of_finrankH_zero_tensorObj_toModules_ker", "AlgebraicGeometry.Scheme.isVeryAmple_of_degree"]
order = 742
uses = ["def-sc-ample", "def-sc-curves", "def-sc-genus", "def-sc-pic0", "lem-sc-dim0-finite", "lem-sc-riemann-roch-large-degree", "thm-pqf-finite-iff-proper-finite-fibres"]
+++
Let $C$ be a proper smooth connected curve of
genus $g$ ([def-sc-genus]) over an algebraically closed
field $k$, and $\mathcal M$ a line bundle on $C$ with
$\deg\mathcal M\geq2g+1$ ([def-sc-pic0]). Then
$\mathcal M$ is very ample.
