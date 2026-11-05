+++
id = "lemma-positivity-euler-factors"
kind = "lemma"
title = "Positivity of Euler factors"
order = 1158
lean = ["AlgebraicGeometry.WeilSheaf.IsReal.inv_localPolynomial_stalk_tensorPow_nonneg", "AlgebraicGeometry.WeilGroup.IsReal.hasNonnegCoeffs_eulerFactor_tensorPower"]
uses = ["lemma-stability", "proposition-six-operations-change-coefficients"]
+++
Let $\mathcal G$ be an $\iota$-real Weil sheaf, let $m\ge1$, and let
$x$ be a closed point. Then the power series
$\iota\det(1-\operatorname{Frob}_xt^{\deg(x)}\mid\mathcal G^{\otimes2m}_{\bar x})^{-1}$
has nonnegative real coefficients and constant coefficient one.
