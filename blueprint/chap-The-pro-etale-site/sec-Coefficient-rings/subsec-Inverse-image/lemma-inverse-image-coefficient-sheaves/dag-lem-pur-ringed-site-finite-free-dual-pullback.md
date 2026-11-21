+++
id = "dag-lem-pur-ringed-site-finite-free-dual-pullback"
kind = "dag-lemma"
title = "Pullback of the dual of a finite locally free module on a ringed site"
name_showing = false
order = 187521
tags = ["sheaf-dag"]
split_from = "lemma-inverse-image-coefficient-sheaves--2"
dag_id = "lem-pur-ringed-site-finite-free-dual-pullback"
dag_kind = "statement"
dag_status = "split"
serial = false
dag_lean = ["SheafOfModules.ringedSitePullbackFunctor", "SheafOfModules.ringedSitePullbackSection", "SheafOfModules.finite_free_dual_pullback"]
uses = ["dag-def-pur-localized-ringed-site", "dag-def-pur-sheaf-hom"]
+++
Let $\mathcal C,\mathcal D$ be sites small relative to the universe of sheaves [def-weil-size-convention, def-weil-pbc-sites-and-cohomology], with finite limits, and let $u:\mathcal C\to\mathcal D$ preserve finite limits and coverings. Let $f^{-1}:\operatorname{Sh}(\mathcal C)\to\operatorname{Sh}(\mathcal D)$ be the associated geometric inverse image `lem-weil-pbc-left-exact-site-inverse-image-tensor`. Let $R$ on $\mathcal C$ and $S$ on $\mathcal D$ be sheaves of commutative rings, with a ring map $c:f^{-1}R\to S$. For an $R$-module sheaf $N$ `def-weil-sheaf-of-modules-category` put $f^*N=S\otimes_{f^{-1}R}f^{-1}N$, with sheaf tensor product [dag-def-pur-sheaf-tensor-product]. Let $L$ be an $R$-module sheaf that is finite locally free, meaning that there is a covering $\{V_i\to1_{\mathcal C}\}$ and integers $r_i\ge0$ with $L|_{V_i}\cong(R|_{V_i})^{\oplus r_i}$ on the localized sites [dag-def-pur-localized-ringed-site]. Write $L^\vee=\mathcal Hom_R(L,R)$, using sheaf Hom [dag-def-pur-sheaf-hom]. The canonical $S$-linear map
$$\delta_{f,L}:f^*(L^\vee)\longrightarrow\mathcal Hom_S(f^*L,S),$$
obtained from the pullback of the evaluation pairing $L^\vee\otimes_R L\to R$, the relative tensor comparison `lem-weil-pbc-ringed-topoi-module-pullback-tensor`, and $f^*R\cong S$, is an isomorphism. It is natural contravariantly in $L$. On a pulled-back local basis $e_1,\ldots,e_{r_i}$ it sends the pulled-back dual basis functional $e_j^\vee$ to the functional taking $f^*e_k$ to $\delta_{jk}\cdot1_S$. No flatness assumption on $c$ is required.

(SHEAF DAG node `lem-pur-ringed-site-finite-free-dual-pullback`; machine-alignment layer.) Split from [lemma-inverse-image-coefficient-sheaves--2]. DAG kind: statement. Placed through `det-prop-sfb-cartesian-coefficients-twists` (ancestor-1). DAG status: split. Statement dependencies not drawn: `def-weil-sheaf-of-modules-category`, `def-weil-size-convention`, `sk-def-pbc-conventions`.
