+++
kind = "proof"
of = "proposition-exact-products"
order = 89
uses = ["definition-ind-etale-pro-etale-weakly", "definition-weak-contractibility", "corollary-evaluation-weakly-contractible-objects"]
+++
By Corollary [corollary-evaluation-weakly-contractible-objects](3),
exactness of sheaves can be checked on affine weakly contractible $W$, and
by part (1) evaluation at such $W$ is exact. Since limits are computed on sections, a
product of short exact sequences therefore evaluates on $W$ to a product of short exact
sequences of $\mathcal R(W)$-modules, which is exact because by the axiom
of choice we may lift a tuple coordinate by coordinate. This proves the
first assertion.

The derived product is the termwise product of K-injective
representatives (complexes $I$ such that maps from acyclic complexes to
$I$ are null-homotopic, the unbounded analogue of bounded-below injective
complexes). Since products are exact, a product of quasi-isomorphisms is a
quasi-isomorphism: its cone is the product of the cones, which is
acyclic. We may therefore replace the K-injective representatives by any
quasi-isomorphic ones. Hence termwise products compute the product in
$D(X_{\mathrm{pro}\acute{e}t},\mathcal R)$, and they commute with cohomology because
products are exact; see [Stacks, [0947](https://stacks.math.columbia.edu/tag/0947), [08TB](https://stacks.math.columbia.edu/tag/08TB)].
