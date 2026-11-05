+++
kind = "proof"
of = "lemma-stable-subspaces-center"
order = 1725
uses = ["proposition-cartier-s-theorem"]
+++
In both assertions we compare a closed subgroup with $G$, namely the
stabilizer of a subspace in the first and the kernel of the adjoint
representation in the second. We compute the Lie algebra of this
subgroup with dual numbers and conclude with
Lemma [lemma-connected-components-images-homomorphisms](3).

Let $U\subseteq M$ be a subspace. In a basis of $M$ extending a basis
of $U$, the scheme-theoretic stabilizer $S\subseteq G$ of $U$ is the
closed subgroup defined by the vanishing of the lower-left block of
$r(g)$. Since the lower-left block of $r(1+\varepsilon X)=1+\varepsilon\,dr(X)$
is $\varepsilon$ times that of $dr(X)$, we find

$$
\operatorname{Lie}(S)
=\{X\in\operatorname{Lie}(G):dr(X)U\subseteq U\}.
$$

If $U$ is $\operatorname{Lie}(G)$-stable, then
$\operatorname{Lie}(S)=\operatorname{Lie}(G)$, and
Lemma [lemma-connected-components-images-homomorphisms](3) shows that $S=G$. Conversely, if
$U$ is $G$-stable, then $S=G$, and the displayed formula shows that $U$
is $\operatorname{Lie}(G)$-stable.

Put $\mathfrak g=\operatorname{Lie}(G)$. We claim that the kernel of the
adjoint representation $G\to\GL(\mathfrak g)$ is the center. Indeed, if
$g$ acts trivially on $\mathfrak g$, consider the centralizer $C_G(g)$.
It is a closed subgroup scheme whose Lie algebra is the fixed space of
$\operatorname{Ad}(g)$, that is, all of $\mathfrak g$. So $C_G(g)=G$
by Lemma [lemma-connected-components-images-homomorphisms](3). Conversely, a central element
acts trivially. Since the kernel and the center are reduced by
Cartier's theorem, their equality on $\Omega$-points is an equality of
schemes.

The Lie algebra of the center is now the kernel of a differential. The formula

$$
\operatorname{Ad}(1+\varepsilon X)(Y)=Y+\varepsilon[X,Y]
$$

shows that the differential of $\operatorname{Ad}$ is $\operatorname{ad}$.
The center is a closed subgroup of $\GL(V)$, so the dual-number
description applies to it. By this description, the Lie algebra of
the kernel of a representation is the kernel of its differential. Hence
$\operatorname{Lie}(Z(G))=\ker(\operatorname{ad})=Z(\mathfrak g)$.
By Proposition [proposition-cartier-s-theorem], $Z(G)^\circ$ has the
same Lie algebra as $Z(G)$.
