+++
id = "lem-kun-0F0C"
kind = "lemma"
title = "Proper base change with $\\mathbf Z/n\\mathbf Z$-coefficients"
order = 6102
lean = ["AlgebraicGeometry.Etale.IsProper.unboundedExchange_isIso"]
uses = ["def-kun-unbounded-exchange", "lem-kun-hocolim-truncations", "lem-kun-0F10", "lem-kun-0F11", "def-kun-truncations", "def-kun-cd", "lem-kun-unbounded-exchange-natural"]
+++
Let $f:X\to Y$ be a proper morphism of schemes, let $g:Y'\to Y$ be any
morphism, set $X'=Y'\times_YX$, and write $f':X'\to Y'$ and $g':X'\to X$ for
the projections. For $K\in D(X_{\Et},\mathbf Z/n\mathbf Z)$, the exchange
morphism of [def-kun-unbounded-exchange]
$$
\Ex_{\square,K}:g^{-1}Rf_*K\longrightarrow Rf'_*(g')^{-1}K
$$
is an isomorphism.

## Proof

Write $K=\operatorname{hocolim}_N\tau_{[-N,N]}K$ ([def-kun-truncations],
[lem-kun-hocolim-truncations]). Each $\tau_{[-N,N]}K$ is bounded, hence
bounded below with torsion cohomology, so the exchange morphism is an
isomorphism for it by the bounded-below proper base-change theorem.

The exchange morphism is natural in $K$
([lem-kun-unbounded-exchange-natural]), and both sides commute with homotopy
colimits: $g^{-1}$ is exact, and $Rf_*$, $Rf'_*$ preserve direct sums
because $f$ and $f'$ are proper morphisms of finite type over a field, so
that $\operatorname{cd}(f),\operatorname{cd}(f')<\infty$ by
[lem-kun-0F10](1) and [lem-kun-0F11] applies. Passing to the homotopy
colimit therefore gives the assertion for arbitrary $K$.

Unresolved dependencies: def:weil-pbc-scheme-conventions, thm:weil-pbc-bounded-below
