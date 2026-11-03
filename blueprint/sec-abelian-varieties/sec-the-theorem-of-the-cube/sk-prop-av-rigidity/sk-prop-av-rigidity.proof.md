+++
kind = "proof"
of = "sk-prop-av-rigidity"
+++
Let $W\subset Z$ be an affine open containing $h(X\times y_0)$. Since
$X$ is proper, the image in $Y$ of the closed set $h^{-1}(Z\setminus W)$
is closed, and its complement contains $y_0$; let $V$ be an affine
open neighbourhood of $y_0$ in this complement. Then $h$ maps
$X\times V$ into the affine scheme $W$, so it is determined by the ring
map $\mathcal O(W)\to H^0(X\times V,\mathcal O)$ [Stacks, Tag 01I1](https://stacks.math.columbia.edu/tag/01I1). By flat
base change [Stacks, Tag 02KH](https://stacks.math.columbia.edu/tag/02KH) and $H^0(X,\mathcal O_X)=k$ [Stacks, Tag 0BUG](https://stacks.math.columbia.edu/tag/0BUG), we
have $H^0(X\times V,\mathcal O)=\mathcal O(V)$. Hence the ring map is
$\operatorname{pr}_2^*$ composed with a ring map $\mathcal O(W)\to\mathcal O(V)$,
which defines $g$.
