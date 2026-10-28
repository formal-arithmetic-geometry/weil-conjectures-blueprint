+++
id = "def-weil-pbc-C6"
kind = "definition"
title = "Assertion (C6): invariance under algebraically closed extension, coefficient prime to the characteristic"
lean = ["AlgebraicGeometry.IsCurve.BaseChangeOfInvertibleOrder"]
order = 1558
uses = ["def-weil-pbc-curve-setting", "def-sc-field-extension", "def-weil-pbc-primary-torsion"]
+++
For every curve coefficient pair [def-weil-pbc-curve-setting] $(C,F)$ with $F$
prime to $\operatorname{char}k$ [def-weil-pbc-primary-torsion]: for every
algebraically closed extension $k'/k$ and every integer $q\geq0$, the pullback
map [def-sc-field-extension] $\rho^q_{k'/k}(C,F)$ is an isomorphism.
