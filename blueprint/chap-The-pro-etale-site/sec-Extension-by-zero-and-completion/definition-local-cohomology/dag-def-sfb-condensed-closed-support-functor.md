+++
id = "dag-def-sfb-condensed-closed-support-functor"
kind = "dag-definition"
title = "Canonical closed-support kernel functor for condensed module sheaves"
name_showing = false
order = 204501
tags = ["sheaf-dag"]
split_from = "definition-local-cohomology--1"
dag_id = "def-sfb-condensed-closed-support-functor"
dag_kind = "definition"
dag_status = "split"
serial = false
dag_lean = ["AlgebraicGeometry.ProEtale.CondensedRing.supportModules", "AlgebraicGeometry.ProEtale.CondensedRing.supportModules_grothendieck", "AlgebraicGeometry.ProEtale.CondensedRing.supportPullback", "AlgebraicGeometry.ProEtale.CondensedRing.supportPullback_additive", "AlgebraicGeometry.ProEtale.CondensedRing.supportKernel", "AlgebraicGeometry.ProEtale.CondensedRing.supportKernelι", "AlgebraicGeometry.ProEtale.CondensedRing.closedSupport", "AlgebraicGeometry.ProEtale.CondensedRing.closedSupport_additive"]
uses = ["dag-def-weil-pbc-proetale-site", "dag-lem-sfb-transfinite-plus-finite-limits", "dag-lem-sfb-transfinite-plus-sheaf-orthogonality"]
+++
Let $\Lambda$ be a condensed ring, not necessarily commutative `sk-def-sfb-condensed-ring`. For each scheme $S$ `def-pc-scheme`, put $\Lambda_S=p_S^*\Lambda$ `sk-def-sfb-pulled-back-coefficients` and $\mathcal M_S=\operatorname{Mod}_{\Lambda_S}(\operatorname{Sh}(S_{\mathrm{pro\acute et}},\mathrm{Ab}))$ `sk-def-sfb-module-objects` [dag-def-weil-pbc-proetale-site]. For a scheme morphism $f:S\to T$, use the abelian-sheaf inverse and direct images `def-weil-proetale-inverse-image`, their transport to module objects `sk-def-sfb-transport`, and the canonical coefficient isomorphism $\alpha_f:f^*\Lambda_T\simeq\Lambda_S$ and its mate $\eta_f:\Lambda_T\to f_*\Lambda_S$ [dag-sk-def-sfb-coefficient-morphisms]. Define module inverse image by transporting along $f^*$ and restricting scalars along $\alpha_f^{-1}$, and module direct image by transporting along $f_*$ and restricting along $\eta_f$, using `sk-def-sfb-change-of-scalars`. Write $u_j:\mathrm{id}\to j_*j^*$ for the unit of their canonical module adjunction. For arbitrary scheme morphisms $i:Z\to X$ and $j:U\to X$, define $K_j(M)=\ker(u_{j,M}:M\to j_*j^*M)$ in $\mathcal M_X$, its natural inclusion $\kappa_M:K_j(M)\to M$, and the additive functor
$$\Gamma_{i,j}:\mathcal M_X\longrightarrow\mathcal M_Z,\qquad \Gamma_{i,j}(M)=i^*K_j(M).$$
On a module map $a:M\to N$, $K_j(a)$ is the unique kernel map satisfying $\kappa_N\circ K_j(a)=a\circ\kappa_M$, using naturality of $u_j$, and $\Gamma_{i,j}(a)=i^*K_j(a)$. In particular, for a closed immersion $i$ `def-weil-closed-immersion` with complementary open immersion $j$ `def-weil-open-immersion`, this defines the closed-support functor $\Gamma_Z(M)=i^*\ker(M\to j_*j^*M)$. The definition uses the actual unit and kernel, with no exceptional adjunction or derived identification chosen as data.

(SHEAF DAG node `def-sfb-condensed-closed-support-functor`; machine-alignment layer.) Split from [definition-local-cohomology--1]. DAG kind: definition. DAG status: split. Statement dependencies not drawn: `def-pc-scheme`, `def-sfb-qlbar-coefficient-ring`, `def-sfb-upper-star-from-point`, `def-weil-closed-immersion`, `def-weil-open-immersion`, `det-def-sfb-ring-object`, `det-def-sfb-ring-object-rings`, `det-def-sfb-sheaf-tensor-presheaf`, `lem-coef-grothendieck-locally-presentable`, `lem-sfb-modobj-abelian`, `lem-sfb-modobj-grothendieck`, `lem-weil-pbc-sheaf-tensor-closed`, `pur713-def-coefficient-rings`, `sk-def-sfb-module-objects`, `sk-def-sfb-pulled-back-coefficients`, `sk-def-sfb-ring-object`.
