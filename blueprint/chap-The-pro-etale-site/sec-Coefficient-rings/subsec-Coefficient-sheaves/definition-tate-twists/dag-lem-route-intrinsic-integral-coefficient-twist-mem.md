+++
id = "dag-lem-route-intrinsic-integral-coefficient-twist-mem"
kind = "dag-lemma"
title = "The existing signed completed root line is intrinsically constructible and complete."
name_showing = false
order = 184530
tags = ["sheaf-dag"]
split_from = "definition-tate-twists--1"
dag_id = "lem-route-intrinsic-integral-coefficient-twist-mem"
dag_kind = "statement"
dag_status = "split"
serial = false
dag_lean = ["WeilConjectures.intrinsicIntegralCoefficientTwist_mem"]
uses = ["dag-def-pur-twist-sheaves", "dag-def-pur-sheaf-tensor-product", "dag-def-pur-sheaf-hom"]
+++
Fix a finite-field datum $D$ of characteristic $p$ `def-weil-finite-field-fiber`, a prime $\ell\ne p$, a finite extension $E/\mathbf Q_\ell$ with valuation ring $\mathcal O_E$ and chosen uniformizer $\varpi_E$ `def-weil-l-adic-coefficient-extension`, and any scheme $W$ on which $\ell$ is invertible in every residue field. Write $A_n=\mathcal O_E/\varpi_E^n$ for $n\ge1$, and $R=\widehat{\mathcal O}_{E,W}=\varprojlim_n(A_n)_W$ for the completed coefficient sheaf on the small pro-etale site `def-weil-completed-integral-coefficients`. Let $L=\mathcal O_E(1)_W$ be the concrete completed integral root module of [dag-def-pur-twist-sheaves]. Using sheaf tensor and sheaf Hom [def-pur-sheaf-tensor-product, def-pur-sheaf-hom], put
$$
L_m=\begin{cases}R,&m=0,\\ L^{\otimes_R m},&m>0,\\ \mathcal Hom_R(L^{\otimes_R(-m)},R),&m<0.\end{cases}
$$
For every $m\in\mathbf Z$, the degree-zero derived object $K_m=L_m[0]$ belongs to the intrinsic bounded constructible derived-complete integral category `def-weil-derived-complete-integral-detailed`. In other words, its canonical derived reduction tower is derived complete `def-weil-derived-complete`, and there exist $a\le b$ such that every derived reduction $K_m\otimes_R^L(A_n)_W$ is finite-torsion constructible `def-weil-finite-torsion-constructibility` with cohomological support `def-weil-cohomological-support` contained in $[a,b]$, independently of $n$. Here one can take $a=b=0$. This is precisely $\operatorname{sfIntegralConstructible}(\ell,E,W)(K_m)$ for the published object $\operatorname{integralCoefficientTwist}(D,\ell,E,W,m)$; $D$ supplies the auxiliary parameter of that construction and imposes no structure morphism on $W$.

(SHEAF DAG node `lem-route-intrinsic-integral-coefficient-twist-mem`; machine-alignment layer.) Split from [definition-tate-twists--1]. DAG kind: statement. Placed through `def-coefficient-twists-detailed` (ancestor-1). DAG status: split. Statement dependencies not drawn: `def-weil-finite-field-fiber`, `def-weil-l-adic-coefficient-extension`, `def-weil-finite-torsion-constructibility`, `def-weil-cohomological-support`.
