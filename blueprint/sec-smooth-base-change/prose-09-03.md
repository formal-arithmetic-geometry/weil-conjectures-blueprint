+++
id = "prose-09-03"
kind = "hidden"
title = "Outline of the proof for torsion sheaves"
order = 2211
+++
As for proper base change, we transport the problem to the étale site by
the comparison theorems of Section “The pro-étale site and its comparison theorems”. Since
$F$ is classical, $F=\nu_X^*F_{\mathrm{\acute et}}$ for a torsion abelian sheaf
$F_{\mathrm{\acute et}}$ on $X_{\mathrm{\acute et}}$. As $f$ and $f'$ are qcqs,
[sk-thm-pe-direct-image-comparison] and
[sk-lem-sbc-exchange-compatibility] identify both sides and the
base change map with the inverse images of the corresponding étale objects.
We may therefore work on the étale sites in the proof below, where $g^{-1}$
denotes inverse image of étale sheaves.

We follow the second
proof of [Stacks, Tag 0EYU](https://stacks.math.columbia.edu/tag/0EYU) (see also SBCBP), which is
an induction on the cohomological degree $q$. In degree zero the base
change map can be computed on sections. Since base change may be checked
étale locally and is stable under composition, étale coordinates then
reduce us to the case where $g$ is a smooth affine curve. Suppose base
change holds in degrees below $q$ and fails in degree $q$. A failure in
degree $q$ persists when we shrink the source of the direct image by limit
arguments and when we make integral changes of the source and of the base.
In this way we reduce the failure to a single situation: constant coefficients
$\mathbf Z/m$, a smooth affine curve $C$ over the spectrum $S$ of a
normal domain whose fraction field $L$ is algebraically closed, and the
morphism $h:C_\Omega\to C$ for an algebraically closed extension $\Omega$
of $L$.
But in this situation $R^qh_*\mathbf Z/m=0$. For $q\geq2$, this holds because affine
curves over an algebraically closed field have no cohomology in degree
at least two (Appendix “Cohomology of curves”). For $q=1$, we must show that every class in $H^1(C_\Omega,\mathbf Z/m)$
vanishes étale locally on $C$. Such a class comes from a
$\mathbf Z/m$-torsor on $C_L$, and this torsor becomes trivial on a
finite étale Galois cover $Z$ of $C_L$, namely a connected component of
the torsor. By the extension theorem for generic Galois covers
[Stacks, Tag 0EZJ](https://stacks.math.columbia.edu/tag/0EZJ), recalled in the proof of
[sk-thm-vanishing] below, $Z$ extends to a finite étale
cover of $C$, and on this cover the class vanishes.
