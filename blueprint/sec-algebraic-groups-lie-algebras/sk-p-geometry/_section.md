+++
id = "sk-p-geometry"
kind = "proposition"
title = "Algebraic-group geometry"
order = 2831
uses = ["sk-d-geometry", "sk-i-cartier", "sk-i-geometry"]
lean = ["Matrix.GeneralLinearGroup.isPrime_identityComponent", "Matrix.GeneralLinearGroup.normal_zeroLocus_identityComponent", "Matrix.GeneralLinearGroup.finiteIndex_zeroLocus_identityComponent", "Matrix.GeneralLinearGroup.toPrimeSpectrum_mem_connectedComponentIn_iff", "AlgebraicGeometry.isClosed_range_of_isMonHom", "AlgebraicGeometry.isIso_left_of_topologicalKrullDim_eq"]
tags = ["sketch"]
+++
For matrix algebraic groups over $k$:

1. $G^\circ$ is a closed, normal, irreducible subgroup, and its
finitely many cosets are exactly the connected components of $G$.
1. The image on $k$-points of a regular homomorphism $G\to K$
is a closed subgroup of $K$, with its reduced structure.
1. If $G$ is connected and a closed subgroup $J\subseteq G$ has
$\dim J=\dim G$, then $J=G$.
