+++
id = "lem-pc-projective-space-coherent-finiteness"
kind = "lemma"
title = "Coherent cohomology of projective space over a Noetherian ring"
lean = ["AlgebraicGeometry.ProjectiveSpace.finite_H"]
order = 659
uses = ["def-pc-projective-space-twist", "lem-pc-projective-space-cohomology-bound", "lem-pc-projective-space-twist-cohomology", "lem-pc-projective-space-twist-quotient", "pqf-def-coherent", "pqf-def-cohomology"]
+++
Let $A$ be Noetherian, $P=\hyperref[def-pc-projective-space-twist]{\mathbf P^n_A}$,
and $\mathcal F$ a coherent module.
Then each $H^q(P,\mathcal F)$ is a finite $A$-module.
