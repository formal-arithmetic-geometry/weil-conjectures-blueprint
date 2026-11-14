+++
id = "dag-lem-poincare-integral-residue-free-comparison"
kind = "dag-lemma"
title = "Free integral modules on constant residue groups are the actual residue diagram"
name_showing = false
order = 184537
tags = ["sheaf-dag"]
split_from = "definition-tate-twists--13"
dag_id = "lem-poincare-integral-residue-free-comparison"
dag_kind = "statement"
dag_status = "split"
serial = false
dag_lean = ["AlgebraicGeometry.ProEtale.integralResidueAbTransition", "AlgebraicGeometry.ProEtale.constantTateResidueSystem", "AlgebraicGeometry.ProEtale.constantTateResidueSystem_free_iso"]
uses = ["dag-def-weil-pbc-constant-sheaf", "dag-lem-poincare-integral-residue-module-limit", "dag-lem-sfb-transfinite-plus-finite-limits", "dag-lem-sfb-transfinite-plus-sheaf-orthogonality"]
+++
Let X be a scheme and l a prime. Set R_X=p_X^*continuousMapRingObj(Z_l). Let C_n be the constant abelian sheaf on ULift(ZMod(l^n)), with transitions induced by the usual reduction homomorphisms [dag-def-weil-pbc-constant-sheaf]. Let Q_n be the actual R_X-module of continuous ZMod(l^n)-valued functions, with action through chartComparison followed by PadicInt.toZModPow and the actual reduction transitions of [dag-lem-poincare-integral-residue-module-limit]. Then the diagrams n|->Mod.freeFunctor(R_X)(C_n) [dag-def-pur-condensed-tate-twists] and n|->Q_n are naturally isomorphic. Both include n=0. No invertibility or finiteness assumption on X is required.

(SHEAF DAG node `lem-poincare-integral-residue-free-comparison`; machine-alignment layer.) Split from [definition-tate-twists--13]. DAG kind: statement. Placed through `sk-def-sp-tate-twist` (ancestor-1). DAG status: split. Statement dependencies not drawn: `def-sfb-padic-condensed-ring`, `def-sfb-padic-int-condensed-ring`, `def-sfb-padic-subfield-condensed-ring`, `def-sfb-qlbar-coefficient-ring`, `def-sfb-upper-star-from-point`, `det-def-sfb-ring-object`, `det-def-sfb-ring-object-rings`, `lem-coef-grothendieck-locally-presentable`, `lem-weil-pbc-sheaf-tensor-closed`, `pur713-def-coefficient-rings`, `sk-def-sfb-pulled-back-coefficients`, `sk-def-sfb-ring-object`.
