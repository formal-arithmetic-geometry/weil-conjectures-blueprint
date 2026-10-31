+++
kind  = "proof"
of    = "lem-weil-pbc-comparison-injective-acyclicity"
+++
We apply Cartan's criterion, part (2) of [lem-weil-pbc-cech-criterion], to
$F=\nu_X^*I$, with $P$ the class of affine pro-etale objects. (For sheaves of
$\Lambda$-modules the same argument runs with free sheaves of
$\Lambda$-modules in place of free abelian sheaves.)

Let $U$ be an affine pro-etale object and $R$ a covering sieve of $U$. By
[lem-weil-pbc-ind-etale-basis] and [lem-weil-pbc-ind-etale-stability], $R$
contains a finite jointly surjective family $V_a\to U$ of affine pro-etale
objects. Put $V=\coprod_aV_a$, an affine pro-etale object, and let
$f\colon V\to U$ be the induced map; it generates a covering sieve. The terms
$V\times_U\cdots\times_UV$ of its Cech nerve are again affine pro-etale. A
cohomology class on $U$ that vanishes on every $V_a$ vanishes on $V$, because
cohomology of a finite disjoint union is the product of the cohomologies.

It remains to show that every positive-degree Cech cocycle of $\nu_X^*I$
along $f$ is a coboundary. Write $U=\varprojlim_iU_i$ with $U_i$ affine etale
over $X$. By the descent of finite-presentation data
[lem-weil-pbc-etale-finite-data-descent], $f$ is the limit of affine etale
maps $f_\lambda\colon V_\lambda\to U_\lambda$ between affine etale
$X$-schemes, which are surjective at all sufficiently late stages, and the
terms of the Cech nerve of $f$ are the limits of the corresponding terms for
the $f_\lambda$, formed by fibre products. By
[lem-weil-pbc-comparison-sections], applied to each term, the Cech complex
[def-weil-pbc-cover-cech] of $\nu_X^*I$ along $f$ is the filtered colimit of
the Cech complexes of $I$ along the etale coverings $f_\lambda$. Each of these
has no positive cohomology by part (1) of [lem-weil-pbc-cech-criterion],
since $I$ is injective, and filtered colimits are exact. Cartan's criterion
now gives $H^q(U,\nu_X^*I)=0$ for $q>0$. The equivalent form on $U_{\Proet}$
is [lem-weil-pbc-proetale-restriction-injectives]. This is the argument of
[Stacks Project, Tag 099U](https://stacks.math.columbia.edu/tag/099U).
