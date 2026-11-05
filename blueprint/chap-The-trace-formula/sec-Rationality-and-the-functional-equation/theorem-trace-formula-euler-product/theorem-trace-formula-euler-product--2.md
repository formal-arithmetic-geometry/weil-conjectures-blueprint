+++
id = "theorem-trace-formula-euler-product--2"
kind = "theorem"
title = "The trace formula as an Euler product (2)"
name_showing = false
order = 1036002
aliases = ["bp-r317-2"]
lean = ["AlgebraicGeometry.Scheme.Hom.finite_setOf_degreeOver_le", "AlgebraicGeometry.WeilSheaf.X_pow_dvd_lFactor_sub_one"]
uses = ["theorem-trace-formula-euler-product--1"]
+++
Let $X_0$ be of finite type over $\mathbf F_q$. For every $n\geq0$, the
set of closed points $x$ with $\deg(x)\leq n$ is finite.

For a constructible Weil sheaf $\mathcal F$ with
$\overline{\mathbf Q}_\ell$-coefficients, where $\ell\nmid q$, and an
embedding $\iota:\overline{\mathbf Q}_\ell\hookrightarrow\mathbf C$, put

$$
l_{x,\iota}(T)=
\iota\!\left(\det(1-T^{\deg(x)}\operatorname{Frob}_x
\mid\mathcal F_{\bar x})\right)^{-1},
$$

where $\iota$ acts on coefficients. If $\deg(x)>n$, then
$l_{x,\iota}(T)\equiv1\pmod{T^{n+1}}$. Thus only finitely many local
factors can differ from $1$ modulo a prescribed power of $T$.
