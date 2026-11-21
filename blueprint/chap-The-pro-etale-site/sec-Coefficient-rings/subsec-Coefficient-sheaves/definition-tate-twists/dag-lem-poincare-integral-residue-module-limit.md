+++
id = "dag-lem-poincare-integral-residue-module-limit"
kind = "dag-lemma"
title = "The regular integral coefficient module is the limit of its concrete residue modules"
name_showing = false
order = 184538
tags = ["sheaf-dag"]
split_from = "definition-tate-twists--13"
dag_id = "lem-poincare-integral-residue-module-limit"
dag_kind = "statement"
dag_status = "split"
serial = false
dag_lean = ["AlgebraicGeometry.ProEtale.tateResidueMap", "AlgebraicGeometry.ProEtale.tateResidueMap_isMonHom", "AlgebraicGeometry.ProEtale.tateResidueTransition", "AlgebraicGeometry.ProEtale.tateResidueTransition_isMonHom", "AlgebraicGeometry.ProEtale.tateResidueCoefficientMap", "AlgebraicGeometry.ProEtale.tateResidueCoefficientMap_isMonHom", "AlgebraicGeometry.ProEtale.tateResidueCoefficientMap_compat", "AlgebraicGeometry.ProEtale.tateResidueModuleLevel", "AlgebraicGeometry.ProEtale.tateResidueModuleTransition", "AlgebraicGeometry.ProEtale.tateResidueModuleSystem", "AlgebraicGeometry.ProEtale.tateResidueModuleProjection", "AlgebraicGeometry.ProEtale.tateResidueModuleCone", "AlgebraicGeometry.ProEtale.tateResidueModuleCone_isLimit"]
uses = ["dag-lem-sfb-transfinite-plus-finite-limits", "dag-lem-sfb-transfinite-plus-sheaf-orthogonality"]
+++
For any scheme X and prime l, let R_X=p_X^*continuousMapRingObj(Z_l) `def-sfb-padic-int-condensed-ring`. Define q_n:R_X->C(-,Z/l^n) as the canonical condensed-to-continuous chartComparison of `lem-weil-pbc-continuous-coefficient-realizations` followed by the actual continuous reduction toZModPow n. Regard C(-,Z/l^n) `lem-weil-pbc-continuous-regular-functions` as an R_X-module by restriction along q_n, with transitions the usual residue reductions. The cone of q_n with vertex regular R_X is a limit cone in internal R_X-modules. This includes n=0, where Z/l^0 is the zero ring. No invertibility or finiteness hypothesis on X is required.

(SHEAF DAG node `lem-poincare-integral-residue-module-limit`; machine-alignment layer.) Split from [definition-tate-twists--13]. DAG kind: statement. Placed through `sk-def-sp-tate-twist` (ancestor-1). DAG status: split. Statement dependencies not drawn: `def-sfb-padic-condensed-ring`, `def-sfb-padic-int-condensed-ring`, `def-sfb-padic-subfield-condensed-ring`, `def-sfb-qlbar-coefficient-ring`, `def-sfb-upper-star-from-point`, `det-def-sfb-ring-object`, `det-def-sfb-ring-object-rings`, `lem-coef-grothendieck-locally-presentable`, `lem-weil-pbc-sheaf-tensor-closed`, `pur713-def-coefficient-rings`, `sk-def-sfb-pulled-back-coefficients`, `sk-def-sfb-ring-object`.
