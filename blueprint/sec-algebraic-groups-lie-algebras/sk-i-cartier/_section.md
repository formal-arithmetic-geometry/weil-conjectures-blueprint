+++
id = "sk-i-cartier"
kind = "proposition"
title = "Cartier's theorem"
lean = ["AlgebraicGeometry.isReduced_of_grpObj", "AlgebraicGeometry.smooth_of_grpObj_of_charZero", "AlgebraicGeometry.GrpObj.finrank_lie_eq_topologicalKrullDim", "AlgebraicGeometry.GeneralLinearGroup.finrank_lie_eq_ringKrullDim", "AlgebraicGeometry.GrpObj.lieEquivIdentityComponent", "AlgebraicGeometry.GeneralLinearGroup.lieAlgebraEquivIdentityComponent", "AlgebraicGeometry.GrpObj.lieEquiv_mul"]
order = 3880
tags = ["sketch"]
+++
Throughout this appendix, $L$ is an algebraically closed field of
characteristic zero, and all Lie algebras and representations are
finite-dimensional. An algebraic group is a group scheme of finite type
over $L$. Stabilizers and centralizers are taken as subgroup schemes. The
Lie algebra $\Lie(G)$ of an algebraic group $G$ is its tangent space at
the identity; for a closed subgroup of $\GL(V)$ it is described by dual
numbers in [sk-p-comparison].

Every algebraic group over $L$ is smooth and reduced. In particular

$$
\dim\Lie(G)=\dim G,
\qquad \Lie(G^\circ)=\Lie(G).
$$

*Complement.* More generally, every group scheme locally of finite type
over a field of characteristic zero is reduced and smooth over that field,
and $\dim\Lie(G)=\dim G$ for every group scheme $G$ of finite type over
such a field; for a closed subgroup scheme $G=V(I)\subseteq\GL_n$ this is
the Krull dimension of its coordinate ring. For a group scheme of finite
type over any field, the identity component is open and has the same Lie
algebra as the whole group; for a closed subgroup scheme of $\GL_n$ over
$L$ it is also the reduced closed subgroup on the connected component of
$1$. In particular, closed subgroup schemes defined by stabilizer and
centralizer equations are reduced, so their tangent spaces can be read off
from these equations. The group law on tangent vectors at $1$ is addition:
the differential of the multiplication at $(1,1)$ is $(X,Y)\mapsto X+Y$.
