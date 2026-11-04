+++
id = "prose-14-23"
kind = "hidden"
title = "Rankin's bound (1)"
order = 1143
+++
We bound the local eigenvalues of a real sheaf by the eigenvalues of
Frobenius on $H^2_c$ of its even tensor powers
(Proposition [proposition-bound-largest-determinant-weight]). Only $H^2_c$ is needed, and
Lemma [lemma-degree-zero-top-cohomology] computes it by Poincaré
duality as the coinvariants of the geometric monodromy.

Rankin's argument uses one fact from each side of the trace
formula. On the cohomological side, an affine curve has $H^0_c=0$, so
only $H^2_c$ can produce poles of the $L$-function. We can compute
this group without knowing anything about $H^1_c$. Its eigenvalues are
$q$ times eigenvalues of Frobenius on a quotient of the generic fibre. On
the side of the Euler product, if the local factors have nonnegative
coefficients, then each of them is holomorphic wherever the product is.

For example, for the constant sheaf on $\mathbf G_m$ we have

$$
L(\mathbf G_m,\overline{\mathbf Q}_\ell,t)=\prod_{x\in|\mathbf G_m|}(1-t^{\deg(x)})^{-1}
=\frac{1-t}{1-qt},
$$

where $1-t$ comes from $H^1_c$ and the pole at $t=q^{-1}$ from
$H^2_c=\overline{\mathbf Q}_\ell(-1)$. Each local factor has its poles on the circle
$|t|=1$, outside the disc $|t|<q^{-1}$, as
Lemma [lemma-positivity-convergence] predicts. We apply the two facts to
the even tensor powers of a real sheaf. Their $H^2_c$ is bounded by the
determinant weights of Section [sec-Determinant-weights], and this gives
Proposition [proposition-bound-largest-determinant-weight].
