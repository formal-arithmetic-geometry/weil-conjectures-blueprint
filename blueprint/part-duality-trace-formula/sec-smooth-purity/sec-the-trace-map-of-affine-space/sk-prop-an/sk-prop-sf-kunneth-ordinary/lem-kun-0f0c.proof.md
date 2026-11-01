+++
kind  = "proof"
of    = "lem-kun-0f0c"
+++
This is [Stacks, Tag 0F0C], and we follow its proof. The assertion is
local on $Y'$ and on $Y$, so we may assume $Y$ and $Y'$ affine, in
particular quasi-compact; then $X$ and $X'$ are quasi-compact, and the
dimensions of the fibres of the proper morphism $f$, and hence of its
base change $f'$, are bounded by some integer $e$ (Stacks Project,
Morphisms, Lemma 29.29.5). Hence $\kuncd(f),\kuncd(f')<\infty$
(Stacks Project, Étale Cohomology, Lemma 59.92.2), and [lem-kun-0f11]
applies to $f$ and $f'$ ([def-kun-cd]).

Write $K=\operatorname{hocolim}_N\tau_{[-N,N]}K$
([def-kun-truncations], [lem-kun-hocolim-truncations]). Each
$\tau_{[-N,N]}K$ is bounded, hence bounded below with torsion
cohomology, so the exchange morphism is an isomorphism for it by
[thm-weil-pbc-bounded-below]. The exchange morphism of
[def-kun-unbounded-exchange] is natural in $K$
([lem-kun-unbounded-exchange-natural]), and both sides
commute with homotopy colimits: $g^{-1}$ is exact, and $Rf_*$,
$Rf'_*$ preserve direct sums by [lem-kun-0f11], as just shown. Passing to the homotopy colimit therefore gives
the assertion for arbitrary $K$.
