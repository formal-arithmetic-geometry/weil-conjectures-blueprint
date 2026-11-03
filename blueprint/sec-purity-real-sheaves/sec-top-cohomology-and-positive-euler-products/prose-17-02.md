+++
id = "prose-17-02"
kind = "hidden"
title = "Top cohomology and positive Euler products"
order = 681
+++
We bound the local eigenvalues of a real sheaf by the eigenvalues of
Frobenius on $H^2_c$ of its even tensor powers
(Proposition [sk-p-real-rankin]). Only $H^2_c$ enters, and by
Poincaré duality it is given by the coinvariants of the geometric
monodromy (Lemma [sk-lem-wrp-hc2]).

The two inputs of Rankin's argument sit on the two sides of the trace
formula. On the cohomological side, an affine curve has $H^0_c=0$, so
the $L$-function of a lisse sheaf is the ratio of the characteristic
polynomials on $H^1_c$ and $H^2_c$, and only $H^2_c$ can produce
poles. This group can be computed without knowing anything about
$H^1_c$: its eigenvalues are $q$ times eigenvalues of Frobenius on a
quotient of the generic fibre. On the side of the Euler product,
positivity of the local factors forces each of them to be holomorphic
wherever the product is. For the constant sheaf on $\mathbf G_m$,

$$
L(\mathbf G_m,\overline{\mathbf Q}_\ell,t)=\prod_{x\in|\mathbf G_m|}(1-t^{\deg(x)})^{-1}
=\frac{1-t}{1-qt},
$$

where $1-t$ comes from $H^1_c$ and the pole at $t=q^{-1}$ from
$H^2_c=\overline{\mathbf Q}_\ell(-1)$; each local factor has its poles on the circle
$|t|=1$, outside the disc $|t|<q^{-1}$, as
Lemma [sk-lem-wrp-positive-euler] predicts. Applied to the even tensor
powers of a real sheaf, whose $H^2_c$ is bounded by the determinant
weights of Section [sec-determinant-weights], these two facts give
Proposition [sk-p-real-rankin].
