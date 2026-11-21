+++
id = "dag-sk-def-sp-tate-twist"
kind = "dag-definition"
title = "Tate twists"
name_showing = false
order = 184547
tags = ["sheaf-dag"]
split_from = "definition-tate-twists--13"
dag_id = "sk-def-sp-tate-twist"
dag_kind = "definition"
dag_status = "split"
serial = false
dag_lean = ["AlgebraicGeometry.ProEtale.spInternalSignedTwist", "AlgebraicGeometry.ProEtale.spInternalComplexTwist"]
uses = ["dag-def-weil-pbc-proetale-site", "dag-def-weil-pbc-constant-sheaf"]
+++
Fix a prime $\ell$, an algebraic closure $\overline{\mathbf Q}_\ell$ of $\mathbf Q_\ell$, and a scheme $X$ on which $\ell$ is invertible. Use the universe convention `def-weil-size-convention` and the small pro-etale site [dag-def-weil-pbc-proetale-site]. Coefficient rings are commutative. For each finite intermediate extension $\mathbf Q_\ell\subseteq E\subseteq\overline{\mathbf Q}_\ell$, use its ring of integers $\mathcal O_E$ and a uniformizer $\pi_E$ `def-weil-l-adic-coefficient-extension`. The coefficient sheaves $\mathcal O_{E,X}$ and $E_X$ are the pullbacks of their continuous-function condensed rings `sk-def-sfb-condensed-ring`, `sk-def-sfb-pulled-back-coefficients`. Likewise $\overline{\mathbf Q}_{\ell,X}=p_X^*\underline{\overline{\mathbf Q}}_\ell$, using the finite-subextension-valued condensed ring of `sk-def-sfb-qlbar-condensed`; it is not the full continuous-function sheaf. For a finite discrete ring $B$, $B_X$ denotes the constant sheaf [dag-def-weil-pbc-constant-sheaf].

For $n\geq1$, take the sheaf $\mu_{\ell^n,X}$ and its $(\mathbf Z/\ell^n\mathbf Z)_X$-module structure from [dag-def-pur-roots-of-unity-sheaf]:
$$
\mu_{\ell^n,X}(U)=\{u\in\Gamma(U,\mathcal O_U)^\times:u^{\ell^n}=1\},
\qquad \mu_{\ell^{n+1},X}\longrightarrow\mu_{\ell^n,X},\quad u\longmapsto u^\ell.
$$
Use the tensor product of sheaves and extension of scalars [dag-def-pur-sheaf-tensor-product]. For a finite commutative ring $A$ and an integer $r\geq1$ such that $\ell^r A=0$, put
$$
 A_X(1)=\mu_{\ell^r,X}\otimes_{(\mathbf Z/\ell^r\mathbf Z)_X}A_X.
$$
Regard these expressions for different annihilating exponents as canonically identified by the Kummer maps $u\mapsto u^{\ell^{r'-r}}$ for $r'\geq r$, by clause 2 of `det-def-sp-tate-twist-locally-free`. These identifications have identity at $r'=r$ and compose because the corresponding power maps compose.

Set $B_{E,n}=\mathcal O_E/\ell^n\mathcal O_E$ and form the inverse limit of sheaves [dag-def-pur-sheaf-inverse-limit]
$$
 \mathcal O_{E,X}(1)=\varprojlim_{n\geq1}(B_{E,n})_X(1),
 \qquad (B_{E,n})_X(1)=\mu_{\ell^n,X}\otimes_{(\mathbf Z/\ell^n\mathbf Z)_X}(B_{E,n})_X.
$$
The transition sends $u\otimes a$ to $u^\ell\otimes\bar a$. The action of $\mathcal O_{E,X}$ on the limit is coordinatewise through the quotient maps to $(B_{E,n})_X$. Here use the integral coefficient comparison `det-prop-sfb-qlbar-colimit-x-integral-limit`, with the cofinal $\ell$-power ideals in place of the $\pi_E$-power ideals: writing $\ell=v\pi_E^e$ with $v$ a unit and $e\geq1$, we have $\ell^n\mathcal O_E=\pi_E^{en}\mathcal O_E$. A compatible sequence at indices $en$ extends uniquely to index $k$ by reducing any coordinate with $en\geq k$. Define
$$
 E_X(1)=\mathcal O_{E,X}(1)\otimes_{\mathcal O_{E,X}}E_X,
 \qquad \overline{\mathbf Q}_{\ell,X}(1)=\varinjlim_E E_X(1).
$$
The first expression inverts $\ell$ by `det-prop-sfb-qlbar-colimit-x-invert-ell`. For $E\subseteq F$, the map on integral twists is induced at level $n$ by $u\otimes a\mapsto u\otimes a$ along $\mathcal O_E/\ell^n\to\mathcal O_F/\ell^n$; the map $E_X(1)\to F_X(1)$ is its localization. Thus the final colimit is a specified diagram indexed by the directed, universe-small poset of finite intermediate extensions. Colimits of abelian sheaves mean sheafifications of sectionwise colimits `lem-weil-pbc-site-abelian-sheaves-filtered-colimits-exact`. Its scalar action is defined first on the sectionwise colimit presheaves: for $a\in E_X(U)$ and $t\in F_X(1)(U)$, choose a finite intermediate field $H$ containing $E$ and $F$, and set $[a][t]=[i_{E,H}(a)j_{F,H}(t)]$, where $i$ and $j$ are the coefficient and twist transition maps. These transitions are semilinear: $j_{F,H}(bt)=i_{F,H}(b)j_{F,H}(t)$. Any two choices of $H$ agree after mapping to their compositum, so the action is independent of representatives and satisfies the module axioms there. Sheafify this action to obtain an action of the coefficient colimit sheaf on the twist colimit sheaf. Sections of the sheafified colimits need only have such representatives locally. The coefficient identification $\varinjlim_E E_X=\overline{\mathbf Q}_{\ell,X}$ used here is obtained from the sectionwise union defining `sk-def-sfb-qlbar-condensed` by the left adjoint $p_X^*$ of `sk-def-sfb-pullback-from-point`, which preserves colimits `lem-weil-pbc-left-adjoint-preserves-colimits`.

For $\Lambda\in\{A,\mathcal O_E,E,\overline{\mathbf Q}_\ell\}$ let $\Lambda_X(1)$ denote the corresponding sheaf just constructed. Each $\Lambda_X(1)$ is pro-etale locally free of rank one. Explicitly, use clause 1 of `det-def-sp-tate-twist-locally-free` to choose a pro-etale cover $\widetilde X\to X$ with compatible generators $\zeta_n$, $\zeta_{n+1}^{\ell}=\zeta_n$. On its slice site the maps $a\mapsto\zeta_r\otimes a$ identify $A_{\widetilde X}$ with $A_X(1)|_{\widetilde X}$. The maps $a\mapsto\zeta_n\otimes a$ likewise identify $(B_{E,n})_{\widetilde X}$ with $(B_{E,n})_X(1)|_{\widetilde X}$; compatibility follows from $\zeta_{n+1}\otimes a\mapsto\zeta_n\otimes\bar a$. Their inverse limit identifies $\mathcal O_{E,\widetilde X}$ with $\mathcal O_{E,X}(1)|_{\widetilde X}$ by the integral coefficient comparison above. Extending scalars identifies $E_{\widetilde X}$ with $E_X(1)|_{\widetilde X}$. These maps commute with every finite-field-extension transition, since the chosen $\zeta_n$ do not depend on $E$; their sheafified colimit identifies $\overline{\mathbf Q}_{\ell,\widetilde X}$ with $\overline{\mathbf Q}_{\ell,X}(1)|_{\widetilde X}$ by the coefficient-colimit identification above. These calculations take place on the slice site: restriction keeps the same sections at its objects and the same covering families, so sectionwise limits and sheafified colimits have the displayed restrictions. Only clauses 1 and 2 of the cited theorem are used, not its clause 3 for other coefficient categories. Define
$$
 \Lambda_X(0)=\Lambda_X,\qquad
 \Lambda_X(d)=\Lambda_X(1)^{\otimes_{\Lambda_X}d}\ (d\geq1),\qquad
 \Lambda_X(-d)=\mathcal Hom_{\Lambda_X}(\Lambda_X(d),\Lambda_X)\ (d\geq1),
$$
where $\mathcal Hom$ is sheaf Hom [dag-def-pur-sheaf-hom]. Let $D(X_{\mathrm{proet}},\Lambda)$ mean the unbounded derived category `def-weil-abstract-derived-category` of sheaves of $\Lambda_X$-modules `def-weil-sheaf-of-modules-category`. For any $K$ in this category and $d\in\mathbf Z$, put
$$
 K(d)=K\otimes^{\mathbf L}_{\Lambda_X}\Lambda_X(d),
$$
placing $\Lambda_X(d)$ in degree zero and using the derived tensor bifunctor on an arbitrary ringed site of `lem-weil-pbc-site-derived-tensor-descent`. In particular the non-finite coefficients here are pulled-back condensed coefficient sheaves, not discrete constant rings or common-stage rationalized integral categories.

(SHEAF DAG node `sk-def-sp-tate-twist`; machine-alignment layer.) Split from [definition-tate-twists--13]. DAG kind: definition. DAG status: split. Statement dependencies not drawn: `def-weil-size-convention`, `def-weil-l-adic-coefficient-extension`, `sk-def-sfb-condensed-ring`, `sk-def-sfb-pulled-back-coefficients`, `sk-def-sfb-qlbar-condensed`, `def-pur-roots-of-unity-sheaf`, `def-pur-sheaf-tensor-product`, `det-def-sp-tate-twist-locally-free`, `def-pur-sheaf-inverse-limit`, `det-prop-sfb-qlbar-colimit-x-integral-limit`, `det-prop-sfb-qlbar-colimit-x-invert-ell`, `lem-weil-pbc-site-abelian-sheaves-filtered-colimits-exact`, `sk-def-sfb-pullback-from-point`, `lem-weil-pbc-left-adjoint-preserves-colimits`, `def-pur-sheaf-hom`, `def-weil-abstract-derived-category`, `def-weil-sheaf-of-modules-category`, `lem-weil-pbc-site-derived-tensor-descent`, `def-weil-pbc-internal-abelian-sheaf-module-equivalence`.
