+++
id = "g1-finite-pushforward-cohomology-comparison"
kind = "lemma"
title = "FinitePushforwardCohomologyComparison"
uses = ["def-weil-pbc-constructible-torsion", "def-weil-pbc-curve-setting", "def-weil-pbc-etale-cohomology", "def-weil-pbc-primary-torsion"]
lean = ["AlgebraicGeometry.IsCurve.finite_pushforward_cohomology_comparison"]
+++
Let $k$ be algebraically closed, $(X,F)$ a torsion curve coefficient pair [def-weil-pbc-curve-setting], $Y$ a curve over $k$, and $f:X\to Y$ finite over $k$ `AlgebraicGeometry.IsFinite, AlgebraicGeometry.IsIntegralHom` ([Mathlib source](https://github.com/leanprover-community/mathlib4/blob/master/Mathlib/AlgebraicGeometry/Morphisms/Finite.lean), [Mathlib source](https://github.com/leanprover-community/mathlib4/blob/master/Mathlib/AlgebraicGeometry/Morphisms/Integral.lean)). Convert $F$ and $f_*F$ to $\operatorname{ULift}\mathbb Z$-module sheaves, and write $A_X,A_Y$ for their underlying abelian sheaves. For each $q\ge0$ there is an additive equivalence $H^q(Y,A_Y)\simeq H^q(X,A_X)$ [def-weil-pbc-etale-cohomology].
