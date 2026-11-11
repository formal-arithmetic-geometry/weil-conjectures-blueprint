+++
id = "lemma-positivity-euler-factors"
kind = "lemma"
title = "Positivity of Euler factors"
order = 1158
lean = ["AlgebraicGeometry.WeilSheaf.IsReal.inv_localPolynomial_stalk_tensorPow_nonneg"]
uses = ["definition-ind-etale-pro-etale-weakly", "lemma-stability", "definition-small-pro-etale-site", "proposition-pro-etale-coverings", "proposition-topos-functoriality", "example-locally-constant-functions-w-local", "proposition-sp-unique-adjoint", "lemma-perfect-complexes-geometric-point", "definition-real-sheaves"]
+++
Let $\mathcal G$ be an $\iota$-real Weil sheaf, let $m\ge1$, and let
$x$ be a closed point. Then the power series
$\iota\det(1-\operatorname{Frob}_xt^{\deg(x)}\mid\mathcal G^{\otimes2m}_{\bar x})^{-1}$
has nonnegative real coefficients and constant coefficient one.
