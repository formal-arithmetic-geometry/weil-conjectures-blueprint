+++
id = "lemma-connected-components-images-homomorphisms"
kind = "lemma"
title = "Connected components and images of homomorphisms"
order = 1720
lean = ["AlgebraicGeometry.finite_connectedComponents", "AlgebraicGeometry.GrpObj.isClopen_connectedComponent_onePoint", "AlgebraicGeometry.instGrpObjOverSchemeSpecOfIdentityComponent", "AlgebraicGeometry.GrpObj.irreducibleSpace_identityComponent", "AlgebraicGeometry.GrpObj.range_conj_subset_connectedComponent", "AlgebraicGeometry.GrpObj.image_mulLeft_connectedComponent_onePoint", "AlgebraicGeometry.GrpObj.range_identityComponentTranslate", "AlgebraicGeometry.exists_isMonHom_imageι", "AlgebraicGeometry.GeneralLinearGroup.eq_of_le_of_lieSubalgebra_eq"]
uses = []
+++
Let $G$ be an algebraic group.

1. $G$ has finitely many connected components. Its
   identity component $G^\circ$ is an open, closed, irreducible normal
   subgroup, and the other components are its cosets.
2. The image of a homomorphism $G\to G'$ of algebraic groups is a
   closed subgroup of $G'$.
3. If $G$ is connected and $K\subseteq G$ is a closed subgroup scheme
   with $\operatorname{Lie}(K)=\operatorname{Lie}(G)$, then $K=G$.
