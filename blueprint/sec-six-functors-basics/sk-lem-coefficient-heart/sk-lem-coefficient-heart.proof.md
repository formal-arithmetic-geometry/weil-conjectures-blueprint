+++
kind  = "proof"
of    = "sk-lem-coefficient-heart"
+++
(1) Given finitely many constructible sheaves, refine their stratifications to a common one;
all three closure properties can then be checked on one stratum $S$.

*Extensions.* Let $0\to F'\to F\to F''\to0$ be exact with $F'$ and $F''$ lisse on $S$. After
passing to a cover, $F''$ is free, and a basis of $F''$ lifts to sections of $F$. This splits
the sequence locally, so $F$ is locally free of finite rank.

*Kernels and cokernels.* On the topologically Noetherian scheme $S$, the kernel and cokernel
of a morphism of lisse $\Lambda_S$-modules are lisse (Bhatt–Scholze, *The pro-étale topology
for schemes*, Corollary 6.8.5); in particular its rank is locally constant on $S$, and no
further stratification is needed. This applies to $E$ and to $\Qlb$, since our coefficient
sheaves are those of loc. cit., by its Lemma 6.8.2 and [sk-prop-sfb-qlbar-colimit-x].
Restriction to strata is exact, so the kernel and cokernel on $X$ are constructible.
Details: [det-lem-coefficient-heart-common-stratification] and
[det-lem-coefficient-heart-closure].

(2) Choose the sites in a fixed universe. A constructible sheaf is determined up to
isomorphism by a finite stratification together with, on each stratum, finite-rank descent
data on a covering, and these form a set. Details: [det-lem-coefficient-heart-small].

(3) Refine the stratification of $F$, by Noetherian induction, so that there is an open
stratum $u\colon S\hookrightarrow X$ with closed complement $i\colon Z\hookrightarrow X$ that is
again a union of strata. The exact sequence $0\to u_!u^*F\to F\to i_*i^*F\to0$ splits off the
stratum $S$, and $u^*F$ is lisse. Applying the same step to $i^*F$ on $Z$ and iterating gives
a finite filtration of $F$ whose subquotients are $a_!(F|_S)$ for the strata
$a\colon S\hookrightarrow X$, and each $F|_S$ is lisse. Details:
[det-lem-coefficient-heart-filtration].
