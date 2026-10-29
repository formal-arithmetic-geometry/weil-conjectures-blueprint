+++
id = "thm-sp-spectral-object-yields"
kind = "theorem"
title = "The spectral sequence of a filtered complex"
lean = ["CategoryTheory.DecreasingFiltration.exactCouple", "CategoryTheory.DecreasingFiltration.exactCouple_d", "CategoryTheory.DecreasingFiltration.homologyFiltration", "CategoryTheory.DecreasingFiltration.convergesTo_exactCouple", "CategoryTheory.ExactCouple.spectralSequence", "CategoryTheory.ExactCouple.Hom.spectralSequenceMap", "HomologicalComplex.HomologySequence.δ_naturality", "CategoryTheory.ExactCouple.IsFirstQuadrant", "CategoryTheory.ExactCouple.firstQuadrantSpectralSequence", "CategoryTheory.ExactCouple.firstQuadrantAbutment"]
order = 612
uses = ["def-sp-convergence", "def-sp-exact-couple", "def-sp-filtration", "def-sp-image-filtration", "def-sp-spectral-sequence", "lem-sp-couple-morphism", "lem-sp-long-exact-of-triangle", "lem-sp-page-induction"]
+++
Let $\mathcal A$ be an abelian category and let $K^\bullet$ be a complex in
$\mathcal A$ equipped with a decreasing filtration
[def-sp-filtration] $F^\bullet K^\bullet$ by subcomplexes, with graded
pieces $\operatorname{gr}^pK^\bullet=F^pK^\bullet/F^{p+1}K^\bullet$. Then:

- (a) the long exact cohomology sequences of the short exact sequences
  $0\to F^{p+1}K^\bullet\to F^pK^\bullet\to\operatorname{gr}^pK^\bullet\to0$
  form an exact couple [def-sp-exact-couple] with
  $$
   D^{p,q}=H^{p+q}\bigl(F^pK^\bullet\bigr),\qquad
   E^{p,q}=H^{p+q}\bigl(\operatorname{gr}^pK^\bullet\bigr),
  $$
  $\alpha$ induced by the inclusions, $g$ by the projections and $f$ the
  connecting homomorphisms (bidegrees $(-1,+1)$, $(0,0)$, $(+1,0)$); its
  spectral sequence [def-sp-spectral-sequence] $\bigl(E_r^{p,q},d_r\bigr)_{r\geq1}$
  has
  $$
   E_1^{p,q}=H^{p+q}\bigl(\operatorname{gr}^pK^\bullet\bigr),
   \qquad
   d_r:E_r^{p,q}\longrightarrow E_r^{p+r,q-r+1},
  $$
  the differential $d_1$ being the composite of the connecting homomorphism
  $H^{p+q}(\operatorname{gr}^pK^\bullet)\to H^{p+q+1}(F^{p+1}K^\bullet)$ and
  of the projection
  $H^{p+q+1}(F^{p+1}K^\bullet)\to H^{p+q+1}(\operatorname{gr}^{p+1}K^\bullet)$;
- (b) if the filtration is *bounded*, that is, for every degree $n$ one has
  $F^pK^n=K^n$ for $p\ll0$ and $F^pK^n=0$ for $p\gg0$, then the induced
  filtration [def-sp-image-filtration]
  $F^pH^n(K^\bullet):=\operatorname{im}\bigl(H^n(F^pK^\bullet)\to
  H^n(K^\bullet)\bigr)$ is finite and separated on each $H^n(K^\bullet)$, and
  the spectral sequence converges [def-sp-convergence] to it along the maps
  $H^{p+q}(F^pK^\bullet)\to H^{p+q}(K^\bullet)$; in particular
  $E_\infty^{p,q}\cong\operatorname{gr}^pH^{p+q}(K^\bullet)$;
- (c) the construction is functorial in the pair
  $(K^\bullet,F^\bullet K^\bullet)$: a morphism of filtered complexes induces
  a morphism of the exact couples of (a), hence of the spectral sequences,
  and if it induces isomorphisms on the $E_1$-terms, then it induces
  isomorphisms on all pages [lem-sp-page-induction];
- (d) first-quadrant variant: if $E_1^{p,q}=0$ unless $p\geq0$ and $q\geq0$,
  then the pages $E_r$, $r\geq2$, form a first-quadrant cohomological
  spectral sequence whose entries stabilize for $r>\max(p,q+1)$; if moreover
  the filtration is bounded, with $F^0H^n(K^\bullet)=H^n(K^\bullet)$ and
  $F^{n+1}H^n(K^\bullet)=0$ for $n\geq0$, then by (b) this first-quadrant
  spectral sequence abuts to $\bigl(H^n(K^\bullet)\bigr)_{n\geq0}$ with the
  induced filtrations.
