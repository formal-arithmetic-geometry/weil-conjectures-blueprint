+++
id = "prop-duality-reciprocity"
kind = "theorem"
title = "Duality reciprocity"
order = 124
tags = ["latex:proposition"]
uses = ["def-betti-numbers", "def-canonical-cohomological-factors", "def-determinant-constants", "def-smooth-proper-cohomological-family", "def-smooth-proper-datum", "prop-integral-recovery", "prop-poincare-pairing"]
+++
Let $\mathscr X=(X_0,d,X)$ be a smooth-proper datum. For every prime
$\ell\neq p$ and $0\leq i\leq2d$, Poincare duality identifies the multiset of
Frobenius eigenvalues in degree $2d-i$ with

$$
\left\{\frac{q^d}{\alpha}:\alpha
\text{ is an eigenvalue in degree }i\right\},
$$

including algebraic multiplicity. Moreover,

$$
b_i=b_{2d-i},
\qquad
D_iD_{2d-i}=q^{db_i},
$$

and the integral factors satisfy the Laurent-polynomial identity

$$
P_{2d-i}(q^{-d}T^{-1})
=(-1)^{b_i}T^{-b_i}D_i^{-1}P_i(T)
\quad\text{in }\mathbf Q[T,T^{-1}].
$$

For $i=d$, the middle pairing is $(-1)^d$-symmetric. In particular,
if $d$ is odd, then $b_d$ is even.
