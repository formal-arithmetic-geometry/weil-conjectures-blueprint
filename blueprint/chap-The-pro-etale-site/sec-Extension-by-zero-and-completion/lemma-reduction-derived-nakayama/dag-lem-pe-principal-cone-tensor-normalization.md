+++
id = "dag-lem-pe-principal-cone-tensor-normalization"
kind = "dag-lemma"
title = "Principal scalar cones normalized against derived tensor"
name_showing = false
order = 210503
tags = ["sheaf-dag"]
split_from = "lemma-reduction-derived-nakayama--1"
dag_id = "lem-pe-principal-cone-tensor-normalization"
dag_kind = "statement"
dag_status = "split"
serial = false
dag_lean = ["AlgebraicGeometry.ProEtale.PrincipalNormalization.principal_cone_tensor_normalization"]
uses = ["dag-det-pe-derived-nakayama-resolution", "dag-lem-sfb-transfinite-plus-finite-limits", "dag-lem-sfb-transfinite-plus-sheaf-orthogonality", "dag-sk-def-pe-derived-completion"]
+++
For the coefficient categories and uniformizer endomorphism d of [dag-det-pe-derived-nakayama-resolution], with the scalar power identity on cochain complexes, there are natural isomorphisms Q Cone(d^(n+1)) ≅ Q followed by right derived tensor with the pulled-back quotient module in degree zero, for each n≥0. They take cone.map(d,id) to tensoring the specified quotientStep of [dag-sk-def-pe-derived-completion], and cone.inr to the right-unitor inverse followed by tensoring ε_Q and Q(single.map(finiteUnit)). With the standard derived tensor shifts of `def-weil-triangulated-category`, they intertwine the inverse mappingCone.shiftIso and the shift comparison of Q. This statement makes no identification with derived extension followed by restriction.

(SHEAF DAG node `lem-pe-principal-cone-tensor-normalization`; machine-alignment layer.) Split from [lemma-reduction-derived-nakayama--1]. DAG kind: statement. DAG status: split. Statement dependencies not drawn: `def-pc-flat-sheaf-modules`, `def-sfb-derived-tensor-modules`, `def-sfb-modobj-internal-hom`, `def-sfb-modobj-relative-tensor`, `def-sfb-modobj-symmetric-tensor`, `def-sfb-qlbar-coefficient-ring`, `def-sfb-torsion-stratum-coefficients`, `def-sfb-upper-star-from-point`, `def-weil-abstract-derived-category`, `def-weil-triangulated-category`, `det-def-sfb-ring-object`, `det-def-sfb-ring-object-rings`, `det-def-sfb-sheaf-tensor-presheaf`, `lem-coef-grothendieck-locally-presentable`, `lem-pc-derived-category-locally-small`, `lem-sc-derived-tensor-shift-independent-universe`, `lem-sfb-abelian-functorial-flat-resolution`, `lem-sfb-derived-monoidal`, `lem-sfb-grothendieck-k-injective`, `lem-sfb-modobj-abelian`, `lem-sfb-modobj-flat-resolutions`, `lem-sfb-modobj-grothendieck`, `lem-sfb-modobj-symmetric-bimodules`, `lem-sfb-proetale-sheaves-grothendieck`, `lem-sfb-sheaf-functorial-flat-resolution`, `lem-sfb-total-tensor-homotopy`, `lem-weil-l-adic-extension-integers-dvr`, `lem-weil-pbc-module-functorial-flat-resolution`, `lem-weil-pbc-module-relative-tensor-adjoint`, `lem-weil-pbc-sheaf-tensor-closed`, `pur713-def-coefficient-rings`, `pur713-def-relative-tensor`, `sk-def-sfb-derived-tensor-hom`, `sk-def-sfb-pulled-back-coefficients`, `sk-def-sfb-ring-object`.
