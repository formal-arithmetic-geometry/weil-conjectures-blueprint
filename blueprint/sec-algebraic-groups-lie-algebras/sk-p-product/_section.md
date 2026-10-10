+++
id = "sk-p-product"
kind = "proposition"
title = "The central–geometric product"
order = 2522
uses = ["sk-d-geometry", "sk-d-monodromy", "sk-d-tangent", "sk-i-cartier", "sk-i-restriction", "sk-p-comparison", "sk-p-geometry", "sk-p-lie"]
lean = ["AlgebraicGeometry.GeneralLinearGroup.surjective_mulCenterIdentityComponent", "AlgebraicGeometry.GeneralLinearGroup.exists_mul_eq_of_containsCommutators", "AlgebraicGeometry.Monodromy.RepresentedDegreeDatum.surjective_mul_center_geometricMonodromy", "AlgebraicGeometry.Monodromy.RepresentedDegreeDatum.exists_mem_center_mul_mem_geometricMonodromy_eq"]
tags = ["sketch"]
+++
For a semisimple represented degree datum over an algebraically
closed field $k$ of characteristic zero, the
identity components and center satisfy

$$
G^\circ=Z(G^\circ)^\circ H^\circ:
$$

the multiplication morphism $Z(G^\circ)^\circ\times_k H^\circ\to G^\circ$
is surjective, and every $g\in G^\circ(k)$ is a product $g=ch$ with
$c\in Z(G^\circ)^\circ(k)$ and $h\in H^\circ(k)$. More generally, the
same holds for closed subgroup schemes $H\subseteq G$ of $\GL_n$ over
such a $k$ such that $H$ contains the commutators of $G$ and $k^n$ is a
semisimple representation of $G^\circ(k)$.
