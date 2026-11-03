+++
id = "prose-17-05"
kind = "hidden"
title = "Rankin's argument"
order = 690
+++
Proposition [sk-p-real-rankin] only bounds the local eigenvalues
by the largest determinant weight. To bound the eigenvalues of each
constituent by its own determinant weight, we apply the proposition to
exterior powers, which separate the determinant weights of the simple
factors.

Tensor powers cannot do this. Suppose $\mathcal G=\mathcal G_1\oplus\mathcal G_2$
with determinant weights $\gamma_1>\gamma_2$. In
$\mathcal G^{\otimes m}$ the largest determinant weight $m\gamma_1$
belongs to the factors of $\mathcal G_1^{\otimes m}$, and every factor
involving $\mathcal G_2$ lies strictly below it, so the bound of
Proposition [sk-p-real-rankin] says nothing sharp about
$\mathcal G_2$. An exterior power uses each basis vector of
$\mathcal G_1$ at most once. If $r_1$ is the rank of $\mathcal G_1$,
every graded piece of $\bigwedge^{r_1+1}\mathcal G$ involves
$\mathcal G_2$, and the summand $\det\mathcal G_1\otimes\mathcal G_2$
has the largest determinant weight $r_1\gamma_1+\gamma_2$. The
eigenvalues of $\det\mathcal G_1$ are known by
Corollary [sk-d-real-detweights], and so a bound for this summand is a
bound for $\mathcal G_2$. The argument runs on an affine curve, where
the proposition applies, and passes to an arbitrary curve by
restriction to affine opens, which preserves irreducibility.
