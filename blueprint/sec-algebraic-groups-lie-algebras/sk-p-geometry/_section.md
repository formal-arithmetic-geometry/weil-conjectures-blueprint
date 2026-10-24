+++
id = "sk-p-geometry"
kind = "lemma"
title = "Components, images, and equal Lie algebras"
lean = ["AlgebraicGeometry.finite_connectedComponents", "AlgebraicGeometry.GrpObj.isClopen_connectedComponent_onePoint", "AlgebraicGeometry.GrpObj.irreducibleSpace_identityComponent", "AlgebraicGeometry.GrpObj.finiteIndex_range_identityComponentι", "AlgebraicGeometry.GrpObj.image_mulLeft_connectedComponent_onePoint", "AlgebraicGeometry.isClosed_range_of_isMonHom", "AlgebraicGeometry.isIso_left_of_topologicalKrullDim_eq", "AlgebraicGeometry.GeneralLinearGroup.RationalHom.mem_range_points_iff", "AlgebraicGeometry.GeneralLinearGroup.eq_of_le_of_lieSubalgebra_eq"]
order = 3699
uses = ["sk-i-cartier"]
tags = ["sketch"]
+++
An algebraic group $G$ has finitely many connected components. Its
identity component $G^\circ$ is an open, closed, irreducible normal
subgroup, and the other components are its cosets. The image of a
homomorphism of algebraic groups is closed. If $G$ is connected and
$J\subseteq G$ is a closed subgroup scheme with $\dim J=\dim G$, then
$J=G$.

For closed subgroups $G\subseteq\GL(V)$ and $G'\subseteq\GL(W)$, the
image $f(G(L))$ of a regular homomorphism $f\colon G\to G'$ is the set of
$L$-points of a closed subgroup of $G'$, taken with its reduced
structure. If $G\subseteq\GL(V)$ is a connected closed subgroup and
$K\subseteq G$ is a closed subgroup with $\Lie(K)=\Lie(G)$, then $K=G$.
