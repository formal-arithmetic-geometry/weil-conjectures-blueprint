+++
id = "g1-finite-pushforward-pullback-comparison"
kind = "lemma"
title = "FinitePushforwardPullbackComparison"
uses = ["def-weil-pbc-cartesian-square", "def-weil-pbc-cohomology-pullback", "def-weil-pbc-constructible-torsion", "def-weil-pbc-curve-setting", "def-weil-pbc-primary-torsion"]
lean = ["AlgebraicGeometry.IsCurve.finite_pushforward_pullback_comparison"]
source = "literature/stacks-project/etale-cohomology.tex, Etale Cohomology, Section 03SB, Lemma 0A5D (lemma-finite-pushforward-statements); its proof uses Proposition 03QP (vanishing of R^qf_* for finite f), the Leray spectral sequence (Cohomology on Sites, Lemma 0733 sites-cohomology-lemma-apply-Leray) and Lemma 0959 (finite pushforward commutes with base change)"
+++
Let $k$ be algebraically closed, $(X,F)$ a torsion curve coefficient pair [def-weil-pbc-curve-setting], $Y$ a curve over $k$, and $f:X\to Y$ finite over $k$ `AlgebraicGeometry.IsFinite, AlgebraicGeometry.IsIntegralHom` ([Mathlib source](https://github.com/leanprover-community/mathlib4/blob/master/Mathlib/AlgebraicGeometry/Morphisms/Finite.lean), [Mathlib source](https://github.com/leanprover-community/mathlib4/blob/master/Mathlib/AlgebraicGeometry/Morphisms/Integral.lean)). Let $A_X,A_Y$ be the underlying abelian sheaves after converting $F,f_*F$ to $\operatorname{ULift}\mathbb Z$-modules. In any cartesian square with upper arrow $b:X\prime\to X$, lower arrow $a:Y\prime\to Y$ and vertical arrows $f\prime,f$ [def-weil-pbc-cartesian-square], for every $q\ge0$ the pullback on $H^q(Y,A_Y)$ along $a$ is bijective (respectively surjective) if and only if the pullback on $H^q(X,A_X)$ along $b$ is bijective (respectively surjective) [def-weil-pbc-cohomology-pullback].
