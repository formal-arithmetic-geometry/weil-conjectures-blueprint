+++
id = "dag-lem-weil-pbc-comparison-direct-image-canonical-mate"
kind = "dag-lemma"
title = "Canonical derived direct-image comparison is the invertible counit mate"
name_showing = false
order = 136501
tags = ["sheaf-dag"]
split_from = "lemma-comparison-direct-images-compatibilities--2"
dag_id = "lem-weil-pbc-comparison-direct-image-canonical-mate"
dag_kind = "statement"
dag_status = "split"
serial = false
dag_lean = ["AlgebraicGeometry.ProEtale.fixedComparisonPullbackPlus", "AlgebraicGeometry.ProEtale.fixedComparisonDirectImageMatePlus", "AlgebraicGeometry.ProEtale.isIso_fixedComparisonDirectImageMatePlus", "AlgebraicGeometry.ProEtale.fixedComparisonDirectImageMatePlus_counit"]
uses = ["dag-def-sfb-finite-lower-star", "dag-def-sfb-finite-upper-star", "dag-lem-sfb-finite-upper-star-exact", "dag-lem-sfb-transfinite-plus-finite-limits", "dag-lem-sfb-transfinite-plus-sheaf-orthogonality"]
+++
Let $\Lambda$ be a finite discrete commutative ring and $u:U\to V$ a quasi-compact, quasi-separated morphism of schemes. Work on the small etale and pro-etale sites with the constant coefficient module categories `def-weil-pbc-derived-categories`, `def-weil-pbc-proetale-modules`. Write $A_T=\nu_T^*$ for the exact derived comparison `def-weil-pbc-site-comparison-morphism`, and $l_u=u_{\Et}^{-1}$, $r_u=Ru_{\Et,*}$, $p_u=Lu_{\Proet}^*$, $s_u=Ru_{\Proet,*}$ for the canonical derived module adjoint pairs $l_u\dashv r_u$ and $p_u\dashv s_u$ `def-weil-pbc-proetale-operations`. Denote their units and counits by $\eta_u^e,\varepsilon_u^e$ and $\eta_u^p,\varepsilon_u^p$. In the constant-ring identifications `prop-weil-pbc-proetale-constant-ring-map`, let $a_u:A_Ul_u\xrightarrow{\sim}p_uA_V$ be the specified pullback comparison `lem-weil-pbc-comparison-pullback`. For $K\in\Dplus(U_{\Et},\Lambda)$ define $b_{u,K}:A_Vr_uK\to s_uA_UK$ to be the adjoint transpose `def-weil-pbc-adjunction-mate` of
$$q_{u,K}=A_U(\varepsilon^e_{u,K})\circ a_{u,r_uK}^{-1}:p_uA_Vr_uK\to A_UK.$$
Then $b_u$ is natural in $K$ and every $b_{u,K}$ is an isomorphism. It satisfies the specified normalization
$$\varepsilon^p_{u,A_UK}\circ p_u(b_{u,K})\circ a_{u,r_uK}=A_U(\varepsilon^e_{u,K}).$$
Here invertibility concerns this named morphism, not merely the existence of some isomorphism between its source and target.

(SHEAF DAG node `lem-weil-pbc-comparison-direct-image-canonical-mate`; machine-alignment layer.) Split from [lemma-comparison-direct-images-compatibilities--2]. DAG kind: statement. DAG status: split. Statement dependencies not drawn: `def-pc-flat-sheaf-modules`, `def-pc-kflat-complex`, `def-pc-module-kflat-complex`, `def-sc-field-extension`, `def-sfb-finite-derived-adjunction-plus`, `def-sfb-finite-upper-lower-star-adjunction`, `def-weil-derived-direct-image`, `def-weil-pbc-adjunction-mate`, `def-weil-pbc-derived-inverse-image`, `def-weil-pbc-direct-image`, `def-weil-pbc-inverse-image`, `det-def-sfb-sheaf-tensor-presheaf`, `lem-coef-grothendieck-locally-presentable`, `lem-pc-derived-category-locally-small`, `lem-sfb-grothendieck-k-injective`, `lem-sfb-proetale-sheaves-grothendieck`, `lem-sfb-sequential-kflat-derivability`, `lem-sfb-sheaf-functorial-flat-resolution`, `lem-sfb-total-tensor-homotopy`, `lem-sfb-unary-left-derived-calculus`, `lem-weil-pbc-direct-image-left-exact`, `lem-weil-pbc-flat-coproduct`, `lem-weil-pbc-sheaf-tensor-closed`, `lem-weil-pbc-termwise-adjunction-homotopy`, `sk-def-sfb-derived-extension-of-scalars`, `sk-def-sfb-finite-derived-functors`, `sk-def-sfb-module-derived-pushpull`, `src-right-derived-functor-plus-compatibility`.
