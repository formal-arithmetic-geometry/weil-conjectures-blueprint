+++
id = "dag-lem-pur-signed-line-algebraic-pullback"
kind = "dag-lemma"
title = "Signed line algebraic pullback"
name_showing = false
order = 187526
tags = ["sheaf-dag"]
split_from = "lemma-inverse-image-coefficient-sheaves--2"
dag_id = "lem-pur-signed-line-algebraic-pullback"
dag_kind = "statement"
dag_status = "split"
serial = false
dag_lean = ["SheafOfModules.SignedLineDerivedBaseChange.algebraic_pullback_of_presentations"]
uses = ["dag-def-pur-signed-line-derived-action-data", "dag-def-pur-signed-line-pullback-unit-presentation", "dag-lem-pur-ringed-site-finite-free-dual-pullback", "dag-lem-pur-ringed-site-module-pullback-exists-universes"]
+++
Let F be the specified module pullback for a:R→U_*S. Given compatible unit presentations identifying S with the set inverse image of R and identifying the underlying sets of F with the set inverse image, there exists an AlgebraicInverseImage whose module functor is F, whose ring-underlying comparison is the inverse ring presentation, and whose module-underlying comparison is the given one. Its additive and scalar operation comparisons satisfy the defining graph equations. All fields are constructed from these presentations.

(SHEAF DAG node `lem-pur-signed-line-algebraic-pullback`; machine-alignment layer.) Split from [lemma-inverse-image-coefficient-sheaves--2]. DAG kind: statement. Placed through `det-prop-sfb-cartesian-coefficients-twists` (ancestor-2). DAG status: split. Statement dependencies not drawn: `def-sf-ringed-kflat-tensor-representative-data`, `def-weil-sheaf-of-modules-category`, `lem-weil-pbc-kflat-fixed-tensor-triangulated`.
