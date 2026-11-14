+++
id = "dag-lem-pur-ringed-site-pullback-dual-free-chart"
kind = "dag-lemma"
title = "Invertibility of a pulled evaluation comparison on a finite-free chart"
name_showing = false
order = 187523
tags = ["sheaf-dag"]
split_from = "lemma-inverse-image-coefficient-sheaves--2"
dag_id = "lem-pur-ringed-site-pullback-dual-free-chart"
dag_kind = "statement"
dag_status = "split"
serial = false
dag_lean = ["SheafOfModules.isIso_over_pullback_dual_of_free"]
uses = ["dag-def-pur-localized-ringed-site", "dag-def-pur-sheaf-hom"]
+++
Let $\mathcal C,\mathcal D$ be sites small relative to a universe $W$ [def-weil-size-convention, def-weil-pbc-sites-and-cohomology], both with finite limits. Let $U:\mathcal C\to\mathcal D$ be continuous and preserve finite limits and covering sieves. Let $R$ and $S$ be sheaves of commutative rings on the respective sites, with a morphism of underlying ring sheaves $a:R\to U_*S$. Use the module sheaf categories `def-weil-sheaf-of-modules-category`, internal sheaf Hom [dag-def-pur-sheaf-hom] and slice restriction [dag-def-pur-localized-ringed-site]. Assume that for every $V\in\mathcal C$, the slice site $\mathcal C/V$ has additive sheafification and its sheafification equivalences are exactly the locally bijective maps. Suppose $F$ is the module left adjoint to $U_*$, with adjunction unit $\eta$. Let $L$ be an $R$-module sheaf, and let $d:F(\mathcal Hom_R(L,R))\to\mathcal Hom_S(F(L),S)$ be $S$-linear. Suppose that for all $T\in\mathcal C$, $\varphi\in\mathcal Hom_R(L,R)(T)$ and $m\in L(T)$, the equation $d(\eta(\varphi))(\eta(m))=a_T(\varphi(m))$ holds, with evaluation at the identity object of each slice. Fix $V\in\mathcal C$ and $r\in\mathbf N$ and an isomorphism $L|_V\cong(R|_V)^{\oplus r}$, with the free module indexed by the universe-$W$ lift of $\operatorname{Fin}(r)$. Then $d|_{U(V)}$ is an isomorphism of $S|_{U(V)}$-module sheaves. Neither a global covering family nor global invertibility nor naturality of a family of comparisons is asserted.

(SHEAF DAG node `lem-pur-ringed-site-pullback-dual-free-chart`; machine-alignment layer.) Split from [lemma-inverse-image-coefficient-sheaves--2]. DAG kind: statement. Placed through `det-prop-sfb-cartesian-coefficients-twists` (ancestor-1). DAG status: split. Statement dependencies not drawn: `def-weil-sheaf-of-modules-category`, `def-weil-size-convention`, `sk-def-pbc-conventions`.
