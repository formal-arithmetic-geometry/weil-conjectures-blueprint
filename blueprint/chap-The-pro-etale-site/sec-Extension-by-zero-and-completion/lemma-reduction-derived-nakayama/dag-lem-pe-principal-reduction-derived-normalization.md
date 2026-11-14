+++
id = "dag-lem-pe-principal-reduction-derived-normalization"
kind = "dag-lemma"
title = "Normalized comparison of principal scalar cones with canonical derived quotients"
name_showing = false
order = 210511
tags = ["sheaf-dag"]
split_from = "lemma-reduction-derived-nakayama--2"
dag_id = "lem-pe-principal-reduction-derived-normalization"
dag_kind = "statement"
dag_status = "split"
serial = false
dag_lean = ["AlgebraicGeometry.ProEtale.PrincipalNormalization.derived_principal_normalization"]
uses = ["dag-lem-sfb-transfinite-plus-finite-limits", "dag-lem-sfb-transfinite-plus-sheaf-orthogonality", "dag-sk-def-pe-derived-completion"]
+++
Let l be prime, let E/Q_l be finite, and let X be any scheme, with the pulled-back integral coefficient ring R and canonical quotient maps of [dag-sk-def-pe-derived-completion]. Let d be an endomorphism of the regular condensed integral module whose section formula is multiplication by the specified uniformizer. Write a_n(M) for its (n+1)-st power acting on an unbounded complex M and suppose a_(n+1)(M)=d_M followed by a_n(M). Then the standard scalar-cone functors Q Cone(a_n) admit natural isomorphisms to canonical derived coefficient extension at level n+1 followed by exact restriction to R. They send the cone transition (d,id) to integralStep and the cone inclusion to the actual derived scalar-extension adjunction unit. There are coherent shifts on the latter derived functors for which these isomorphisms commute with the inverse standard mappingCone.shiftIso at every integer shift. With these shifts the functors are additive and triangulated. All comparisons refer to the existing functors and adjunctions, without changing any coefficient objects.

(SHEAF DAG node `lem-pe-principal-reduction-derived-normalization`; machine-alignment layer.) Split from [lemma-reduction-derived-nakayama--2]. DAG kind: statement. Placed through `det-pe-derived-nakayama-first-reduction` (ancestor-1). DAG status: split. Statement dependencies not drawn: `def-pc-flat-sheaf-modules`, `def-sfb-derived-extend-levelwise-adjunction`, `def-sfb-integers-to-subfield-point`, `def-sfb-modobj-extension`, `def-sfb-modobj-internal-hom`, `def-sfb-modobj-relative-tensor`, `def-sfb-modobj-symmetric-tensor`, `def-sfb-qlbar-coefficient-ring`, `def-sfb-torsion-stratum-coefficients`, `def-sfb-upper-star-from-point`, `def-weil-abstract-derived-category`, `det-def-sfb-ring-object`, `det-def-sfb-ring-object-rings`, `det-def-sfb-sheaf-tensor-presheaf`, `det-pe-derived-nakayama-resolution`, `lem-coef-grothendieck-locally-presentable`, `lem-pc-derived-category-locally-small`, `lem-sfb-abelian-functorial-flat-resolution`, `lem-sfb-extend-scalars-kflat`, `lem-sfb-grothendieck-k-injective`, `lem-sfb-modobj-abelian`, `lem-sfb-modobj-flat-resolutions`, `lem-sfb-modobj-forget-creates`, `lem-sfb-modobj-grothendieck`, `lem-sfb-modobj-symmetric-bimodules`, `lem-sfb-proetale-sheaves-grothendieck`, `lem-sfb-sheaf-functorial-flat-resolution`, `lem-weil-l-adic-extension-integers-dvr`, `lem-weil-pbc-module-functorial-flat-resolution`, `lem-weil-pbc-module-relative-tensor-adjoint`, `lem-weil-pbc-sheaf-tensor-closed`, `pur713-def-coefficient-rings`, `pur713-def-relative-tensor`, `sk-def-sfb-change-of-scalars`, `sk-def-sfb-derived-extension-of-scalars`, `sk-def-sfb-finite-derived-functors`, `sk-def-sfb-module-derived-pushpull`, `sk-def-sfb-pulled-back-coefficients`, `sk-def-sfb-ring-object`.
