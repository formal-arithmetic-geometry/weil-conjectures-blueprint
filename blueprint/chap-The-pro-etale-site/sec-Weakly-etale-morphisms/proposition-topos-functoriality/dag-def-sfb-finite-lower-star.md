+++
id = "dag-def-sfb-finite-lower-star"
kind = "dag-definition"
title = "Pushforward $g_*$ along base change"
name_showing = false
order = 39501
tags = ["sheaf-dag"]
split_from = "proposition-topos-functoriality--2"
dag_id = "def-sfb-finite-lower-star"
dag_kind = "definition"
dag_status = "imported"
serial = false
dag_lean = ["AlgebraicGeometry.ProEtale.lowerStar", "AlgebraicGeometry.Scheme.ProEt.isContinuous_overPullback", "AlgebraicGeometry.ProEtale.lowerStar_obj_val_obj"]
uses = ["dag-def-weil-pbc-proetale-site"]
+++
Let $\mathcal A$ be a Grothendieck abelian category and $g\colon Z\to Y$ an arbitrary
morphism of schemes. Base change $V\mapsto V\times_YZ$ is a functor
$Y_{\mathrm{proét}}\to Z_{\mathrm{proét}}$ of small pro-étale sites
[dag-def-weil-pbc-proetale-site], and it is continuous. The *pushforward*

$$
g_*\colon\Sh(Z_{\mathrm{proét}},\mathcal A)\to\Sh(Y_{\mathrm{proét}},\mathcal A),
\qquad (g_*G)(V):=G(V\times_YZ),
$$

is restriction of sheaves along base change.

(SHEAF DAG node `def-sfb-finite-lower-star`; machine-alignment layer.) Split from [proposition-topos-functoriality--2]. DAG kind: definition. DAG status: imported.
