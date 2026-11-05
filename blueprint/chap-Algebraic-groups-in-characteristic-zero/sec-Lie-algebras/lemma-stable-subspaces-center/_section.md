+++
id = "lemma-stable-subspaces-center"
kind = "lemma"
title = "Stable subspaces and the center"
order = 1727
lean = ["AlgebraicGeometry.GeneralLinearGroup.invariant_iff_differential_invariant", "AlgebraicGeometry.GeneralLinearGroup.range_lieAlgebraMap_identityComponent_center"]
uses = ["lemma-normality-geometric-monodromy"]
+++
Let $G\subseteq\GL(V)$ be a connected closed subgroup and
$r:G\to\GL(M)$ an algebraic representation. A subspace of $M$ is $G$-stable if and only if it is
$\operatorname{Lie}(G)$-stable. Moreover

$$
\operatorname{Lie}\bigl(Z(G)^\circ\bigr)
=Z\bigl(\operatorname{Lie}(G)\bigr).
$$
