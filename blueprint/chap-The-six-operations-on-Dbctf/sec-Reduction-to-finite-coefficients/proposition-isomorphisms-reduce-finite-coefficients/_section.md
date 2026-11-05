+++
id = "proposition-isomorphisms-reduce-finite-coefficients"
kind = "proposition"
title = "Isomorphisms reduce to finite coefficients"
order = 653
lean = []
uses = ["definition-small-pro-etale-site", "definition-constructible-sheaves", "proposition-six-operations-change-coefficients"]
+++
For each admissible $\Lambda$ let
$F_\Lambda,G_\Lambda:D^b_{\mathrm{ctf}}(X,\Lambda)\to D^b_{\mathrm{ctf}}(Y,\Lambda)$ be exact
functors and $\theta_\Lambda:F_\Lambda\to G_\Lambda$ a natural
transformation of exact functors. Assume that for each coefficient map
$\Lambda\to\Lambda'$ of Proposition [proposition-six-operations-change-coefficients] there are
isomorphisms $F_\Lambda(K)\otimes\Lambda'\simeq F_{\Lambda'}(K\otimes\Lambda')$
and $G_\Lambda(K)\otimes\Lambda'\simeq G_{\Lambda'}(K\otimes\Lambda')$ carrying
$\theta_\Lambda(K)\otimes\Lambda'$ to $\theta_{\Lambda'}(K\otimes\Lambda')$. This
holds, by Proposition [proposition-six-operations-change-coefficients], whenever $F$, $G$ and $\theta$ are
built from the six operations, their units and counits and base change
maps, covariantly in $K$. If
$\theta_A(K)$ is an isomorphism for every finite ring $A$ and every
$K\in D^b_{\mathrm{ctf}}(X,A)$, then $\theta_\Lambda(K)$ is an isomorphism for every
admissible $\Lambda$ and every $K\in D^b_{\mathrm{ctf}}(X,\Lambda)$.
