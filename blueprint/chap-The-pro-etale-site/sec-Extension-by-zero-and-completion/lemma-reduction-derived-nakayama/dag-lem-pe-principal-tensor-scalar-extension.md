+++
id = "dag-lem-pe-principal-tensor-scalar-extension"
kind = "dag-lemma"
title = "Natural tensor identification with the canonical scalar-extension tower"
name_showing = false
order = 210512
tags = ["sheaf-dag"]
split_from = "lemma-reduction-derived-nakayama--2"
dag_id = "lem-pe-principal-tensor-scalar-extension"
dag_kind = "statement"
dag_status = "split"
serial = false
dag_lean = ["AlgebraicGeometry.ProEtale.PrincipalNormalization.principal_tensor_scalar_extension"]
uses = ["dag-lem-sfb-transfinite-plus-finite-limits", "dag-lem-sfb-transfinite-plus-sheaf-orthogonality", "dag-sk-def-pe-derived-completion"]
+++
For the native internal coefficient modules of [dag-det-pe-derived-nakayama-resolution] and the actual quotient maps and adjunctions of [dag-sk-def-pe-derived-completion], the derived right tensor functor with the pulled-back quotient module at exponent n+1 is naturally isomorphic to derived extension along the quotient followed by exact restriction. The isomorphisms intertwine tensoring quotientStep with integralStep, and the right-unitor inverse followed by tensoring ε_Q and Q(single.map(finiteUnit)) with the actual derived scalar-extension adjunction unit. No scalar cone or cone-shift normalization is asserted.

(SHEAF DAG node `lem-pe-principal-tensor-scalar-extension`; machine-alignment layer.) Split from [lemma-reduction-derived-nakayama--2]. DAG kind: statement. Placed through `det-pe-derived-nakayama-first-reduction` (ancestor-1). DAG status: split. Statement dependencies not drawn: `def-pc-flat-sheaf-modules`, `def-sfb-derived-extend-levelwise-adjunction`, `def-sfb-derived-tensor-modules`, `def-sfb-integers-to-subfield-point`, `def-sfb-modobj-extension`, `def-sfb-modobj-internal-hom`, `def-sfb-modobj-relative-tensor`, `def-sfb-modobj-symmetric-tensor`, `def-sfb-qlbar-coefficient-ring`, `def-sfb-torsion-stratum-coefficients`, `def-sfb-upper-star-from-point`, `det-def-sfb-ring-object`, `det-def-sfb-ring-object-rings`, `det-def-sfb-sheaf-tensor-presheaf`, `det-pe-derived-nakayama-resolution`, `lem-coef-grothendieck-locally-presentable`, `lem-pc-derived-category-locally-small`, `lem-sfb-abelian-functorial-flat-resolution`, `lem-sfb-extend-scalars-kflat`, `lem-sfb-grothendieck-k-injective`, `lem-sfb-modobj-abelian`, `lem-sfb-modobj-flat-resolutions`, `lem-sfb-modobj-forget-creates`, `lem-sfb-modobj-grothendieck`, `lem-sfb-modobj-symmetric-bimodules`, `lem-sfb-proetale-sheaves-grothendieck`, `lem-sfb-sheaf-functorial-flat-resolution`, `lem-weil-pbc-module-functorial-flat-resolution`, `lem-weil-pbc-module-relative-tensor-adjoint`, `lem-weil-pbc-sheaf-tensor-closed`, `pur713-def-coefficient-rings`, `pur713-def-relative-tensor`, `sk-def-sfb-change-of-scalars`, `sk-def-sfb-derived-extension-of-scalars`, `sk-def-sfb-derived-tensor-hom`, `sk-def-sfb-finite-derived-functors`, `sk-def-sfb-module-derived-pushpull`, `sk-def-sfb-pulled-back-coefficients`, `sk-def-sfb-ring-object`.
