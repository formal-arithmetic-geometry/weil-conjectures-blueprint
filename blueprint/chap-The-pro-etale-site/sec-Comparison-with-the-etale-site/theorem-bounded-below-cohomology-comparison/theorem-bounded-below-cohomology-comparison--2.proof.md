+++
kind = "proof"
of = "theorem-bounded-below-cohomology-comparison--2"
order = 123004
+++
Since $\nu_X^*$ is exact, applying it termwise preserves acyclic complexes
and quasi-isomorphisms, so it defines
$\nu_X^*:D(X_{\acute{e}t},\Lambda)\to D(X_{\mathrm{pro}\acute{e}t},\Lambda)$ on the unbounded derived
categories. As in clause [proposition-unbounded-functors-products--1], sheaves of $\Lambda$-modules on
$X_{\mathrm{pro}\acute{e}t}$ form a Grothendieck category, every complex $N$ has a K-injective
resolution $N\to J$ [Stacks, [079P](https://stacks.math.columbia.edu/tag/079P)], and $R\nu_{X,*}N$ is represented by
$\nu_{X,*}J$.

We first check that $R\nu_{X,*}$ is right adjoint to $\nu_X^*$ on the
unbounded derived categories. Write $[C,C']$ for maps of complexes up to
homotopy. The adjunction $\nu_X^*\dashv\nu_{X,*}$ on sheaves of modules gives,
for complexes $C$ on $X_{\acute{e}t}$ and $J$ on $X_{\mathrm{pro}\acute{e}t}$, an isomorphism of Hom
complexes, hence a bijection $[C,\nu_{X,*}J]\simeq[\nu_X^*C,J]$. If $J$ is
K-injective and $C$ is acyclic, then $\nu_X^*C$ is acyclic, so
$[\nu_X^*C,J]=0$ and therefore $[C,\nu_{X,*}J]=0$. Thus $\nu_{X,*}J$ is
K-injective. Maps in the derived category into a K-injective complex are
maps up to homotopy, so for every $K$ and every $N$ with K-injective
resolution $N\to J$ we obtain bijections, natural in $K$ and $N$,

$$
\Hom(K,R\nu_{X,*}N)=[K,\nu_{X,*}J]\simeq[\nu_X^*K,J]
=\Hom(\nu_X^*K,N).
$$

For any adjunction with unit $\eta$, the map $f\mapsto\nu_X^*f$ is the
composite of $f\mapsto\eta_M\circ f$, from $\Hom(K,M)$ to
$\Hom(K,R\nu_{X,*}\nu_X^*M)$, with the adjunction bijection; this is one of
the triangle identities. It therefore suffices to show that
$\eta_M:M\to R\nu_{X,*}\nu_X^*M$ is an isomorphism for
$M\in D^+(X_{\acute{e}t},\Lambda)$. For such $M$ the complex $\nu_X^*M$ is bounded
below, and a bounded-below complex of injectives is K-injective. So
$R\nu_{X,*}\nu_X^*M$ and $\eta_M$ are the object and the map of
(2.7), and clause [theorem-bounded-below-cohomology-comparison--1] shows that $\eta_M$ is an
isomorphism. Restricting to $K\in D^+(X_{\acute{e}t},\Lambda)$ gives the final
assertion.

*Source:* the proof of Theorem [theorem-bounded-below-cohomology-comparison].
