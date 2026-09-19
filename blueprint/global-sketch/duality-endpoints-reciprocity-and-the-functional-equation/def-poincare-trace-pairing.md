+++
id = "def-poincare-trace-pairing"
kind = "definition"
title = "Poincare cup-product pairing"
order = 119
uses = ["def-cohomological-cup-product", "def-poincare-trace", "def-smooth-proper-datum"]
+++
For a smooth-proper datum $\mathscr X=(X_0,d,X)$, a prime $\ell\neq p$,
and every integer $0\leq i\leq2d$, define

$$
\langle x,y\rangle_i=
\operatorname{tr}^{(-d)}_{X,\ell}(x\smile y):
H^i(X,\Ql)\times H^{2d-i}(X,\Ql)
\longrightarrow\Ql(-d).
$$
