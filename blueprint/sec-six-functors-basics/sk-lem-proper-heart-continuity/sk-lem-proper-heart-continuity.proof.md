+++
kind = "proof"
of = "sk-lem-proper-heart-continuity"
uses = ["sk-cor-pe-sections", "sk-prop-pe-hypercover"]
+++
Let $W$ be an affine weakly contractible object. The functor $\Gamma(W,-)$ is exact
([sk-cor-pe-sections]) and preserves direct sums
([Stacks, Tag 0935](https://stacks.math.columbia.edu/tag/0935)). An exact additive functor that preserves
direct sums preserves all colimits, because every colimit is the cokernel of a map between two direct
sums. Hence $\Gamma(W,-)$ also preserves filtered colimits.

By [sk-prop-pe-hypercover], there is a hypercovering $Z_\bullet\to Z$ with every $Z_n$ affine weakly
contractible, and $R\Gamma(Z,M)$ is computed by the cochain complex $M(Z_\bullet)$. Each term of this
complex commutes with filtered colimits and direct sums in $M$, and so does the cohomology of complexes
of abelian groups. This proves the first assertion.

For the second assertion, let $V\to Y$ be affine weakly contractible and put $X_V=X\times_YV$, a
quasi-compact and quasi-separated scheme. Since $\Gamma(V,-)$ is exact, we have

$$
(R^qp_*M)(V)=H^q((X_V)_{\mathrm{proét}},M|_{X_V}).
$$

Restriction to $X_V$ and $\Gamma(V,-)$ preserve colimits, and hence the first assertion for $Z=X_V$ shows
that the map $\colim_iR^qp_*M_i\to R^qp_*(\colim_iM_i)$ is an isomorphism on sections over $V$, and
similarly for direct sums. Since such $V$ form a basis of the site, evaluation on them detects
isomorphisms of sheaves ([sk-cor-pe-sections]). For abelian sheaves, this second assertion is
[det-pe-bounded-continuity-direct-image].
