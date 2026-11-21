+++
id = "dag-lem-pur-signed-line-localized-coherence"
kind = "dag-lemma"
title = "Signed line LocalizedCoherence"
name_showing = false
order = 187529
tags = ["sheaf-dag"]
split_from = "lemma-inverse-image-coefficient-sheaves--2"
dag_id = "lem-pur-signed-line-localized-coherence"
dag_kind = "statement"
dag_status = "split"
serial = false
dag_lean = ["SheafOfModules.SignedLineDerivedBaseChange.signed_line_localized_coherence"]
uses = ["dag-def-pur-signed-line-derived-action-data", "dag-def-pur-signed-line-pullback-normalization-data", "dag-def-pur-signed-line-scalar-normalization-data", "dag-lem-pur-ringed-site-finite-free-dual-pullback", "dag-lem-pur-ringed-site-module-pullback-exists-universes"]
+++
Let F be an exact module pullback, T a normalized signed family [dag-def-pur-signed-line-pullback-normalization-data], gamma_d its ordinary tensor comparison with the prescribed pure-section formula, and b_d a family satisfying DerivedAction(F,P^$[d]$,Q^$[d]$,gamma_d,b_d) [dag-def-pur-signed-line-derived-action-data]. Then DerivedFamilyCoherence(F,P,Q,b) holds: the same eta family commutes with normalized derived right unitors, positive-power products and negative-positive evaluations on every unbounded derived object.

(SHEAF DAG node `lem-pur-signed-line-localized-coherence`; machine-alignment layer.) Split from [lemma-inverse-image-coefficient-sheaves--2]. DAG kind: statement. Placed through `det-prop-sfb-cartesian-coefficients-twists` (ancestor-2). DAG status: split. Statement dependencies not drawn: `def-sf-ringed-kflat-tensor-representative-data`, `def-weil-sheaf-of-modules-category`, `lem-pur-signed-line-scalar-pullback-square`, `lem-pur-signed-line-scalar-tensor-tower`, `lem-weil-pbc-kflat-fixed-tensor-triangulated`.
