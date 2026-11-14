+++
id = "dag-lem-pur-signed-line-derived-base-change"
kind = "dag-lemma"
title = "Signed line comparisons and their unbounded derived tensor action"
name_showing = false
order = 187528
tags = ["sheaf-dag"]
split_from = "lemma-inverse-image-coefficient-sheaves--2"
dag_id = "lem-pur-signed-line-derived-base-change"
dag_kind = "statement"
dag_status = "split"
serial = false
dag_lean = ["SheafOfModules.SignedLineDerivedBaseChange.signed_line_derived_base_change"]
uses = ["dag-def-pur-localized-ringed-site", "dag-def-pur-signed-line-derived-action-data", "dag-def-pur-signed-line-pullback-normalization-data", "dag-def-pur-signed-line-scalar-normalization-data", "dag-lem-pur-ringed-site-finite-free-dual-pullback", "dag-lem-pur-ringed-site-module-pullback-exists-universes"]
+++
Let $f:(\operatorname{Sh}(\mathcal D),S)\to(\operatorname{Sh}(\mathcal C),R)$ be a morphism of ringed topoi on sites small relative to the sheaf universe [def-weil-size-convention, def-weil-pbc-ringed-topos-morphism], associated to a finite-limit- and covering-preserving functor $u:\mathcal C\to\mathcal D$ between sites with finite limits, with $R,S$ commutative and structural ring isomorphism $a:f^{-1}R\xrightarrow{\sim}S$. Let $P$ be an $R$-module sheaf on $\mathcal C$ and $Q$ an $S$-module sheaf on $\mathcal D$ `def-weil-sheaf-of-modules-category`. Suppose both are locally free of rank one, meaning they restrict to the coefficient ring on a covering of the final object of their site [dag-def-pur-localized-ringed-site]. Put $F(M)=S\otimes_{f^{-1}R}f^{-1}M$, using sheaf tensor [dag-def-pur-sheaf-tensor-product], and fix an isomorphism $t:F(P)\xrightarrow{\sim}Q$.
Define $P^{[0]}=R$, $P^{[m]}=P^{\otimes_R m}$ for $m\ge1$, and $P^{[-m]}=\mathcal Hom_R(P^{[m]},R)$ for $m\ge1$, with $Q^{[d]}$ defined in the same way [dag-def-pur-sheaf-hom]. There is a unique family of isomorphisms $t_d:F(P^{[d]})\xrightarrow{\sim}Q^{[d]}$ with the following normalization: $t_0$ is the coefficient-unit comparison and $t_1=t$; $t_{m+1}$ for $m\ge1$ is obtained from $t_m\otimes t$ by the canonical relative tensor comparison and the fixed right-associated powers; and, for $m\ge1$, $t_{-m}$ is characterized by
$$\operatorname{ev}_{Q^{[m]}}\circ(t_{-m}\otimes t_m)=(F\operatorname{ev}_{P^{[m]}})\circ\sigma^{-1},$$
with both sides mapped to $S$ by the unit comparison and $\sigma:F(P^{[-m]}\otimes_RP^{[m]})\cong F(P^{[-m]})\otimes_SF(P^{[m]})$. In particular it sends the pulled-back functional dual to a local basis of $P^{[m]}$ to the functional dual to its image under $t_m$. This family is natural in isomorphisms of the line data, and in scalar-extension identifications of these data: for commutative ring maps $R\to R'$, $S\to S'$ and a ring isomorphism $a':f^{-1}R'\xrightarrow{\sim}S'$ compatible with $a$, equip $P'=R'\otimes_RP$, $Q'=S'\otimes_SQ$ and $t'$ with the induced comparison; then its $t'_d$ is the scalar extension of $t_d$ under the canonical signed-power identifications.
The exact functor $F$ induces termwise pullback $D(F):D(R)\to D(S)$ on the ordinary unbounded derived categories `def-weil-abstract-derived-category`, with derived tensor of `lem-weil-pbc-site-derived-tensor-descent`. For every $K\in D(R)$ and $d\in\mathbf Z$ there is a natural isomorphism
$$D(F)(K\otimes_R^{\mathbf L}P^{[d]}[0])\xrightarrow{\sim}D(F)(K)\otimes_S^{\mathbf L}Q^{[d]}[0],$$
namely the canonical derived tensor-pullback comparison followed by $1\otimes t_d[0]$. It respects the preceding unit, positive-power and evaluation normalizations. No boundedness, constructibility or finite-Tor condition on $K$ is imposed.

(SHEAF DAG node `lem-pur-signed-line-derived-base-change`; machine-alignment layer.) Split from [lemma-inverse-image-coefficient-sheaves--2]. DAG kind: statement. Placed through `det-prop-sfb-cartesian-coefficients-twists` (ancestor-1). DAG status: split. Statement dependencies not drawn: `def-sf-ringed-kflat-tensor-representative-data`, `def-weil-abstract-derived-category`, `def-weil-sheaf-of-modules-category`, `def-weil-size-convention`, `lem-pur-signed-line-scalar-pullback-square`, `lem-pur-signed-line-scalar-tensor-tower`, `lem-weil-pbc-kflat-fixed-tensor-triangulated`.
