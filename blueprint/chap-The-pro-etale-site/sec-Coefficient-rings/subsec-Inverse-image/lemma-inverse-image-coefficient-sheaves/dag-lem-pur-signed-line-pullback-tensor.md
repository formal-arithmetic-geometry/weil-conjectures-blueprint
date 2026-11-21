+++
id = "dag-lem-pur-signed-line-pullback-tensor"
kind = "dag-lemma"
title = "Signed line PullbackTensor"
name_showing = false
order = 187535
tags = ["sheaf-dag"]
split_from = "lemma-inverse-image-coefficient-sheaves--2"
dag_id = "lem-pur-signed-line-pullback-tensor"
dag_kind = "statement"
dag_status = "split"
serial = false
dag_lean = ["SheafOfModules.SignedLineDerivedBaseChange.identified_ring_pullback_tensor"]
uses = ["dag-def-pur-signed-line-derived-action-data", "dag-lem-pur-ringed-site-finite-free-dual-pullback", "dag-lem-pur-ringed-site-module-pullback-exists-universes"]
+++
Let U preserve finite limits and coverings, let the adjunct of a:R→U_*S be invertible, and fix an isomorphism t:F(L)≅N of module sheaves. There exists a natural isomorphism gamma:(- tensor L)⋙F≅F⋙(- tensor N). On every source pure section x tensor y inserted by the pullback unit, gamma is the pure tensor of the inserted x and t applied to the inserted y. No flatness or rank assumption on L is needed.

(SHEAF DAG node `lem-pur-signed-line-pullback-tensor`; machine-alignment layer.) Split from [lemma-inverse-image-coefficient-sheaves--2]. DAG kind: statement. Placed through `det-prop-sfb-cartesian-coefficients-twists` (ancestor-2). DAG status: split. Statement dependencies not drawn: `def-sf-ringed-kflat-tensor-representative-data`, `def-weil-sheaf-of-modules-category`, `lem-weil-pbc-kflat-fixed-tensor-triangulated`.
