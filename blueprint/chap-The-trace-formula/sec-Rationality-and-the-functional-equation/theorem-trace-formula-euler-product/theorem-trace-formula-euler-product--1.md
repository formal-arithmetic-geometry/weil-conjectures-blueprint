+++
id = "theorem-trace-formula-euler-product--1"
kind = "theorem"
title = "The trace formula as an Euler product (1)"
name_showing = false
order = 1036001
aliases = ["bp-r317-1"]
lean = ["AlgebraicGeometry.WeilSheaf.nonempty_equiv_stalkAt"]
uses = ["definition-weil-structure"]
+++
Let $X_0$ be a scheme over $\mathbf F_q$, let $\ell\nmid q$, and let
$\mathcal F$ be a constructible Weil sheaf with $\overline{\mathbf Q}_\ell$-coefficients.
Put $X=X_0\times_{\mathbf F_q}\overline{\mathbf F}_q$. Suppose that two
geometric points of $X$ lie over the same point $x$ of $X_0$ with finite
residue field. For $m\geq0$, suppose that both geometric points are
compatible with the $m$-th geometric Frobenius, up to the corresponding
Frobenius on $\overline{\mathbf F}_q$. Then their stalks, equipped with
the operators induced by the $m$-fold iterated Weil structure, are
isomorphic as Frobenius modules. In particular, their Frobenius operators are conjugate.

Apply this to the cohomology sheaves of a Weil complex
$K\in\Dbc(X,\overline{\mathbf Q}_\ell)$ and to $m=\deg(x)$.
If $J\subset\mathbf Z$ is finite and $\mathcal H^j(K)=0$ for $j\notin J$,
the local alternating determinant is

$$
\Delta_x(T)=\prod_{j\in J}
\det\bigl(1-T^{\deg(x)}\operatorname{Frob}_x\mid
\mathcal H^j(K)_{\bar x}\bigr)^{(-1)^j}.
$$

Its inverse is the local factor of $L(X_0,K,T)$, and it is independent
of the geometric point chosen over $x$. In Lean the stalk is the
Frobenius module on each cohomology sheaf; this finite product is
`LinearMap.alternatingCharpolyRevProd`.
