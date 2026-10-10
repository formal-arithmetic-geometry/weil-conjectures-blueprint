+++
id = "thm-sp-if-e1"
kind = "theorem"
title = "Hypercohomology spectral sequence via a Cartan--Eilenberg resolution"
order = 522
uses = ["def-sp-convergence", "def-sp-double-complex-total", "def-sp-injective-resolutions", "def-sp-kinjective-bridge", "def-sp-left-exact-additive", "def-sp-truncation-couple", "lem-sp-kinjective-computes", "thm-sp-double-complex-spectral-sequences", "thm-sp-spectral-object-yields"]
+++
Let $v$ be as in [def-sp-truncation-couple] and let $A^{\bullet,\bullet}$ be
a Cartan--Eilenberg resolution of a bounded-below complex $K^\bullet$: the
row $A^{\bullet,s}$ is an injective resolution
[def-sp-injective-resolutions] of $K^s$, and the column cohomologies are the
$\mathcal H^s(K^\bullet)$. Then the filtration of the total complex by the
*second* degree gives the spectral sequence

$$
 E_1^{r,s}=R^rv(K^s)\Longrightarrow
 \mathcal H^{r+s}(RvK^\bullet),
$$

$d_1:E_1^{r,s}\to E_1^{r,s+1}$, induced by the differential of $K^\bullet$,
and the abutment is the cohomology of the derived functor of $K^\bullet$,
independent of the resolution.
