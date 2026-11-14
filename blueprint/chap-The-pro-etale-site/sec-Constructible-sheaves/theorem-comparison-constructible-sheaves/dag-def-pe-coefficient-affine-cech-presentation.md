+++
id = "dag-def-pe-coefficient-affine-cech-presentation"
kind = "dag-definition"
title = "Compatible coefficient-site finite Cech presentation data"
name_showing = false
order = 149501
tags = ["sheaf-dag"]
split_from = "theorem-comparison-constructible-sheaves"
dag_id = "def-pe-coefficient-affine-cech-presentation"
dag_kind = "definition"
dag_status = "split"
serial = false
dag_lean = ["AlgebraicGeometry.ProEtale.CoefficientAffineCechPresentation"]
+++
Fix X, a finite family V_a to U in the coefficient-sized pro-etale model [dag-lem-pe-coefficient-comparison-data], a SiteCechComplex S for it `def-weil-pbc-site-cech-complex`, and a small index category J in universe u+1. CoefficientAffineCechPresentation is the structure of source-model base and family objects, covering arrows, a chosen SiteCechComplex at each stage, functorial transition maps on every tuple, projections from each S.W to the included stage tuple, compatibility with every index map, and absolute affineness of every stage tuple and S.W. Its nerve is the stage tuple diagram and its cone has vertex S.W and the specified projections. The structure only records data and equations; it asserts no existence, exactness, sections, or cohomology.

(SHEAF DAG node `def-pe-coefficient-affine-cech-presentation`; machine-alignment layer.) Split from [theorem-comparison-constructible-sheaves]. DAG kind: definition. Placed through `sk-thm-pe-constructible-comparison` (ancestor-1). DAG status: split. Statement dependencies not drawn: `def-weil-pbc-site-cech-complex`.
