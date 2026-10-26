+++
id = "def-sfb-finite-lower-star"
kind = "definition"
title = "Pushforward $g_*$ along base change"
order = 876
uses = ["def-weil-pbc-proetale-site"]
lean = ["AlgebraicGeometry.ProEtale.lowerStar", "AlgebraicGeometry.Scheme.ProEt.isContinuous_overPullback"]
+++
Let $\mathcal A$ be a Grothendieck abelian category and $g\colon Z\to Y$ an arbitrary
morphism of schemes. Base change $V\mapsto V\times_YZ$ is a functor
$Y_{\mathrm{proét}}\to Z_{\mathrm{proét}}$ of small pro-étale sites
[def-weil-pbc-proetale-site], and it is continuous. The *pushforward*

$$
g_*\colon\Sh(Z_{\mathrm{proét}},\mathcal A)\to\Sh(Y_{\mathrm{proét}},\mathcal A),
\qquad (g_*G)(V):=G(V\times_YZ),
$$

is restriction of sheaves along base change.
