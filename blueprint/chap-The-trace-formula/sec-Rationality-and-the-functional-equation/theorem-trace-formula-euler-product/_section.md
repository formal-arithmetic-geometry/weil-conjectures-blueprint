+++
id = "theorem-trace-formula-euler-product"
kind = "theorem"
title = "The trace formula as an Euler product"
order = 1036
lean = ["AlgebraicGeometry.WeilComplex.coeff_prod_inv_alternatingCharpolyRevProd_stalk"]
uses = ["definition-ind-etale-pro-etale-weakly", "definition-small-pro-etale-site", "proposition-topos-functoriality", "definition-compactification-refinement", "lemma-schematic-closure-uniqueness", "proposition-compactifying-union-two-opens", "lemma-affine-covers-dense-intersection"]
+++
Let $X_0$ be separated and of finite type over $\mathbf F_q$, let
$\Lambda\in\{\mathbf Q_\ell,E,\overline{\mathbf Q}_\ell\}$, and let $K\in\Dbc(X,\Lambda)$ carry a Weil
structure, with stalk Frobenius maps $\operatorname{Frob}_{y,m}$ as in
Theorem [theorem-grothendieck-lefschetz-trace-formula]. For each closed
point $x\in|X_0|$, let $\deg(x)=[\kappa(x):\mathbf F_q]$ be its degree,
choose one of the $\deg(x)$ points $y\in X_0(\mathbf F_{q^{\deg(x)}})$ lying
over $x$, write $\bar x=\bar y$ for the corresponding geometric point,
and let $\operatorname{Frob}_x=\operatorname{Frob}_{y,\deg(x)}$ be its
action on $K_{\bar x}$. Another choice of $y$ replaces
$\operatorname{Frob}_x$ by a conjugate. Define

$$
L(X_0,K,T)
:=\prod_{x\in|X_0|}
\det\bigl(1-T^{\deg(x)}\operatorname{Frob}_x\mid K_{\bar x}\bigr)^{-1}.
\tag{12.6}
$$

For every $n$, only finitely many factors differ from $1$ modulo $T^n$,
so the product converges $T$-adically in $1+T\Lambda[[T]]$, and

$$
L(X_0,K,T)
=\prod_i\det\bigl(1-T\operatorname{Frob}_{X,K}\mid H_c^i(X_{\mathrm{pro}\acute{e}t},K)\bigr)^{(-1)^{i+1}}.
\tag{12.7}
$$

In particular, $L(X_0,K,T)$ is the expansion at zero of a rational
function in $\Lambda(T)$ with value $1$ at zero. If $X_0$ is proper, we
may replace $H_c^i$ by $H^i$.
