+++
id = "dag-lem-route-sp-rational-twist-map-comp"
kind = "dag-lemma"
title = "Field-extension transitions compose."
name_showing = false
order = 184541
tags = ["sheaf-dag"]
split_from = "definition-tate-twists--13"
dag_id = "lem-route-sp-rational-twist-map-comp"
dag_kind = "statement"
dag_status = "split"
serial = false
dag_lean = ["AlgebraicGeometry.ProEtale.spRationalTwistMap_comp"]
uses = ["dag-def-weil-pbc-proetale-site"]
+++
Fix a prime $\ell$, an algebraic closure $\overline{\mathbf Q}_\ell$ of $\mathbf Q_\ell$, and an arbitrary scheme $X$, with its small pro-etale site [dag-def-weil-pbc-proetale-site]. Let $E\subseteq F\subseteq H$ be finite intermediate extensions, with rings of integers as in `def-weil-l-adic-coefficient-extension`. Write $A_K=K_X$ and $R_K=\mathcal O_{K,X}$ for the pulled-back condensed coefficient rings `sk-def-sfb-pulled-back-coefficients`, and $a_K:R_K\to A_K$ for `def-sfb-integers-to-subfield`, for $K=E,F,H$. Write $c_{KL}:A_K\to A_L$ for the field inclusions `def-sfb-subfield-coefficient-map`, $r_{KL}:R_K\to R_L$ for the uniquely characterized integral maps of [dag-lem-route-sp-integers-map-exists-unique], and $q_{KL,n}:B_{K,n}\to B_{L,n}$ for the uniquely characterized quotient maps of [dag-lem-route-sp-ell-map-exists-unique], where $B_{K,n}=(\mathcal O_K/\ell^{n+1})_X$ and $d_{K,n}:R_K\to B_{K,n}$ is reduction.

Let $M_n=\mu_{\ell^{n+1},X}$, with its power transitions [dag-def-pur-roots-of-unity-sheaf]. Form $L_K=\varprojlim_{n\geq0}(B_{K,n}\otimes_{\mathbf Z_X}M_n)$ in $R_K$-modules, with transitions reduction on $B$ tensored with the power map on $M$, and let $p_{K,n}$ be its projections [def-pur-sheaf-inverse-limit, def-pur-sheaf-tensor-product]. Let $u_{KL}:L_K\to L_L$ be the unique morphism of underlying abelian sheaves satisfying $p_{L,n}\circ u_{KL}=(q_{KL,n}\otimes1)\circ p_{K,n}$ for all $n$ [dag-lem-route-sp-integral-twist-map-exists-unique]. Put $T_K=A_K\otimes_{R_K}L_K$, with the defining tensor quotient $e_K:A_K\otimes_{\mathbf Z_X}L_K\to T_K$. Let $j_{KL}:T_K\to T_L$ be the unique morphism of abelian sheaves with
$$j_{KL}\circ e_K=e_L\circ(c_{KL}\otimes u_{KL})$$
as in [dag-lem-route-sp-rational-twist-map-exists-unique]. Then these specified rational transitions compose:
$$j_{EH}=j_{FH}\circ j_{EF}.$$
This is the equality of underlying abelian-sheaf morphisms denoted by $\mathrm{spRationalTwistMap}\ X\ \ell\ (h.\mathrm{trans}\ k)=\mathrm{spRationalTwistMap}\ X\ \ell\ h\;\gg\;\mathrm{spRationalTwistMap}\ X\ \ell\ k$ for $h:E\leq F$ and $k:F\leq H$. No invertibility hypothesis on $\ell$ on $X$ is needed for this composition assertion.

(SHEAF DAG node `lem-route-sp-rational-twist-map-comp`; machine-alignment layer.) Split from [definition-tate-twists--13]. DAG kind: statement. Placed through `sk-def-sp-tate-twist` (ancestor-1). DAG status: split. Statement dependencies not drawn: `def-weil-l-adic-coefficient-extension`, `sk-def-sfb-pulled-back-coefficients`, `def-sfb-integers-to-subfield`, `def-sfb-subfield-coefficient-map`, `lem-route-sp-integers-map-exists-unique`, `lem-route-sp-ell-map-exists-unique`, `def-pur-roots-of-unity-sheaf`, `def-pur-sheaf-inverse-limit`, `def-pur-sheaf-tensor-product`, `lem-route-sp-integral-twist-map-exists-unique`, `lem-route-sp-rational-twist-map-exists-unique`.
