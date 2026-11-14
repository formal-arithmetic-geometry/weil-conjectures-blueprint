+++
id = "dag-lem-pe-coefficient-finite-local-model-pullback"
kind = "dag-lemma"
title = "Finite module local models survive iterated inverse image"
name_showing = false
order = 149523
tags = ["sheaf-dag"]
split_from = "theorem-comparison-constructible-sheaves"
dag_id = "lem-pe-coefficient-finite-local-model-pullback"
dag_kind = "lemma"
dag_status = "split"
serial = false
dag_lean = ["AlgebraicGeometry.ProEtale.coefficientProEtale_finite_iso", "AlgebraicGeometry.ProEtale.coefficientProEtale_finite_comp"]
uses = ["dag-def-pe-etale-constructible-module"]
+++
On the coefficient-sized pro-etale sites of `def-sfb-affine-locally-constructible-proetale-modules`, for composable scheme maps f and g, if inverse image along g of an A-module sheaf has finite locally constant models as in [dag-def-pe-etale-constructible-module], then inverse image along f followed by g has the same property. No Noetherianity is required. The module also proves invariance under isomorphism.

(SHEAF DAG node `lem-pe-coefficient-finite-local-model-pullback`; machine-alignment layer.) Split from [theorem-comparison-constructible-sheaves]. DAG kind: lemma. Placed through `sk-thm-pe-constructible-comparison` (ancestor-1). DAG status: split. Statement dependencies not drawn: `def-sfb-affine-locally-constructible-proetale-modules`.
