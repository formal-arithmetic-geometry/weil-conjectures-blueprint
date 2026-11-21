+++
id = "dag-def-sfb-finite-upper-star"
kind = "dag-definition"
title = "Pullback $g^*$ along base change"
name_showing = false
order = 39502
tags = ["sheaf-dag"]
split_from = "proposition-topos-functoriality--2"
dag_id = "def-sfb-finite-upper-star"
dag_kind = "definition"
dag_status = "imported"
serial = false
dag_lean = ["AlgebraicGeometry.ProEtale.upperStar"]
uses = ["dag-def-weil-pbc-proetale-site"]
+++
Let $\mathcal A$ and $g\colon Z\to Y$ be as in [dag-def-sfb-finite-lower-star], with
$b\colon Y_{\mathrm{proét}}\to Z_{\mathrm{proét}}$ the base change functor. The *pullback*

$$
g^*\colon\Sh(Y_{\mathrm{proét}},\mathcal A)\to\Sh(Z_{\mathrm{proét}},\mathcal A),
\qquad g^*F:=\operatorname{sheafify}\bigl(\operatorname{Lan}_{b^{\mathrm{op}}}F\bigr),
$$

is the left Kan extension of the underlying presheaf of $F$ along
$b^{\mathrm{op}}$, followed by sheafification on $Z_{\mathrm{proét}}$.

(SHEAF DAG node `def-sfb-finite-upper-star`; machine-alignment layer.) Split from [proposition-topos-functoriality--2]. DAG kind: definition. DAG status: imported.
