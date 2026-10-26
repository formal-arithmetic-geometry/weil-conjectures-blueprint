+++
id = "lem-sfb-finite-upper-star-unit"
kind = "lemma"
title = "$g^*$ preserves the unit"
order = 885
uses = ["def-sfb-finite-lower-star-lax-monoidal", "def-sfb-finite-upper-lower-star-adjunction", "def-weil-pbc-proetale-modules", "lem-weil-pbc-sheaf-tensor-closed"]
lean = ["AlgebraicGeometry.ProEtale.isIso_η_upperStar"]
+++
Let $\mathcal A$ be a closed braided monoidal Grothendieck abelian category and
$g\colon Z\to Y$ a morphism of schemes. The map $g^*\mathbf 1\to\mathbf 1$, mate under
$g^*\dashv g_*$ ([def-sfb-finite-upper-lower-star-adjunction]) of the unit map
$\mathbf 1\to g_*\mathbf 1$ of [def-sfb-finite-lower-star-lax-monoidal], is an isomorphism.

In particular, for a finite discrete ring $\Lambda$ and $\mathcal A$ the category of
$\Lambda$-modules, the unit on $Y_{\mathrm{proét}}$ is the sheaf $\Lambda_{Y,\Proet}$ of
[def-weil-pbc-proetale-modules], and the structure map
$g^{-1}\Lambda_{Y,\Proet}\to\Lambda_{Z,\Proet}$ is an isomorphism.
