+++
kind = "proof"
of = "sk-lem-proper-heart-continuity"
+++
Let $W$ be an affine weakly contractible object. The functor $\Gamma(W,-)$ is exact
([sk-cor-pe-wc-sections]) and preserves direct sums (Stacks, Tag 0935). An exact additive functor that
preserves direct sums preserves all colimits, because every colimit is the cokernel of a map between
two direct sums. So $\Gamma(W,-)$ also preserves filtered colimits ([det-proper-heart-continuity-sections]).

By [sk-prop-pe-hypercover] there is a hypercovering $Z_\bullet\to Z$ with every $Z_n$ affine weakly
contractible, and $R\Gamma(Z,M)$ is computed by the cochain complex $M(Z_\bullet)$. Each term of this
complex commutes with filtered colimits and direct sums in $M$, and so does taking cohomology of
complexes of abelian groups. This proves the first assertion ([det-proper-heart-continuity-cohomology]).

For the second, let $V\to Y$ be affine weakly contractible and put $X_V=X\times_YV$, a quasi-compact and
quasi-separated scheme. Since $\Gamma(V,-)$ is exact,

$$
(R^qp_*M)(V)=H^q((X_V)_{\mathrm{proét}},M|_{X_V}).
$$

Restriction to $X_V$ preserves colimits, so the first assertion for $Z=X_V$ shows that the comparison map
for $R^qp_*$ is an isomorphism on sections over $V$. Such $V$ form a basis of the site, so evaluation on
them detects isomorphisms of sheaves ([sk-cor-pe-sections]; [det-proper-heart-continuity-direct-image]).
