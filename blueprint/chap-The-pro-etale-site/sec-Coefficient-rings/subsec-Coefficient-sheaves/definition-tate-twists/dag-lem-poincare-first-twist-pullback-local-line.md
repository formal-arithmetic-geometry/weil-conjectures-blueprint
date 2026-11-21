+++
id = "dag-lem-poincare-first-twist-pullback-local-line"
kind = "dag-lemma"
title = "The first rational Tate twist has local bases after pullback"
name_showing = false
order = 184536
tags = ["sheaf-dag"]
split_from = "definition-tate-twists--13"
dag_id = "lem-poincare-first-twist-pullback-local-line"
dag_kind = "statement"
dag_status = "split"
serial = false
uses = ["dag-def-sfb-finite-upper-star", "dag-lem-sfb-transfinite-plus-finite-limits", "dag-lem-sfb-transfinite-plus-sheaf-orthogonality"]
+++
Let l be a prime, X a scheme with l invertible in Gamma(X,O_X), and f:Y->X arbitrary. Let B_X=p_X^*padicAlgClRingObj(l) and let L_X=tateTwistOne X l be the scalar extension of the actual integral inverse-limit module [dag-def-pur-condensed-tate-twists]. There is a pro-etale covering (u_i:V_i->Y) on which mapMod(u_i^*) mapMod(f^*) L_X is isomorphic to the regular module over u_i^*f^*B_X [dag-def-sfb-finite-upper-star].

(SHEAF DAG node `lem-poincare-first-twist-pullback-local-line`; machine-alignment layer.) Split from [definition-tate-twists--13]. DAG kind: statement. Placed through `sk-def-sp-tate-twist` (ancestor-1). DAG status: split. Lean names not on master: `AlgebraicGeometry.ProEtale.tateTwistOne_pullback_locally_trivial`. Statement dependencies not drawn: `def-pur-condensed-tate-twists`, `def-sfb-modobj-transport`, `def-sfb-qlbar-coefficient-ring`, `def-sfb-upper-star-from-point`, `det-def-sfb-ring-object`, `det-def-sfb-ring-object-rings`, `lem-coef-grothendieck-locally-presentable`, `lem-sfb-finite-upper-star-braided`, `lem-sfb-modobj-symmetric-bimodules`, `lem-weil-pbc-sheaf-tensor-closed`, `pur713-def-coefficient-rings`, `pur713-def-relative-tensor`, `sk-def-sfb-pulled-back-coefficients`, `sk-def-sfb-qlbar-condensed`, `sk-def-sfb-ring-object`, `sk-def-sfb-transport`.
