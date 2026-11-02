+++
id = "det-pe-classical-sheaves-modules"
kind = "lemma"
title = "The module form of the classical equivalence"
lean = ["AlgebraicGeometry.ProEtale.proEtaleClassicalSheavesModules"]
order = 1009
uses = ["det-pe-classical-sheaves-unit", "prop-weil-pbc-site-comparison-finite-level"]
+++
Let $\Lambda$ be a discrete commutative ring, $\Lambda_{X,\Et}$ its constant
sheaf on $X_{\Et}$, and identify $\Lambda_X=\nu_X^*\Lambda_{X,\Et}$. Then
$\nu_X^*$ and $\nu_{X,*}$ restrict to an adjoint pair between
$\Mod(X_{\Et},\Lambda)$ and $\Mod(X_{\Proet},\Lambda_X)$; the functor
$\nu_X^*\colon\Mod(X_{\Et},\Lambda)\to\Mod(X_{\Proet},\Lambda_X)$ is exact and
fully faithful, and it is an equivalence onto the full subcategory of
classical $\Lambda_X$-module sheaves, with quasi-inverse $\nu_{X,*}$.
