+++
id = "sk-i-cartier"
kind = "proposition"
title = "Characteristic-zero group smoothness"
order = 2489
uses = ["sk-d-geometry", "sk-d-tangent", "sk-i-geometry"]
lean = ["AlgebraicGeometry.isReduced_of_grpObj", "AlgebraicGeometry.smooth_of_grpObj_of_charZero", "AlgebraicGeometry.GrpObj.finrank_lie_eq_topologicalKrullDim", "AlgebraicGeometry.GeneralLinearGroup.finrank_lie_eq_ringKrullDim", "AlgebraicGeometry.GrpObj.lieEquivIdentityComponent", "AlgebraicGeometry.GeneralLinearGroup.lieAlgebraEquivIdentityComponent", "AlgebraicGeometry.GrpObj.lieEquiv_mul"]
tags = ["sketch"]
+++
Every group scheme locally of finite type over a field of
characteristic zero is reduced and smooth over that field; in particular
every finite-type matrix group scheme over $k$ is
smooth and reduced. Thus $\dim\Lie(G)=\dim G$ for every group scheme $G$
of finite type over a field of characteristic zero; for a closed subgroup
scheme $G=V(I)\subseteq\GL_n$ this is the Krull dimension of its
coordinate ring. For a group scheme of finite type over a field, the
identity component is open and has the same Lie algebra as the whole
group; for a matrix group scheme over $k$ (algebraically closed of
characteristic zero) this is also the reduced identity component.
Closed subgroup schemes defined by stabilizer and centralizer equations
are included; no passage to the reduced structure changes their tangent
spaces in this characteristic-zero setting.
The group law on tangent vectors at $1$ is addition: differentiating
multiplication at $(1,1)$ gives $(X,Y)\mapsto X+Y$.
