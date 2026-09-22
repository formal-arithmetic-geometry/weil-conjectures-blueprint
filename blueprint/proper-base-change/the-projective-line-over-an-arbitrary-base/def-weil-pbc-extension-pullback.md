+++
id = "def-weil-pbc-extension-pullback"
kind = "definition"
title = "Base change of the coefficient and the pullback map"
order = 1139
lean = ["AlgebraicGeometry.Etale.CurveCoefficientPair.baseChange", "AlgebraicGeometry.Etale.CurveCoefficientPair.cohomologyPullback"]
uses = ["def-weil-pbc-curve-setting"]
+++
For a curve coefficient pair [def-weil-pbc-curve-setting] $(C,F)$ and an
algebraically closed extension $k'/k$, write

$$
 \pi_{k'}:C_{k'}=C\times_k k'\longrightarrow C,
 \qquad F_{k'}=\pi_{k'}^{-1}F,
$$

and let

$$
 \rho^q_{k'/k}(C,F):H^q(C_{\Et},F)\longrightarrow
 H^q((C_{k'})_{\Et},F_{k'})
$$

be the *pullback map* in degree $q$.

Unresolved dependencies: def:weil-pbc-etale-cohomology
