+++
id = "prop-integral-factor-existence"
kind = "theorem"
title = "Existence and uniqueness of integral cohomological factors"
order = 110
tags = ["latex:proposition"]
uses = ["def-frobenius-characteristic-factors", "def-point-count-zeta", "def-smooth-proper-datum", "prop-euler-product", "prop-trace-determinant", "prop-weight-purity"]
+++
For every smooth-proper datum $\mathscr X=(X_0,d,X)$, there is a unique
tuple of polynomials

$$
(P_0(\mathscr X),\ldots,P_{2d}(\mathscr X))\in\mathbf Z[T]^{2d+1}
$$

such that, for every $0\leq i\leq2d$, one has
$P_i(\mathscr X)(0)=1$ and, for every prime $\ell\neq p$, coefficient
extension gives

$$
(\mathbf Z[T]\longrightarrow\Ql[T])\bigl(P_i(\mathscr X)\bigr)
=P_{i,\ell}.
$$

The tuple is independent of every auxiliary algebraic closure and every
embedding used to compare algebraic numbers with $\ell$-adic numbers.
