+++
id = "dag-det-lem-formal-closed-support-adjunction"
kind = "dag-lemma"
title = "Sections with closed support: adjunction and fiber triangle for all coefficients"
name_showing = false
order = 204502
tags = ["sheaf-dag"]
split_from = "definition-local-cohomology--1"
dag_id = "det-lem-formal-closed-support-adjunction"
dag_kind = "statement"
dag_status = "split"
serial = false
dag_lean = ["AlgebraicGeometry.ProEtale.CondensedRing.supportModules", "AlgebraicGeometry.ProEtale.CondensedRing.supportModules_grothendieck", "AlgebraicGeometry.ProEtale.CondensedRing.supportPullback", "AlgebraicGeometry.ProEtale.CondensedRing.supportPullback_additive", "AlgebraicGeometry.ProEtale.CondensedRing.supportPullback_leftExact", "AlgebraicGeometry.ProEtale.CondensedRing.supportPullback_rightExact", "AlgebraicGeometry.ProEtale.CondensedRing.supportCoefficientEquivalence", "AlgebraicGeometry.ProEtale.CondensedRing.supportPullbackAdjunction", "AlgebraicGeometry.ProEtale.CondensedRing.supportKernel", "AlgebraicGeometry.ProEtale.CondensedRing.supportKernelι", "AlgebraicGeometry.ProEtale.CondensedRing.closedSupport", "AlgebraicGeometry.ProEtale.CondensedRing.closedSupport_additive", "AlgebraicGeometry.ProEtale.CondensedRing.closedSupportKernelComparison", "AlgebraicGeometry.ProEtale.CondensedRing.closedSupportKernelComparison_isIso", "AlgebraicGeometry.ProEtale.CondensedRing.closedSupportCounit", "AlgebraicGeometry.ProEtale.CondensedRing.existsUnique_closedSupportAdjunction", "AlgebraicGeometry.ProEtale.CondensedRing.closedSupportAdjunction", "AlgebraicGeometry.ProEtale.CondensedRing.closedSupport_leftExact", "AlgebraicGeometry.ProEtale.CondensedRing.closedSupport_lowerStarExact", "AlgebraicGeometry.ProEtale.CondensedRing.closedSupportDerivedAdjunction", "AlgebraicGeometry.ProEtale.CondensedRing.closedSupportOpenDerivedAdjunction", "AlgebraicGeometry.ProEtale.CondensedRing.closedSupport_open_isKInjective", "AlgebraicGeometry.ProEtale.CondensedRing.closedSupport_globalRHom", "AlgebraicGeometry.ProEtale.CondensedRing.closedSupport_injective_unit_epi", "AlgebraicGeometry.ProEtale.CondensedRing.closedSupport_triangle", "AlgebraicGeometry.ProEtale.CondensedRing.closedSupport_fiber"]
uses = ["dag-def-sfb-finite-upper-star", "dag-def-weil-pbc-proetale-site", "dag-lem-sfb-transfinite-plus-finite-limits", "dag-lem-sfb-transfinite-plus-sheaf-orthogonality"]
+++
Let $\Lambda$ be a condensed ring (in particular any admissible one), $i\colon Z\hookrightarrow X$
a closed immersion with quasi-compact open complement $j\colon V\hookrightarrow X$, and
$\underline\Gamma_Z(M)=i^*\ker(M\to j_*j^*M)$ for $\Lambda_X$-modules $M$
(as in `def-exc-proetale-sections-with-support`, with $\Lambda$ in place of a finite ring).

1. $\ker(M\to j_*j^*M)=i_*\underline\Gamma_Z(M)$, and $\underline\Gamma_Z$ is right adjoint to
   $i_*$ on module sheaves; it is left exact.
2. $R\underline\Gamma_Z$, computed on K-injective complexes, is right adjoint to $i_*$ on
   $D(-_{\mathrm{proét}},\Lambda)$; equivalently
   $R\operatorname{Hom}_X(i_*A,K)\cong R\operatorname{Hom}_Z(A,R\underline\Gamma_ZK)$.
3. For an injective $\Lambda_X$-module $I$, the unit $I\to j_*j^*I$ is surjective.
4. There is a distinguished triangle
   $i_*R\underline\Gamma_ZK\to K\to Rj_*j^*K\to i_*R\underline\Gamma_ZK[1]$, natural in $K$, and
   $R\underline\Gamma_ZK\cong i^*\fib(K\to Rj_*j^*K)$.

(SHEAF DAG node `det-lem-formal-closed-support-adjunction`; machine-alignment layer.) Split from [definition-local-cohomology--1]. DAG kind: statement. DAG status: split. Lean names not on master: `AlgebraicGeometry.ProEtale.CondensedRing.closedSupport_recordedDerived`, `AlgebraicGeometry.ProEtale.CondensedRing.closedSupportComputedOnKInjective`. Statement dependencies not drawn: `def-sfb-module-lower-star`, `def-sfb-qlbar-coefficient-ring`, `def-sfb-upper-star-from-point`, `def-sp-injective-resolutions`, `def-weil-abstract-derived-category`, `def-weil-closed-immersion`, `def-weil-derived-direct-image`, `def-weil-finite-type-morphism`, `def-weil-open-immersion`, `def-weil-sheaf-of-modules-category`, `def-weil-size-convention`, `def-weil-triangulated-category`, `det-def-sfb-ring-object`, `det-def-sfb-ring-object-rings`, `det-def-sfb-sheaf-tensor-presheaf`, `lem-coef-grothendieck-locally-presentable`, `lem-pc-derived-category-locally-small`, `lem-sfb-finite-upper-star-braided`, `lem-sfb-grothendieck-k-injective`, `lem-sfb-modobj-abelian`, `lem-sfb-modobj-grothendieck`, `lem-weil-pbc-sheaf-tensor-closed`, `pur713-def-coefficient-rings`, `sk-def-sfb-finite-derived-functors`, `sk-def-sfb-module-derived-pushpull`, `sk-def-sfb-module-pushforward-pullback`, `sk-def-sfb-pulled-back-coefficients`, `sk-def-sfb-ring-object`.
