+++
id = "sk-p-geometry"
kind = "lemma"
title = "Components, images, and equal Lie algebras"
lean = ["Matrix.GeneralLinearGroup.isPrime_identityComponent", "Matrix.GeneralLinearGroup.normal_zeroLocus_identityComponent", "Matrix.GeneralLinearGroup.finiteIndex_zeroLocus_identityComponent", "Matrix.GeneralLinearGroup.toPrimeSpectrum_mem_connectedComponentIn_iff", "AlgebraicGeometry.isClosed_range_of_isMonHom", "AlgebraicGeometry.isIso_left_of_topologicalKrullDim_eq"]
order = 3699
uses = ["sk-i-cartier"]
tags = ["sketch"]
+++
An algebraic group $G$ has finitely many connected components. Its
identity component $G^\circ$ is an open, closed, irreducible normal
subgroup, and the other components are its cosets. The image of a
homomorphism of algebraic groups is a closed subgroup. If $G$ is connected
and $K\subseteq G$ is a closed subgroup scheme with $\Lie(K)=\Lie(G)$,
then $K=G$.

*Complement.* For closed subgroups of $\GL(V)$ the image on $L$-points of a
regular homomorphism $G\to K$ is the set of $L$-points of a closed
subgroup of $K$, taken with its reduced structure; and if $G$ is connected
and a closed subgroup $J\subseteq G$ has $\dim J=\dim G$, then $J=G$.
