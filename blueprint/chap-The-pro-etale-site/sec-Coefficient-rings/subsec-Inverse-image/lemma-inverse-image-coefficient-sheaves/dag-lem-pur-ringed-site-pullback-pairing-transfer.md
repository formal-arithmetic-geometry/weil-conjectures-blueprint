+++
id = "dag-lem-pur-ringed-site-pullback-pairing-transfer"
kind = "dag-lemma"
title = "Extension of module pairings along a ringed site morphism"
name_showing = false
order = 187525
tags = ["sheaf-dag"]
split_from = "lemma-inverse-image-coefficient-sheaves--2"
dag_id = "lem-pur-ringed-site-pullback-pairing-transfer"
dag_kind = "statement"
dag_status = "split"
serial = false
dag_lean = ["SheafOfModules.exists_pullback_pairing_transfer"]
uses = ["dag-def-pur-localized-ringed-site", "dag-def-pur-sheaf-hom"]
+++
Let $\mathcal C,\mathcal D$ be sites small relative to a universe $W$ [def-weil-size-convention, def-weil-pbc-sites-and-cohomology], both with finite limits. Let $U:\mathcal C\to\mathcal D$ be continuous and preserve finite limits and covering sieves. Let $R$ and $S$ be sheaves of commutative rings on the respective sites, with a morphism of underlying ring sheaves $a:R\to U_*S$. Use the module sheaf categories `def-weil-sheaf-of-modules-category`, internal sheaf Hom [dag-def-pur-sheaf-hom] and slice restriction [dag-def-pur-localized-ringed-site]. Assume that for every $V\in\mathcal C$, the slice site $\mathcal C/V$ has additive sheafification and its sheafification equivalences are exactly the locally bijective maps. Suppose the module direct image $U_*$ has a left adjoint $F$, equipped with its adjunction. Write $\eta_M:M\to U_*FM$ for its adjunction unit. For every pair of $R$-module sheaves $L,P$ and every $R$-linear $b:P\to\mathcal Hom_R(L,R)$, there exists a unique $S$-linear morphism $d:F(P)\to\mathcal Hom_S(F(L),S)$ such that for every $V\in\mathcal C$, $p\in P(V)$ and $m\in L(V)$ one has $d(\eta_P(p))(\eta_L(m))=a_V(b(p)(m))$. Evaluation on either side is over the identity object of the corresponding slice. No finite freeness or invertibility of $d$ is asserted.

(SHEAF DAG node `lem-pur-ringed-site-pullback-pairing-transfer`; machine-alignment layer.) Split from [lemma-inverse-image-coefficient-sheaves--2]. DAG kind: statement. Placed through `det-prop-sfb-cartesian-coefficients-twists` (ancestor-1). DAG status: split. Statement dependencies not drawn: `def-weil-sheaf-of-modules-category`, `def-weil-size-convention`, `sk-def-pbc-conventions`.
