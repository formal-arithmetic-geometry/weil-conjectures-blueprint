+++
kind  = "proof"
of    = "lem-kun-0f0c"
+++
Write $K=\operatorname{hocolim}_N\tau_{[-N,N]}K$
([def-kun-truncations], [lem-kun-hocolim-truncations]). Each
$\tau_{[-N,N]}K$ is bounded, hence bounded below with torsion
cohomology, so the exchange morphism is an isomorphism for it by
[thm-weil-pbc-bounded-below]. The exchange morphism of
[def-kun-unbounded-exchange] is natural in $K$
([lem-kun-unbounded-exchange-natural]), and both sides
commute with homotopy colimits: $g^{-1}$ is exact, and $Rf_*$,
$Rf'_*$ preserve direct sums because $f$ and $f'$ are proper
morphisms of finite type over a field, so that $\kuncd(f),\kuncd(f')< \infty$ by [lem-kun-0f10](1) and [lem-kun-0f11] applies
([def-kun-cd]). Passing to the homotopy colimit therefore gives
the assertion for arbitrary $K$.
