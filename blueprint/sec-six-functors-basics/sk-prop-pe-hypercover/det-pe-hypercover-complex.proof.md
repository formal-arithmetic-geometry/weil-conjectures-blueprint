+++
kind = "proof"
of = "det-pe-hypercover-complex"
+++
*Finiteness.* $C^{r,b}\neq0$ only for $r\geq0$ and $b\geq a$, so in total degree $q$ only
$0\leq r\leq q-a$ contribute, and $\operatorname{Tot}$ is a finite direct sum in each
degree. The two differentials commute up to the sign $(-1)^r$, so the total differential
squares to zero.

*Injective case.* Choose a bounded-below injective resolution $K^\bullet\to I^\bullet$ with
$I^b=0$ for $b<a$ (possible since $K^\bullet$ is bounded below). Then
$R\Gamma(U,K^\bullet)=I^\bullet(U)$. For an injective $\mathcal R$-module $J$, the
augmented complex $0\to J(U)\to J(W_0)\to J(W_1)\to\cdots$ (alternating sums of face maps)
is exact: this is the hypercovering theorem (Verdier; Stacks Project, Hypercoverings), which says that $\Hom(\mathbf Z[W_\bullet],J)$
computes $\Hom(\mathbf Z[U],J)$ with no higher cohomology, $\mathbf Z[W_\bullet]\to
\mathbf Z[U]$ being a resolution after sheafification. Applying this to each $I^b$, the
double complex $I^b(W_r)$ augmented by the column $I^b(U)$ has exact rows (fixed $b$). It
lies in the region $r\geq-1$, $b\geq a$, so the standard first-quadrant argument (filter by
$b$; the filtration is finite in each total degree) shows that
$I^\bullet(U)\to\operatorname{Tot}(I^b(W_r))$ is a quasi-isomorphism.

*Comparison.* For each $r$, $K^\bullet(W_r)\to I^\bullet(W_r)$ is a quasi-isomorphism,
because evaluation at the weakly contractible $W_r$ is exact
([det-pe-wc-sections-exact]) and so carries the acyclic cone of $K^\bullet\to I^\bullet$
to an acyclic complex. The map of double complexes $K^b(W_r)\to I^b(W_r)$ is thus a
quasi-isomorphism on every column (fixed $r$, up to the sign $(-1)^r$ which does not affect
cohomology). Both lie in the region $r\geq0$, $b\geq a$; filtering by $r$ (finite in each
total degree) shows that the induced map of total complexes is a quasi-isomorphism.
Combining, $R\Gamma(U,K^\bullet)=I^\bullet(U)\simeq\operatorname{Tot}(I^b(W_r))\simeq
\operatorname{Tot}(C)$. A map $K^\bullet\to K'^\bullet$ extends to the injective
resolutions, uniquely up to homotopy, and all maps above are compatible with it, which
gives naturality.
