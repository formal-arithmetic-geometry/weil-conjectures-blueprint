+++
id = "dag-lem-poincare-integral-tate-pullback-local-line"
kind = "dag-lemma"
title = "Integral Tate modules have local bases after pullback"
name_showing = false
order = 184540
tags = ["sheaf-dag"]
split_from = "definition-tate-twists--13"
dag_id = "lem-poincare-integral-tate-pullback-local-line"
dag_kind = "statement"
dag_status = "split"
serial = false
uses = ["dag-def-sfb-finite-upper-star", "dag-lem-sfb-transfinite-plus-finite-limits", "dag-lem-sfb-transfinite-plus-sheaf-orthogonality"]
+++
Let l be a prime, X a scheme with l a unit in Gamma(X,O_X), and f:Y->X any scheme morphism. Put R_X=p_X^* continuousMapRingObj(Z_l) and T_X=lim_(r>=0) Mod.freeFunctor(R_X)(mu_(l^r)), with the l-th power transitions, exactly as in [dag-def-pur-condensed-tate-twists]. There is a pro-etale covering (u_i:V_i->Y) such that mapMod(u_i^*) mapMod(f^*) T_X is isomorphic to the regular module over u_i^*f^*R_X. Inverse image is the actual functor of [dag-def-sfb-finite-upper-star]. No finite-type, quasi-compactness or Noetherian hypothesis is imposed.

(SHEAF DAG node `lem-poincare-integral-tate-pullback-local-line`; machine-alignment layer.) Split from [definition-tate-twists--13]. DAG kind: statement. Placed through `sk-def-sp-tate-twist` (ancestor-1). DAG status: split. Lean names not on master: `AlgebraicGeometry.ProEtale.tateModule_pullback_locally_trivial`. Statement dependencies not drawn: `def-pur-condensed-tate-twists`, `def-sfb-modobj-transport`, `def-sfb-padic-condensed-ring`, `def-sfb-padic-int-condensed-ring`, `def-sfb-padic-subfield-condensed-ring`, `def-sfb-qlbar-coefficient-ring`, `def-sfb-upper-star-from-point`, `det-def-sfb-ring-object`, `det-def-sfb-ring-object-rings`, `lem-coef-grothendieck-locally-presentable`, `lem-sfb-finite-upper-star-braided`, `lem-sfb-modobj-symmetric-bimodules`, `lem-weil-pbc-sheaf-tensor-closed`, `pur713-def-coefficient-rings`, `pur713-def-relative-tensor`, `sk-def-sfb-pulled-back-coefficients`, `sk-def-sfb-ring-object`, `sk-def-sfb-transport`.
