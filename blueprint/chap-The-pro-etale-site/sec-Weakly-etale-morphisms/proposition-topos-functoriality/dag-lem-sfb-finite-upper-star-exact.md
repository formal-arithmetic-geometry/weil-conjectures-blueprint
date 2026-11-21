+++
id = "dag-lem-sfb-finite-upper-star-exact"
kind = "dag-lemma"
title = "$g^*$ is exact"
name_showing = false
order = 39505
tags = ["sheaf-dag"]
split_from = "proposition-topos-functoriality--2"
dag_id = "lem-sfb-finite-upper-star-exact"
dag_kind = "statement"
dag_status = "split"
serial = false
dag_lean = ["AlgebraicGeometry.ProEtale.preservesFiniteLimits_upperStar", "AlgebraicGeometry.ProEtale.additive_upperStar", "AlgebraicGeometry.ProEtale.upperStarLowerStarAdjunction", "AlgebraicGeometry.ProEtale.preservesHomology_upperStar"]
uses = ["dag-def-sfb-finite-lower-star", "dag-def-sfb-finite-upper-star"]
+++
For every morphism $g\colon Z\to Y$ the pullback $g^*$ of [dag-def-sfb-finite-upper-star]
preserves finite limits. Being also a left adjoint
(`def-sfb-finite-upper-lower-star-adjunction`), it is exact.

(SHEAF DAG node `lem-sfb-finite-upper-star-exact`; machine-alignment layer.) Split from [proposition-topos-functoriality--2]. DAG kind: statement. DAG status: split.
