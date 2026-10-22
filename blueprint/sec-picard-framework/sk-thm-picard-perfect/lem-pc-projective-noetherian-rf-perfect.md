+++
id = "lem-pc-projective-noetherian-rf-perfect"
kind = "lemma"
title = "Perfect direct image for a projective Noetherian family"
lean = ["AlgebraicGeometry.Scheme.Modules.isPerfect_Q_cechModuleComplex_of_isClosedImmersion"]
order = 679
uses = ["def-pc-derived-direct-image", "def-pc-morphism-conventions", "def-pc-perfect-complex", "def-pc-projective-morphism", "lem-pc-cech-resolution", "lem-pc-noetherian-flat-complex-perfect", "lem-pc-projective-coherent-finiteness", "lem-pc-rf-base-change-flat-module", "pqf-def-coherent"]
+++
Let $S=\operatorname{Spec}(A)$ be an affine scheme with $A$ Noetherian,
let $f:X\to S$ be
projective, i.e. the composite of a closed immersion
$X\to\mathbf P^n_S$ and the projection, and let
$\mathcal G$ be a coherent
$\mathcal O_X$-module flat over $S$. Let $\mathcal U$ be a finite cover of
$X$ by affine opens. Then the derived direct image
$Rf_*\mathcal G$, represented in $D(A)$ by the Cech complex
$\check C^\bullet(\mathcal U,\mathcal G)$ ([lem-pc-cech-resolution]), is a
perfect object of $D(A)$, i.e. isomorphic in $D(A)$ to a bounded
complex of finite projective $A$-modules.
