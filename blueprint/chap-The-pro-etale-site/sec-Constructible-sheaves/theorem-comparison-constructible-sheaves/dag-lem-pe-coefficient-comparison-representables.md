+++
id = "dag-lem-pe-coefficient-comparison-representables"
kind = "dag-lemma"
title = "Large-index continuity of etale representables"
name_showing = false
order = 149520
tags = ["sheaf-dag"]
split_from = "theorem-comparison-constructible-sheaves"
dag_id = "lem-pe-coefficient-comparison-representables"
dag_kind = "lemma"
dag_status = "split"
serial = false
dag_lean = ["AlgebraicGeometry.ProEtale.coefficientComparison_representable_preservesColimit"]
uses = ["dag-det-pe-classical-definition-continuity-map"]
+++
For a scheme X in universe u, an affine etale presentation P of det-pe-classical-definition-continuity-map indexed by a small cofiltered category in universe u+1, and an etale object V in the coefficient-sized model of def-weil-pbc-site-comparison-morphism, the covariant hom functor from the corresponding opposite pro-etale object preserves the colimit diagram (P.diagram followed by AsSmall.up).op. Equivalently, maps from the affine limit to V factor through a stage and equality is detected at a later stage. The coefficient-model size max(v,u+1) is independent of the scheme universe.

(SHEAF DAG node `lem-pe-coefficient-comparison-representables`; machine-alignment layer.) Split from [theorem-comparison-constructible-sheaves]. DAG kind: lemma. Placed through `sk-thm-pe-constructible-comparison` (ancestor-1). DAG status: split.
