+++
id = "theorem-trace-formula-euler-product--1"
kind = "theorem"
title = "The trace formula as an Euler product (1)"
name_showing = false
order = 1037001
aliases = ["bp-r317-1"]
lean = ["AlgebraicGeometry.WeilSheaf.lSeries"]
uses = ["definition-ind-etale-pro-etale-weakly--3", "lemma-stability--1", "lemma-stability--2", "definition-small-pro-etale-site--1", "proposition-pro-etale-coverings--2", "proposition-topos-functoriality--2", "example-locally-constant-functions-w-local--1"]
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
