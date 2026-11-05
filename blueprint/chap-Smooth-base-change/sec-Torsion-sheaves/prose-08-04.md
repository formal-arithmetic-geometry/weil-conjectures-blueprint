+++
id = "prose-08-04"
kind = "hidden"
title = "Torsion sheaves (2)"
order = 663
+++
As for proper base change, we transport the problem to the étale site by
the comparison theorems of Chapter [chap-The-pro-etale-site]. Since
$F$ is classical, $F=\nu_X^*F_{\acute{e}t}$ for a torsion abelian sheaf
$F_{\acute{e}t}$ on $X_{\acute{e}t}$. As $f$ and $f'$ are qcqs,
Theorem [theorem-comparison-direct-images] and
Lemma [lemma-naturality-pasting-comparison] identify both sides and the
base change map with the inverse images of the corresponding étale objects.
We may therefore work on the étale sites in the proof below, where $g^{-1}$
denotes inverse image of étale sheaves.

We follow the second proof of [Stacks, [0EYU](https://stacks.math.columbia.edu/tag/0EYU)], an induction on the
cohomological degree $q$. The idea is to concentrate a first failure of
base change in a single sheaf $R^qh_*\mathbf Z/m$, and then to show that
this sheaf vanishes. In degree zero, by contrast, the base change map can be
computed directly on sections. Moreover, base change may be checked étale
locally and is stable under composition, so that étale coordinates reduce
us to the case where $g$ is a smooth affine curve.

Now suppose that base change holds in degrees below $q$ but fails in degree
$q$. The failure persists when we shrink the source of the direct image by
limit arguments, and also when we make integral changes of the source and
of the base. In this way it is concentrated in a single situation, in which
the coefficients are constant, equal to $\mathbf Z/m$, and we have a smooth
affine curve $C$ over the spectrum $S$ of a normal domain whose fraction
field $L$ is algebraically closed, together with the morphism
$h:C_\Omega\to C$ for an algebraically closed extension $\Omega$ of $L$.
But in this situation $R^qh_*\mathbf Z/m=0$. For $q\geq2$ the reason is that affine curves over
an algebraically closed field have no cohomology in degree at least two
(Appendix [chap-Cohomology-of-torsion-sheaves-on-curves]). For $q=1$ it follows from the
invariance of $H^1$ of curves and an extension theorem for covers
(Section [sec-Change-of-base-field]).
