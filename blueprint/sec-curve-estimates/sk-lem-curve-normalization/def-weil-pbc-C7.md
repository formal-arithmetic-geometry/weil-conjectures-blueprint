+++
id = "def-weil-pbc-C7"
kind = "definition"
title = "Assertion (C7): invariance under algebraically closed extension for a proper curve"
lean = ["AlgebraicGeometry.IsCurve.BaseChangeOfIsProper"]
order = 1451
uses = ["def-weil-pbc-curve-setting", "def-sc-field-extension"]
+++
For every curve coefficient pair [def-weil-pbc-curve-setting] $(C,F)$ with $C$
proper over $k$: for every algebraically closed extension $k'/k$ and every
integer $q\geq0$, the pullback map [def-sc-field-extension]
$\rho^q_{k'/k}(C,F)$ is an isomorphism, without a restriction on the torsion
of $F$.
