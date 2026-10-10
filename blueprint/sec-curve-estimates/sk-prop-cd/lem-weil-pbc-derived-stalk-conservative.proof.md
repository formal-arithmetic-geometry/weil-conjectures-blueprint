+++
kind  = "proof"
of    = "lem-weil-pbc-derived-stalk-conservative"
+++
By [def-weil-pbc-derived-categories] the category $\Dplus(T_{\Et})$ is the
full subcategory of the Verdier localization of the complex category at the
quasi-isomorphisms consisting of the bounded-below complexes, so a morphism
of complexes is an isomorphism of $\Dplus(T_{\Et})$ precisely when it is a
quasi-isomorphism, that is, precisely when it induces an isomorphism on every
cohomology sheaf.

Assume that $\mathcal H^i(K)_{\bar t}\to\mathcal H^i(L)_{\bar t}$ is an
isomorphism for every geometric point $\bar t$ and every $i$. By
[prop-weil-pbc-geometric-stalks-exact] the stalk functor is exact, so it
commutes with the formation of cohomology sheaves and the stalk of the
morphism $\mathcal H^i(K)\to\mathcal H^i(L)$ of sheaves of
[def-weil-pbc-etale-sheaves] at $\bar t$ is the displayed isomorphism. By
[lemma-weil-pbc-geometric-stalk-conservative] each $\mathcal H^i(K)\to\mathcal
H^i(L)$ is therefore an isomorphism of sheaves, so $K\to L$ is a
quasi-isomorphism, hence an isomorphism of $\Dplus(T_{\Et})$.

Conversely, an isomorphism of $\Dplus(T_{\Et})$ is a quasi-isomorphism, so it
induces isomorphisms $\mathcal H^i(K)\to\mathcal H^i(L)$ for all $i$;
applying the exact stalk functor of
[prop-weil-pbc-geometric-stalks-exact] gives the asserted isomorphisms on
geometric stalks.
