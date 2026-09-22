+++
id = "sbc-def-universal-local-acyclicity"
kind = "definition"
title = "Universal local acyclicity"
order = 5232
lean = ["AlgebraicGeometry.IsUniversallyLocallyAcyclic"]
uses = ["sbc-def-local-acyclicity"]
+++
Let $f:X\to S$ be a morphism of schemes and $K\in D(X_{\Et})$.

1. $f$ is *universally locally acyclic relative to $K$* if for every
   $S'\to S$ the base change $f':X'\to S'$ is locally acyclic relative to
   the pullback of $K$, in the sense of [sbc-def-local-acyclicity].
2. $f$ is *locally acyclic* if it is locally acyclic relative to the
   constant sheaf $\underline{\mathbf Z/n\mathbf Z}$ for all geometric
   points $\bar x$ of $X$ and all $n$ prime to the characteristic of
   $\kappa(\bar x)$.
3. $f$ is *universally locally acyclic* if every base change is locally
   acyclic, i.e. for every $S'\to S$ the base change $f'$ satisfies (2).

Unresolved dependencies: def:weil-pbc-scheme-conventions
