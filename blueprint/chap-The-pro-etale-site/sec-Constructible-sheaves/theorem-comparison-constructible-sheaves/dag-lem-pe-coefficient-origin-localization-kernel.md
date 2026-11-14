+++
id = "dag-lem-pe-coefficient-origin-localization-kernel"
kind = "dag-lemma"
title = "The classical open kernel of coefficient-sized localization"
name_showing = false
order = 149532
tags = ["sheaf-dag"]
split_from = "theorem-comparison-constructible-sheaves"
dag_id = "lem-pe-coefficient-origin-localization-kernel"
dag_kind = "lemma"
dag_status = "split"
serial = false
dag_lean = ["AlgebraicGeometry.ProEtale.coefficientFixed_localization_kernel_origin"]
+++
Let X be affine in universe u, i:Z→X a closed immersion and j:U→X a quasi-compact open immersion with complementary ranges. Let A be a commutative ring in max v (u+1) and F a coefficient-sized pro-etale sheaf of A-modules. Let eta_F:F→i_*i^*F be the unit of any adjunction between the canonical fixed-module inverse-image/direct-image functors of `def-weil-proetale-inverse-image`. If j^*F lies in the essential image of the comparison of `def-weil-pbc-site-comparison-morphism` over U, then eta_F is epic and ker(eta_F) lies in that essential image over X. No assumption on i^*F is made.

(SHEAF DAG node `lem-pe-coefficient-origin-localization-kernel`; machine-alignment layer.) Split from [theorem-comparison-constructible-sheaves]. DAG kind: lemma. Placed through `sk-thm-pe-constructible-comparison` (ancestor-1). DAG status: split. Statement dependencies not drawn: `def-weil-pbc-site-comparison-morphism`, `def-weil-proetale-inverse-image`.
