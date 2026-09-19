+++
id = "prop-integral-recovery"
kind = "theorem"
title = "Integral factor recovery"
order = 112
tags = ["latex:proposition"]
uses = ["def-canonical-cohomological-factors", "def-frobenius-characteristic-factors", "def-point-count-zeta", "def-smooth-proper-datum", "prop-integral-factor-existence", "prop-trace-determinant"]
+++
Let $\mathscr X=(X_0,d,X)$ be a smooth-proper datum. For every integer
$0\leq i\leq2d$, its canonical factor $P_i\in\mathbf Z[T]$ has
$P_i(0)=1$ and, for every prime $\ell\neq p$, satisfies

$$
(\mathbf Z[T]\longrightarrow\Ql[T])(P_i)=P_{i,\ell}.
$$

If another family
$(\widetilde P_i)_{0\leq i\leq2d}$ in $\mathbf Z[T]$ has constant
term one and the same
realizations for all primes $\ell\neq p$, then
$\widetilde P_i=P_i$ for every $0\leq i\leq2d$. Moreover,

$$
Z(X_0,T)=\prod_{i=0}^{2d}P_i(T)^{(-1)^{i+1}}
\quad\text{in }\mathbf Q(T).
$$

For every $0\leq i\leq2d$ and every prime $\ell\neq p$,

$$
\deg P_i=\dim_{\Ql}H^i(X,\Ql).
$$
