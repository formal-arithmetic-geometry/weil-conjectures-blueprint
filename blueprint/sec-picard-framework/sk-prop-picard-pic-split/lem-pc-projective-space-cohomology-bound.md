+++
id = "lem-pc-projective-space-cohomology-bound"
kind = "lemma"
title = "Cohomology above the number of projective coordinates"
order = 629
uses = ["def-pc-projective-space-twist", "lem-pc-cech-computes", "pqf-def-coherent", "pqf-def-cohomology"]
lean = ["AlgebraicGeometry.ProjectiveSpace.subsingleton_H_of_lt"]
+++
For any commutative ring $A$, any $n\ge0$, and any
quasi-coherent module $\mathcal F$ on
$\hyperref[def-pc-projective-space-twist]{\mathbf P^n_A}$,
one has $H^q(\mathbf P^n_A,\mathcal F)=0$ for $q>n$.
