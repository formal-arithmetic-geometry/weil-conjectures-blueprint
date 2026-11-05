+++
id = "lemma-connected-components-images-homomorphisms"
kind = "lemma"
title = "Connected components and images of homomorphisms"
order = 1723
lean = ["AlgebraicGeometry.GrpObj.isIso_left_of_differential_bijective", "AlgebraicGeometry.GrpObj.lieEquivIdentityComponent", "AlgebraicGeometry.isClosed_range_of_isMonHom", "AlgebraicGeometry.GeneralLinearGroup.eq_of_le_of_lieSubalgebra_eq", "AlgebraicGeometry.exists_isMonHom_imageι"]
+++
Let $G$ be an algebraic group.

1. $G$ has finitely many connected components. Its
   identity component $G^\circ$ is an open, closed, irreducible normal
   subgroup, the other components are its cosets, and
   $\operatorname{Lie}(G^\circ)=\operatorname{Lie}(G)$.
2. The image of a homomorphism $G\to G'$ of algebraic groups is a
   closed subgroup of $G'$.
3. If $G$ is connected and $K\subseteq G$ is a closed subgroup scheme
   with $\operatorname{Lie}(K)=\operatorname{Lie}(G)$, then $K=G$.
