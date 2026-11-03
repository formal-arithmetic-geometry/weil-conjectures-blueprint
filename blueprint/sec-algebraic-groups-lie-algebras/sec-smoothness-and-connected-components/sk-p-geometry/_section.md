+++
id = "sk-p-geometry"
kind = "lemma"
title = "Connected components and images of homomorphisms"
order = 984
lean = ["AlgebraicGeometry.finite_connectedComponents", "AlgebraicGeometry.GrpObj.isClopen_connectedComponent_onePoint", "AlgebraicGeometry.GrpObj.irreducibleSpace_identityComponent", "AlgebraicGeometry.GrpObj.finiteIndex_range_identityComponentι", "AlgebraicGeometry.GrpObj.image_mulLeft_connectedComponent_onePoint", "AlgebraicGeometry.isClosed_range_of_isMonHom", "AlgebraicGeometry.isIso_left_of_topologicalKrullDim_eq", "AlgebraicGeometry.GeneralLinearGroup.RationalHom.mem_range_points_iff", "AlgebraicGeometry.GeneralLinearGroup.eq_of_le_of_lieSubalgebra_eq"]
uses = ["sk-i-cartier"]
tags = ["sketch"]
+++
An algebraic group $G$ has finitely many connected components. Its
identity component $G^\circ$ is an open, closed, irreducible normal
subgroup, and the other components are its cosets. The image of a
homomorphism of algebraic groups is a closed subgroup. If $G$ is
connected and $K\subseteq G$ is a closed subgroup scheme with
$\operatorname{Lie}(K)=\operatorname{Lie}(G)$, then $K=G$.
