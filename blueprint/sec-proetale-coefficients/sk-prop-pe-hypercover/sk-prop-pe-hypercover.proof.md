+++
kind = "proof"
of = "sk-prop-pe-hypercover"
+++
Start with a weakly contractible cover of $U$, and at each stage cover the matching object
by weakly contractible affines; a matching object need not itself be weakly contractible.
The matching objects are finite limits of quasi-compact, quasi-separated schemes and stay
in that subsite, and finite disjoint unions give a single affine term at each stage
(Stacks, Tag 09A1).

For a sheaf $M$, the hypercover spectral sequence has $E_1^{r,s}=H^s(W_r,M)$, and the rows
with $s>0$ vanish by [sk-cor-pe-wc-sections]. The remaining row is the cosimplicial section
complex. For bounded-below $K^\bullet$, choose a bounded-below injective resolution
$K^\bullet\to I^\bullet$. Since evaluation on $W_r$ is exact, $K^\bullet(W_r)\to
I^\bullet(W_r)$ is a quasi-isomorphism. After a shift both double complexes lie in the
first quadrant, so their total complexes are quasi-isomorphic, and hypercover descent for
$I^\bullet$ identifies the second with $R\Gamma(U,K)$ (Stacks, Tag 09A2).
