+++
id = "dag-lem-poincare-integral-tate-local-basis"
kind = "dag-lemma"
title = "Integral Tate modules have pro-etale local bases"
name_showing = false
order = 184539
tags = ["sheaf-dag"]
split_from = "definition-tate-twists--13"
dag_id = "lem-poincare-integral-tate-local-basis"
dag_kind = "statement"
dag_status = "split"
serial = false
dag_lean = ["AlgebraicGeometry.ProEtale.tateModule_locally_trivial"]
uses = ["dag-def-sfb-finite-upper-star", "dag-lem-sfb-transfinite-plus-finite-limits", "dag-lem-sfb-transfinite-plus-sheaf-orthogonality"]
+++
Let l be a prime and X any scheme with l invertible in Gamma(X,O_X). Let R_X=p_X^*continuousMapRingObj(Z_l) and let T_X=tateModule X l be exactly the inverse limit of the internal free root modules with power transitions of [dag-def-pur-condensed-tate-twists]. There is a pro-etale covering (u_i:U_i->X) such that mapMod(u_i^*) T_X is isomorphic to the regular module over u_i^*R_X [dag-def-sfb-finite-upper-star]. No quasi-compactness, separation or finiteness assumption is imposed on X.

(SHEAF DAG node `lem-poincare-integral-tate-local-basis`; machine-alignment layer.) Split from [definition-tate-twists--13]. DAG kind: statement. Placed through `sk-def-sp-tate-twist` (ancestor-1). DAG status: split. Statement dependencies not drawn: `def-pur-condensed-tate-twists`, `def-sfb-modobj-transport`, `def-sfb-padic-condensed-ring`, `def-sfb-padic-int-condensed-ring`, `def-sfb-padic-subfield-condensed-ring`, `def-sfb-qlbar-coefficient-ring`, `def-sfb-upper-star-from-point`, `det-def-sfb-ring-object`, `det-def-sfb-ring-object-rings`, `lem-coef-grothendieck-locally-presentable`, `lem-sfb-finite-upper-star-braided`, `lem-sfb-modobj-symmetric-bimodules`, `lem-weil-pbc-sheaf-tensor-closed`, `pur713-def-coefficient-rings`, `pur713-def-relative-tensor`, `sk-def-sfb-pulled-back-coefficients`, `sk-def-sfb-ring-object`, `sk-def-sfb-transport`.
