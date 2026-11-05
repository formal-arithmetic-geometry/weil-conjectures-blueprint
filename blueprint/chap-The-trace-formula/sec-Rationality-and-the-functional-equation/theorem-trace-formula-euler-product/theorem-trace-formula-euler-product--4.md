+++
id = "theorem-trace-formula-euler-product--4"
kind = "theorem"
title = "The trace formula as an Euler product (4)"
name_showing = false
order = 1036004
aliases = ["bp-r317-4"]
lean = ["AlgebraicGeometry.WeilComplex.coeff_prod_inv_alternatingCharpolyRevProd_stalk"]
uses = ["definition-weil-structure", "definition-frobenius-operator", "theorem-trace-formula-euler-product--1"]
+++
Let $X_0$ be separated and of finite type over $\mathbf F_q$, let
$\ell\nmid q$, and let $K\in\Dbc(X,\overline{\mathbf Q}_\ell)$ carry a
Weil structure, where $X=X_0\times_{\mathbf F_q}\overline{\mathbf F}_q$.
Let $S,J\subset\mathbf Z$ be finite sets such that
$H_c^i(X_{\mathrm{pro}\acute{e}t},K)=0$ for $i\notin S$ and
$\mathcal H^j(K)=0$ for $j\notin J$. Use $J$ to form $\Delta_x(T)$ as
in [theorem-trace-formula-euler-product--1], and put

$$
C_K(T)=\prod_{i\in S}
\det\bigl(1-T\operatorname{Frob}_{X,K}\mid
H_c^i(X_{\mathrm{pro}\acute{e}t},K)\bigr)^{(-1)^{i+1}}.
$$

For every $n\geq0$ and every finite set $s$ of closed points containing
all those of degree at most $n$, we have

$$
[T^n]\prod_{x\in s}\Delta_x(T)^{-1}=[T^n]C_K(T).
$$

Here $[T^n]$ denotes the coefficient of $T^n$. This is the
coefficientwise Euler-product identity over $\overline{\mathbf Q}_\ell$.
