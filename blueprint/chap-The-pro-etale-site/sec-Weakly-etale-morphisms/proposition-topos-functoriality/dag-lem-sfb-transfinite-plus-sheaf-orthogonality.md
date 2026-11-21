+++
id = "dag-lem-sfb-transfinite-plus-sheaf-orthogonality"
kind = "dag-lemma"
title = "The transfinite plus unit is orthogonal to every sheaf"
name_showing = false
order = 39509
tags = ["sheaf-dag"]
split_from = "proposition-topos-functoriality--2"
dag_id = "lem-sfb-transfinite-plus-sheaf-orthogonality"
dag_kind = "statement"
dag_status = "unsplit"
serial = false
dag_lean = ["CategoryTheory.GrothendieckTopology.W_toTransfinitePlus_app", "CategoryTheory.GrothendieckTopology.toTransfinitePlus"]
+++
Fix a universe $\mathcal V$, a $\mathcal V$-small site $(\mathcal C,J)$ `def-weil-pbc-sites-and-cohomology`, and a Grothendieck abelian category $\mathcal A$ relative to $\mathcal V$, with $\mathcal V$-small Hom sets `def-sp-grothendieck-abelian`. For an $\mathcal A$-valued presheaf $P$, put $P^+(U)=\operatorname{colim}_{S\in J(U)^{\mathrm{op}}}M_S(P)$, where $J(U)$ is the poset of covering sieves of $U$ for the Grothendieck topology $J$ `def-weil-pbc-topos`, ordered by inclusion, and $M_S(P)$ is the limit of $P(V)$ over arrows $V\to U$ in $S$, with compatibility along arrows over $U$; its maps for sieve refinements are restriction maps. The canonical $P\to P^+$ is induced by the restriction maps from $P(U)$ to matching objects. For an infinite regular cardinal $\kappa\in\mathcal V$, form the functorial transfinite iteration $P_0=P$, $P_{\alpha+1}=P_\alpha^+$, $P_\lambda=\operatorname{colim}_{\alpha<\lambda}P_\alpha$ at nonzero limit ordinals, and $Q_\kappa(P)=\operatorname{colim}_{\alpha<\kappa}P_\alpha$, with canonical map $\eta_P:P\to Q_\kappa(P)$ `def-weil-pbc-category-colimit`. For every sheaf $F$ (meaning $U\mapsto\operatorname{Hom}_{\mathcal A}(T,F(U))$ is a sheaf of sets for every $T\in\mathcal A$), precomposition with $\eta_P$ is a bijection $\operatorname{Hom}_{\operatorname{PSh}}(Q_\kappa(P),F)\xrightarrow{\sim}\operatorname{Hom}_{\operatorname{PSh}}(P,F)$. This bijection is natural in $P$ and $F$. No claim that $Q_\kappa(P)$ is a sheaf is made.

(SHEAF DAG node `lem-sfb-transfinite-plus-sheaf-orthogonality`; machine-alignment layer.) Split from [proposition-topos-functoriality--2]. DAG kind: statement. Placed through `lem-sfb-finite-upper-star-exact` (ancestor-1). DAG status: unsplit. Statement dependencies not drawn: `def-weil-pbc-sites-and-cohomology`, `def-sp-grothendieck-abelian`, `def-weil-pbc-category-colimit`, `def-weil-pbc-topos`.
