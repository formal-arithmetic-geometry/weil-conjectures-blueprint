+++
id = "theorem-picard-scheme-jacobian-over-separably--3"
kind = "theorem"
title = "The degree-zero component and its rational points"
name_showing = false
order = 1549003
aliases = ["bp-r483-3"]
lean = ["AlgebraicGeometry.exists_jacobian"]
uses = ["theorem-picard-scheme-jacobian-over-separably--1", "definition-abelian-variety"]
+++
Let $k$ and $C$ be as in
[theorem-picard-scheme-jacobian-over-separably--1]. The degree-zero
functor $\operatorname{Pic}^0_{C/k}$ is represented by a commutative
group scheme $J$, proper, smooth of dimension $g$ and geometrically
integral over $k$. Its group law corresponds to tensor product of
invertible sheaves. Thus $J$ is an abelian variety.

Put $\operatorname{Pic}^0(C)=\ker(\deg:\operatorname{Pic}(C)\to\mathbf Z)$.
There is a group isomorphism

$$
\operatorname{Pic}^0(C)\simeq J(k)
$$

sending an invertible sheaf of degree zero to the point classifying
its image in $\operatorname{Pic}^0_{C/k}(k)$.
