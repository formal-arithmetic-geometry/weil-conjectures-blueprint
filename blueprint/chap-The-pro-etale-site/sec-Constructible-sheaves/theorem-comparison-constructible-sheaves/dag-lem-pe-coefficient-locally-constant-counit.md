+++
id = "dag-lem-pe-coefficient-locally-constant-counit"
kind = "dag-lemma"
title = "Coefficient-universe classicality of locally constant set sheaves"
name_showing = false
order = 149528
tags = ["sheaf-dag"]
split_from = "theorem-comparison-constructible-sheaves"
dag_id = "lem-pe-coefficient-locally-constant-counit"
dag_kind = "statement"
dag_status = "split"
serial = false
dag_lean = ["AlgebraicGeometry.ProEtale.coefficientLocallyConstant_counit_isIso"]
uses = ["dag-def-weil-pbc-constant-sheaf", "dag-lem-route-small-model-comparison-inclusion-is-continuous"]
+++
Let X be a scheme and let H be a sheaf of sets in Type (max v (u+1)) on its coefficient-sized pro-etale model [def-weil-pbc-site-comparison-morphism, def-weil-proetale-inverse-image]. Suppose a coefficient-sized family W covers the final object and every slice restriction H.over(W_j) is isomorphic to the constant sheaf of some coefficient-sized set Q_j [dag-def-weil-pbc-constant-sheaf]. Then the canonical counit nu^* nu_* H -> H of smallModelProEtaleComparison is an isomorphism. This is a single-sheaf structural assertion; there is no family of H, no local inhabitedness assumption, and no covering-family conclusion.

(SHEAF DAG node `lem-pe-coefficient-locally-constant-counit`; machine-alignment layer.) Split from [theorem-comparison-constructible-sheaves]. DAG kind: statement. Placed through `sk-thm-pe-constructible-comparison` (ancestor-1). DAG status: split.
