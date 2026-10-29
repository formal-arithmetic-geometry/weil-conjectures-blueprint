+++
kind = "proof"
of = "sk-prop-pe-unbounded-classical"
uses = ["sk-prop-sf-comparison", "sk-thm-pe-direct-image-comparison", "sk-thm-pe-classical-sheaves"]
+++
By uniform bounds on cohomological dimension, both sides in a fixed degree depend only on a
bounded-below truncation of $K$, where [sk-prop-sf-comparison] and
[sk-thm-pe-direct-image-comparison] apply. The bounds must not depend on the affine object on which
sections are taken, and on the pro-étale side the Milnor sequence costs one extra degree.

We first prove the bounds; throughout, $d=\dim(X)+\operatorname{cd}_\ell(k)$. Let
$U=\varprojlim_iU_i$ be an object of the affine pro-étale basis of $X$, with $U_i$ affine étale over
$X$, and let $V=\varprojlim_iV_i$ be an object of the affine pro-étale basis of $Y$, with $V_i$ affine
étale over $Y$. Each $U_i$ is affine of finite type over $k$ with $\dim(U_i)\leq\dim(X)$, so by
[Stacks, Tag 0F0V](https://stacks.math.columbia.edu/tag/0F0V) we have
$\operatorname{cd}_\ell(U_i)\leq d$ for sheaves of $A$-modules. This bound is independent of $i$. A
bound of the same kind holds for the fixed morphism $g$ of finite type and its étale base changes
([Stacks, Tag 0F10](https://stacks.math.columbia.edu/tag/0F10)). For the schemes $X\times_YV_i$, we
choose a fixed finite affine open cover of $X$. Since $X$ and $Y$ are separated over $k$, its
intersections and their pullbacks to the affine $V_i$ are affine. Each pullback is étale over the
corresponding intersection and has dimension at most $\dim(X)$. If the cover has $r$ members, the
alternating Čech complex has length $r-1$, so the Čech spectral sequence gives the bound $d+r-1$,
independent of $i$. All these bounds hold for arbitrary sheaves of $A$-modules. On a pro-étale affine
limit, the bound for classical sheaves follows from the comparison of cohomology and continuity.

Next we give the truncation argument on the pro-étale side. Let $U$ be an affine object of
$X_{\Proet}$, and let $L$ be a pro-étale complex with classical cohomology and $H^q(L)=0$ for $q>b$.
By left completeness,

$$
L\simeq R\varprojlim_n\tau_{\geq-n}L.
$$

For each bounded-below term, the derived sections over $U$ have cohomology only up to degree $b+d$.
Derived sections preserve the displayed inverse limit, so by the Milnor sequence $R\Gamma(U,L)$ has no
cohomology above $b+d+1$. We apply this to $L=\tau_{<N}\nu_X^*K$, for which $b=N-1$, so that
$H^jR\Gamma(U,L)=0$ for $j>N+d$. Fix a degree $m$. By the triangle
$L\to\nu_X^*K\to\tau_{\geq N}\nu_X^*K$, as soon as $N<m-d$ (so that $H^m$ and $H^{m+1}$ of
$R\Gamma(U,L)$ vanish) the map

$$
H^mR\Gamma(U,\nu_X^*K)\longrightarrow H^mR\Gamma(U,\tau_{\geq N}\nu_X^*K)
$$

is an isomorphism. The choice of $N$ depends only on $m$ and the bound, so the argument applies to
every $K\in D(X_{\Et},A)$.

On the étale side, the functor $\Gamma(U,-)$ on sheaves of $A$-modules has cohomological dimension at
most $d$. By [Stacks, Tag 07K7](https://stacks.math.columbia.edu/tag/07K7), if a right derived functor
has finite cohomological dimension $d$, then for every complex $K$ its $H^m$ depends only on
$\tau_{\geq m-d}K$. Applied to $R\Gamma(U,-)$, this shows that
$H^mR\Gamma(U,K)\to H^mR\Gamma(U,\tau_{\geq N}K)$ is an isomorphism whenever $N\le m-d$, so the
truncation chosen on the pro-étale side above works on the étale side as well. Full faithfulness of
$\nu_X^*$ means that the unit $K\to R\nu_{X,*}\nu_X^*K$ is an isomorphism, and it suffices to check
this on $H^m$ for each $m$, that is, on the maps $H^mR\Gamma(U,K)\to H^mR\Gamma(U,\nu_X^*K)$ for
affine étale $U$. Since $\nu_X^*$ is exact, it commutes with $\tau_{\geq N}$, so both sides are
unchanged when $K$ is replaced by $\tau_{\geq N}K$. For the bounded-below complex $\tau_{\geq N}K$ the
map is an isomorphism by [sk-prop-sf-comparison], and hence so is the unbounded unit.

For direct images, we evaluate on the object $V=\varprojlim_iV_i$ above. For a classical sheaf, the
cohomology of $X\times_YV$ is the filtered colimit of the cohomology of the $X\times_YV_i$, and by the
uniform bounds we may use the same truncation in a fixed degree on both sides. Explicitly, consider the
triangle $\tau_{<N}K\to K\to\tau_{\geq N}K$. By the relative bound for $g$, the complex
$Rg_{\Et,*}\tau_{<N}K$ has cohomology sheaves in degrees at most $N-1+\operatorname{cd}_\ell(g)$.
Hence $\nu_Y^*Rg_{\Et,*}\tau_{<N}K$ has classical cohomology in the same range, and the truncation
argument above, applied on $Y$ with the bound $\dim(Y)+\operatorname{cd}_\ell(k)$, shows that its
derived sections over $V$ vanish above degree $N+\operatorname{cd}_\ell(g)+\dim(Y)+\operatorname{cd}_\ell(k)$.
On the pro-étale side,
$R\Gamma(V,Rg_{\Proet,*}\nu_X^*\tau_{<N}K)=R\Gamma(X\times_YV,\nu_X^*\tau_{<N}K)$, and the same
argument with the bound $d+r-1$ gives vanishing above degree $N+d+r-1$. Fix a degree $m$ and choose
$N$ so small that $H^m$ and $H^{m+1}$ of the derived sections of $\tau_{<N}K$ over $V$ vanish on both
sides. Then both sides of the comparison map, evaluated on $V$ in degree $m$, are unchanged when $K$
is replaced by $\tau_{\geq N}K$, and for this bounded-below complex the map is an isomorphism by
[sk-thm-pe-direct-image-comparison]. Since the objects $V$ form a basis of $Y_{\Proet}$, the map is an
isomorphism. Finally, $\nu_X^*$ preserves sums because it is an exact left adjoint. In particular,
classical sheaves of $A$-modules are closed under arbitrary direct sums in $\Mod(X_{\Proet},A)$, since
by [sk-thm-pe-classical-sheaves] they are the essential image of $\nu_X^*$.
