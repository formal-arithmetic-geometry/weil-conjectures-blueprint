+++
id = "def-sfb-finite-derived-global-sections"
kind = "definition"
title = "Derived global sections $R\\Gamma(X,-)$"
order = 2518
uses = ["def-weil-pbc-proetale-site", "det-def-sfb-derived-categories"]
lean = ["AlgebraicGeometry.ProEtale.rightDerivedGlobalSections"]
+++
For a scheme $X$ and a Grothendieck abelian category $\mathcal A$, the *derived global
sections* functor

$$
R\Gamma(X,-):=R\Gamma(X_{\mathrm{proét}},-)\colon D(X_{\mathrm{proét}},\mathcal A)\to D(\mathcal A)
$$

is the right derived functor [det-def-sfb-derived-categories] of the global sections functor
$F\mapsto F(X)$, evaluation at the terminal object $X$ of $X_{\mathrm{proét}}$
[def-weil-pbc-proetale-site].
