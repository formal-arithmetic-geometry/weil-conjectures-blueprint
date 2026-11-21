+++
id = "dag-lem-weil-pbc-w-local-closed-points-components-homeomorphism"
kind = "dag-lemma"
title = "Closed points and connected components of a w-local space"
name_showing = false
order = 45501
tags = ["sheaf-dag"]
split_from = "proposition-w-local-components--1"
dag_id = "lem-weil-pbc-w-local-closed-points-components-homeomorphism"
dag_kind = "statement"
dag_status = "split"
serial = false
dag_lean = ["WLocalSpace.isHomeomorph_connectedComponents_closedPoints", "WLocalSpace.closedPointsHomeomorph", "WLocalSpace.closedPoints_eq_of_mk_eq"]
uses = ["dag-def-weil-pbc-w-local", "dag-sk-def-pe-wlocal"]
+++
Let $X$ be a spectral space `def-weil-spectral-space`. Let $X^c$ be its subspace of closed points `def-weil-closed-points`. Assume that $X^c$ is closed and that whenever a point specializes to two closed points, those closed points are equal. Let $\pi_0(X)$ be the set of connected components, with its quotient topology. Then the canonical map $X^c\to\pi_0(X)$, sending a point to its connected component, is a homeomorphism.

(SHEAF DAG node `lem-weil-pbc-w-local-closed-points-components-homeomorphism`; machine-alignment layer.) Split from [proposition-w-local-components--1]. DAG kind: statement. DAG status: split. Statement dependencies not drawn: `def-weil-closed-points`, `def-weil-spectral-space`.
