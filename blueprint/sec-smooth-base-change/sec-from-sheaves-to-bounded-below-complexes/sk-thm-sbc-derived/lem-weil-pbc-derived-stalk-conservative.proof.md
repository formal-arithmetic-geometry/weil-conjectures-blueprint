+++
kind  = "proof"
of    = "lem-weil-pbc-derived-stalk-conservative"
+++
By [def-weil-pbc-derived-categories] the category $\Dplus(T_{\Et})$ is a
full subcategory of the Verdier localization of the complex category at the
quasi-isomorphisms, and the cohomology functors $\mathcal H^i$ on it are
jointly conservative: a morphism of $\Dplus(T_{\Et})$ is an isomorphism
precisely when it induces an isomorphism on every cohomology sheaf (represent
it by a roof of morphisms of complexes whose backward arrow is a
quasi-isomorphism; it is invertible precisely when the forward arrow is a
quasi-isomorphism too).

Assume that $\mathcal H^i(K)_{\bar t}\to\mathcal H^i(L)_{\bar t}$ is an
isomorphism for every point $t$ and every $i$. By
[prop-weil-pbc-geometric-stalks-exact] the stalk functor is exact, so it
commutes with the formation of cohomology sheaves and the stalk of the
morphism $\mathcal H^i(K)\to\mathcal H^i(L)$ of sheaves of
[def-weil-pbc-etale-sheaves] at $\bar t$ is the displayed isomorphism. By
[lemma-weil-pbc-geometric-stalk-conservative], applied to the family of the
chosen geometric points $\bar t$, one over each point of $T$, each
$\mathcal H^i(K)\to\mathcal H^i(L)$ is therefore an isomorphism of sheaves,
hence $K\to L$ is an isomorphism of $\Dplus(T_{\Et})$.

Conversely, an isomorphism of $\Dplus(T_{\Et})$ induces isomorphisms $\mathcal H^i(K)\to\mathcal H^i(L)$ for all $i$;
applying the exact stalk functor of
[prop-weil-pbc-geometric-stalks-exact] gives the asserted isomorphisms on
geometric stalks.
