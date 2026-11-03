+++
id = "thm-sp-if-e1"
kind = "theorem"
title = "Hypercohomology spectral sequence of the stupid filtration"
lean = ["CategoryTheory.Functor.stupidFiltrationExactCouple", "CategoryTheory.Functor.stupidFiltrationSpectralSequence", "CategoryTheory.Functor.stupidFiltrationE\u2081Iso", "CategoryTheory.Functor.isZero_stupidFiltrationExactCouple_E", "CategoryTheory.Functor.stupidFiltrationE\u2081Iso_inv_comp_d_comp_hom", "CategoryTheory.Functor.stupidFiltrationExactCouple_convergesTo", "CochainComplex.stupidTower", "CategoryTheory.Functor.stupidFiltrationTower", "CategoryTheory.Functor.stupidFiltrationAbutmentFiltration"]
order = 522
uses = ["def-sp-convergence", "def-sp-exact-couple", "def-sp-kinjective-bridge", "def-sp-left-exact-additive", "def-sp-truncation-couple", "lem-sp-kinjective-computes", "lem-sp-long-exact-of-triangle"]
+++
Let $v:\mathcal A\to\mathcal B$ be as in [def-sp-truncation-couple] and let
$K^\bullet$ be a bounded-below complex in $\mathcal A$, with derived functor
$RvK^\bullet$ as in [def-sp-kinjective-bridge]. The stupid truncations
$\sigma_{\geq s}K^\bullet=K^{\geq s}$ give degreewise split short exact
sequences of complexes

$$
 0\to\sigma_{\geq s+1}K^\bullet\to\sigma_{\geq s}K^\bullet\to
 K^s[-s]\to0,
$$

hence distinguished triangles, and applying $Rv$ and taking cohomology gives
an exact couple [def-sp-exact-couple], indexed by $s$ and the total degree
$n$, with

$$
 D^{s,n}=\mathcal H^n\bigl(Rv\,\sigma_{\geq s}K^\bullet\bigr),\qquad
 E^{s,n}=\mathcal H^n\bigl(Rv(K^s[-s])\bigr)\cong R^{n-s}v(K^s).
$$

Its spectral sequence, started at the first page and written with $r=n-s$,
is

$$
 E_1^{r,s}=R^rv(K^s)\Longrightarrow
 \mathcal H^{r+s}(RvK^\bullet),
$$

with $d_1:E_1^{r,s}\to E_1^{r,s+1}$ equal to $R^rv(d_K)$, induced by the
differential of $K^\bullet$. It converges [def-sp-convergence] to
$\mathcal H^n(RvK^\bullet)$ filtered by the images of the maps
$\mathcal H^n(Rv\,\sigma_{\geq s}K^\bullet)\to\mathcal H^n(RvK^\bullet)$, and
the abutment depends only on $K^\bullet$, not on any choice of resolution.
