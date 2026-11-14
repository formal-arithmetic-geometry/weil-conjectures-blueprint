+++
id = "dag-lem-sfb-shifted-line-square"
kind = "dag-lemma"
title = "Composition of normalized unshifted rational Tate-line comparisons"
name_showing = false
order = 187548
tags = ["sheaf-dag"]
split_from = "lemma-inverse-image-coefficient-sheaves--2"
dag_id = "lem-sfb-shifted-line-square"
dag_kind = "statement"
dag_status = "split"
serial = false
dag_lean = ["AlgebraicGeometry.ProEtale.RationalP1.shifted_line_square"]
+++
Let l be prime, c a finite rational coefficient index or the algebraic-closure index, k a field of prime characteristic p distinct from l, and Y a k-scheme. Put Λ=(coefficient l c).X and L_X=line l c X as in `def-sfb-rational-tate-pullback-comparison`, T_X=L_X$[0]$$[2]$, q:P¹_Y→Y, and W=P¹_Y×_Y P¹_Y with projections p₁,p₂ as in `def-sfb-internal-diagonal-tensor-comparison` and `def-sfb-projective-diagonal-pullback`. The total derived pullbacks are those of `sk-def-sfb-module-derived-pushpull`. Let θ: Lp₂*∘Lq* ≅ Lp₁*∘Lq* be the canonical ambient pullback-square comparison of `def-weil-pbc-ambient-ringed-exchange`. Let e_q:Lq*(T_Y)≅T_{P¹_Y} be scalarQLineIso of `def-sfb-rational-p1-scalar-chern-maps`, and let e₁:Lp₁*(T_{P¹_Y})≅T_W and e₂:Lp₂*(T_{P¹_Y})≅T_W be firstLineComparisonForTrace and secondLineComparison of `def-sfb-rational-p1-second-pretrace-data` and `def-sfb-rational-tate-pullback-comparison`. Then the actual shifted line square commutes: θ_{T_Y} ≫ Lp₁*(e_q.hom) ≫ e₁.hom = Lp₂*(e_q.hom) ≫ e₂.hom. Here every comparison is the prescribed root-normalized comparison, with the canonical degree-zero and shift transports; no trace or adjunction-unit equation is assumed.

(SHEAF DAG node `lem-sfb-shifted-line-square`; machine-alignment layer.) Split from [lemma-inverse-image-coefficient-sheaves--2]. DAG kind: statement. Placed through `det-prop-sfb-cartesian-coefficients-twists` (ancestor-1). DAG status: split. Statement dependencies not drawn: `def-sfb-rational-tate-pullback-comparison`, `def-sfb-internal-diagonal-tensor-comparison`, `def-weil-pbc-ambient-ringed-exchange`, `def-sfb-rational-p1-scalar-chern-maps`, `def-sfb-rational-p1-second-pretrace-data`, `sk-def-sfb-module-derived-pushpull`, `def-sfb-projective-diagonal-pullback`.
