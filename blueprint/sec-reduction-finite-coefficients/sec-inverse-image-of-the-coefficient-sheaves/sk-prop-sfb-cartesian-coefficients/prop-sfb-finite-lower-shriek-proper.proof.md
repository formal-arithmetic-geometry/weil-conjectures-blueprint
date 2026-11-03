+++
kind  = "proof"
of    = "prop-sfb-finite-lower-shriek-proper"
uses = ["def-sfb-finite-extension-by-zero-adjunction", "lem-sfb-finite-extension-by-zero-fully-faithful"]
+++
Let $(X\xrightarrow{i}\bar X\xrightarrow{g}Y)$ be the chosen compactification. Apart from
$g_*(i_!\to i_*)$, the factors of $\iota_f$ are isomorphisms, so it suffices that
$i_!\to i_*$ is an isomorphism. Since $g$ is separated and $f=g\circ i$ is proper, $i$ is
proper. A proper open immersion has closed image, so $i(X)$ is open and closed.

Let $j\colon U\to S$ be an open immersion with closed image, and let $k\colon W\to S$ be
the open complement. Then $\{j,k\}$ is a Zariski cover, hence a pro-étale cover, and the
restrictions $j^*$, $k^*$ are jointly conservative. It therefore suffices to check that
$j^*$ and $k^*$ of the map $j_!F\to j_*F$ are isomorphisms.

- $j^*(j_!F\to j_*F)$ is an isomorphism. Both $\mathrm{id}\to j^*j_!$ and
  $j^*j_*\to\mathrm{id}$ are isomorphisms ([lem-sfb-finite-extension-by-zero-fully-faithful]),
  and the triangle identities identify the restricted map with their composite.
- $k^*j_*F=0$. For $T$ over $W$ the fibre product $T\times_SU$ is empty, since the images
  are disjoint, and a sheaf has zero sections over the empty scheme. So
  $(k^*j_*F)(T)=F(T\times_SU)=0$.
- $k^*j_!F$ is initial. For every $H$,
  $\Hom(k^*j_!F,H)\cong\Hom(j_!F,k_*H)\cong\Hom(F,j^*k_*H)$ by the two adjunctions
  ([def-sfb-finite-extension-by-zero-adjunction]), and $j^*k_*H=0$ by the previous step
  with $j$ and $k$ exchanged.

Hence $k^*(j_!F\to j_*F)$ is a map between zero objects, so it is an isomorphism. The zero
object of the abelian category $\mathcal A$ is used here.
