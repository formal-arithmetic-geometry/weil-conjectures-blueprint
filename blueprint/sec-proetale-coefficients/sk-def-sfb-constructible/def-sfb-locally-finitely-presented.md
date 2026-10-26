+++
id = "def-sfb-locally-finitely-presented"
kind = "definition"
title = "Locally finitely presented modules on the pro-étale site"
order = 1207
uses = ["def-sfb-finitely-presented-module", "def-weil-pbc-proetale-site", "lem-weil-pbc-sheaf-tensor-closed", "det-def-sfb-ring-object", "def-sfb-finite-upper-star", "def-sfb-finite-upper-star-monoidal", "det-def-sfb-transport"]
lean = ["AlgebraicGeometry.ProEtale.IsLocallyFinitelyPresented"]
+++
Let $\mathcal A$ be a closed symmetric monoidal Grothendieck abelian category whose tensor
product is additive, let $X$ be a scheme, and let $\mathcal R$ be a ring object of
$\Sh(X_{\mathrm{proét}},\mathcal A)$. An $\mathcal R$-module $M$ is *locally finitely
presented* if there is a pro-étale cover $\{u_i\colon U_i\to X\}$
[def-weil-pbc-proetale-site] such that, for every $i$, the $u_i^*\mathcal R$-module
$\operatorname{mapMod}(u_i^*)(M)$ is finitely presented
[def-sfb-finitely-presented-module]. Here $u_i^*$ is the pullback of pro-étale sheaves
[def-sfb-finite-upper-star], and $\operatorname{mapMod}$ transports modules
along the monoidal functor $u_i^*$ ([def-sfb-finite-upper-star-monoidal],
[det-def-sfb-transport]).
