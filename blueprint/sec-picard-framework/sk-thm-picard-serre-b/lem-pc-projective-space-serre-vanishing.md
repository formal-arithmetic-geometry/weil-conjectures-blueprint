+++
id = "lem-pc-projective-space-serre-vanishing"
kind = "lemma"
title = "Serre vanishing on projective space over a Noetherian ring"
lean = ["AlgebraicGeometry.ProjectiveSpace.exists_subsingleton_H_tensor_twist_of_isNoetherianRing", "AlgebraicGeometry.ProjectiveSpace.exists_subsingleton_H_tensor_twist"]
order = 633
uses = ["def-pc-projective-space-twist", "lem-pc-projective-space-cohomology-bound", "lem-pc-projective-space-twist-cohomology", "lem-pc-projective-space-twist-quotient", "pqf-def-coherent", "pqf-def-cohomology"]
+++
Let $A$ be Noetherian and $\mathcal F$ a
coherent module on
$P=\hyperref[def-pc-projective-space-twist]{\mathbf P^n_A}$.
There is $d_0\ge0$ such that $H^q(P,\mathcal F(d))=0$ for
all $d\ge d_0$ and all $q>0$.
