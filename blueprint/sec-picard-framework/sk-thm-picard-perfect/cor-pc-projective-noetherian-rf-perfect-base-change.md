+++
id = "cor-pc-projective-noetherian-rf-perfect-base-change"
kind = "theorem"
title = "Arbitrary base change for a projective Noetherian family"
lean = ["AlgebraicGeometry.Scheme.Modules.isPerfect_Q_cechModuleComplex_baseChange_of_isClosedImmersion"]
order = 758
tags = ["latex:corollary"]
uses = ["def-pc-base-change", "def-pc-derived-direct-image", "def-pc-derived-pullback", "def-pc-morphism-conventions", "def-pc-perfect-complex", "def-pc-projective-morphism", "lem-pc-projective-noetherian-rf-perfect", "lem-pc-rf-base-change-flat-module", "pqf-def-coherent"]
+++
Let $S=\operatorname{Spec}(A)$ be an affine scheme with $A$ Noetherian,
let $f:X\to S$ be
projective, let
$\mathcal G$ be a coherent
$\mathcal O_X$-module flat over $S$, and let $\mathcal U$ be a finite cover
of $X$ by affine opens.
For any morphism $g:T\to S$ from an affine scheme
$T=\operatorname{Spec}(B)$, without a Noetherian hypothesis on
$B$, the canonical base-change map of [lem-pc-rf-base-change-flat-module]

$$
Lg^*(Rf_*\mathcal G)\longrightarrow Rf_{T,*}\mathcal G_T
$$

is an isomorphism in $D(B)$, and both sides are perfect objects of
$D(B)$. Here $Rf_*\mathcal G$ and $Rf_{T,*}\mathcal G_T$ are represented by
the Cech complexes of $\mathcal U$ and of its pullback to $X_T$, and
$Lg^*$ denotes the derived pullback.
