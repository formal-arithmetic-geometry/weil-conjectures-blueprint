+++
id = "cor-sf-no-bounded-hypercover"
kind = "theorem"
title = "The question of a bounded weakly contractible hypercovering has a negative answer"
order = 3742
tags = ["latex:corollary"]
uses = ["def-weil-full-cohomological-dimension", "def-weil-pbc-proetale-site", "lem-sf-acyclic-hypercover-terms-vanishing", "lem-sf-hypercover-nonempty-terms", "rem-sf-continuity-obstruction", "rem-sf-fullcd-general-form"]
+++
Let $T$ be a scheme and let $U\to T$ be a nonempty object of the
small pro-étale site $T_{\Proet}$ of
[def-weil-pbc-proetale-site]. Then:

1. **(i)** for every hypercovering $K$ of $U$ with terms
$K_n=\{U_{n,i}\to U\}_{i\in I_n}$ and every integer $N$ there are $n>N$
and $i\in I_n$ with $U_{n,i}\neq\emptyset$; in particular $U$ admits no
*bounded* hypercovering, whether its terms are required to be weakly
contractible or not;
1. **(ii)** consequently the question whether every affine finite-type scheme
over a separably closed field of dimension at most $d$, and every
base-changed source of [def-weil-full-cohomological-dimension], admits a
weakly contractible hypercovering whose length is bounded by a function of
$d$ alone has a *negative* answer for every nonempty member of that class
and every $d$, the obstruction being the coskeleton condition (b) of
[lem-sf-hypercover-nonempty-terms] and not the weak contractibility of the
terms; and the implication recorded in [rem-sf-fullcd-general-form], that
a bounded weakly contractible hypercovering would give
$H^q(U,\mathcal F)=0$ for every $q>N$ and *every* sheaf $\mathcal F$
of abelian groups, therefore has no instance and supplies no bound on the
vanishing degree;
1. **(iii)** the residue isolated in [rem-sf-continuity-obstruction] is
accordingly not reduced by the hypercovering route: what the hypercoverings of
Pro-étale Cohomology, Lemma 61.14.1,
[Tag 09A1](https://stacks.math.columbia.edu/tag/09A1), with Lemma 61.14.2,
[Tag 09A2](https://stacks.math.columbia.edu/tag/09A2), bound is the
vanishing degree of a *given* coefficient sheaf, through
[lem-sf-acyclic-hypercover-terms-vanishing], and never the vanishing degree
of all sheaves at once.

## Proof

(i) is [lem-sf-hypercover-nonempty-terms], whose proof never uses the
weak contractibility of the terms. For (ii) it suffices to observe that a
nonempty affine finite-type scheme over a separably closed field, and every
nonempty base-changed source $\overline X\times_YV$ of
[def-weil-full-cohomological-dimension], is a nonempty object of its own
small pro-étale site, so that (i)
applies; the second half of (ii) restates the implication recorded in
[rem-sf-fullcd-general-form] and notes that its hypothesis is never
satisfied. (iii) restates [rem-sf-continuity-obstruction] and names
[lem-sf-acyclic-hypercover-terms-vanishing] as the hypercover-theoretic
statement that is available in its place.
