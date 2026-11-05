+++
id = "theorem-trace-formula-euler-product--3"
kind = "theorem"
title = "The trace formula as an Euler product (3)"
name_showing = false
order = 1036003
aliases = ["bp-r317-3"]
lean = ["AlgebraicGeometry.WeilSheaf.lSeries", "AlgebraicGeometry.WeilSheaf.hasProd_lFactor"]
uses = ["theorem-trace-formula-euler-product--2"]
+++
For $X_0$, $\mathcal F$, and $\iota$ as in
[theorem-trace-formula-euler-product--2], define

$$
L_\iota(X_0,\mathcal F,T)=\prod_{x\in|X_0|}l_{x,\iota}(T)
\quad\text{in }\mathbf C[[T]].
$$

The net of finite partial products converges to this series in the
product topology on its coefficients. Every coefficient is eventually
constant, and the constant coefficient of the limit is $1$.

This is the topological product used in Lean for Weil sheaves after
transport by $\iota$. For general Weil complexes, the Euler product is
expressed by the coefficient identity in
[theorem-trace-formula-euler-product--4].
