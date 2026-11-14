+++
id = "dag-lem-pe-normalized-integral-quotient-cone"
kind = "dag-lemma"
title = "Normalized compact ideal-power quotient cone"
name_showing = false
order = 178501
tags = ["sheaf-dag"]
split_from = "lemma-comparison-completed-coefficients--1"
dag_id = "lem-pe-normalized-integral-quotient-cone"
dag_kind = "statement"
dag_status = "split"
serial = false
dag_lean = ["AlgebraicGeometry.ProEtale.sfb_normalized_integral_quotient_cone"]
uses = ["dag-def-sfb-finite-upper-star", "dag-lem-sfb-transfinite-plus-finite-limits", "dag-lem-sfb-transfinite-plus-sheaf-orthogonality"]
+++
Let R be a compact Hausdorff commutative topological ring, I an ideal, with every R/I^n finite and discrete. Assume the quotient maps jointly separate points. Using the quotient tower and constant-section maps of `def-pe-completed-coefficient-comparison-data`, there exists a cone rho from the condensed R ring to the constant quotient rings, normalized on constant sections by the actual quotient maps. For every scheme X its image under p_X^* is limiting and its diagram is naturally isomorphic to the constant quotient diagram on X. For every scheme map f:X→Y, f^* of that cone over Y is still limiting.

(SHEAF DAG node `lem-pe-normalized-integral-quotient-cone`; machine-alignment layer.) Split from [lemma-comparison-completed-coefficients--1]. DAG kind: statement. DAG status: split. Statement dependencies not drawn: `def-pe-completed-coefficient-comparison-data`, `def-sfb-padic-condensed-ring`, `def-sfb-padic-int-condensed-ring`, `def-sfb-padic-subfield-condensed-ring`, `def-sfb-upper-star-from-point`, `det-def-sfb-ring-object`, `det-def-sfb-ring-object-rings`, `lem-coef-grothendieck-locally-presentable`, `lem-sfb-finite-upper-star-braided`, `lem-weil-pbc-sheaf-tensor-closed`, `sk-def-sfb-ring-object`.
