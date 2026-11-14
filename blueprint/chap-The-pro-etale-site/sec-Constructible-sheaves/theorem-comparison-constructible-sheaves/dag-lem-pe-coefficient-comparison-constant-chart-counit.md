+++
id = "dag-lem-pe-coefficient-comparison-constant-chart-counit"
kind = "dag-lemma"
title = "Comparison counit on a single constant etale chart"
name_showing = false
order = 149509
tags = ["sheaf-dag"]
split_from = "theorem-comparison-constructible-sheaves"
dag_id = "lem-pe-coefficient-comparison-constant-chart-counit"
dag_kind = "lemma"
dag_status = "split"
serial = false
dag_lean = ["AlgebraicGeometry.ProEtale.coefficientComparison_counit_isIso_of_constant_over"]
uses = ["dag-def-weil-pbc-constant-sheaf"]
+++
Let X be a scheme, A an independently sized commutative ring, F a module sheaf on the coefficient-sized pro-etale site, and V an object of its coefficient-sized etale site. Use the canonical comparison inclusion i and its Kan-extension/sheafification adjunction [def-weil-pbc-site-comparison-morphism, def-weil-proetale-inverse-image], and constant module sheaves [def-weil-pbc-constant-sheaf, def-weil-sheaf-of-modules-category]. If F restricted to i(V) is isomorphic to the constant sheaf of some A-module M, then restriction of the comparison counit at F to i(V) is an isomorphism. No finite-presentation or local constancy condition on F elsewhere, and no covering family, is assumed.

(SHEAF DAG node `lem-pe-coefficient-comparison-constant-chart-counit`; machine-alignment layer.) Split from [theorem-comparison-constructible-sheaves]. DAG kind: lemma. Placed through `sk-thm-pe-constructible-comparison` (ancestor-1). DAG status: split. Statement dependencies not drawn: `def-weil-pbc-site-comparison-morphism`, `def-weil-proetale-inverse-image`, `def-weil-sheaf-of-modules-category`.
