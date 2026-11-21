+++
id = "dag-lem-sfb-monic-spectral-value-coefficients"
kind = "dag-lemma"
title = "Coefficient criterion for the spectral value of a monic polynomial"
name_showing = false
order = 187553
tags = ["sheaf-dag"]
split_from = "lemma-inverse-image-coefficient-sheaves--3"
dag_id = "lem-sfb-monic-spectral-value-coefficients"
dag_kind = "statement"
dag_status = "split"
serial = false
+++
Let R be a normed division ring and P a monic polynomial over R `def-weil-polynomial-ring`. Write d for its natural degree and let s(P) be the supremum, over n < d, of the real numbers ‖P.coeff n‖^(1/(d-n)), with the other terms zero; this is Mathlib spectralValue P. Then s(P) ≤ 1 if and only if ‖P.coeff n‖ ≤ 1 for every natural number n.

(SHEAF DAG node `lem-sfb-monic-spectral-value-coefficients`; machine-alignment layer.) Split from [lemma-inverse-image-coefficient-sheaves--3]. DAG kind: statement. Placed through `det-prop-sfb-cartesian-coefficients-finite-free` (ancestor-1). DAG status: split. Lean names not on master: `spectralValue_le_one_iff`. Statement dependencies not drawn: `def-weil-polynomial-ring`.
