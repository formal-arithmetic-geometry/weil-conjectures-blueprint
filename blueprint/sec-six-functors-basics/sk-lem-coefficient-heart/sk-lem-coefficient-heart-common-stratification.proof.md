+++
kind  = "proof"
of    = "det-lem-coefficient-heart-common-stratification"
+++
(1) The pairwise intersections of strata of two stratifications are locally closed and
finitely many, and partition $X$. Iterate for finitely many stratifications. Each locally
closed subset of a Noetherian space has finitely many connected components, each locally
closed; replacing strata by their components keeps a finite stratification. For the order:
by Noetherian induction, a finite stratification of a Noetherian space has a stratum which
is open in $X$ (let $\eta$ be the generic point of an irreducible component $C$ of $X$ and $S\ni\eta$ its
stratum; write $S=U\cap Z$ with $U$ open and $Z$ closed; then $Z\supseteq C$, and
$W=U\smallsetminus\bigcup_{C'\ne C}C'$, the union over the other, finitely many,
components, is an open subset of $X$ containing $\eta$ and contained in $C\cap U\subseteq S$.
Replace $S$ by $W$ and $S\smallsetminus W$, which is again locally closed). Removing it and repeating on the closed
complement, the process terminates by Noetherian induction and produces the order.

(2) If $M|_{U_i}$ is free of finite rank on a cover $\{U_i\to S\}$, then the base change
$\{U_i\times_ST\to T\}$ is a cover of $T$ on which $M|_T$ is free of the same rank, since
pullback preserves free modules (it preserves $\Lambda$ by
[sk-prop-sfb-cartesian-coefficients] and direct sums).

(3) $g^{-1}$ is exact as the inverse image of a morphism of topoi. A sheaf on $X$ vanishes iff
its restriction to every stratum vanishes: every point of $X$ lies in a stratum, and
vanishing on the pro-étale site can be checked after restriction to the strata by the
localization sequences $0\to j_!j^*N\to N\to i_*i^*N\to0$ for an open stratum $j$ and its
closed complement $i$, using induction on the number of strata. Applying this to kernels,
cokernels and cohomology gives the claim.
