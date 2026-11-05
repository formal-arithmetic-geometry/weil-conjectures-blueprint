+++
id = "corollary-open-direct-image-over-field--2"
kind = "corollary"
title = "Open direct image over a field (2)"
name_showing = false
order = 586002
aliases = ["bp-r178-2"]
lean = ["AlgebraicGeometry.Etale.isIso_baseChangeHomologyMap_of_isOpenImmersion_of_field", "AlgebraicGeometry.Etale.isIso_baseChange_app_of_isOpenImmersion_of_field", "AlgebraicGeometry.ProEtale.isIso_derivedBaseChangeMap_app_of_isOpenImmersion_of_field"]
+++
Let $k$ be a field and let $A$ be a commutative ring killed by a positive
integer $n$ invertible in $k$. Let $j:X\hookrightarrow Y$ be an open
immersion of $k$-schemes of finite type, let $T$ be a $k$-scheme of finite
type, and write $j_T:X_T\hookrightarrow Y_T$ and
$g_X:X_T\to X$, $g_Y:Y_T\to Y$ for the base change and projections.

For every étale sheaf $F$ of $A$-modules on $X$ and every $i\in\mathbf Z$,
the map

$$
g_Y^*R^ij_*F\longrightarrow R^ij_{T,*}g_X^*F
$$

is an isomorphism. In particular, for every
$L\in D^b_c(X_{\acute{e}t},A)$, the derived base change map

$$
g_Y^*Rj_*L\longrightarrow Rj_{T,*}g_X^*L
$$

is an isomorphism. The pro-étale base change map is also an isomorphism
for every $K\in D(X_{\mathrm{pro}\acute{e}t},A)$ admitting an isomorphism
$K\simeq\nu_X^*L$ with such an $L$.
