+++
id = "sk-p-product"
kind = "lemma"
title = "The identity component"
order = 667
lean = ["AlgebraicGeometry.GeneralLinearGroup.surjective_mulCenterIdentityComponent", "AlgebraicGeometry.GeneralLinearGroup.exists_mul_eq_of_containsCommutators", "AlgebraicGeometry.Monodromy.RepresentedDegreeDatum.surjective_mul_center_geometricMonodromy", "AlgebraicGeometry.Monodromy.RepresentedDegreeDatum.exists_mem_center_mul_mem_geometricMonodromy_eq", "AlgebraicGeometry.Monodromy.RepresentedDegreeDatum.isSemisimpleRepresentation_standardRepresentation_identityComponent", "AlgebraicGeometry.GeneralLinearGroup.lie_mem_range_lieAlgebraMap", "AlgebraicGeometry.GeneralLinearGroup.lie_mem_range_lieAlgebraMap_identityComponent", "AlgebraicGeometry.Monodromy.RepresentedDegreeDatum.lie_mem_lieAlgebra_geometricMonodromy", "AlgebraicGeometry.Monodromy.RepresentedDegreeDatum.lie_mem_lieAlgebra_identityComponent_geometricMonodromy"]
uses = ["sk-d-real-weil", "sk-i-restriction", "sk-lem-walg-normal-commutator", "sk-i-cartier", "sk-p-comparison", "sk-p-geometry", "sk-p-lie", "sec-algebraic-groups-lie-algebras"]
tags = ["sketch"]
+++
If $V$ is a semisimple $W(U_0)$-representation, then

$$
G^\circ=Z(G^\circ)^\circ H^\circ.
$$

*Complement.* If $\rho$ is semisimple, then $V$ is a semisimple
representation of $G^\circ(\overline{\mathbf Q}_\ell)$. For closed subgroup
schemes $H\subseteq G$ of $\GL_n$ over a field $k$ such that $H$ contains
the commutators of $G$ (as in [sk-lem-walg-normal-commutator]),
$[\Lie(G),\Lie(G)]\subseteq\Lie(H)$; if $k$ is algebraically closed of
characteristic zero, then moreover
$[\Lie(G^\circ),\Lie(G^\circ)]\subseteq\Lie(H^\circ)$. The multiplication
morphism $Z(G^\circ)^\circ\times H^\circ\to G^\circ$ is surjective, and
every $g\in G^\circ(\overline{\mathbf Q}_\ell)$ is a product $g=ch$ with
$c\in Z(G^\circ)^\circ$ and $h\in H^\circ$. More generally, the same holds
over any algebraically closed field $k$ of characteristic zero for closed
subgroup schemes $H\subseteq G$ of $\GL_n$ such that $H$ contains the
commutators of $G$ and $k^n$ is a semisimple representation of
$G^\circ(k)$.
