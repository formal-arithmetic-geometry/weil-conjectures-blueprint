+++
kind  = "proof"
of    = "sk-p-comparison"
+++
Let $U\subseteq M$ be a subspace. In a basis of $M$ extending a basis of
$U$, the scheme-theoretic stabilizer $S\subseteq G$ of $U$ is the closed
subgroup defined by the vanishing of the lower-left block of $r(g)$.
Differentiating these equations, we find

$$
\Lie(S)=\{X\in\Lie(G):dr(X)U\subseteq U\}.
$$

If $U$ is $\Lie(G)$-stable, then $\Lie(S)=\Lie(G)$, and [sk-p-geometry]
shows that $S=G$. Conversely, if $U$ is $G$-stable, then $S=G$, and the
displayed formula shows that $U$ is $\Lie(G)$-stable.

Put $\mathfrak g=\Lie(G)$. We claim that the kernel of the adjoint
representation $G\to\GL(\mathfrak g)$ is the center. Indeed, if $g$ acts
trivially on $\mathfrak g$, then the centralizer $C_G(g)$ is a closed
subgroup scheme with Lie algebra $\mathfrak g$, so it equals $G$ by
[sk-p-geometry]. Conversely, a central element acts trivially. Since the
kernel and the center are reduced by Cartier's theorem [sk-i-cartier],
their equality on $L$-points is an equality of schemes. Finally, the
formula

$$
\operatorname{Ad}(1+\epsilon X)(Y)=Y+\epsilon[X,Y]
$$

shows that $\Lie(Z(G))=\ker(\operatorname{ad})=Z(\mathfrak g)$, and
$Z(G)^\circ$ has the same Lie algebra as $Z(G)$ by [sk-i-cartier].
