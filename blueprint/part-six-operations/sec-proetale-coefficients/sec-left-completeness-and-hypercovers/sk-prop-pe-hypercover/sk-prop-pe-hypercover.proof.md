+++
kind = "proof"
of = "sk-prop-pe-hypercover"
uses = ["sk-cor-pe-sections"]
+++
We build a hypercover whose terms have no higher cohomology, so that
the hypercover spectral sequence collapses to the complex of sections.
We start with a weakly contractible cover of $U$, and at each stage we cover
the matching object by weakly contractible affines, as for fibre
products above. The matching objects are
finite limits of quasi-compact, quasi-separated schemes, so they are again
quasi-compact and quasi-separated and are covered by finitely many affine
weakly contractible objects. Taking finite disjoint unions, we get a single affine
term in each degree; see [Stacks, Tag 09A1](https://stacks.math.columbia.edu/tag/09A1).

For a sheaf $M$, the hypercover spectral sequence has
$E_1^{r,s}=H^s(W_r,M)$, and the rows with $s>0$ vanish by
Corollary [sk-cor-pe-sections](1). The remaining row is the
cosimplicial complex of sections. For bounded-below $K^\bullet$, choose
a bounded-below injective resolution $K^\bullet\to I^\bullet$. Since
evaluation on $W_r$ is exact, $K^\bullet(W_r)\to I^\bullet(W_r)$ is a
quasi-isomorphism. After a shift, both double complexes lie in the
first quadrant, so their total complexes are quasi-isomorphic, and
hypercover descent for $I^\bullet$ identifies the second with
$R\Gamma(U,K)$. See [Stacks, Tag 09A2](https://stacks.math.columbia.edu/tag/09A2).
