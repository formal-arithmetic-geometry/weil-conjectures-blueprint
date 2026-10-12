+++
id = "sk-i-restriction"
kind = "proposition"
title = "Normal restriction and passage to closure"
order = 2853
uses = ["sk-d-geometry", "sk-d-linear", "sk-d-monodromy", "sk-d-tangent", "sk-i-cartier", "sk-i-geometry"]
lean = ["Representation.isSemisimpleRepresentation_comp_subtype", "AlgebraicGeometry.IsMonHom.ContainsCommutators", "AlgebraicGeometry.IsMonHom.Normal.of_containsCommutators", "AlgebraicGeometry.GeneralLinearGroup.containsCommutators_subgroupSchemeHom", "AlgebraicGeometry.GeneralLinearGroup.lie_mem_range_lieAlgebraMap", "AlgebraicGeometry.GeneralLinearGroup.lie_mem_range_lieAlgebraMap_identityComponent", "AlgebraicGeometry.Monodromy.RepresentedDegreeDatum.arithmeticMonodromy_le_geometricMonodromy", "AlgebraicGeometry.Monodromy.RepresentedDegreeDatum.normal_zeroLocus_geometricMonodromy", "AlgebraicGeometry.Monodromy.RepresentedDegreeDatum.commutator_zeroLocus_le_zeroLocus_geometricMonodromy", "AlgebraicGeometry.Monodromy.RepresentedDegreeDatum.containsCommutators_subgroupSchemeHom_arithmeticMonodromy_le_geometricMonodromy", "AlgebraicGeometry.Monodromy.RepresentedDegreeDatum.lie_mem_lieAlgebra_geometricMonodromy", "AlgebraicGeometry.Monodromy.RepresentedDegreeDatum.lie_mem_lieAlgebra_identityComponent_geometricMonodromy", "AlgebraicGeometry.Monodromy.RepresentedDegreeDatum.isSemisimpleRepresentation_standardRepresentation_identityComponent", "AlgebraicGeometry.GeneralLinearGroup.derivedIdeal", "AlgebraicGeometry.GeneralLinearGroup.containsCommutators_iff_le_derivedIdeal", "AlgebraicGeometry.Monodromy.RepresentedDegreeDatum.geometricMonodromy_le_derivedIdeal_arithmeticMonodromy"]
tags = ["sketch"]
+++
A finite-dimensional semisimple representation restricts semisimply
to a normal subgroup.
For a rational action, invariance under a Zariski-dense subgroup is
equivalent to invariance under its closure: the stabilizer equations
are closed. Invariant subspaces and quotients carry induced rational
actions; direct sums, tensor products, exterior powers and determinants
of rational actions are rational. The closures $G,H$ of
[sk-d-monodromy] are algebraic groups, closed subgroup schemes of
$\GL_n$ with $H\subseteq G$; for every $k$-algebra $R$, $H(R)$ is normal
in $G(R)$, and

$$
aba^{-1}b^{-1}\in H(R)\quad(a,b\in G(R)),\qquad
[\Lie(G),\Lie(G)]\subseteq\Lie(H).
$$

Thus $H$ contains the commutators of $G$ as group schemes; equivalently,
$H$ contains the derived subgroup $[G,G]$, the smallest closed subgroup
scheme of $G$ containing the commutators of $G$. More generally, if
$H\subseteq G$ are closed subgroup schemes of $\GL_n$ such that the
commutators of $G(R)$ lie in $H(R)$ for every $k$-algebra $R$, then $H$
contains the commutators of $G$ as group schemes, hence is normal in $G$,
and $[\Lie(G),\Lie(G)]\subseteq\Lie(H)$. If $k$ is algebraically closed
of characteristic zero, then moreover
$[\Lie(G^\circ),\Lie(G^\circ)]\subseteq\Lie(H^\circ)$, and for a
semisimple datum $k^n$ is a semisimple representation of $G^\circ(k)$.
