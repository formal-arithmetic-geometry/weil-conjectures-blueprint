+++
id = "sk-p-comparison"
kind = "proposition"
title = "Group–Lie comparison"
order = 2800
uses = ["sk-d-geometry", "sk-d-lie", "sk-d-tangent", "sk-i-cartier", "sk-p-geometry"]
lean = ["AlgebraicGeometry.GeneralLinearGroup.invariant_iff_differential_invariant", "AlgebraicGeometry.GeneralLinearGroup.range_lieAlgebraMap_identityComponent_center"]
tags = ["sketch"]
+++
Let $k$ be algebraically closed of characteristic zero and let $G$ be a
connected matrix algebraic group over $k$.
For a rational representation $r:G\to\GL(M)$, $M=k^m$,
a subspace $U\subseteq M$ is invariant under $G(k)$ if and only if it is
invariant under $dr(\Lie(G))$. Moreover,

$$
\Lie\bigl(Z(G)^\circ\bigr)=Z\bigl(\Lie(G)\bigr),
$$

as subspaces of $\Lie(G)$ via the differential of the inclusion
$Z(G)^\circ\subseteq G$.
