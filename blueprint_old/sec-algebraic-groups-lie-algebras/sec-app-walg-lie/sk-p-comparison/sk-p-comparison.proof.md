+++
kind = "proof"
of = "sk-p-comparison"
+++
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
Lemma [sk-p-geometry] shows that $S=G$. Conversely, if
$U$ is $G$-stable, then $S=G$, and the displayed formula shows that $U$
is $\operatorname{Lie}(G)$-stable.

Put $\mathfrak g=\operatorname{Lie}(G)$. We claim that the kernel of the
adjoint representation $G\to\GL(\mathfrak g)$ is the center. Indeed, if
$g$ acts trivially on $\mathfrak g$, then the centralizer $C_G(g)$ is a
closed subgroup scheme whose Lie algebra, the fixed space of
$\operatorname{Ad}(g)$, is $\mathfrak g$, so it equals $G$
by Lemma [sk-p-geometry]. Conversely, a central element
acts trivially. Since the kernel and the center are reduced by
Cartier's theorem, their equality on $\Omega$-points is an equality of
schemes. Finally, the formula

$$
\operatorname{Ad}(1+\varepsilon X)(Y)=Y+\varepsilon[X,Y]
$$

shows that
$\operatorname{Lie}(Z(G))=\ker(\operatorname{ad})=Z(\mathfrak g)$,
and $Z(G)^\circ$ has the same Lie algebra as $Z(G)$ by
Proposition [sk-i-cartier].
