+++
id = "lemma-injectivity-base-change-map-degree--3"
kind = "lemma"
title = "Injectivity of the base change map in degree $q$ (3)"
name_showing = false
order = 673003
aliases = ["bp-r202-3"]
lean = ["AlgebraicGeometry.Etale.mono_cokernelDesc"]
+++
Let $\Lambda$ be a commutative ring, $g:Y'\to Y$ a morphism of schemes,
and $q\in\mathbf Z$ with $q\geq1$. Suppose that degree-$(q-1)$ base
change along $g$ is an isomorphism for every qcqs morphism $f:Z\to Y$
and every sheaf of $\Lambda$-modules on $Z_{\acute{e}t}$.

For such an $f$, form $Z'=Y'\times_Y Z$ with projections $g':Z'\to Z$
and $f':Z'\to Y'$. Write $b_M^r$ for the map on degree-$r$ cohomology
of [definition-derived-base-change-map] evaluated at $M[0]$.
For an embedding $M\hookrightarrow I$ into an injective sheaf of
$\Lambda$-modules on $Z_{\acute{e}t}$, the natural map
$R^qf'_*g'^{-1}M\to R^qf'_*g'^{-1}I$ induces an injection

$$
\operatorname{coker}(b_M^q)\hookrightarrow R^qf'_*g'^{-1}I.
$$

Here $R^qf'_*g'^{-1}I$ denotes $H^q(Rf'_*g'^*(I[0]))$.
