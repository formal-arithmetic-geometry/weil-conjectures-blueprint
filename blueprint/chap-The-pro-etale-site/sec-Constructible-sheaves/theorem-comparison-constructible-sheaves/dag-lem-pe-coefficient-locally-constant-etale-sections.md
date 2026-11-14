+++
id = "dag-lem-pe-coefficient-locally-constant-etale-sections"
kind = "dag-lemma"
title = "Joint etale-local sections of coefficient-sized locally constant set sheaves"
name_showing = false
order = 149529
tags = ["sheaf-dag"]
split_from = "theorem-comparison-constructible-sheaves"
dag_id = "lem-pe-coefficient-locally-constant-etale-sections"
dag_kind = "statement"
dag_status = "split"
serial = false
dag_lean = ["AlgebraicGeometry.ProEtale.coefficientLocallyConstant_etaleSections"]
uses = ["dag-def-weil-pbc-constant-sheaf"]
+++
Let X be a scheme, with the equivalent coefficient-sized etale and pro-etale sites and inclusion i of [def-weil-pbc-site-comparison-morphism, def-weil-proetale-inverse-image]. Let H_a be a coefficient-sized family of set-valued sheaves on the pro-etale model. Suppose every H_a is locally constant: some family W_j covering the final object identifies each slice restriction with the constant sheaf of a coefficient-sized set Q_j [dag-def-weil-pbc-constant-sheaf]. Suppose also a pro-etale family U_j covering the final object has, for every j, a section of at least one H_a on U_j. Then there is a coefficient-sized family V_j of etale objects such that i(V_j) cover the final pro-etale object and every i(V_j) has a section of some H_a. No nonemptiness of the family, coefficient sets, or X is assumed.

(SHEAF DAG node `lem-pe-coefficient-locally-constant-etale-sections`; machine-alignment layer.) Split from [theorem-comparison-constructible-sheaves]. DAG kind: statement. Placed through `sk-thm-pe-constructible-comparison` (ancestor-1). DAG status: split.
