+++
id = "sk-prop-injectivity"
kind = "lemma"
title = "Injectivity in the lowest unknown degree"
order = 1427
uses = ["sk-def-bc", "sk-def-exchange"]
lean = ["AlgebraicGeometry.Etale.mono_baseChangeHomologyMap", "AlgebraicGeometry.Etale.mono_cokernelMap", "AlgebraicGeometry.Etale.mono_cokernelDesc"]
tags = ["sketch"]
+++
Let $g:Y'\to Y$ be a morphism and $n$ an integer invertible on $Y$. Recall that
$\mathrm{BC}(g,n,r)$ means: for every scheme $T$ over $Y$, every qcqs morphism $Z\to T$,
every sheaf of $\mathbf Z/n$-modules $M$ on $Z_{\mathrm{\acute et}}$ and every
$0\leq i\leq r$, the degree-$i$ exchange map ([sk-def-exchange]) for the square with base
change $Y'\times_YT\to T$ and direct image along $Z\to T$ is an isomorphism.

Suppose $q\geq1$ and $\mathrm{BC}(g,n,q-1)$ holds. For every square
obtained by base change as in the definition of $\mathrm{BC}$ and every
sheaf of $\mathbf Z/n$-modules $M$ on $Z_{\mathrm{\acute et}}$, the degree-$q$ exchange map
$b_M^q\colon g^{-1}R^qf_*M\to R^qf'_*u^{-1}M$ is injective. An inclusion
$M\hookrightarrow N$ induces

$$
 \operatorname{coker}(b_M^q)
   \hookrightarrow\operatorname{coker}(b_N^q).
$$

For an embedding $M\hookrightarrow I$ with $I$ injective in the
category of étale sheaves of $\mathbf Z/n$-modules, this cokernel
embeds into $R^qf'_*u^{-1}I$.

*Complement.* In the notation of [sk-def-bc] (smooth side $f$, qcqs side $g$), the same holds
for an arbitrary commutative ring $\Lambda$ in place of $\mathbf Z/n$:

Let $\Lambda$ be a commutative ring, let $q\ge1$ and assume
$\mathrm{BC}(f,\Lambda,q-1)$ of [sk-def-bc] holds. Then for every square
as there (with $g$ quasi-compact and quasi-separated) and every sheaf
$\mathcal F$ of $\Lambda$-modules on $T_{\Et}$:

1. the base-change map
$f^{-1}R^qg_*\mathcal F\to R^qh_*e^{-1}\mathcal F$ is *injective*;
1. if $\mathcal F\subseteq\mathcal G$ with $\mathcal G$ a sheaf of
$\Lambda$-modules, the cokernel for $\mathcal F$ is contained in the cokernel for
$\mathcal G$;
1. if moreover $\mathcal G$ is an injective sheaf of
$\Lambda$-modules, that cokernel is contained in
$R^qh_*e^{-1}\mathcal G$.

Consequently a failure of $\mathrm{BC}(f,\Lambda,q)$ is witnessed by a nonzero
element of the cokernel in the stalk at a geometric point of $X$.
