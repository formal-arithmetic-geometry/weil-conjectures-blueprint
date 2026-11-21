+++
id = "dag-lem-pe-internal-section-tensor-comparison"
kind = "dag-lemma"
title = "Relative tensor and K-flatness under the internal-to-sectionwise module equivalence"
name_showing = false
order = 208504
tags = ["sheaf-dag"]
split_from = "definition-derived-adic-completeness--1"
dag_id = "lem-pe-internal-section-tensor-comparison"
dag_kind = "statement"
dag_status = "split"
serial = false
dag_lean = ["CategoryTheory.InternalAbelianSheafModule.comparison_essentiallySmall", "CategoryTheory.InternalAbelianSheafModule.comparison_sheafTensorLeft", "CategoryTheory.InternalAbelianSheafModule.comparison_sheafTensorRight", "CategoryTheory.InternalAbelianSheafModule.comparison_internalColimits", "CategoryTheory.InternalAbelianSheafModule.comparison_additive", "CategoryTheory.InternalAbelianSheafModule.comparison_internalTotalExists", "CategoryTheory.InternalAbelianSheafModule.comparison_internalTmul", "CategoryTheory.InternalAbelianSheafModule.comparison_sectionTmul", "CategoryTheory.InternalAbelianSheafModule.internal_section_tensor_comparison"]
+++
Let $C$ be a site whose objects and morphisms lie in the coefficient universe. Assume abelian sheafification exists, its local equivalences are monoidal, and the category $\mathcal A=\operatorname{Sh}(C,\operatorname{Ab})$ has the closed symmetric monoidal structure given by sheafified objectwise tensor over $\mathbf Z$ [det-def-sfb-sheaf-tensor-structure, sk-def-sfb-sheaf-tensor]. Let $R$ be a commutative ring object of $\mathcal A$, let $R_{\mathrm{sec}}$ be its reconstructed section-ring sheaf, and let
$$E_R:\operatorname{Mod}_R(\mathcal A)\simeq\operatorname{Mod}(R_{\mathrm{sec}})$$
be the equivalence of `def-weil-pbc-internal-abelian-sheaf-module-equivalence`, which leaves underlying abelian sheaves and maps unchanged. Give the source the coequalizer relative tensor `def-sfb-modobj-relative-tensor` and the target the sheafification of sectionwise balanced tensor [dag-def-pur-sheaf-tensor-product]. Then $E_R$ is exact and has natural isomorphisms
$$E_R(M\otimes_RN)\cong E_R(M)\otimes_{R_{\mathrm{sec}}}E_R(N),\qquad E_R(R)\cong R_{\mathrm{sec}},$$
characterized on local pure tensors by $m\otimes n\mapsto m\otimes n$. These comparisons respect associators, unitors and symmetry. Applied termwise to cochain complexes `def-weil-abstract-derived-category`, $E_R$ identifies the direct-sum total tensor complexes `def-pc-tensor-complex-sheaves` and preserves and reflects acyclicity, flat modules `def-pc-flat-sheaf-modules` and K-flat complexes `def-pc-kflat-complex`; in the internal category, flatness and K-flatness mean the same exact-tensor and acyclic-total-tensor tests.

(SHEAF DAG node `lem-pe-internal-section-tensor-comparison`; machine-alignment layer.) Split from [definition-derived-adic-completeness--1]. DAG kind: statement. Placed through `sk-def-pe-derived-completion` (ancestor-1). DAG status: split. Statement dependencies not drawn: `def-pc-flat-sheaf-modules`, `def-pc-kflat-complex`, `def-pc-tensor-complex-sheaves`, `def-pur-sheaf-tensor-product`, `def-sfb-modobj-relative-tensor`, `def-sfb-modobj-symmetric-tensor`, `def-weil-abstract-derived-category`, `def-weil-pbc-internal-abelian-sheaf-module-equivalence`, `det-def-sfb-ring-object`, `det-def-sfb-ring-object-rings`, `det-def-sfb-sheaf-tensor-presheaf`, `lem-sfb-modobj-symmetric-bimodules`, `pur713-def-relative-tensor`, `sk-def-sfb-ring-object`, `sk-def-sfb-sheaf-tensor`.
