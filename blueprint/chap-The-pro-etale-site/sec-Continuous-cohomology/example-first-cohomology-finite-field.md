+++
id = "example-first-cohomology-finite-field"
kind = "example"
title = "The first cohomology of a finite field"
order = 198
+++
For $X=\operatorname{Spec}\mathbf F_q$ and $\ell\nmid q$,

$$
H^1(X_{\mathrm{pro}\acute{e}t},\mathbf Z_{\ell,X})\simeq\mathbf Z_\ell,
\qquad H^1(X_{\mathrm{pro}\acute{e}t},\mathbf Q_{\ell,X})\simeq\mathbf Q_\ell.
$$

At each finite level the first cohomology is
$\operatorname{Hom}_{\mathrm{cont}}(\widehat{\mathbf Z},
\mathbf Z/\ell^n)=\mathbf Z/\ell^n$, and the groups in degree zero are
finite, so that their $\varprojlim^1$ vanishes. Hence the sequence
(2.11) for $F_n=(\mathbf Z/\ell^n)_X$
proves the integral statement. Since $X$ is qcqs, its
pro-étale cohomology commutes with filtered colimits [Stacks, [09A3](https://stacks.math.columbia.edu/tag/09A3)], in
particular with inverting $\ell$, and the rational statement follows. For
the constant étale sheaf with value the discrete group $\mathbf Q_\ell$,
on the other hand, the first cohomology is
$\operatorname{Hom}_{\mathrm{cont}}(\widehat{\mathbf Z},\mathbf Q_\ell)=0$,
because a continuous homomorphism from a profinite group to a discrete
torsion-free group has finite, hence zero, image.
