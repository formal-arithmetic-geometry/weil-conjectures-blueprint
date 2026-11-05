+++
kind = "proof"
of = "proposition-unbounded-comparison-finite-coefficients--2"
order = 166004
+++
By the two lemmas, both sides in a fixed degree depend only on a
bounded-below truncation of $K$, where
Theorems [theorem-bounded-below-cohomology-comparison]
and [theorem-comparison-direct-images] apply. Let $d$ and $c$ be as
in Lemma [lemma-uniform-bounds-pro-etale-affines], fix $K\in
D(X_{\acute{e}t},A)$ and a degree $m$, and consider the triangle
$\tau_{<N}K\to K\to\tau_{\geq N}K$ for an integer $N$ chosen below.

For direct images, we evaluate (2.9)
on a pro-étale affine $V$ over $Y$; these objects form a basis of
$Y_{\mathrm{pro}\acute{e}t}$. The complex $Rg_{\acute{e}t,*}\tau_{<N}K$ has cohomology sheaves
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
degree $N+c$. Choosing $N$ so small that $H^m$ and $H^{m+1}$ vanish on
both sides, both sides of (2.9),
evaluated on $V$ in degree $m$, are unchanged when $K$ is replaced by
$\tau_{\geq N}K$, and for this bounded-below complex the map is an
isomorphism by Theorem [theorem-comparison-direct-images].

*Source:* the proof of Proposition [proposition-unbounded-comparison-finite-coefficients].
