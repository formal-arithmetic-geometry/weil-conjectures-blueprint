+++
kind = "proof"
of = "proposition-unbounded-comparison-finite-coefficients"
order = 167
uses = ["proposition-etale-implications", "lemma-stability", "proposition-topos-functoriality", "proposition-pro-etale-affines-form-basis", "proposition-left-completeness", "definition-classical-pro-etale-sheaves", "theorem-classical-sheaves-essential-image", "lemma-acyclicity-pulled-back-injectives", "theorem-bounded-below-cohomology-comparison", "corollary-bounded-below-classical-complexes", "lemma-uniform-bounds-pro-etale-affines", "lemma-acyclic-resolutions", "proposition-sp-unique-adjoint", "definition-compactification-refinement"]
+++
By the two lemmas, both sides in a fixed degree depend only on a
bounded-below truncation of $K$, where
Theorems [theorem-bounded-below-cohomology-comparison]
and [theorem-comparison-direct-images] apply. Let $d$ and $c$ be as
in Lemma [lemma-uniform-bounds-pro-etale-affines], fix $K\in
D(X_{\acute{e}t},A)$ and a degree $m$, and consider the triangle
$\tau_{<N}K\to K\to\tau_{\geq N}K$ for an integer $N$ chosen below.

Full faithfulness of $\nu_X^*$ means that the unit
$K\to R\nu_{X,*}\nu_X^*K$ is an isomorphism, and it suffices to check
this on the maps $H^mR\Gamma(U,K)\to H^mR\Gamma(U,\nu_X^*K)$ for affine
étale $U$ over $X$. We first reduce to bounded-below complexes. On the étale side, $\Gamma(U,-)$ has
cohomological dimension at most $d$ on sheaves of $A$-modules, and by
[Stacks, [07K7](https://stacks.math.columbia.edu/tag/07K7)] the group $H^mR\Gamma(U,K)$ depends only on
$\tau_{\geq N}K$ as soon as $N\leq m-d$. On the pro-étale side, since
$\nu_X^*$ is exact it commutes with truncations, and
Lemma [lemma-truncation-pro-etale-sections], applied with $e=d$ to
$L=\nu_X^*\tau_{<N}K$ and $b=N-1$, shows that $H^m$ and $H^{m+1}$ of
$R\Gamma(U,L)$ vanish as soon as $N<m-d$. Hence for such $N$ both sides are
unchanged when $K$ is replaced by $\tau_{\geq N}K$, and for this
bounded-below complex the map is an isomorphism by
Theorem [theorem-bounded-below-cohomology-comparison].

For direct images, we evaluate (2.9)
on a pro-étale affine $V$ over $Y$; these objects form a basis of
$Y_{\mathrm{pro}\acute{e}t}$. As before, we bound the contribution of $\tau_{<N}K$ on both sides. On the étale side, the complex $Rg_{\acute{e}t,*}\tau_{<N}K$ has cohomology sheaves
in degrees at most $N-1+\operatorname{cd}_\ell(g)$, so
$\nu_Y^*Rg_{\acute{e}t,*}\tau_{<N}K$ has classical cohomology in the same range,
and Lemma [lemma-truncation-pro-etale-sections] on $Y$, with
$e=\dim(Y)+\operatorname{cd}_\ell(k)$ (Lemma [lemma-uniform-bounds-pro-etale-affines]
for $Y$), shows that its derived sections
over $V$ vanish above degree
$N+\operatorname{cd}_\ell(g)+\dim(Y)+\operatorname{cd}_\ell(k)$. On the
other side,
$R\Gamma(V,Rg_{\mathrm{pro}\acute{e}t,*}\nu_X^*\tau_{<N}K)=R\Gamma(X\times_YV,\nu_X^*\tau_{<N}K)$,
and the same lemma with $W=X\times_YV$ and $e=c$ gives vanishing above
degree $N+c$. Therefore, choosing $N$ so small that $H^m$ and $H^{m+1}$ vanish on
both sides, both sides of (2.9),
evaluated on $V$ in degree $m$, are unchanged when $K$ is replaced by
$\tau_{\geq N}K$, and for this bounded-below complex the map is an
isomorphism by Theorem [theorem-comparison-direct-images].

The functor $\nu_X^*$ preserves direct sums because it is an exact left
adjoint.
