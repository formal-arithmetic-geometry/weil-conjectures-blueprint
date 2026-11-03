+++
id = "prose-F-03"
kind = "hidden"
title = "The Lie algebra and the differential of a representation"
order = 986
+++
Lemma [sk-p-product] compares the monodromy groups through
their Lie algebras, and needs two translations between a connected
group and its Lie algebra: the two have the same stable subspaces in a
representation, and the Lie algebra of the identity component of the
center is the center of the Lie algebra
(Lemma [sk-p-comparison]). The first turns semisimplicity of the
Weil representation into semisimplicity of a module over the Lie
algebra, where Proposition [sk-p-lie] applies. The
second converts the decomposition of the Lie algebra into the identity
$G^\circ=Z(G^\circ)^\circ H^\circ$. Both are proved by the principle of the
previous subsection, applied to a stabilizer and to the kernel of the
adjoint representation, after computing their Lie algebras with dual
numbers. Connectedness is needed in the first translation: the finite
group $\{\pm1\}\subset\GL_1$ has zero Lie algebra, so every subspace is
stable under its Lie algebra, but $-1$ need not stabilize a line of a
representation: if $-1$ acts on $V=\Lambda^2$ by
$\operatorname{diag}(1,-1)$, it does not stabilize the line spanned by
$(1,1)$.

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
lie in the subring $\Omega[\varepsilon\eta]$, which is a ring of dual numbers,
and the equations of $G$ hold for it in the larger ring, hence in this
subring. Therefore $[X,Y]\in\operatorname{Lie}(G)$. The
differential of a representation $r:G\to\GL(M)$ is characterized
by

$$
r(1+\varepsilon X)=1+\varepsilon\,dr(X).
$$

Applying $r$ to the commutator of $1+\varepsilon X$ and $1+\eta Y$ shows
that $dr[X,Y]=[dr(X),dr(Y)]$, so $dr$ is a Lie algebra homomorphism.
