+++
id = "dag-lem-weil-pbc-completed-koszul-quotient-comparison"
kind = "dag-lemma"
title = "Canonical completion comparison (merged into the current principal Roos construction)"
name_showing = false
order = 210515
tags = ["sheaf-dag"]
split_from = "lemma-reduction-derived-nakayama--2"
dag_id = "lem-weil-pbc-completed-koszul-quotient-comparison"
dag_kind = "statement"
dag_status = "merged"
serial = false
uses = ["dag-lem-pe-principal-reduction-cone-calculus", "dag-lem-sfb-transfinite-plus-finite-limits", "dag-lem-sfb-transfinite-plus-sheaf-orthogonality", "dag-sk-def-pe-derived-completion"]
+++
Let $\ell$ be prime, $E/\mathbf Q_\ell$ finite with uniformizer $\pi$, and $X$ any scheme. Work in $D(R)$ for $R=\mathcal O_{E,X}=p_X^*\underline{\mathcal O_E}$, with the coefficient category of [dag-sk-def-pe-derived-completion] and localization $Q$ of `def-weil-abstract-derived-category`. For an unbounded complex $M$ take the strict reduction tower $D_\bullet(M)$, its transitions and maps $j_n$ of [dag-lem-pe-principal-reduction-cone-calculus], and apply the Roos functor $H$ of [dag-lem-pe-roos-cone-calculus]. The formula $F(QM)=QH(D_\bullet(M))$ descends to an additive endofunctor $F:D(R)\to D(R)$, and
$$c_M(m)=(((m,0))_{n\ge1},0)$$
descends to a natural transformation $c:\mathrm{id}\Rightarrow F$ which is the canonical completion map of [dag-sk-def-pe-derived-completion] up to isomorphism: for every $K\in D(R)$ there is an isomorphism from $F(K)$ to the derived limit $R\varprojlim_nK_n$ specified there, under which $c_K$ corresponds to the specified canonical map $K\to R\varprojlim_nK_n$. In particular $K$ is derived complete if and only if $c_K$ is an isomorphism. There are coherent natural comparisons $\sigma_{K,r}:F(K[r])\xrightarrow{\sim}F(K)[r]$ for all $r\in\mathbf Z$, satisfying $\sigma_{K,r}c_{K[r]}=c_K[r]$. For every distinguished triangle $T=(K\xrightarrow{f}L\to C\xrightarrow{w}K[1])$, its image $F(T)$, whose last arrow is $\sigma_{K,1}F(w)$, is distinguished, and $(c_K,c_L,c_C):T\to F(T)$ is a morphism of triangles, including its last square with $c_K[1]$.

(SHEAF DAG node `lem-weil-pbc-completed-koszul-quotient-comparison`; machine-alignment layer.) Split from [lemma-reduction-derived-nakayama--2]. DAG kind: statement. Placed through `det-pe-derived-nakayama-first-reduction` (ancestor-1). DAG status: merged. Statement dependencies not drawn: `def-pc-kflat-complex`, `def-pc-module-kflat-complex`, `def-sfb-modobj-internal-hom`, `def-sfb-modobj-relative-tensor`, `def-sfb-modobj-symmetric-tensor`, `def-sfb-qlbar-coefficient-ring`, `def-sfb-torsion-stratum-coefficients`, `def-sfb-upper-star-from-point`, `def-weil-abstract-derived-category`, `def-weil-strict-roos-model`, `def-weil-tower-transition-endomorphism`, `det-def-sfb-ring-object`, `det-def-sfb-ring-object-rings`, `det-def-sfb-sheaf-tensor-presheaf`, `det-pe-derived-nakayama-resolution`, `lem-coef-grothendieck-locally-presentable`, `lem-pc-derived-category-locally-small`, `lem-sfb-grothendieck-k-injective`, `lem-sfb-modobj-abelian`, `lem-sfb-modobj-grothendieck`, `lem-sfb-modobj-symmetric-bimodules`, `lem-sfb-proetale-sheaves-grothendieck`, `lem-weil-pbc-module-relative-tensor-adjoint`, `lem-weil-pbc-sheaf-tensor-closed`, `pur713-def-coefficient-rings`, `pur713-def-relative-tensor`, `sk-def-sfb-pulled-back-coefficients`, `sk-def-sfb-ring-object`.
