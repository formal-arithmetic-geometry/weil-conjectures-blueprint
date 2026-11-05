+++
id = "theorem-weil-conjectures-smooth-proper-schemes--1"
kind = "theorem"
title = "Existence of integral characteristic polynomials"
order = 1388002
aliases = ["bp-r429-1"]
lean = ["AlgebraicGeometry.Scheme.exists_isWeilFactorization_of_smoothProper"]
uses = ["corollary-point-counting-zeta-function"]
+++
There is an integral Weil factorization $P=(P_0,\ldots,P_{2d})$ of $Z(X_0,T)$ such that, for every prime $\ell\nmid q$ and $0\leq i\leq2d$,
$$
P_i=\overline P_{i,\ell}\quad\hbox{in }\overline{\mathbf Q}_\ell[T].
$$
For every complex root $z$ of $P_i$, one has $\lvert z\rvert=q^{-i/2}$. Moreover, the multiset of complex roots of $P_{2d-i}$ is the image of that of $P_i$ under $z\mapsto(q^dz)^{-1}$.
