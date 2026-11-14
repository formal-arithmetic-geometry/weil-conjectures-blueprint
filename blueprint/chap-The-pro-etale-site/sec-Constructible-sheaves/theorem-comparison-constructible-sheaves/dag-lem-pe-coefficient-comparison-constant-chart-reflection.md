+++
id = "dag-lem-pe-coefficient-comparison-constant-chart-reflection"
kind = "dag-lemma"
title = "Reflection of a single constant chart under coefficient-sized comparison"
name_showing = false
order = 149510
tags = ["sheaf-dag"]
split_from = "theorem-comparison-constructible-sheaves"
dag_id = "lem-pe-coefficient-comparison-constant-chart-reflection"
dag_kind = "lemma"
dag_status = "split"
serial = false
dag_lean = ["AlgebraicGeometry.ProEtale.coefficientComparison_constant_over_reflect"]
uses = ["dag-def-weil-pbc-constant-sheaf"]
+++
Let X be any scheme, A any commutative ring in max(v,u+1), F an A-module sheaf on the coefficient-sized etale site, V an object of that site, and M an A-module in the same coefficient universe. Use the comparison inverse image P and inclusion i of `def-weil-pbc-site-comparison-morphism`, with the coefficient-sized models of `def-weil-proetale-inverse-image`, and constant sheaves [dag-def-weil-pbc-constant-sheaf]. An isomorphism (P F).over i(V) ≅ constant M on the pro-etale slice implies that F.over V ≅ constant M on the etale slice. There is no covering hypothesis, no finite generation or finite presentation hypothesis on M, and no Noetherian hypothesis on A.

(SHEAF DAG node `lem-pe-coefficient-comparison-constant-chart-reflection`; machine-alignment layer.) Split from [theorem-comparison-constructible-sheaves]. DAG kind: lemma. Placed through `sk-thm-pe-constructible-comparison` (ancestor-1). DAG status: split. Statement dependencies not drawn: `def-weil-sheaf-of-modules-category`.
