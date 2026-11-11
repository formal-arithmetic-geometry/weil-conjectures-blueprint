+++
id = "proposition-jacobian-over-ground-field--5"
kind = "proposition"
title = "Galois equivariance"
order = 1565010
aliases = ["bp-r488-5"]
lean = ["AlgebraicGeometry.exists_jacobian_descent"]
uses = ["definition-relative-picard-functor", "theorem-picard-scheme-jacobian-over-separably", "definition-compactification-refinement--1", "definition-relative-picard-functor--2", "theorem-picard-scheme-jacobian-over-separably--5"]
+++
For every $\sigma\in\operatorname{Gal}(\bar k/k)$, let
$\gamma:C\to C$ be the automorphism over $C_0$ lying over
$\operatorname{Spec}(\sigma)$. Pullback by $\gamma$ preserves
$\operatorname{Pic}^0(C)$, and the isomorphism
$e:\operatorname{Pic}^0(C)\simeq J_0(\bar k)$ satisfies

$$
e(\gamma^*\mathcal L)=e(\mathcal L)\circ\operatorname{Spec}(\sigma).
$$

Thus the identification of geometric points is Galois-equivariant.
