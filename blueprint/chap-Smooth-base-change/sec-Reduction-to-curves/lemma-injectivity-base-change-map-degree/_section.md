+++
id = "lemma-injectivity-base-change-map-degree"
kind = "lemma"
title = "Injectivity of the base change map in degree $q$"
order = 672
lean = ["AlgebraicGeometry.Etale.mono_baseChangeHomologyMap", "AlgebraicGeometry.Etale.mono_cokernelMap", "AlgebraicGeometry.Etale.mono_cokernelDesc"]
uses = ["definition-derived-base-change-map", "prose-08-06"]
+++
Suppose $q\geq1$ and $\mathrm{BC}(g,n,q-1)$ holds. For every square
obtained by base change as in the definition of $\mathrm{BC}$ and every
sheaf of $\mathbf Z/n$-modules $M$ on $Z_{\acute{e}t}$, the base change map
$b_M^q:g^{-1}R^qf_*M\to R^qf'_*g'^{-1}M$ in degree $q$ is injective. An inclusion
$M\hookrightarrow N$ induces

$$
\operatorname{coker}(b_M^q)
\hookrightarrow\operatorname{coker}(b_N^q).
$$

For an embedding $M\hookrightarrow I$ with $I$ injective in the
category of étale sheaves of $\mathbf Z/n$-modules, the cokernel of
$b_M^q$ embeds into $R^qf'_*g'^{-1}I$.
