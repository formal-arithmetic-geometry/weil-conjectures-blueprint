+++
kind = "proof"
of = "det-pe-unbounded-classical-unit"
+++
Put $e=2\dim X+1$. Every $A$-module sheaf is torsion, since $A$ is finite.

*Cohomology sheaves as sheafified sections.* For $M\in D(X_{\Proet},A)$,
$H^m(R\nu_{X,*}M)$ is the sheafification of $W\mapsto H^mR\Gamma(W_{\Proet},M|_W)$
on affine étale $W\to X$: compute $R\nu_{X,*}$ by a K-injective resolution, whose
restriction to each $W$ is K-injective because restriction has the exact left
adjoint extension by zero; then argue as in [det-pe-injective-acyclicity-reduction],
part (1). Likewise $H^m(K)$ is the sheafification of
$W\mapsto H^mR\Gamma(W_{\Et},K|_W)$, and the unit induces on these presheaves the
maps $R\Gamma(W_{\Et},K)\to R\Gamma(W_{\Proet},\nu_X^*K)$.

*Fixed-degree truncation.* Fix $m$, an affine étale $W\to X$, and $N<m-e-1$.
By [det-pe-unbounded-classical-bounds], $\Gamma(W_{\Et},-)$ has cohomological
dimension at most $e$ on $A$-module sheaves, so by Stacks Project, Tag 07K7,
$R\Gamma(W_{\Et},\tau_{<N}K)$ lies in degrees $\leq N-1+e$ and
$H^mR\Gamma(W_{\Et},K)\to H^mR\Gamma(W_{\Et},\tau_{\geq N}K)$ is an isomorphism.
On the pro-étale side, $W$ (with the constant presentation) satisfies the bound
$e$ for classical sheaves by [det-pe-unbounded-classical-bounds], part (1), and
$\nu_X^*K$ has classical cohomology, so by
[det-pe-unbounded-classical-truncation]
$H^mR\Gamma(W_{\Proet},\nu_X^*K)\to H^mR\Gamma(W_{\Proet},\tau_{\geq N}\nu_X^*K)$
is an isomorphism; and $\tau_{\geq N}\nu_X^*K=\nu_X^*\tau_{\geq N}K$ by exactness.

*Conclusion.* In the commutative square formed by the unit maps for $K$ and for
$\tau_{\geq N}K$ and the two truncation maps, the unit map for the bounded-below
complex $\tau_{\geq N}K$ is an isomorphism on derived sections over $W$ by the
bounded-below comparison ([lem-weil-pbc-comparison-global-cohomology] applied on
$W$, i.e. [sk-prop-sf-comparison]). Hence
$H^mR\Gamma(W_{\Et},K)\to H^mR\Gamma(W_{\Proet},\nu_X^*K)$ is an isomorphism for all
$m$ and all affine étale $W$, so the unit induces isomorphisms of the sheafified
cohomology sheaves, i.e. it is an isomorphism.

Full faithfulness follows as for sheaves: the composite
$\Hom(K,K')\to\Hom(\nu_X^*K,\nu_X^*K')\cong\Hom(K,R\nu_{X,*}\nu_X^*K')$ is
composition with the unit of $K'$. Finally $\nu_X^*$ is exact, so it is computed
termwise and is left adjoint to $R\nu_{X,*}$ on unbounded derived categories; a
left adjoint preserves all direct sums.
