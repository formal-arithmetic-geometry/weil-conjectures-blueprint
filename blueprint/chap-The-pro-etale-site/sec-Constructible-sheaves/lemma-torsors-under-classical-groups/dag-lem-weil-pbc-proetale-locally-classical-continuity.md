+++
id = "dag-lem-weil-pbc-proetale-locally-classical-continuity"
kind = "dag-lemma"
title = "Local classicality gives affine section continuity"
name_showing = false
order = 143504
tags = ["sheaf-dag"]
split_from = "lemma-torsors-under-classical-groups--1"
dag_id = "lem-weil-pbc-proetale-locally-classical-continuity"
dag_kind = "statement"
dag_status = "split"
serial = false
dag_lean = ["AlgebraicGeometry.Scheme.proEtale_locallyClassical_continuity"]
uses = ["dag-def-weil-pbc-ind-etale-basis", "dag-def-weil-pbc-proetale-site", "dag-sk-def-pe-morphisms"]
+++
Let X be a scheme and F a pro-etale sheaf of sets [dag-def-weil-pbc-proetale-site]. Suppose a pro-etale covering family U_i has F restricted to each U_i isomorphic to ν_(U_i)^*G_i for an etale sheaf G_i `def-weil-pbc-site-comparison-morphism`. Then every small cofiltered presentation of an affine ind-etale X-object by affine etale X-objects [dag-lem-weil-pbc-ind-etale-basis] is carried by F to the colimit of its section sets, with the canonical restriction maps.

(SHEAF DAG node `lem-weil-pbc-proetale-locally-classical-continuity`; machine-alignment layer.) Split from [lemma-torsors-under-classical-groups--1]. DAG kind: statement. Placed through `lem-weil-pbc-proetale-locally-classical-etale-cover` (ancestor-1). DAG status: split.
