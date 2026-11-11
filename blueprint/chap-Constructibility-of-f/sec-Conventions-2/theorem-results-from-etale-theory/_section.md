+++
id = "theorem-results-from-etale-theory"
kind = "theorem"
title = "Results from the étale theory"
order = 537
aliases = ["remark-results-from-etale-theory"]
lean = ["AlgebraicGeometry.Etale.isIso_derivedBaseChangeMap_of_isProper_of_isAddTorsion_ring", "AlgebraicGeometry.Etale.hasFiniteCohomologicalDimensionMorphism", "AlgebraicGeometry.Etale.isZero_homology_rightDerivedLowerShriek_singleFunctor"]
+++
Let $f:X\to S$ be a morphism of schemes of finite type over $k$.

1. (Proper base change) If $f$ is proper, then for every morphism of schemes
   $g:S'\to S$, not necessarily of finite type over $k$, and every $K\in D(X_{\acute{e}t},A)$, the base change map
   $g^*Rf_*K\to Rf'_*g'^*K$ is an isomorphism, where $f':X'\to S'$ and
   $g':X'\to X$ are the projections of $X'=X\times_SS'$. In particular, the
   geometric stalks of $Rf_*K$ are the cohomology of the geometric fibres.
2. (Finiteness) If $f$ is separated, then $Rf_!$ maps $\Dbc(X,A)$ into
   $\Dbc(S,A)$.
3. (Cohomological dimension) The functors $Rf_*$ and, if $f$ is
   separated, $Rf_!$ have finite cohomological amplitude on torsion
   sheaves. In particular $\operatorname{cd}_\ell(f)<\infty$ in the sense of
   Definition [definition-cohomological-dimension].
