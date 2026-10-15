+++
kind = "proof"
of = "det-pe-wc-rings-retraction"
+++
*Choice of components.* By [det-pe-wlocal-components], $T$ and $R^c:=(\operatorname{Spec}R)^c$
are profinite and $R^c\cong\pi_0(\operatorname{Spec}R)$, which is extremally disconnected
because $R$ is w-contractible. The map $T\to R^c$ is continuous and surjective
([det-pe-wc-rings-w-local-refinement], 3). By [det-pe-stonean-projective] (1 $\Rightarrow$ 3)
it has a continuous section $\sigma$. Its image $T'=\sigma(R^c)$ is compact, hence closed
in $T$ and in $\operatorname{Spec}B'$, and $T'\to R^c$ is a continuous bijection of compact
Hausdorff spaces, hence a homeomorphism.

*The algebra $B''$.* By [lem-weil-pbc-retained-localization], $B'\to B''$ is ind-Zariski,
the points of $\operatorname{Spec}B''$ are the points of $\operatorname{Spec}B'$
generalizing a point of $T'$, with unchanged local rings, and $\operatorname{Spec}B''$ is
w-local with closed point set $T'$. By [lem-weil-pbc-ind-etale-stability], $R\to B''$ is
ind-étale, in particular flat.

*Bijectivity on spectra and local rings.* Let $t\in T'$ lie over $\mathfrak m\in R^c$.
Since $R$ is w-strictly local, $R_{\mathfrak m}$ is strictly henselian, so
$R_{\mathfrak m}\to B''_t=B'_t$ is an isomorphism by [det-pe-wc-rings-local-iso]. The
points of $\operatorname{Spec}B''$ generalizing $t$ are the primes of $B''_t$, so they map
bijectively onto the primes of $R_{\mathfrak m}$, i.e. onto the primes $\mathfrak p\subset
\mathfrak m$ of $R$, with $R_{\mathfrak p}\to B''_{\mathfrak q}$ an isomorphism (a
localization of $R_{\mathfrak m}\cong B''_t$). Every point of $\operatorname{Spec}B''$
generalizes exactly one $t\in T'$ (w-locality), every prime $\mathfrak p$ of $R$ lies in
exactly one maximal ideal $\mathfrak m$ (w-locality of $R$), and $t\mapsto\mathfrak m$ is a
bijection $T'\to R^c$. Hence $\operatorname{Spec}B''\to\operatorname{Spec}R$ is bijective,
and $R_{\mathfrak q\cap R}\to B''_{\mathfrak q}$ is an isomorphism for every prime
$\mathfrak q$ of $B''$.

*$R\to B''$ is an isomorphism.* It suffices that $R_{\mathfrak p}\to
B''\otimes_RR_{\mathfrak p}$ is an isomorphism for every prime $\mathfrak p$ of $R$. Let
$\mathfrak q$ be the unique prime of $B''$ over $\mathfrak p$. The primes of
$B''\otimes_RR_{\mathfrak p}$ are the primes $\mathfrak q'$ of $B''$ with
$\mathfrak q'\cap R\subset\mathfrak p$. For such $\mathfrak q'$, going down for the flat map
$R\to B''$ gives a prime $\mathfrak q''\subset\mathfrak q$ with
$\mathfrak q''\cap R=\mathfrak q'\cap R$; by injectivity $\mathfrak q''=\mathfrak q'$, so
$\mathfrak q'\subset\mathfrak q$. Hence $B''\otimes_RR_{\mathfrak p}$ is local with maximal
ideal $\mathfrak q$, so it equals its localization $B''_{\mathfrak q}$, and
$R_{\mathfrak p}\to B''_{\mathfrak q}$ is an isomorphism by the previous step.

The composite $B\to B'\to B''\xrightarrow{\ \sim\ }R$ (inverse of $R\to B''$) is an
$R$-algebra map whose composite with $R\to B$ is the identity.
