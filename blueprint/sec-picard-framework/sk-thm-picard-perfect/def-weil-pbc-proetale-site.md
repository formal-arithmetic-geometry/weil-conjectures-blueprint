+++
id = "def-weil-pbc-proetale-site"
kind = "definition"
title = "Small pro-etale site"
lean = ["AlgebraicGeometry.Scheme.ProEt", "AlgebraicGeometry.Scheme.ProEt.topology", "AlgebraicGeometry.ProEtale.ModuleDerivedCategory"]
order = 668
uses = ["def-weil-abstract-derived-category", "def-weil-pbc-scheme-conventions", "def-weil-scheme-morphism-properties", "def-weil-size-convention"]
+++
Fix universes $\mathcal U\in\mathcal V$ as in the size convention
[def-weil-size-convention] and a $\mathcal U$-small scheme $Y$; all
categories below are formed inside $\mathcal V$. The *small pro-etale site*
$Y_{\mathrm{proet}}$ has as objects the weakly etale maps $U\to Y$ from
$\mathcal U$-small schemes $U$, where a weakly etale map
[def-weil-scheme-morphism-properties] (see also
[def-weil-pbc-scheme-conventions]) is flat with flat diagonal. A family
$\{U_i\to U\}_{i\in I}$ is a covering if every arrow is weakly etale and, for
every affine open $V\subset U$, finitely many affine opens $V_j\subset
U_{i_j}$ have images covering $V$ (so the coverings are the jointly
surjective fpqc covering families of weakly etale maps).

For a commutative ring $A$, let $A_Y$ be the sheafification of the constant
presheaf $U\mapsto A$ on $Y_{\mathrm{proet}}$. Let
$\Sh(Y_{\mathrm{proet}},A)$ be the abelian category of sheaves of
$A_Y$-modules, and set

$$
 D(Y_{\mathrm{proet}},A)=D\bigl(\Sh(Y_{\mathrm{proet}},A)\bigr),
$$

using the derived category of cochain complexes
[def-weil-abstract-derived-category].
