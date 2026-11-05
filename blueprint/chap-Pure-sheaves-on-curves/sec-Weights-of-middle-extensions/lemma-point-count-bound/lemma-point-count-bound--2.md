+++
id = "lemma-point-count-bound--2"
kind = "lemma"
title = "A point-count bound (2)"
name_showing = false
order = 1177002
aliases = ["bp-r363-2"]
lean = ["AlgebraicGeometry.Scheme.Hom.card_fieldPoints_base_eq_le"]
+++
Lean bypasses the separate finite-scheme statement below, using a
bound over each point with finite residue field.

For a finite $k_0$-scheme, the
number of $k_n$-points is bounded independently of $n$.

The bound used in Lean is the following. Let $X_0$ be a scheme over
a field $k_0$, let $K$ be a finite field equipped with a
$k_0$-algebra structure, and let $x\in X_0$ have finite residue
field. Then
$$
\#\{y\in X_0(K):y\text{ maps to }x\}\le[\kappa(x):k_0].
$$
