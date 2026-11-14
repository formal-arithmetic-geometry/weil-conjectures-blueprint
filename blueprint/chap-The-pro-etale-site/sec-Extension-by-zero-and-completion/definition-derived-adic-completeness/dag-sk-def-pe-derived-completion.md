+++
id = "dag-sk-def-pe-derived-completion"
kind = "dag-definition"
title = "Derived adic completeness"
name_showing = false
order = 208507
tags = ["sheaf-dag"]
split_from = "definition-derived-adic-completeness--1"
dag_id = "sk-def-pe-derived-completion"
dag_kind = "definition"
dag_status = "split"
serial = false
dag_lean = ["AlgebraicGeometry.ProEtale.IsDerivedComplete", "AlgebraicGeometry.ProEtale.AdicCompletion.ring", "AlgebraicGeometry.ProEtale.AdicCompletion.Modules", "AlgebraicGeometry.ProEtale.AdicCompletion.finiteRing", "AlgebraicGeometry.ProEtale.AdicCompletion.quotientRing_isCommMonObj", "AlgebraicGeometry.ProEtale.AdicCompletion.quotient", "AlgebraicGeometry.ProEtale.AdicCompletion.finiteTopology", "AlgebraicGeometry.ProEtale.AdicCompletion.continuous_transition", "AlgebraicGeometry.ProEtale.AdicCompletion.transitionRingSheaf", "AlgebraicGeometry.ProEtale.AdicCompletion.transitionRing", "AlgebraicGeometry.ProEtale.AdicCompletion.transition", "AlgebraicGeometry.ProEtale.AdicCompletion.transition_isMonHom", "AlgebraicGeometry.ProEtale.AdicCompletion.coefficient_linearity", "AlgebraicGeometry.ProEtale.AdicCompletion.quotientUnit", "AlgebraicGeometry.ProEtale.AdicCompletion.quotientStep", "AlgebraicGeometry.ProEtale.AdicCompletion.finiteModule", "AlgebraicGeometry.ProEtale.AdicCompletion.finiteUnit", "AlgebraicGeometry.ProEtale.AdicCompletion.level", "AlgebraicGeometry.ProEtale.AdicCompletion.levelStep", "AlgebraicGeometry.ProEtale.AdicCompletion.levelUnit", "AlgebraicGeometry.ProEtale.AdicCompletion.product", "AlgebraicGeometry.ProEtale.AdicCompletion.oneSubShift", "AlgebraicGeometry.ProEtale.AdicCompletion.roosX", "AlgebraicGeometry.ProEtale.AdicCompletion.roosD", "AlgebraicGeometry.ProEtale.AdicCompletion.roosD_sq", "AlgebraicGeometry.ProEtale.AdicCompletion.roos", "AlgebraicGeometry.ProEtale.AdicCompletion.unitProduct", "AlgebraicGeometry.ProEtale.AdicCompletion.augmentation_comm", "AlgebraicGeometry.ProEtale.AdicCompletion.augmentation", "AlgebraicGeometry.ProEtale.AdicCompletion.quotient_transition", "AlgebraicGeometry.ProEtale.AdicCompletion.FiniteDerived", "AlgebraicGeometry.ProEtale.AdicCompletion.derivedReduction", "AlgebraicGeometry.ProEtale.AdicCompletion.restrict", "AlgebraicGeometry.ProEtale.AdicCompletion.finiteExtend", "AlgebraicGeometry.ProEtale.AdicCompletion.finiteRestrict", "AlgebraicGeometry.ProEtale.AdicCompletion.restrictComp", "AlgebraicGeometry.ProEtale.AdicCompletion.reductionComp", "AlgebraicGeometry.ProEtale.AdicCompletion.derivedStep", "AlgebraicGeometry.ProEtale.AdicCompletion.completionMap", "AlgebraicGeometry.ProEtale.AdicCompletion.isDerivedComplete_iff", "AlgebraicGeometry.ProEtale.AdicCompletion.integralLevel", "AlgebraicGeometry.ProEtale.AdicCompletion.integralStep", "AlgebraicGeometry.ProEtale.AdicCompletion.derivedTower", "AlgebraicGeometry.ProEtale.AdicCompletion.reductionUnit_compatible", "AlgebraicGeometry.ProEtale.AdicCompletion.roos_isDerivedLimit", "AlgebraicGeometry.ProEtale.AdicCompletion.adjunctionAssociation", "AlgebraicGeometry.ProEtale.AdicCompletion.roosMap", "AlgebraicGeometry.ProEtale.AdicCompletion.productMap", "AlgebraicGeometry.ProEtale.AdicCompletion.roosMap_comm"]
uses = ["dag-lem-sfb-transfinite-plus-finite-limits", "dag-lem-sfb-transfinite-plus-sheaf-orthogonality"]
+++
Let $E/\Ql$ be finite, with uniformizer $\pi_E$, and let
$\mathcal O_{E,X}=p_X^*\underline{\mathcal O_E}$ and $(\mathcal O_E/\pi_E^n)_X$ be
the integral and finite coefficient sheaves of
`sk-def-sfb-pulled-back-coefficients`. A complex
$K\in D(X_{\Proet},\mathcal O_E)$ is *derived complete* if its canonical map

$$
K\longrightarrow R\varprojlim_n\bigl(K\otimes^{\mathbf L}_{\mathcal O_{E,X}}(\mathcal O_E/\pi_E^n)_X\bigr)
$$

is an isomorphism. For
$K_n=K\otimes^{\mathbf L}_{\mathcal O_{E,X}}(\mathcal O_E/\pi_E^n)_X$, the canonical
transitions satisfy the derived reduction identities
$K_{n+1}\otimes^{\mathbf L}_{(\mathcal O_E/\pi_E^{n+1})_X}(\mathcal O_E/\pi_E^n)_X\simeq K_n$;
a compatible tower with these identities is called *normalized*.

Normalization is a property of the complexes $K_n$; their cohomology sheaves
$H^q(K_n)$ need not form a normalized tower under the ordinary tensor product.

(SHEAF DAG node `sk-def-pe-derived-completion`; machine-alignment layer.) Split from [definition-derived-adic-completeness--1]. DAG kind: definition. DAG status: split. Lean names not on master: `AlgebraicGeometry.ProEtale.AdicCompletion.IsNormalized`, `AlgebraicGeometry.ProEtale.AdicCompletion.derivedReduction_isNormalized`. Statement dependencies not drawn: `def-pc-flat-sheaf-modules`, `def-pc-kflat-complex`, `def-pc-module-kflat-complex`, `def-sfb-derived-extend-levelwise-adjunction`, `def-sfb-integers-to-subfield-point`, `def-sfb-modobj-extension`, `def-sfb-modobj-internal-hom`, `def-sfb-modobj-relative-tensor`, `def-sfb-modobj-symmetric-tensor`, `def-sfb-qlbar-coefficient-ring`, `def-sfb-torsion-stratum-coefficients`, `def-sfb-upper-star-from-point`, `def-weil-derived-limit`, `def-weil-inverse-system`, `det-def-sfb-ring-object`, `det-def-sfb-ring-object-rings`, `det-def-sfb-sheaf-tensor-presheaf`, `det-pe-derived-nakayama-resolution`, `lem-coef-grothendieck-locally-presentable`, `lem-pc-derived-category-locally-small`, `lem-sfb-abelian-functorial-flat-resolution`, `lem-sfb-extend-scalars-kflat`, `lem-sfb-grothendieck-k-injective`, `lem-sfb-modobj-abelian`, `lem-sfb-modobj-flat-resolutions`, `lem-sfb-modobj-forget-creates`, `lem-sfb-modobj-grothendieck`, `lem-sfb-modobj-symmetric-bimodules`, `lem-sfb-proetale-sheaves-grothendieck`, `lem-sfb-sheaf-functorial-flat-resolution`, `lem-weil-l-adic-extension-integers-dvr`, `lem-weil-pbc-module-functorial-flat-resolution`, `lem-weil-pbc-module-relative-tensor-adjoint`, `lem-weil-pbc-sheaf-tensor-closed`, `pur713-def-coefficient-rings`, `pur713-def-relative-tensor`, `sk-def-sfb-change-of-scalars`, `sk-def-sfb-derived-extension-of-scalars`, `sk-def-sfb-finite-derived-functors`, `sk-def-sfb-module-derived-pushpull`, `sk-def-sfb-pulled-back-coefficients`, `sk-def-sfb-ring-object`.
