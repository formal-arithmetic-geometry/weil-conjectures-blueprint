+++
id = "dag-lem-weil-pbc-proetale-continuous-counit-sets"
kind = "dag-lemma"
title = "Affine continuity makes the set comparison counit invertible"
name_showing = false
order = 143503
tags = ["sheaf-dag"]
split_from = "lemma-torsors-under-classical-groups--1"
dag_id = "lem-weil-pbc-proetale-continuous-counit-sets"
dag_kind = "statement"
dag_status = "split"
serial = false
dag_lean = ["AlgebraicGeometry.Scheme.proEtaleComparisonCounitSets_isIso_of_continuous"]
uses = ["dag-def-weil-pbc-ind-etale-basis", "dag-def-weil-pbc-proetale-site", "dag-sk-def-pe-morphisms"]
+++
For a scheme X and a pro-etale sheaf of sets F [dag-def-weil-pbc-proetale-site], suppose F sends every affine ind-etale presentation by affine etale X-schemes [dag-lem-weil-pbc-ind-etale-basis] to a colimit of section sets. Then the counit ν_X^*ν_{X,*}F→F `def-weil-pbc-site-comparison-morphism` is invertible.

(SHEAF DAG node `lem-weil-pbc-proetale-continuous-counit-sets`; machine-alignment layer.) Split from [lemma-torsors-under-classical-groups--1]. DAG kind: statement. Placed through `lem-weil-pbc-proetale-locally-classical-etale-cover` (ancestor-1). DAG status: split. Statement dependencies not drawn: `def-weil-pbc-site-comparison-morphism`.
