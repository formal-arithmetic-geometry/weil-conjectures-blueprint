+++
id = "dag-def-pur-proetale-units-sheaf"
kind = "dag-definition"
title = "The multiplicative group sheaf G_m on the small pro-etale site"
name_showing = false
order = 184506
tags = ["sheaf-dag"]
split_from = "definition-tate-twists--1"
dag_id = "def-pur-proetale-units-sheaf"
dag_kind = "definition"
dag_status = "mathlib"
serial = false
dag_lean = ["AlgebraicGeometry.Scheme.proEtaleUnitsPresheaf", "AlgebraicGeometry.Scheme.proEtaleUnitsPresheaf_isSheaf", "AlgebraicGeometry.Scheme.proEtaleUnitsSheaf"]
uses = ["dag-def-weil-pbc-small-proetale-site"]
+++
Let $S$ be a scheme, $S_{\mathrm{proet}}$ its small pro-etale site
[dag-def-weil-pbc-small-proetale-site] and $\mathcal O_S$ its structure sheaf of rings
[dag-def-pur-proetale-structure-sheaf]. The *multiplicative group*
$\mathbf G_{m,S}=\mathcal O_S^\times$ is the presheaf of abelian groups (written
multiplicatively)

$$
 \mathbf G_{m,S}(U)=\Gamma(U,\mathcal O_U)^\times\qquad(U\to S\text{ weakly etale}),
$$

the group of units of the ring $\mathcal O_S(U)$, with the restriction maps of
$\mathcal O_S$ (a ring map sends units to units). It is a sheaf of abelian groups on
$S_{\mathrm{proet}}$: let $\{U_i\to U\}$ be a covering and $u_i\in\mathbf G_{m,S}(U_i)$
agree on the overlaps $U_i\times_UU_j$; since $\mathcal O_S$ is a sheaf, the $u_i$ glue
to a unique $u\in\mathcal O_S(U)$ and the inverses $u_i^{-1}$, which also agree on the
overlaps, glue to a unique $v\in\mathcal O_S(U)$; then $uv$ restricts to $1$ on every
$U_i$, so $uv=1$ by the uniqueness of gluing, and $u$ is a unit. Uniqueness of the
glued unit is that in $\mathcal O_S$.

(SHEAF DAG node `def-pur-proetale-units-sheaf`; machine-alignment layer.) Split from [definition-tate-twists--1]. DAG kind: definition. Placed through `def-coefficient-twists-detailed` (ancestor-1). DAG status: mathlib.
