+++
id = "lem-weil-pbc-closed-immersion-localized-section-map"
kind = "lemma"
title = "A surjective localized section map gives a closed immersion on a basic open"
uses = ["def-pc-scheme"]
lean = ["AlgebraicGeometry.isClosedImmersion_restrict_basicOpen_of_localizedMap_surjective"]
+++
Let $f:X\to S$ be an affine morphism of schemes [def-pc-scheme], meaning that inverse images of affine opens are affine. Let $U\subseteq S$ be affine, $A=\Gamma(U,\mathcal O_S)$, $B=\Gamma(f^{-1}U,\mathcal O_X)$, and $\varphi:A\to B$ its section map. For $a\in A$, suppose that the localization at $\{1,a,a^2,\ldots\}$ of the $A$-linear map $\varphi$ is surjective. Then the restriction of $f$ over the principal open $D_U(a)\subseteq S$ is a closed immersion `AlgebraicGeometry.IsClosedImmersion` ([Mathlib source](https://github.com/leanprover-community/mathlib4/blob/master/Mathlib/AlgebraicGeometry/Morphisms/ClosedImmersion.lean)).
