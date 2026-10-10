+++
kind  = "proof"
of    = "sk-p-product"
+++
Throughout, $k$ is algebraically closed of characteristic zero; this is
used through [sk-i-cartier] (Lie algebras compute dimensions, and
$\Lie(G^\circ)=\Lie(G)$) and through [sk-p-comparison].

*Reduction to the general version.* For a semisimple represented degree
datum, the closures $H\subseteq G$ of [sk-d-monodromy] are closed subgroup
schemes of $\GL_n$, $H$ contains the commutators of $G$ by
[sk-i-restriction], and $k^n$ is a semisimple representation of
$G^\circ(k)$ by the last clause of [sk-i-restriction]. So it suffices to
treat closed subgroup schemes $H\subseteq G$ of $\GL_n$ with these two
properties. By [sk-i-cartier] both are reduced, so we may argue with
matrix algebraic groups.

*The Lie algebra.* Let $V=k^n$, $\mathfrak g=\Lie(G^\circ)$,
$\mathfrak h=\Lie(H^\circ)$ and $T=Z(G^\circ)^\circ$. By
[sk-p-comparison], applied to the connected group $G^\circ$ and its
inclusion in $\GL(V)$, whose differential is the inclusion
$\mathfrak g\subseteq\End(V)$ from [sk-d-tangent], a subspace of $V$ is
$G^\circ$-stable if and only if it is $\mathfrak g$-stable; so the
semisimple $G^\circ(k)$-module $V$ is a semisimple, faithful
$\mathfrak g$-module. Then [sk-p-lie], the Lie inclusion
$[\mathfrak g,\mathfrak g]\subseteq\mathfrak h$ of [sk-i-restriction]
(valid as $k$ is algebraically closed of characteristic zero), and the
centre comparison of [sk-p-comparison] give

$$
\mathfrak g=Z(\mathfrak g)+[\mathfrak g,\mathfrak g]
=Z(\mathfrak g)+\mathfrak h
=\Lie(T)+\Lie(H^\circ),
$$

the middle equality because
$[\mathfrak g,\mathfrak g]\subseteq\mathfrak h\subseteq\mathfrak g$.

*The product.* Since $H^\circ$ is connected and contains $1$,
$H^\circ\subseteq G^\circ$, and the central subgroup $T$ of $G^\circ$
commutes with it. So the multiplication $\mu:T\times H^\circ\to G^\circ$
is a homomorphism of group schemes, and its image $K=TH^\circ$ is closed
by [sk-p-geometry]; it is connected, as the image of a connected group.
The differential of $\mu$ is $(x,y)\mapsto x+y$ by [sk-i-cartier]; its
image lies in $\Lie(K)$ and equals $\mathfrak g$. Thus [sk-i-cartier]
gives $\dim K=\dim G^\circ$, and [sk-p-geometry] gives $K=G^\circ$. On
$k$-points this says that every $g\in G^\circ(k)$ is a product $g=ch$
with $c\in T(k)$ and $h\in H^\circ(k)$. Since $k$ is algebraically closed,
the $k$-points of $G^\circ$ are dense and are closed points, and the
image of $\mu$ is closed and contains them all, so $\mu$ is surjective
on underlying spaces.
