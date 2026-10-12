+++
id = "def-sfb-locally-finitely-presented"
kind = "definition"
title = "Locally finitely presented modules on the pro-étale site"
order = 1622
uses = ["def-sfb-finitely-presented-module", "def-weil-pbc-proetale-site", "sk-def-sfb-sheaf-tensor", "sk-def-sfb-ring-object", "sk-def-sfb-finite-pushforward-pullback", "sk-def-sfb-transport"]
lean = ["AlgebraicGeometry.ProEtale.IsLocallyFinitelyPresented"]
+++
Let $\mathcal A$ be a closed symmetric monoidal Grothendieck abelian category whose tensor
product is additive, let $X$ be a scheme, and let $\mathcal R$ be a ring object of
$\Sh(X_{\mathrm{proét}},\mathcal A)$. An $\mathcal R$-module $M$ is *locally finitely
presented* if there is a pro-étale cover $\{u_i\colon U_i\to X\}$
[def-weil-pbc-proetale-site] such that, for every $i$, the $u_i^*\mathcal R$-module
$\operatorname{mapMod}(u_i^*)(M)$ is finitely presented
[def-sfb-finitely-presented-module]. Here $u_i^*$ is the pullback of pro-étale sheaves
[sk-def-sfb-finite-pushforward-pullback], and $\operatorname{mapMod}$ transports modules
along the monoidal functor $u_i^*$ [sk-def-sfb-transport].
