+++
id = "dag-lem-pur-signed-line-unit-presentation-graphs"
kind = "dag-lemma"
title = "Signed line unit presentation graphs"
name_showing = false
order = 187539
tags = ["sheaf-dag"]
split_from = "lemma-inverse-image-coefficient-sheaves--2"
dag_id = "lem-pur-signed-line-unit-presentation-graphs"
dag_kind = "statement"
dag_status = "split"
serial = false
dag_lean = ["CategoryTheory.SignedLinePullbackConstruction.SheafPullbackUnitPresentation.binary_graph", "CategoryTheory.SignedLinePullbackConstruction.SheafPullbackUnitPresentation.constant_graph"]
uses = ["dag-def-pur-signed-line-pullback-unit-presentation"]
+++
Let p,q,r be unit presentations [dag-def-pur-signed-line-pullback-unit-presentation]. Suppose a binary operation on their target sheaves agrees on unit sections with a source operation. For any sheaf Z and source sections x:Z→S, y:Z→S′, z:Z→S″ satisfying z=op(x,y), their transported maps from L(Z) satisfy the corresponding target operation equation. Likewise a target constant agreeing with the source constant on units carries every source constant graph to that target constant graph.

(SHEAF DAG node `lem-pur-signed-line-unit-presentation-graphs`; machine-alignment layer.) Split from [lemma-inverse-image-coefficient-sheaves--2]. DAG kind: statement. Placed through `det-prop-sfb-cartesian-coefficients-twists` (ancestor-2). DAG status: split. Statement dependencies not drawn: `def-weil-size-convention`.
