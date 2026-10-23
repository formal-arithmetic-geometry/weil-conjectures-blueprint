+++
id = "lem-fd-finite-pushforward-cohomology"
kind = "lemma"
title = "Cohomology of a finite pushforward"
lean = ["AlgebraicGeometry.Etale.mapDerivedCategoryLowerStarCompRightDerivedGlobalSectionsIso"]
order = 3940
uses = ["def-fd-artin-schreier-sheaf", "lem-weil-pbc-grothendieck-spectral-sequence", "lemma-weil-pbc-finite-direct-image-exact", "sk-def-sfb-module-derived-pushpull"]
+++
1. For a finite morphism $\pi:Y\to X_0$ and a torsion etale sheaf $\mathcal F$ on $Y$,

   $$
   H^q(X_0,\pi_*\mathcal F)\cong H^q(Y,\mathcal F)\qquad(q\geq0).
   $$

2. For a finite étale morphism $\pi:Y\to X_0$, a condensed ring $\Lambda$ and a
   $\Lambda_Y$-module $\mathcal F$ on $Y_{\mathrm{proét}}$, one has
   $R\pi_*\mathcal F\simeq\pi_*\mathcal F$, and

   $$
   H^q(X_{0,\mathrm{proét}},\pi_*\mathcal F)\cong H^q(Y_{\mathrm{proét}},\mathcal F)\qquad(q\geq0).
   $$
