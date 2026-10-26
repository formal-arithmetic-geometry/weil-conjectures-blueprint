+++
id = "g1-finite-pushforward-cohomology-comparison"
kind = "lemma"
title = "FinitePushforwardCohomologyComparison"
uses = ["def-weil-pbc-constructible-torsion", "def-weil-pbc-curve-setting", "def-weil-pbc-etale-cohomology", "def-weil-pbc-primary-torsion"]
lean = ["AlgebraicGeometry.IsCurve.finite_pushforward_cohomology_comparison"]
order = 1836
+++
Let $k$ be algebraically closed, $(X,F)$ a torsion curve coefficient pair [def-weil-pbc-curve-setting], $Y$ a curve over $k$, and $f:X\to Y$ a finite morphism over $k$. Write $A_X$ and $A_Y$ for the abelian sheaves underlying $F$ and $f_*F$, each regarded as a sheaf of $\mathbb Z$-modules. For each $q\ge0$ there is an isomorphism of abelian groups $H^q(Y,A_Y)\simeq H^q(X,A_X)$ [def-weil-pbc-etale-cohomology].
