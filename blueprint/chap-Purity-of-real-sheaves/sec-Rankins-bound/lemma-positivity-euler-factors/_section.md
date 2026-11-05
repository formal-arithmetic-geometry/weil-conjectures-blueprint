+++
id = "lemma-positivity-euler-factors"
kind = "lemma"
title = "Positivity of Euler factors"
order = 1155
lean = ["AlgebraicGeometry.WeilSheaf.IsReal.inv_localPolynomial_stalk_tensorPow_nonneg", "AlgebraicGeometry.WeilGroup.IsReal.hasNonnegCoeffs_eulerFactor_tensorPower"]
uses = ["definition-ind-etale-pro-etale-weakly", "definition-small-pro-etale-site", "proposition-topos-functoriality", "definition-real-sheaves"]
+++
Let $\mathcal G$ be an $\iota$-real Weil sheaf, let $m\ge1$, and let
$x$ be a closed point. Then the power series
$\iota\det(1-\operatorname{Frob}_xt^{\deg(x)}\mid\mathcal G^{\otimes2m}_{\bar x})^{-1}$
has nonnegative real coefficients and constant coefficient one.
