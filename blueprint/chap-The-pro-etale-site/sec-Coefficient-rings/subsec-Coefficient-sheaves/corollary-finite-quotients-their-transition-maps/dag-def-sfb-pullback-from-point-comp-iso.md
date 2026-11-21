+++
id = "dag-def-sfb-pullback-from-point-comp-iso"
kind = "dag-definition"
title = "The comparison $f^*\\circ p_Y^*\\cong p_X^*$"
name_showing = false
order = 181501
tags = ["sheaf-dag"]
split_from = "corollary-finite-quotients-their-transition-maps--3"
dag_id = "def-sfb-pullback-from-point-comp-iso"
dag_kind = "definition"
dag_status = "split"
serial = false
dag_lean = ["AlgebraicGeometry.ProEtale.upperStarFromPointComp"]
uses = ["dag-def-sfb-finite-upper-star"]
+++
Let $f\colon X\to Y$ be a morphism of schemes, and let $f^*$ be the pullback of abelian pro-étale sheaves of [dag-def-sfb-finite-upper-star]. Write $\pi_X\colon X\to\Spec\Z$ and $\pi_Y\colon Y\to\Spec\Z$ for the structure morphisms, and let $p_X^*=\pi_X^*\circ p^*$ and $p_Y^*=\pi_Y^*\circ p^*$ be as in `def-sfb-upper-star-from-point`. The natural isomorphism
$$
f^*\circ p_Y^*\ \cong\ p_X^*
$$
of functors $\Sh(*_{\mathrm{proét}},\Ab)\to\Sh(X_{\mathrm{proét}},\Ab)$ is defined as the composite
$$
f^*\circ\pi_Y^*\circ p^*\ \cong\ (\pi_Y\circ f)^*\circ p^*=\pi_X^*\circ p^*.
$$
The first step is the inverse of the composition isomorphism $(\pi_Y\circ f)^*\cong f^*\circ\pi_Y^*$ of `def-sfb-finite-upper-star-comp`, precomposed with $p^*$. The equality uses $\pi_Y\circ f=\pi_X$, since $\Spec\Z$ is terminal, as recorded in `sk-def-sfb-pullback-from-point`.

(SHEAF DAG node `def-sfb-pullback-from-point-comp-iso`; machine-alignment layer.) Split from [corollary-finite-quotients-their-transition-maps--3]. DAG kind: definition. DAG status: split. Statement dependencies not drawn: `def-sfb-upper-star-from-point`.
