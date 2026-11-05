+++
id = "proposition-exact-products--2"
kind = "proposition"
title = "Exact products (2)"
name_showing = false
order = 88002
aliases = ["bp-r023-2"]
lean = ["DerivedCategory.isLimitFanMkQObj", "HomologicalComplex.isLimitFanHomology"]
+++
Let $\mathcal A$ be an abelian category and $I$ a set such that
$I$-indexed products exist and are exact in $\mathcal A$. For a family
$(K_i)_{i\in I}$ of complexes in $\mathcal A$, let $P=\prod_{i\in I}K_i$
be their termwise product. If $\mathcal A$ admits K-injective resolutions,
the images of the projections $P\to K_i$ exhibit $P$ as the product of
the $K_i$ in $D(\mathcal A)$.

Moreover, without the assumption on K-injective resolutions, the
projections induce, for every $q\in\mathbf Z$, an isomorphism

$$
H^q(P)\simeq\prod_{i\in I}H^q(K_i).
$$

There is no boundedness assumption on the complexes.

In particular, products in $D(X_{\mathrm{pro}\acute{e}t},\mathcal R)$ are
computed by termwise products of representative complexes, and their
cohomology sheaves are the products of the cohomology sheaves.
