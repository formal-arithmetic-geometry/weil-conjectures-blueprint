+++
id = "dag-lem-pur-twist-sheaf-locally-free"
kind = "dag-lemma"
title = "Condensed Tate lines and their projection-induced finite reductions"
name_showing = false
order = 184529
tags = ["sheaf-dag"]
split_from = "definition-tate-twists--1"
dag_id = "lem-pur-twist-sheaf-locally-free"
dag_kind = "statement"
dag_status = "split"
serial = false
uses = ["dag-def-weil-pbc-proetale-site", "dag-def-coefficient-twists-detailed", "dag-def-pur-roots-of-unity-sheaf", "dag-def-pur-sheaf-inverse-limit", "dag-def-pur-sheaf-tensor-product"]
+++
Fix a prime $\ell$, an algebraic closure $\overline{\mathbf Q}_\ell$ of $\mathbf Q_\ell$, a finite intermediate extension $E/\mathbf Q_\ell$, its valuation ring $\mathcal O_E$, a uniformizer $\pi_E$, and $A_{E,n}=\mathcal O_E/\pi_E^n$ for $n\geq1$. Let $S$ be any scheme on which $\ell$ is invertible. On its small pro-étale site [dag-def-weil-pbc-proetale-site], use the coefficient rings $\Lambda_S=p_S^*\underline\Lambda$ `det-def-sfb-pulled-back-coefficients` and twists of [dag-def-coefficient-twists-detailed], for $\Lambda\in\{A_{E,n},\mathcal O_E,E,\overline{\mathbf Q}_\ell\}$. The finite rings are discrete, the integral and finite-extension rings have their continuous condensed structures, and the algebraic closure has its finite-subextension-valued condensed structure.

Write $R_S=\mathbf Z_{\ell,S}=p_S^*\underline{\mathbf Z}_\ell$. Let
$$T_S=\varprojlim_{r\geq1}\mu_{\ell^r,S}$$
be the inverse limit of the abelian root sheaves [def-pur-roots-of-unity-sheaf, def-pur-sheaf-inverse-limit], with power transitions, and with coordinatewise $R_S$-action through $R_S\cong\varprojlim_r(\mathbf Z/\ell^r\mathbf Z)_S$ [det-prop-sfb-qlbar-colimit-x-integral-limit, $E=\mathbf Q_\ell$]. Denote its projections by $p_r$ and the projections of $\mathcal O_E(1)_S=\varprojlim_n A_{E,n}(1)_S$ by $q_n$. Tensor products are the sheaf tensors of [dag-def-pur-sheaf-tensor-product]. Then:

1. The finite twists $A_{E,n}(1)_S=\mu_{\ell^r,S}\otimes_{(\mathbf Z/\ell^r\mathbf Z)_S}(A_{E,n})_S$, for $\ell^rA_{E,n}=0$, are independent of $r$ by the canonical Kummer isomorphisms. One pro-étale cover $V\to S$ trivializes all four coefficient types and all positive levels: $\Lambda(1)_S|_V\cong\Lambda_V$. Thus they are locally free of rank one.

2. $T_S$ is locally free of rank one over $R_S$, and the projection-induced map
$$
T_S\otimes_{R_S}(\mathbf Z/\ell^r\mathbf Z)_S\longrightarrow\mu_{\ell^r,S},\qquad t\otimes a\longmapsto a\,p_r(t)
$$
is an isomorphism for every $r\geq1$ (the scalar action on roots is exponentiation).

3. There are canonical isomorphisms
$$
T_S\otimes_{R_S}\mathcal O_{E,S}\xrightarrow{\sim}\mathcal O_E(1)_S,
\qquad
\mathcal O_E(1)_S\otimes_{\mathcal O_{E,S}}(A_{E,n})_S\xrightarrow{\sim} A_{E,n}(1)_S.
$$
The first map has $n$-th coordinate $t\otimes b\mapsto p_n(t)\otimes\bar b$, using exponent $n$ for the finite twist (allowed since $\ell^nA_{E,n}=0$). The second map sends $x\otimes a$ to $a\,q_n(x)$. These are maps defined before choosing a trivialization and commute with the respective root and coefficient reduction transitions.

(SHEAF DAG node `lem-pur-twist-sheaf-locally-free`; machine-alignment layer.) Split from [definition-tate-twists--1]. DAG kind: statement. Placed through `def-coefficient-twists-detailed` (ancestor-1). DAG status: split. Statement dependencies not drawn: `det-def-sfb-pulled-back-coefficients`, `det-prop-sfb-qlbar-colimit-x-integral-limit`.
