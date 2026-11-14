+++
id = "dag-lem-route-sp-qbar-twist-action-exists-unique"
kind = "dag-lemma"
title = "The colimit's action is uniquely determined by multiplying at a common finite field."
name_showing = false
order = 187546
tags = ["sheaf-dag"]
split_from = "lemma-inverse-image-coefficient-sheaves--2"
dag_id = "lem-route-sp-qbar-twist-action-exists-unique"
dag_kind = "statement"
dag_status = "split"
serial = false
dag_lean = ["AlgebraicGeometry.ProEtale.spQbarTwistAction_existsUnique"]
uses = ["dag-def-weil-pbc-proetale-site", "dag-def-pur-roots-of-unity-sheaf", "dag-def-pur-sheaf-tensor-product", "dag-def-pur-sheaf-inverse-limit", "dag-lem-route-sp-integral-twist-map-exists-unique", "dag-lem-route-sp-rational-twist-map-exists-unique", "dag-lem-route-sp-rational-twist-map-id", "dag-lem-route-sp-rational-twist-map-comp"]
+++
Fix a prime $\ell$, an algebraic closure $\overline{\mathbf Q}_\ell$ of $\mathbf Q_\ell$, and an arbitrary scheme $X$. Use the universe convention `def-weil-size-convention` and the small pro-étale site [dag-def-weil-pbc-proetale-site]. Let $I$ be the poset of finite intermediate fields $\mathbf Q_\ell\subseteq E\subseteq\overline{\mathbf Q}_\ell$. For a topological ring $R$, write $R_X=p_X^*\underline R$, with $\underline R(S)=C(S,R)$ and pulled-back ring structure [sk-def-sfb-condensed-ring, det-def-sfb-pulled-back-coefficients]. For $n\geq1$, give $B_{E,n}=\mathcal O_E/\ell^n\mathcal O_E$ the discrete topology, where $\mathcal O_E=\{a\in E:|a|\leq1\}$, and put
$$
 T_E=\varprojlim_{n\geq1}\bigl((B_{E,n})_X\otimes_{\mathbf Z_X}\mu_{\ell^n,X}\bigr),\qquad
 M_E=E_X\otimes_{\mathcal O_{E,X}}T_E.
$$
Here $\mu_{\ell^n,X}$ is the root sheaf [dag-def-pur-roots-of-unity-sheaf], tensor and extension of scalars are sheafified tensors [dag-def-pur-sheaf-tensor-product], and the limit is in $\mathcal O_{E,X}$-modules [dag-def-pur-sheaf-inverse-limit]. The action on each finite term is multiplication on the $B$ factor through the quotient $\mathcal O_{E,X}\to(B_{E,n})_X$; its transition is coefficient reduction tensored with $u\mapsto u^\ell$. The scalar-extension map $\mathcal O_{E,X}\to E_X$ is `def-sfb-integers-to-subfield`. Let $\alpha_E:E_X\otimes_{\mathbf Z_X}M_E\to M_E$ be its module action `sk-def-sfb-module-objects`.

For $E\subseteq F$, let $i_{E,F}:E_X\to F_X$ be the pulled-back coefficient inclusion [def-sfb-qlbar-subextension-map, det-def-sfb-pulled-back-coefficients]. Let $J_{E,F}:T_E\to T_F$ be the unique abelian-sheaf map whose $n$th projection is induced by $B_{E,n}\to B_{F,n}$ tensored with the identity on $\mu_{\ell^n,X}$ [dag-lem-route-sp-integral-twist-map-exists-unique]. Let $j_{E,F}:M_E\to M_F$ be the unique abelian-sheaf map with the localization normalization
$$
 j_{E,F}(b\otimes t)=i_{E,F}(b)\otimes J_{E,F}(t),
$$
as an equality of maps out of the sheaf tensor $E_X\otimes_{\mathbf Z_X}T_E$ before the balanced quotient [dag-lem-route-sp-rational-twist-map-exists-unique]. No invertibility of $\ell$ on $X$ is assumed.

The maps $j_{E,F}$ have identity and composition laws [lem-route-sp-rational-twist-map-id, lem-route-sp-rational-twist-map-comp]; form their diagram $M:I\to\operatorname{Sh}(X_{\mathrm{proét}},\operatorname{Ab})$. Let $Q=\operatorname{colim}_{E\in I}M_E$ in abelian sheaves, with coprojections $\eta_E:M_E\to Q$ `def-weil-pbc-category-colimit`. Put $A=\overline{\mathbf Q}_{\ell,X}=p_X^*\underline{\overline{\mathbf Q}}_\ell$, using the finite-subextension-valued condensed ring [sk-def-sfb-qlbar-condensed, def-sfb-qlbar-coefficient-ring], and let $c_E:E_X\to A$ be the actual pulled-back inclusions `def-sfb-qlbar-x-cocone`. Then there exists exactly one $A$-module-object structure on the fixed underlying abelian sheaf $Q$ whose action $a:A\otimes_{\mathbf Z_X}Q\to Q$ satisfies, for all $E,F,H\in I$ with $E,F\subseteq H$,
$$
 a\circ(c_E\otimes\eta_F)
 =\eta_H\circ\alpha_H\circ(i_{E,H}\otimes j_{F,H})
 \colon E_X\otimes_{\mathbf Z_X}M_F\longrightarrow Q.
$$
The colimit here is a sheaf colimit, not an assertion that sections over every pro-étale object are a union of sections from finite stages.

(SHEAF DAG node `lem-route-sp-qbar-twist-action-exists-unique`; machine-alignment layer.) Split from [lemma-inverse-image-coefficient-sheaves--2]. DAG kind: statement. Placed through `det-prop-sfb-cartesian-coefficients-twists` (ancestor-1). DAG status: split. Statement dependencies not drawn: `def-weil-size-convention`, `sk-def-sfb-condensed-ring`, `det-def-sfb-pulled-back-coefficients`, `def-sfb-integers-to-subfield`, `sk-def-sfb-module-objects`, `def-sfb-qlbar-subextension-map`, `def-weil-pbc-category-colimit`, `sk-def-sfb-qlbar-condensed`, `def-sfb-qlbar-coefficient-ring`, `def-sfb-qlbar-x-cocone`.
