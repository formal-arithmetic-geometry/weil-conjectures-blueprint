+++
id = "dag-lem-pe-coefficient-fp-local-system-etale-cover"
kind = "dag-lemma"
title = "Etale constant charts for independently sized finitely presented local systems"
name_showing = false
order = 149526
tags = ["sheaf-dag"]
split_from = "theorem-comparison-constructible-sheaves"
dag_id = "lem-pe-coefficient-fp-local-system-etale-cover"
dag_kind = "lemma"
dag_status = "split"
serial = false
dag_lean = ["AlgebraicGeometry.ProEtale.coefficientFpLocalSystem_etaleCover"]
uses = ["dag-def-weil-pbc-constant-sheaf"]
+++
Let X be a scheme and let A be a commutative ring in the independent coefficient universe. Use the equivalent coefficient-sized sites and inclusion i of [def-weil-pbc-site-comparison-morphism, def-weil-proetale-inverse-image], constant sheaves [dag-def-weil-pbc-constant-sheaf], module sheaves `def-weil-sheaf-of-modules-category`, and finite presentation `def-sc-finitely-presented-module`. If a pro-etale module sheaf F is locally constant with finitely presented models on a covering sieve over every object, then there exist a family V_i of coefficient-sized etale objects and finitely presented A-modules M_i with F restricted to i(V_i) isomorphic to constant M_i on that slice. The objects i(V_i) cover the final object of the pro-etale site. This asserts only etale constant charts, not an etale antecedent or a comparison isomorphism.

(SHEAF DAG node `lem-pe-coefficient-fp-local-system-etale-cover`; machine-alignment layer.) Split from [theorem-comparison-constructible-sheaves]. DAG kind: lemma. Placed through `sk-thm-pe-constructible-comparison` (ancestor-1). DAG status: split. Statement dependencies not drawn: `def-weil-pbc-site-comparison-morphism`, `def-weil-proetale-inverse-image`, `def-weil-sheaf-of-modules-category`, `def-sc-finitely-presented-module`.
