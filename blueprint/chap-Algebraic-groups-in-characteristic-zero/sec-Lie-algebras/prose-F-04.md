+++
id = "prose-F-04"
kind = "hidden"
title = "Lie algebras"
order = 1717
+++
Let $G$ be a connected algebraic group with Lie algebra $\mathfrak g$.
We need two facts (Lemma [lemma-stable-subspaces-center]). In a
representation, $G$ and $\mathfrak g$ have the same stable subspaces.
And the Lie algebra of the identity component of the center of $G$ is
the center of $\mathfrak g$. In the proof of
Lemma [lemma-identity-component] we compare the monodromy groups
through their Lie algebras, and both facts are used there. By the
first, a representation that is semisimple for $G^\circ$ is semisimple
for its Lie algebra. This is what lets
Proposition [proposition-lie-algebras-faithful-semisimple-representation]
apply to the Weil representation. With the second we translate the
decomposition of the Lie algebra into the identity
$G^\circ=Z(G^\circ)^\circ H^\circ$.

We prove both facts by the principle of the previous subsection, applied
to a stabilizer and to the kernel of the adjoint representation. Their
Lie algebras are computed with dual numbers. The first fact needs $G$ to
be connected. For example, the finite group $\{\pm1\}\subset\GL_1$ has
zero Lie algebra, so every subspace of a representation is stable under
its Lie algebra. But if $-1$ acts on $M=\Omega^2$ by
$\operatorname{diag}(1,-1)$, then it does not stabilize the line spanned
by $(1,1)$.

For a closed subgroup $G\subseteq\GL(V)$, the tangent space
$\operatorname{Lie}(G)\subseteq\operatorname{End}(V)$ is described by
dual-number points at $1$:

$$
X\in\operatorname{Lie}(G)
\quad\Longleftrightarrow\quad
1+\varepsilon X\in G(\Omega[\varepsilon]/\varepsilon^2).
$$

The bracket is $[X,Y]=XY-YX$. To see that $\operatorname{Lie}(G)$ is
closed under the bracket, note that over
$\Omega[\varepsilon,\eta]/(\varepsilon^2,\eta^2)$ the commutator of
$1+\varepsilon X$ and $1+\eta Y$ is $1+\varepsilon\eta[X,Y]$. Its entries
lie in the subring $\Omega[\varepsilon\eta]$, which is a ring of dual numbers.
The equations of $G$ hold for this matrix in the larger ring, hence in
this subring. Therefore $[X,Y]\in\operatorname{Lie}(G)$. The
differential of a representation $r:G\to\GL(M)$ is characterized
by

$$
r(1+\varepsilon X)=1+\varepsilon\,dr(X).
$$

Applying $r$ to the commutator of $1+\varepsilon X$ and $1+\eta Y$, we see
that $dr[X,Y]=[dr(X),dr(Y)]$, so $dr$ is a Lie algebra homomorphism.
