+++
id = "dag-det-def-sfb-coefficient-morphisms"
kind = "dag-definition"
title = "The canonical coefficient morphisms $\\alpha_f$, $\\eta_f$"
name_showing = false
order = 187504
tags = ["sheaf-dag"]
split_from = "lemma-inverse-image-coefficient-sheaves--1"
dag_id = "det-def-sfb-coefficient-morphisms"
dag_kind = "definition"
dag_status = "split"
serial = false
dag_lean = ["AlgebraicGeometry.ProEtale.condensedPullbackHom", "AlgebraicGeometry.ProEtale.isMonHom_condensedPullbackHom", "AlgebraicGeometry.ProEtale.coefficientPullbackIso", "AlgebraicGeometry.ProEtale.condensedPushforwardHom", "AlgebraicGeometry.ProEtale.isMonHom_condensedPushforwardHom"]
uses = ["dag-det-def-sfb-pullback-from-point-comp"]
+++
Let $\Lambda$ be a condensed ring, let $f\colon X\to Y$ be a morphism of
schemes, and let $\Lambda_X$, $\Lambda_Y$ be the pulled-back coefficient rings
of `det-def-sfb-pulled-back-coefficients`. The pullback
$f^*\Lambda_Y$ and the pushforward $f_*\Lambda_X$ are ring objects: $f^*$ is
strong monoidal (`def-sfb-finite-upper-star-monoidal`) and $f_*$ is lax monoidal
(`def-sfb-finite-lower-star-lax-monoidal`). Define
$$
\alpha_f\colon f^*\Lambda_Y\longrightarrow\Lambda_X,\qquad
\eta_f\colon\Lambda_Y\longrightarrow f_*\Lambda_X
$$
as follows.

- $\alpha_f$ is the component at $\Lambda$ of the natural isomorphism
  $f^*\circ p_Y^*\cong p_X^*$ of [dag-det-def-sfb-pullback-from-point-comp].
- $\eta_f$ is the mate of $\alpha_f$ under the adjunction $f^*\dashv f_*$
  (`def-sfb-finite-upper-lower-star-adjunction`): the
  unit $\Lambda_Y\to f_*f^*\Lambda_Y$ followed by $f_*\alpha_f$.

Both are morphisms of ring objects. Moreover, $\alpha_f$ underlies an
isomorphism of ring objects $f^*\Lambda_Y\cong\Lambda_X$.

(SHEAF DAG node `det-def-sfb-coefficient-morphisms`; machine-alignment layer.) Split from [lemma-inverse-image-coefficient-sheaves--1]. DAG kind: definition. DAG status: split. Statement dependencies not drawn: `det-def-sfb-pulled-back-coefficients`, `def-sfb-finite-upper-star-monoidal`, `def-sfb-finite-lower-star-lax-monoidal`, `def-sfb-finite-upper-lower-star-adjunction`.
