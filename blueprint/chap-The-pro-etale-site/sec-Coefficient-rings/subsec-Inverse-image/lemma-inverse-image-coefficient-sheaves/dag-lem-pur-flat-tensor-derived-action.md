+++
id = "dag-lem-pur-flat-tensor-derived-action"
kind = "dag-lemma"
title = "FlatTensorDerivedAction"
name_showing = false
order = 187517
tags = ["sheaf-dag"]
split_from = "lemma-inverse-image-coefficient-sheaves--2"
dag_id = "lem-pur-flat-tensor-derived-action"
dag_kind = "statement"
dag_status = "split"
serial = false
dag_lean = ["SheafOfModules.SignedLineDerivedBaseChange.flat_tensor_derived_action"]
uses = ["dag-def-pur-signed-line-derived-action-data"]
+++
Let F be an additive exact functor between the two module-sheaf categories, L and M flat fixed sheaves, and gamma:(- tensor L)⋙F≅F⋙(- tensor M). Then there exists b:DerivedActionData(F,L,M) satisfying DerivedAction(F,L,M,gamma,b) [dag-def-pur-signed-line-derived-action-data]. Thus its resolving comparisons have the prescribed representative normalization and its derived comparison is the unique natural isomorphism whose square on every localized complex is the termwise image of gamma.

(SHEAF DAG node `lem-pur-flat-tensor-derived-action`; machine-alignment layer.) Split from [lemma-inverse-image-coefficient-sheaves--2]. DAG kind: statement. Placed through `det-prop-sfb-cartesian-coefficients-twists` (ancestor-2). DAG status: split. Statement dependencies not drawn: `def-pc-flat-sheaf-modules`, `def-sf-ringed-kflat-tensor-representative-data`, `def-weil-sheaf-of-modules-category`, `lem-weil-pbc-kflat-fixed-tensor-triangulated`.
