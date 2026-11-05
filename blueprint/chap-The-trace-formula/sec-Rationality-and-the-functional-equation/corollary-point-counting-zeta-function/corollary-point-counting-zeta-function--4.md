+++
id = "corollary-point-counting-zeta-function--4"
kind = "corollary"
title = "Euler product"
order = 1040005
aliases = ["bp-r318-4"]
lean = ["AlgebraicGeometry.Scheme.Hom.zetaSeries_eq_tprod"]
+++
Let $X_0$ be any scheme of finite type over $\mathbf F_q$. Then, in
$\mathbf Q[[T]]$,

$$
Z(X_0,T)=\prod_{x\in|X_0|}(1-T^{\deg(x)})^{-1},
\qquad \deg(x)=[\kappa(x):\mathbf F_q].
$$

The product is over closed points and converges coefficient by coefficient:
the coefficient of $T^n$ is already determined by the finitely many points
of degree at most $n$.
