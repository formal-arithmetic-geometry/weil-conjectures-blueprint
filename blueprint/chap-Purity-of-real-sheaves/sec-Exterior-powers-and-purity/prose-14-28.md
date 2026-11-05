+++
id = "prose-14-28"
kind = "hidden"
title = "Exterior powers and purity"
order = 1168
+++
Proposition [proposition-bound-largest-determinant-weight] only bounds the local eigenvalues
by the largest determinant weight. To bound the eigenvalues of each
constituent by its own determinant weight, we apply the proposition to
exterior powers, which separate the determinant weights of the simple
factors.

Tensor powers cannot do this. For example, suppose $\mathcal G=\mathcal G_1\oplus\mathcal G_2$
with determinant weights $\gamma_1>\gamma_2$. In
$\mathcal G^{\otimes m}$ the largest determinant weight $m\gamma_1$
belongs to the factors of $\mathcal G_1^{\otimes m}$, while every factor
involving $\mathcal G_2$ lies strictly below it. So the bound of
Proposition [proposition-bound-largest-determinant-weight] says nothing sharp about
$\mathcal G_2$.

An exterior power, by contrast, uses each basis vector of $\mathcal G_1$ at most once. Thus if
$r_1$ is the rank of $\mathcal G_1$, every graded piece of
$\bigwedge^{r_1+1}\mathcal G$ involves $\mathcal G_2$, and the summand
$\det\mathcal G_1\otimes\mathcal G_2$ has the largest determinant weight
$r_1\gamma_1+\gamma_2$. Since Corollary [corollary-determinant-weights] gives the
eigenvalues of $\det\mathcal G_1$, a bound for this summand is a
bound for $\mathcal G_2$. We argue on an affine curve, where
the proposition applies, and then pass to an arbitrary curve by
restricting to affine opens, which preserves irreducibility.
