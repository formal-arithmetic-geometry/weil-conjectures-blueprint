+++
id = "dag-lem-pur-signed-line-pullback-unique"
kind = "dag-lemma"
title = "Signed line PullbackUnique"
name_showing = false
order = 187536
tags = ["sheaf-dag"]
split_from = "lemma-inverse-image-coefficient-sheaves--2"
dag_id = "lem-pur-signed-line-pullback-unique"
dag_kind = "statement"
dag_status = "split"
serial = false
dag_lean = ["SheafOfModules.signedLinePullback_normalized_unique"]
uses = ["dag-def-pur-signed-line-pullback-normalization-data", "dag-def-pur-signed-line-scalar-normalization-data", "dag-lem-pur-ringed-site-finite-free-dual-pullback", "dag-lem-pur-ringed-site-module-pullback-exists-universes"]
+++
For any ringed-site module pullback F, an isomorphism t:F(P)≅Q, and two signed-power isomorphism families T and T′, if both satisfy SignedLinePullbackNormalized [dag-def-pur-signed-line-pullback-normalization-data], then T=T′. The conclusion requires no rank-one hypothesis beyond the existence of the normalized families.

(SHEAF DAG node `lem-pur-signed-line-pullback-unique`; machine-alignment layer.) Split from [lemma-inverse-image-coefficient-sheaves--2]. DAG kind: statement. Placed through `det-prop-sfb-cartesian-coefficients-twists` (ancestor-2). DAG status: split. Statement dependencies not drawn: `def-weil-sheaf-of-modules-category`, `lem-pur-signed-line-scalar-pullback-square`, `lem-pur-signed-line-scalar-tensor-tower`, `sk-def-pbc-conventions`.
