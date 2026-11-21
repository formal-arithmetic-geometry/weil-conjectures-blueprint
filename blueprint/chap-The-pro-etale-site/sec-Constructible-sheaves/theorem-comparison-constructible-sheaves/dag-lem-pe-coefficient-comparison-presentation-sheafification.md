+++
id = "dag-lem-pe-coefficient-comparison-presentation-sheafification"
kind = "dag-lemma"
title = "Affine-presentation sheafification for coefficient-sized comparison"
name_showing = false
order = 149519
tags = ["sheaf-dag"]
split_from = "theorem-comparison-constructible-sheaves"
dag_id = "lem-pe-coefficient-comparison-presentation-sheafification"
dag_kind = "lemma"
dag_status = "split"
serial = false
dag_lean = ["AlgebraicGeometry.ProEtale.coefficientComparison_presentation_toSheafify_isIso"]
uses = ["dag-det-pe-classical-definition-continuity-map"]
+++
For X, a commutative ring A in max(v,u+1), an A-module sheaf G on the coefficient-sized etale model of def-weil-pbc-site-comparison-morphism, and an affine etale presentation P of det-pe-classical-definition-continuity-map indexed in universe u+1, the unit from the presheaf left Kan extension of G along the opposite comparison inclusion to its pro-etale sheafification is invertible both at AsSmall.up(P.cone.pt) and at every AsSmall.up(P.diagram.obj i). This asserts only pointwise invertibility of sheafification, not that any section cocone is a colimit.

(SHEAF DAG node `lem-pe-coefficient-comparison-presentation-sheafification`; machine-alignment layer.) Split from [theorem-comparison-constructible-sheaves]. DAG kind: lemma. Placed through `sk-thm-pe-constructible-comparison` (ancestor-1). DAG status: split.
