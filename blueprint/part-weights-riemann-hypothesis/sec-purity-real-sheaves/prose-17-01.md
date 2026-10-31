+++
id = "prose-17-01"
kind = "hidden"
title = "Purity of real sheaves on curves"
order = 679
+++
The trace formula tells us about alternating sums of traces, and in an
alternating sum eigenvalues of different sizes may cancel. On an affine
curve $U_0$, for instance, it writes the $L$-function of a lisse sheaf
$\mathcal G$ as

$$
L(U_0,\mathcal G,t)
=\prod_{x\in|U_0|}\det(1-\operatorname{Frob}_xt^{\deg(x)}\mid\mathcal G_{\bar x})^{-1}
=\frac{\det(1-Ft\mid H^1_c(U,\mathcal G))}{\det(1-Ft\mid H^2_c(U,\mathcal G))}.
$$

The poles of the right-hand side are controlled by $H^2_c$, which is
easy (Lemma [sk-lem-wrp-hc2]), but a pole of one local factor on the left
could be cancelled by a zero of the infinite product of the others.
Already for two factors this happens: $(1-2t)^{-1}\cdot(1-2t)=1$ is
holomorphic everywhere, although the first factor has a pole at
$t=1/2$. Positivity rules this out. If all factors are power series with nonnegative
coefficients and constant term $1$, the coefficients of each factor are
bounded by those of the product, so no factor can converge on a smaller
disc than the product (Lemma [sk-lem-wrp-positive-euler]).

This idea is Rankin's. In 1939 he improved the bound for Ramanujan's
function $\tau(n)$ to $O(n^{29/5})$ by studying the Dirichlet series
$\sum_n\tau(n)^2n^{-s}$, whose coefficients are nonnegative, and its
analytic continuation. Deligne used the same device in his first
proof (De1), and in this Part it is what turns the trace
formula into an upper bound on eigenvalues. To make Euler factors positive we need real traces. We
call a lisse Weil sheaf $\mathcal G$ real if its local characteristic
polynomials have real coefficients under $\iota$
(Definition [sk-def-wrp-real-definition]); for example, every sheaf
defined over $k_0$ with rational characteristic polynomials is real.
Then the traces of Frobenius on an even tensor power
$\mathcal G^{\otimes2m}$ are $2m$th powers of real numbers, and the
local factors of $L(U_0,\mathcal G^{\otimes2m},t)$ have nonnegative
coefficients. The Part opening explains how this bounds each local
eigenvalue $\alpha$ of $\mathcal G$ by
$|\iota(\alpha)|^2\le q_x^\beta$, where $\beta$ is the largest
determinant weight of the constituents
(Proposition [sk-p-real-rankin]).

The main theorem of the section is sharper
(Theorem [sk-p-real-purity]):

> on a smooth geometrically connected curve, every irreducible
> constituent of a real lisse Weil sheaf is pure, of weight equal to its
> determinant weight.

In particular a real lisse sheaf is mixed, but it need not be
pure: $\overline{\mathbf Q}_\ell\oplus \overline{\mathbf Q}_\ell(-1)$ is real, with constituents of weights $0$
and $2$, and Proposition [sk-p-real-rankin] gives only the bound $2$
for both. To bound a constituent by its own determinant weight, we
group the constituents by determinant weight,
$\gamma_1>\gamma_2>\cdots$, and look at the summand
$\det\mathcal G_1\otimes\cdots\otimes\det\mathcal G_{i-1}\otimes\mathcal G_i$
of an exterior power of $\mathcal G$. By
Proposition [sk-prop-walg-determinant-weights](2) this summand carries the
largest determinant weight of that exterior power, so
Proposition [sk-p-real-rankin] applies to it, and dividing by the
known eigenvalues of the determinants leaves the bound $\gamma_i$ for
$\mathcal G_i$. The dual of a real sheaf is real, with determinant
weights $-\gamma_j$, and the same argument applied to it gives the
reverse inequality. Positivity only ever gives upper bounds; the lower
bound comes from duality, as it will again in
Section [sec-zeta-weil].

The theorem is used twice: in Section [sec-deligne-laumon-a1], to
show that a twist of the Fourier transform of a pure sheaf is pure, and
in Section [sec-deligne-laumon-general], where we restrict to curves to show that
real sheaves on any base are mixed. A pure sheaf need not be real, but
twisting it to weight zero and adding its dual makes it real
(Proposition [sk-prop-wrp-real-envelope]). The Fourier argument also needs
two facts about pure sheaves on curves that are proved with the same
comparison of an Euler product with its factors. The middle extension
$j_*$ does not increase weights at the boundary points
(Proposition [sk-p-real-semi]): here the boundary Euler factors
of $j_*\mathcal F$ are compared with the $L$-function on the open, and
tensor powers remove an error of $2$ in the weight. And the weight of a
pure sheaf is the growth rate of its sums of squared traces
(Theorem [sk-thm-wrp-l2-dictionary]): here the Euler product of
$\mathcal G\otimes\mathcal G$ for real $\mathcal G$ is shown to have a
pole on the circle determined by $H^2_c$.
