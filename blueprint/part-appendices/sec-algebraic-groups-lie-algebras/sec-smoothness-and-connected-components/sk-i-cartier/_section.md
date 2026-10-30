+++
id = "sk-i-cartier"
kind = "proposition"
title = "Cartier's theorem"
order = 983
lean = ["AlgebraicGeometry.isReduced_of_grpObj", "AlgebraicGeometry.smooth_of_grpObj_of_charZero", "AlgebraicGeometry.GrpObj.finrank_lie_eq_topologicalKrullDim", "AlgebraicGeometry.GeneralLinearGroup.finrank_lie_eq_ringKrullDim", "AlgebraicGeometry.GrpObj.lieEquivIdentityComponent", "AlgebraicGeometry.GeneralLinearGroup.lieAlgebraEquivIdentityComponent", "AlgebraicGeometry.GrpObj.lieEquiv_mul"]
tags = ["sketch"]
+++
Every algebraic group over $\Omega$ is smooth and reduced. In particular

$$
\dim\operatorname{Lie}(G)=\dim G,
\qquad \operatorname{Lie}(G^\circ)=\operatorname{Lie}(G).
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
