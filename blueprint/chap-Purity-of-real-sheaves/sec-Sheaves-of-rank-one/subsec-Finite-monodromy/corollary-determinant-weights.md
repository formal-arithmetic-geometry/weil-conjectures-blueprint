+++
id = "corollary-determinant-weights"
kind = "corollary"
title = "Determinant weights"
order = 1105
lean = ["AlgebraicGeometry.WeilGroup.IsLisse.hasDetWeight", "AlgebraicGeometry.WeilGroup.IsLisse.hasFiniteGeometricDet", "AlgebraicGeometry.WeilGroup.existsUnique_isPunctuallyPure_detLine", "AlgebraicGeometry.WeilGroup.isPunctuallyPure_det_baseChange_iff"]
uses = ["definition-weil-representation"]
+++
Let $\mathcal V$ be a nonzero lisse Weil sheaf of rank $r$ on a smooth
geometrically connected curve.  Its determinant has finite geometric
monodromy and is punctually pure of weight
$r\operatorname{dw}_\iota(\mathcal V)$. The number
$\operatorname{dw}_\iota(\mathcal V)$ does not depend on the choice of
$s$ or of a finite coefficient field over which $\mathcal V$ is defined.
