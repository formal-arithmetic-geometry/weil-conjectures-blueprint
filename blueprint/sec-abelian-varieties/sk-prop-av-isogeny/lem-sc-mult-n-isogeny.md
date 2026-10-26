+++
id = "lem-sc-mult-n-isogeny"
kind = "lemma"
title = "Multiplication by $n$ is surjective with finite kernel"
lean = ["AlgebraicGeometry.surjective_npow_id", "AlgebraicGeometry.isFinite_torsionSubgroupScheme", "AlgebraicGeometry.isMonHom_npow_id", "AlgebraicGeometry.topologicalKrullDim_torsionSubgroupScheme"]
order = 529
uses = ["def-sc-abelian-variety", "def-sc-group-scheme", "def-sc-mult-n", "lem-sc-image-subgroup"]
+++
Let $A$ be an abelian variety
over a field $k$, and let $n\geq1$. Then the map $[n]$ of
[def-sc-mult-n] is a surjective homomorphism of
group schemes, and its kernel
$A[n]$ is a finite group scheme over $k$; in particular $\dim A[n]=0$.
