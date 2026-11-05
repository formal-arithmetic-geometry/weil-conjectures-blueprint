+++
id = "proposition-cartier-s-theorem--2"
kind = "proposition"
title = "Dimension of the matrix Lie algebra"
name_showing = false
order = 1717002
aliases = ["bp-r533-2"]
lean = ["AlgebraicGeometry.GeneralLinearGroup.finrank_lieSubalgebra"]
uses = []
+++
Let $k$ be a field of characteristic zero, let $n$ be finite, and let
$I\subseteq k[\GL_n]$ be a Hopf ideal. Put $G=V(I)$ and
$B=k[\GL_n]/I$. Describe the Lie algebra as the Lie subalgebra

$$
\operatorname{Lie}(G)
=\{X\in\mathfrak{gl}_n(k):1+\varepsilon X\in G(k[\varepsilon]/(\varepsilon^2))\}.
$$

Then

$$
\dim_k\operatorname{Lie}(G)=\dim B=\dim G,
$$

where $\dim B$ is the Krull dimension of the coordinate ring. This is
the closed matrix subgroup case used in the Lean proof.
