+++
kind = "proof"
of = "det-pe-injective-acyclicity-reduction"
+++
*(1).* Choose an injective resolution $G\to J^\bullet$ in
$\Mod(X_{\Proet},\Lambda_X)$. The direct image $\nu_{X,*}$ is restriction to the
étale subsite, so $R\nu_{X,*}G$ is represented by the complex of presheaves
$W\mapsto J^\bullet(W)$ on $X_{\Et}$ (these are already sheaves), and
$R^q\nu_{X,*}G$ is the $q$-th cohomology sheaf of this complex, i.e. the
sheafification of $W\mapsto H^q(J^\bullet(W))$. For an étale $W\to X$, the
restriction $J^\bullet|_W$ is an injective resolution of $G|_W$ on the slice
$W_{\Proet}$ by [lem-weil-pbc-proetale-restriction-injectives], so
$H^q(J^\bullet(W))=H^q(W_{\Proet},G|_W)$. Affine étale objects form a basis
of $X_{\Et}$, so sheafification may be computed from the presheaf on them. If
the presheaf vanishes on this basis, its sheafification is zero.

*(2).* For $W\to X$ étale, the slice of $X_{\Proet}$ over $W$ is $W_{\Proet}$ and
the slice of $X_{\Et}$ over $W$ is $W_{\Et}$; the comparison morphisms commute
with these localizations because $\nu_X^*$ commutes with restriction to $W$ (both
composites are inverse images along the commutative square of continuous
inclusion functors of sites, cf. [def-weil-pbc-site-comparison-morphism]).
Hence $(\nu_X^*I)|_W\cong\nu_W^*(I|_W)$. Restriction to an étale $W$ has the exact
left adjoint extension by zero, so it preserves injectives
([lem-weil-pbc-etale-restriction-injectives]). Now $W$ is affine, and $W$
itself is a basis object of $W_{\Proet}$ (with the constant presentation), so
[lem-weil-pbc-comparison-injective-acyclicity], applied to the affine scheme
$W$ and the injective sheaf $I|_W$, gives
$H^q(W_{\Proet},\nu_W^*(I|_W))=0$ for $q>0$.

The final assertion follows by combining (1) with $G=\nu_X^*I$ and (2).
