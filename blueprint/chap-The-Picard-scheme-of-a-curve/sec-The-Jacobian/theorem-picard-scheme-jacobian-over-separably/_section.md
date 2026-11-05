+++
id = "theorem-picard-scheme-jacobian-over-separably"
kind = "theorem"
title = "The Picard scheme and the Jacobian over a separably closed field"
order = 1549
lean = ["AlgebraicGeometry.isRepresentable_picardFunctor", "AlgebraicGeometry.smoothOfRelativeDimension_of_representableBy_picardFunctor", "AlgebraicGeometry.GrpObj.isSeparated_hom", "AlgebraicGeometry.exists_decomposition_picardFunctor_representableBy", "AlgebraicGeometry.smoothOfRelativeDimension_of_representableBy_picardFunctorDegree", "AlgebraicGeometry.isProper_of_representableBy_picardFunctorDegree", "AlgebraicGeometry.geometricallyIntegral_of_representableBy_picardFunctorDegree", "AlgebraicGeometry.exists_jacobian", "AlgebraicGeometry.nonempty_picardFunctor_iso_of_isPullback", "AlgebraicGeometry.picardFunctorDegreeIsoOfIsPullback"]
uses = ["definition-relative-picard-functor", "definition-abelian-variety"]
+++
Let $k$ be separably closed and let $C/k$ be a smooth proper
connected curve of genus $g$. The fppf Picard functor is represented
by a smooth separated group scheme, locally of finite type over $k$,
with a decomposition

$$
\operatorname{Pic}_{C/k}
=\coprod_{d\in\mathbf Z}\operatorname{Pic}^d_{C/k}.
$$

Each component is a smooth proper geometrically connected variety of
dimension $g$, parametrizing invertible sheaves of degree $d$.
The identity component
$J(C)=\operatorname{Pic}^0_{C/k}$ is an abelian variety, and

$$
J(C)(k)=\operatorname{Pic}^0(C),
\qquad T_0J(C)=H^1(C,\mathcal O_C).
$$

The formation of this representing scheme, its degree components
and $J(C)$ commutes with extension of the ground field.
