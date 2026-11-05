+++
kind = "proof"
of = "proposition-unbounded-comparison-finite-coefficients--1"
order = 166002
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
étale $U$ over $X$. On the étale side, $\Gamma(U,-)$ has
cohomological dimension at most $d$ on sheaves of $A$-modules, and by
[Stacks, [07K7](https://stacks.math.columbia.edu/tag/07K7)] the group $H^mR\Gamma(U,K)$ depends only on
$\tau_{\geq N}K$ as soon as $N\leq m-d$. On the pro-étale side, since
$\nu_X^*$ is exact it commutes with truncations, and
Lemma [lemma-truncation-pro-etale-sections], applied with $e=d$ to
$L=\nu_X^*\tau_{<N}K$ and $b=N-1$, shows that $H^m$ and $H^{m+1}$ of
$R\Gamma(U,L)$ vanish as soon as $N<m-d$. For such $N$ both sides are
unchanged when $K$ is replaced by $\tau_{\geq N}K$, and for this
bounded-below complex the map is an isomorphism by
Theorem [theorem-bounded-below-cohomology-comparison].

The functor $\nu_X^*$ preserves direct sums because it is an exact left
adjoint.

*Source:* the proof of Proposition [proposition-unbounded-comparison-finite-coefficients].
