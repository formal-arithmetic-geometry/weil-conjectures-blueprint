+++
kind = "proof"
of = "proposition-exact-products--2"
order = 88004
uses = ["proposition-exact-products--1"]
+++
First, exactness of the product functor implies that it commutes with
the homology of short complexes. Applying this to the three terms
around each degree of a complex gives
$H^q(\prod_i K_i)\simeq\prod_i H^q(K_i)$, with the comparison induced
by the projections.

Suppose now that $\mathcal A$ admits K-injective resolutions, and choose
quasi-isomorphisms $K_i\to I_i$ with each $I_i$ K-injective. Termwise
products are products in the homotopy category, since maps and
homotopies into a product can be assembled coordinatewise. It follows
that $\prod_i I_i$ is K-injective: every map from an acyclic complex is
zero in the homotopy category after each projection, hence is zero.
Maps into a K-injective complex in the derived category are computed in
the homotopy category. Thus $\prod_i I_i$, with its projections, is
also the product in $D(\mathcal A)$.

The induced map $\prod_i K_i\to\prod_i I_i$ is a quasi-isomorphism by
the cohomology comparison above. Its image in the derived category,
together with the images of the maps $K_i\to I_i$, transports this
product cone to the cone with vertex $P$. The same cohomology comparison
gives the asserted formula for its cohomology.

Finally, $\operatorname{Mod}(X_{\mathrm{pro}\acute{e}t},\mathcal R)$ is
a Grothendieck abelian category, so it admits K-injective resolutions.
Its products are exact by [proposition-exact-products--1], giving the
stated specialization.
