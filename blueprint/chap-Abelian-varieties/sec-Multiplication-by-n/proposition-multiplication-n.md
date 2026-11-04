+++
id = "proposition-multiplication-n"
kind = "proposition"
title = "Multiplication by $n$"
order = 1497
lean = ["AlgebraicGeometry.surjective_npow_id", "AlgebraicGeometry.isIsogeny_npow_id", "AlgebraicGeometry.isogenyDegree_npow_id", "AlgebraicGeometry.isFiniteLocallyFreeOfDegree_npow_id", "AlgebraicGeometry.flat_torsionSubgroupScheme", "AlgebraicGeometry.finrankΓ_torsionSubgroupScheme", "AlgebraicGeometry.etale_npow_id", "AlgebraicGeometry.etale_torsionSubgroupScheme"]
uses = ["definition-abelian-variety"]
+++
Let $A$ be an abelian variety of dimension $g$ over $k$. For every
$n>0$, the morphism $[n]$ is surjective and finite locally free of
degree $n^{2g}$, and its kernel $A[n]$ has rank $n^{2g}$ over $k$. If
$n$ is invertible in $k$, then $[n]$ and $A[n]\to\operatorname{Spec}k$
are finite étale.
