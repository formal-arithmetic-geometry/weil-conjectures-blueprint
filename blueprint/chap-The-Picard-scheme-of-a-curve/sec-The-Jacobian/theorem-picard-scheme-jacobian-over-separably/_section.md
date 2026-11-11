+++
id = "theorem-picard-scheme-jacobian-over-separably"
kind = "theorem"
title = "The Picard scheme and the Jacobian over a separably closed field"
order = 1552
lean = ["AlgebraicGeometry.exists_jacobian_baseChange", "AlgebraicGeometry.nonempty_tangentSpaceAt_linearEquiv_H_one", "AlgebraicGeometry.theorem_of_the_base", "AlgebraicGeometry.Scheme.picDegreeHom"]
uses = ["definition-compactification-refinement", "definition-relative-picard-functor"]
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
