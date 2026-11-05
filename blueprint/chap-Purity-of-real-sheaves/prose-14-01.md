+++
id = "prose-14-01"
kind = "hidden"
title = "Purity of real sheaves"
order = 1086
+++
In Chapter [chap-The-Deligne-Laumon-theorem-for-curves] the Fourier transform of a pure sheaf
produces a lisse sheaf $M'$ whose Frobenius eigenvalues we cannot compute.
What we do know is that a twist of $M'$ is a quotient of a sheaf whose traces
are real, and from this alone we must conclude that $M'$ is pure. In
Chapter [chap-The-Deligne-Laumon-theorem-in-general] the same need returns for the direct
images of a family of curves, which we can make real but do not know to be
mixed. Both arguments rest on one theorem
(Theorem [theorem-purity-real-sheaves-curves]):

> on a smooth geometrically connected curve, every irreducible
> constituent of a real lisse Weil sheaf is pure, of weight equal to its
> determinant weight.

Before this theorem we know the weights of one kind of sheaf only: a lisse
sheaf of rank one on a curve has finite geometric monodromy, and therefore it is
pure (Section [sec-Sheaves-of-rank-one]). In particular the determinant
of every lisse sheaf is pure, and its weight divided by the rank, the determinant
weight, is the average weight of the eigenvalues at each point. The theorem says that on an
irreducible constituent of a real sheaf no eigenvalue deviates from this
average.

The tool is the trace formula. On an affine curve $U_0$ it expresses the
$L$-function of a lisse sheaf $\mathcal G$ as

$$
L(U_0,\mathcal G,t)
=\prod_{x\in|U_0|}\det(1-\operatorname{Frob}_xt^{\deg(x)}\mid\mathcal G_{\bar x})^{-1}
=\frac{\det(1-Ft\mid H^1_c(U,\mathcal G))}{\det(1-Ft\mid H^2_c(U,\mathcal G))}.
$$

The poles of the right-hand side are controlled by $H^2_c$, which is easy to
compute (Lemma [lemma-degree-zero-top-cohomology]). On the left, a large
eigenvalue at a point $x$ gives a pole of the local factor at $x$ close to the
origin. But this pole could be cancelled by a zero of the product of the other
factors, as in $(1-2t)^{-1}\cdot(1-2t)=1$. Positive factors, however, cannot cancel in
this way. Indeed, suppose all factors are power series with nonnegative coefficients
and constant term $1$. Then the coefficients of each factor are bounded by
those of the product, and Lemma [lemma-positivity-convergence] shows that
no factor can converge on a smaller disc than the product.

This idea is Rankin's. In 1939 he improved the bound for Ramanujan's function
$\tau(n)$ to $O(n^{29/5})$ by studying the Dirichlet series
$\sum_n\tau(n)^2n^{-s}$, whose coefficients are nonnegative. Deligne used the
same argument in his first proof [deligne74].

For the Euler factors to be positive, the traces must be real. We therefore call a lisse
Weil sheaf real if its local characteristic polynomials have real coefficients
under the fixed embedding $\iota$ of Convention [situation-weil]
(Definition [definition-real-sheaves]). For example, every sheaf with rational
characteristic polynomials is real, such as a Tate twist of the constant
sheaf. On an even tensor power $\mathcal G^{\otimes2m}$ of a
real sheaf the traces are $2m$th powers of real numbers, and this makes the
Euler factors positive. From this,
Proposition [proposition-bound-largest-determinant-weight] bounds each
local eigenvalue $\alpha$ of $\mathcal G$ by $|\iota(\alpha)|^2\le q_x^\beta$,
where $\beta$ is the largest determinant weight of the constituents.

This is not yet the theorem, because a real sheaf need not be pure. For
example, the sheaf $\overline{\mathbf Q}_\ell\oplus\overline{\mathbf Q}_\ell(-1)$ is real, with constituents of
weights $0$ and $2$, but the bound only gives $2$ for both. To separate the
constituents we pass to exterior powers. In
$\bigwedge^2(\overline{\mathbf Q}_\ell\oplus\overline{\mathbf Q}_\ell(-1))=\det\overline{\mathbf Q}_\ell(-1)\otimes\overline{\mathbf Q}_\ell$ the factor
$\overline{\mathbf Q}_\ell$ appears multiplied by the known eigenvalue $q_x$ of $\det\overline{\mathbf Q}_\ell(-1)$,
so the bound $2$ for this summand leaves the bound $0$ for $\overline{\mathbf Q}_\ell$ itself.
In general,
Proposition [proposition-determinant-weights-tensor-operations](2) finds
the exterior power in which a given group of constituents carries the
largest determinant weight, and the same argument applies there. Positivity,
however, only ever gives upper bounds. The lower bound comes from applying
the same argument to the dual, and in Chapter [chap-Proof-of-the-Weil-conjectures] this
role is played by Poincaré duality.
