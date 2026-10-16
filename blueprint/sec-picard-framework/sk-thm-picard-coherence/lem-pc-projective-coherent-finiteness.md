+++
id = "lem-pc-projective-coherent-finiteness"
kind = "lemma"
title = "Coherent cohomology of a projective scheme over a Noetherian ring"
lean = ["AlgebraicGeometry.Scheme.Modules.subsingleton_H_of_isClosedImmersion", "AlgebraicGeometry.Scheme.Modules.finite_H_of_isClosedImmersion"]
order = 662
uses = ["def-pc-projective-morphism", "def-pc-projective-space-twist", "lem-pc-closed-immersion-coherent-cohomology", "lem-pc-projective-space-coherent-finiteness", "lem-pc-projective-space-cohomology-bound", "pqf-def-coherent", "pqf-def-cohomology"]
+++
Let $A$ be Noetherian, let $f:X\to\operatorname{Spec}(A)$ be
projective, and let
$\mathcal F$ be a coherent module.
Then $H^q(X,\mathcal F)$ is a finite $A$-module for every $q$.
For an embedding $X\hookrightarrow\mathbf P^n_A$, these groups
vanish for $q>n$.
