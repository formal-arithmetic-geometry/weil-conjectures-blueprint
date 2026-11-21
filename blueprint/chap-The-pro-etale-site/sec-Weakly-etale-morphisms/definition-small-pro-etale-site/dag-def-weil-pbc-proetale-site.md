+++
id = "dag-def-weil-pbc-proetale-site"
kind = "dag-definition"
title = "Small pro-etale site"
name_showing = false
order = 34504
tags = ["sheaf-dag"]
split_from = "definition-small-pro-etale-site--1"
dag_id = "def-weil-pbc-proetale-site"
dag_kind = "definition"
dag_status = "split"
serial = false
uses = ["dag-def-weil-pbc-small-proetale-site", "dag-def-weil-pbc-proetale-covering", "dag-def-weil-pbc-fpqc-covering", "dag-def-weil-pbc-constant-sheaf", "dag-def-weil-pbc-sheafification"]
+++
Fix a scheme $Y$ `def-pc-scheme`. Choose Grothendieck universes $\mathcal U\in\mathcal V$ and
a $\mathcal V$-small skeleton, as required by the size convention
`def-weil-size-convention`, and form all categories below inside $\mathcal
V$. The site $Y_{\mathrm{proet}}$ [dag-def-weil-pbc-small-proetale-site] has as objects the $\mathcal U$-bounded
weakly etale maps $U\to Y$, where a weakly etale map
`def-weil-weakly-etale-morphism` is flat with flat diagonal, and as morphisms the $Y$-morphisms. A family
$\{U_i\to U\}_{i\in I}$ is a covering if it is a pro-etale covering [dag-def-weil-pbc-proetale-covering], i.e. an fpqc covering [dag-def-weil-pbc-fpqc-covering]: every arrow is weakly etale and, for
every affine open $V\subset U$, finitely many affine opens $V_j\subset
U_{i_j}$ have images whose union is $V$.

For a commutative ring $A$, let $A_Y$ be the constant sheaf of rings [dag-def-weil-pbc-constant-sheaf], the sheafification [dag-def-weil-pbc-sheafification] of the constant
presheaf $U\mapsto A$ on $Y_{\mathrm{proet}}$. Let
$\Sh(Y_{\mathrm{proet}},A)$ be the abelian category of sheaves of
$A_Y$-modules `def-weil-sheaf-of-modules-category`, and set

$$
 D(Y_{\mathrm{proet}},A)=D\bigl(\Sh(Y_{\mathrm{proet}},A)\bigr),
$$

using the derived category of cochain complexes
`def-weil-abstract-derived-category`.

(SHEAF DAG node `def-weil-pbc-proetale-site`; machine-alignment layer.) Split from [definition-small-pro-etale-site--1]. DAG kind: definition. DAG status: split. Lean names not on master: `AlgebraicGeometry.Scheme.ProEt`. Statement dependencies not drawn: `def-pc-scheme`, `def-weil-size-convention`, `def-weil-weakly-etale-morphism`, `def-weil-sheaf-of-modules-category`, `def-weil-abstract-derived-category`.
