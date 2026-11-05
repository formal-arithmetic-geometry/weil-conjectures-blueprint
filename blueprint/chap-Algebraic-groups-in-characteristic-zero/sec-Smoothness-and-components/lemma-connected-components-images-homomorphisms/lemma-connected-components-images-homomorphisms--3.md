+++
id = "lemma-connected-components-images-homomorphisms--3"
kind = "lemma"
title = "Connected components and images of homomorphisms (3)"
name_showing = false
order = 1720004
aliases = ["bp-r534-3"]
lean = ["AlgebraicGeometry.GeneralLinearGroup.eq_of_le_of_lieSubalgebra_eq"]
uses = []
+++
The criterion for arbitrary group schemes is bypassed by the Lean
route, which uses the following form for closed subgroups of $\GL_n$.

Let $k$ be a field of characteristic zero and let $I\subseteq J$
be Hopf ideals of $k[\GL_n]$, with $I$ prime. Put $G=V(I)$ and
$K=V(J)$. If
$$
\operatorname{Lie}(K)=\operatorname{Lie}(G)
\quad\text{as Lie subalgebras of }\mathfrak{gl}_n(k),
$$
then $J=I$, and hence $K=G$ as closed subgroup schemes. Here the
matrix Lie algebra of $V(I)$ consists of the matrices $X$ for which
$1+\varepsilon X\in V(I)(k[\varepsilon]/(\varepsilon^2))$.
No algebraic closedness assumption on $k$ is needed.
