+++
kind = "proof"
of = "lemma-rigidity"
order = 1484
+++
Near $X\times y_0$ the map $h$ lands in an affine open of $Z$, and a
map to an affine scheme is given by functions. Since $X$ is proper and
geometrically integral, functions on $X\times V$ are functions on $V$.
Hence $h$ factors through $V$.

Let $W\subset Z$ be an affine open containing $h(X\times y_0)$. Since
$X$ is proper, the image in $Y$ of the closed set $h^{-1}(Z\setminus W)$
is closed, and its complement contains $y_0$. Let $V$ be an affine
open neighbourhood of $y_0$ in this complement. Then $h$ maps
$X\times V$ into the affine scheme $W$. It is therefore determined by
the ring map $\mathcal O(W)\to H^0(X\times V,\mathcal O)$ [Stacks, [01I1](https://stacks.math.columbia.edu/tag/01I1)].
By flat base change [Stacks, [02KH](https://stacks.math.columbia.edu/tag/02KH)] and $H^0(X,\mathcal O_X)=k$
[Stacks, [0BUG](https://stacks.math.columbia.edu/tag/0BUG)], we have $H^0(X\times V,\mathcal O)=\mathcal O(V)$. The
ring map is thus $\operatorname{pr}_2^*$ composed with a ring map
$\mathcal O(W)\to\mathcal O(V)$, and this ring map defines $g$.
