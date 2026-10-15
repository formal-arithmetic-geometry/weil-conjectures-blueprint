+++
kind = "proof"
of = "det-pe-unbounded-classical-direct-image"
+++
Put $e_X=2\dim X+1$ and $e_Y=2\dim Y+1$. It suffices to show that
$H^mR\Gamma(V,\alpha_K)$ is an isomorphism for every $m$ and every $V$ in the basis
of affine pro-étale objects $V=\varprojlim_iV_i$ over affine opens of $Y$, since
the cohomology sheaves of both sides are the sheafifications of these groups on
this basis (compare [lem-weil-pbc-basis-derived-detection] for the bounded-below
case; the sheafification description holds for unbounded complexes by
K-injective resolutions).

Fix $m$ and $V$, and choose $N<m-e_X-e_Y-1$. Consider the triangle
$\tau_{<N}K\to K\to\tau_{\geq N}K\to$ and the naturality square of $\alpha$.

*Source.* By [det-pe-unbounded-classical-bounds], part (3), $g_{\Et,*}$ has
cohomological dimension at most $e_X$ on $A$-module sheaves, so by Stacks
Project, Tag 07K7, $Rg_{\Et,*}\tau_{<N}K$ lies in degrees $\leq N-1+e_X$. Its
pullback $\nu_Y^*Rg_{\Et,*}\tau_{<N}K$ has classical cohomology in the same
degrees, and $V$ satisfies the bound $e_Y$ for classical sheaves on $Y$
([det-pe-unbounded-classical-bounds], part (1), for $Y$). By
[det-pe-unbounded-classical-truncation], part (1), its derived sections on $V$
vanish in degrees $>N+e_X+e_Y$, in particular in degrees $m$ and $m+1$.

*Target.* $R\Gamma(V,Rg_{\Proet,*}M)\cong R\Gamma(X\times_YV,M)$ for every $M$,
because $g_{\Proet}^{-1}$ of the object $V$ is $X\times_YV$ and $Rg_{\Proet,*}$
preserves K-injectives. The object $X\times_YV$ of $X_{\Proet}$ satisfies the bound
$e_X$ for classical sheaves ([det-pe-unbounded-classical-bounds], part (2)), and
$\nu_X^*\tau_{<N}K$ has classical cohomology in degrees $\leq N-1$, so its derived
sections on $X\times_YV$ vanish in degrees $>N+e_X$, in particular in degrees $m$
and $m+1$.

*Conclusion.* By the long exact sequences, $H^mR\Gamma(V,-)$ of the source and of
the target for $K$ agree with those for $\tau_{\geq N}K$, compatibly with
$\alpha$. For the bounded-below complex $\tau_{\geq N}K$, $\alpha$ is an
isomorphism by [prop-weil-pbc-comparison-direct-image] ($g$ is quasi-compact and
quasi-separated, being of finite type between Noetherian schemes). Hence
$H^mR\Gamma(V,\alpha_K)$ is an isomorphism, as required.
