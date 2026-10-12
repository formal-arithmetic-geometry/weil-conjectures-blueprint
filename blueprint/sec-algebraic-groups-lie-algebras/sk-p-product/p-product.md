+++
id = "p-product"
kind = "theorem"
title = "The central--geometric product"
order = 2863
tags = ["latex:proposition"]
uses = ["d-monodromy", "lem-ag-closure-commutators", "lem-ag-closure-semisimple", "lem-ag-faithful-semisimple-lie-central-radical", "lem-ag-homomorphism-image-closed", "lem-ag-lie-centre", "lem-ag-lie-stable-subspace", "lem-wf-algebraic-component-cosets", "lem-wf-same-lie-closed-subgroup"]
lean = ["AlgebraicGeometry.GeneralLinearGroup.surjective_mulCenterIdentityComponent", "AlgebraicGeometry.GeneralLinearGroup.exists_mul_eq_of_containsCommutators", "AlgebraicGeometry.Monodromy.RepresentedDegreeDatum.surjective_mul_center_geometricMonodromy", "AlgebraicGeometry.Monodromy.RepresentedDegreeDatum.exists_mem_center_mul_mem_geometricMonodromy_eq"]
+++
For a semisimple represented degree datum ([d-monodromy]) over an
algebraically closed field $k$ of characteristic zero, the
identity components and center satisfy

$$
G^\circ=Z(G^\circ)^\circ H^\circ:
$$

the multiplication morphism $Z(G^\circ)^\circ\times_k H^\circ\to G^\circ$
is surjective, and every $g\in G^\circ(k)$ is a product $g=ch$ with
$c\in Z(G^\circ)^\circ(k)$ and $h\in H^\circ(k)$. More generally, the
same holds for closed subgroup schemes $H\subseteq G$ of
$\operatorname{GL}_n$ over such a $k$ such that $H$ contains the
commutators of $G$ and $k^n$ is a semisimple representation of
$G^\circ(k)$.

This applies to the Weil representation of a lisse Weil sheaf whose Weil
representation is semisimple.
