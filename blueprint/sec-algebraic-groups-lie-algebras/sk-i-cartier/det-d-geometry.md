+++
id = "det-d-geometry"
kind = "definition"
title = "Affine geometry and matrix groups"
order = 3674
uses = ["det-d-linear"]
lean = ["Matrix.GeneralLinearGroup.CoordinateRing", "AlgebraicGeometry.GeneralLinearGroup", "AlgebraicGeometry.GeneralLinearGroup.homMulEquiv", "Matrix.GeneralLinearGroup.zeroLocus", "AlgebraicGeometry.GeneralLinearGroup.subgroupScheme", "Matrix.GeneralLinearGroup.identityComponent", "Matrix.GeneralLinearGroup.center", "AlgebraicGeometry.GeneralLinearGroup.RationalHom"]
+++
An affine variety over $k$ is the spectrum of a
finitely generated reduced commutative $k$-algebra; reduced means that
the algebra has no nonzero nilpotents. Closed subvarieties are given by
radical ideals, and regular maps by homomorphisms of coordinate algebras
in the opposite direction. The Zariski topology has polynomial zero
loci as its closed sets. A closure is the smallest closed set containing
a given subset. A space is connected if it has no decomposition into
two nonempty disjoint open sets, and irreducible if it is not the union
of two proper closed sets. A constructible set is a finite union of
intersections of open and closed sets. Dimension is the supremum of
lengths of strict chains of prime ideals in the coordinate algebra.

The general linear group $\GL(V)=\GL_n$ is the affine group scheme
$\operatorname{Spec}k[x_{ij},\det^{-1}]$, whose $R$-points, for a
commutative $k$-algebra $R$, are the invertible $n\times n$ matrices over
$R$. A matrix algebraic group is a closed subgroup scheme
$G\subseteq\GL(V)$ cut out by a Hopf ideal $I$ of $k[x_{ij},\det^{-1}]$
(not necessarily radical): its $R$-points are the invertible matrices over
$R$ on which every equation in $I$ vanishes, and multiplication and
inversion are regular; its homomorphisms are regular group homomorphisms,
that is, homomorphisms of group schemes over $k$; a homomorphism
$G\to\GL_m$ is a rational representation of $G$ on $k^m$.
We identify its $k$-points with their matrices when writing products. The
identity component $G^\circ$ is the reduced closed subgroup on the
connected component of $1$. The center $Z(G)$ is the reduced closed subgroup of
$G$ consisting of the elements of $G$ commuting with all $g\in G(k)$
(not the centralizer of $G$ in $\GL(V)$).
