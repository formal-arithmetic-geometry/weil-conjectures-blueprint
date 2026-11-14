+++
id = "dag-lem-pe-coefficient-affine-cech-presentation"
kind = "dag-lemma"
title = "Coefficient-site affine finite Cech nerve presentations"
name_showing = false
order = 149504
tags = ["sheaf-dag"]
split_from = "theorem-comparison-constructible-sheaves"
dag_id = "lem-pe-coefficient-affine-cech-presentation"
dag_kind = "statement"
dag_status = "split"
serial = false
dag_lean = ["AlgebraicGeometry.ProEtale.exists_coefficient_affine_cech_presentation"]
uses = ["dag-def-pe-coefficient-affine-cech-presentation", "dag-sk-def-pe-morphisms"]
+++
Let X be any scheme in universe u. Let V_a to U be a Fin m-indexed covering in the coefficient-sized pro-etale model of [dag-lem-pe-coefficient-comparison-data], and suppose the structure morphisms of AsSmall.down U and all AsSmall.down V_a are proAffineEtale [dag-sk-def-pe-morphisms]. Fix any chosen iterated products and index maps S `def-weil-pbc-site-cech-complex`. There is a small cofiltered category J in universe u+1 and compatible affine etale covering approximations of this family in the source model. Their normalized chosen Cech complexes have transitions and projections from S commuting with every index map, not only faces. Every intersection is affine, and the cone from its specified S.W to the corresponding stage diagram is a limit after forgetting to schemes over X. This assertion has no coefficient ring, sheaf, injectivity, degree, or cohomology in it. Empty families, repeated factors and arbitrary non-affine X are included.

(SHEAF DAG node `lem-pe-coefficient-affine-cech-presentation`; machine-alignment layer.) Split from [theorem-comparison-constructible-sheaves]. DAG kind: statement. Placed through `sk-thm-pe-constructible-comparison` (ancestor-1). DAG status: split. Statement dependencies not drawn: `def-weil-pbc-site-cech-complex`.
