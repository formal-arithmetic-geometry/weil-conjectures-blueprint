+++
id = "dag-lem-poincare-compatible-integral-root-bases"
kind = "dag-lemma"
title = "Compatible finite-level bases identify the actual root and residue diagrams"
name_showing = false
order = 184533
tags = ["sheaf-dag"]
split_from = "definition-tate-twists--13"
dag_id = "lem-poincare-compatible-integral-root-bases"
dag_kind = "statement"
dag_status = "split"
serial = false
dag_lean = ["AlgebraicGeometry.ProEtale.exists_tateModule_residue_diagram_iso"]
uses = ["dag-def-sfb-finite-upper-star", "dag-lem-poincare-integral-residue-module-limit", "dag-lem-sfb-transfinite-plus-finite-limits", "dag-lem-sfb-transfinite-plus-sheaf-orthogonality"]
+++
Let l be a prime and X a scheme with l invertible in Gamma(X,O_X). Let T_r=Mod.freeFunctor(R_X)(rootsOfUnitySheaf X (l^r)), with the actual power transitions of [dag-def-pur-condensed-tate-twists], and let Q_r=tateResidueModuleLevel X l r be the actual continuous residue modules, with the specified action and reduction transitions of [dag-lem-poincare-integral-residue-module-limit]. There is a pro-etale cover (u_i:U_i->X) such that the diagrams r|->mapMod(u_i^*) T_r and r|->mapMod(u_i^*) Q_r are naturally isomorphic as diagrams of modules over u_i^*R_X [dag-def-sfb-finite-upper-star]. Both diagrams include r=0. No inverse limits, rational extensions, signed powers or constructibility assertion occur in this statement.

(SHEAF DAG node `lem-poincare-compatible-integral-root-bases`; machine-alignment layer.) Split from [definition-tate-twists--13]. DAG kind: statement. Placed through `sk-def-sp-tate-twist` (ancestor-1). DAG status: split. Statement dependencies not drawn: `def-pur-condensed-tate-twists`, `def-sfb-modobj-transport`, `def-sfb-padic-condensed-ring`, `def-sfb-padic-int-condensed-ring`, `def-sfb-padic-subfield-condensed-ring`, `def-sfb-qlbar-coefficient-ring`, `def-sfb-upper-star-from-point`, `det-def-sfb-ring-object`, `det-def-sfb-ring-object-rings`, `lem-coef-grothendieck-locally-presentable`, `lem-sfb-finite-upper-star-braided`, `lem-weil-pbc-sheaf-tensor-closed`, `pur713-def-coefficient-rings`, `sk-def-sfb-pulled-back-coefficients`, `sk-def-sfb-ring-object`, `sk-def-sfb-transport`.
