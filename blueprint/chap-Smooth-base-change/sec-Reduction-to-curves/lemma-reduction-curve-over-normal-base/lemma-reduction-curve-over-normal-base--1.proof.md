+++
kind = "proof"
of = "lemma-reduction-curve-over-normal-base--1"
order = 682002
+++
The argument does not use that $g$ is affine or smooth. These hypotheses only
serve to make $C$ a smooth affine curve, by base change.

Since $\mathrm{BC}(g,n,q-1)$ holds and $\mathrm{BC}(g,n,q)$ fails,
Lemma [lemma-reduction-field] gives a failure in degree $q$ for an affine
base change $T=\operatorname{Spec}B\to Y$, direct image along a morphism
$f:\operatorname{Spec}\Omega_0\to T$ with $\Omega_0$ a field, and a sheaf $M$
of $\mathbf Z/n$-modules on $\operatorname{Spec}\Omega_0$.

*Algebraic closure.* Let $\Omega$ be an algebraic closure of $\Omega_0$,
and let $\pi:\operatorname{Spec}\Omega\to\operatorname{Spec}\Omega_0$ be the
projection, which is integral and surjective. The hypothesis of
clause [lemma-integral-changes-source-base--1], for $\Lambda=\mathbf Z/n$ and the base change
$Y'\times_YT\to T$, is degree-$(q-1)$ base change for all qcqs morphisms to
$T$ and all sheaves, which is part of $\mathrm{BC}(g,n,q-1)$. The morphism $f$
is a morphism of affine schemes, hence qcqs. So by
clause [lemma-integral-changes-source-base--1] base change in degree $q$ also fails for $f\circ\pi$
and $\pi^{-1}M$.

*Normal base.* Let $R$ be the integral closure in $\Omega$ of the image
of $B\to\Omega$. It is a domain, integrally closed in $\Omega$ and hence
normal. Its fraction field $L$ is algebraically closed: if $\alpha\in\Omega$
is algebraic over the fraction field of the image of $B$, then $d\alpha$ is
integral over that image for some nonzero $d$ in it, so $\alpha\in L$. Thus
$L$ is the algebraic closure of that fraction field in the algebraically
closed field $\Omega$. The morphism $\operatorname{Spec}\Omega\to T$ factors
through $S=\operatorname{Spec}R$, and $S\to T$ is integral. By
clause [lemma-integral-changes-source-base--2], base change in degree $q$ fails for the square with
base change $C=Y'\times_YS\to S$ and direct image along
$f_1:\operatorname{Spec}\Omega\to S$, with the same sheaf $\pi^{-1}M$.

*Constant coefficients.* A sheaf of $\mathbf Z/n$-modules on
$(\operatorname{Spec}\Omega)_{\acute{e}t}$ is a $\mathbf Z/n$-module $N$. An abelian
group of bounded exponent is a direct sum of cyclic groups, so
$N\simeq\bigoplus_i\mathbf Z/m_i$ with $m_i\mid n$. Inverse images commute
with direct sums, and so do higher direct images along the qcqs morphisms
$f_1$ and $h$, because they commute with filtered colimits [Stacks, [09Z1](https://stacks.math.columbia.edu/tag/09Z1)].
Hence the base change map for $N$ is the direct sum of those for the
$\mathbf Z/m_i$, and it fails for some $m=m_i$.

*The source vanishes.* The source of this base change map is the
pullback to $C$ of $R^qf_{1,*}\underline{\mathbf Z/m}$. Its stalk at a
geometric point $\bar s$ of $S$ is the cohomology of
$\operatorname{Spec}\Omega\times_S\operatorname{Spec}\mathcal O^{\mathrm{sh}}_{S,\bar s}$.
This scheme is a limit of étale $\Omega$-schemes. Since $\Omega$ is
algebraically closed, these are disjoint unions of copies of
$\operatorname{Spec}\Omega$. By continuity of cohomology the stalk vanishes
for $q\geq1$. The target is
$R^qh_*$ of the inverse image of $\underline{\mathbf Z/m}$ to $C_\Omega$,
which is $R^qh_*\underline{\mathbf Z/m}$. As the source is zero, the failure
means that $R^qh_*\underline{\mathbf Z/m}\neq0$, and $m\geq2$.
