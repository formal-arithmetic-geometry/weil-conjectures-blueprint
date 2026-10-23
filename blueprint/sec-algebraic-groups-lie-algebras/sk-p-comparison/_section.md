+++
id = "sk-p-comparison"
kind = "lemma"
title = "Stable subspaces and the center"
lean = ["AlgebraicGeometry.GeneralLinearGroup.invariant_iff_differential_invariant", "AlgebraicGeometry.GeneralLinearGroup.range_lieAlgebraMap_identityComponent_center"]
order = 3708
uses = ["sk-i-cartier", "sk-p-geometry"]
tags = ["sketch"]
+++
For a matrix group $G\subseteq\GL(V)$, define $\Lie(G)$ by its
dual-number points at $1$:

$$
X\in\Lie(G)
\quad\Longleftrightarrow\quad
1+\epsilon X\in G(L[\epsilon]/\epsilon^2).
$$

The bracket is $[X,Y]=XY-YX$. To see that $\Lie(G)$ is closed under the
bracket, note that over $L[\epsilon,\eta]/(\epsilon^2,\eta^2)$ the
commutator of $1+\epsilon X$ and $1+\eta Y$ is $1+\epsilon\eta[X,Y]$. The
differential of a representation $r\colon G\to\GL(M)$ is characterized by

$$
r(1+\epsilon X)=1+\epsilon\,dr(X).
$$

These formulas show that $dr$ is a Lie algebra homomorphism.

Let $G$ be a connected algebraic group and $r\colon G\to\GL(M)$ an
algebraic representation. A subspace of $M$ is $G$-stable if and only if
it is $\Lie(G)$-stable. Moreover

$$
\Lie\bigl(Z(G)^\circ\bigr)=Z\bigl(\Lie(G)\bigr).
$$

*Complement.* For a connected closed subgroup $G\subseteq\GL_n$ over $L$
and a rational representation $r\colon G\to\GL_m$, both statements hold
with the Lie algebras computed by dual numbers as above, $\Lie(Z(G)^\circ)$
being regarded as a subspace of $\Lie(G)$ via the differential of the
inclusion $Z(G)^\circ\subseteq G$.
