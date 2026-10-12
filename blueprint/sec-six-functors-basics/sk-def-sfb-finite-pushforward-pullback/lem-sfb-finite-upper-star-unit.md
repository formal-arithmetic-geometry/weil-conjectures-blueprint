+++
id = "lem-sfb-finite-upper-star-unit"
kind = "lemma"
title = "$g^*$ preserves the unit"
order = 1512
uses = ["def-sfb-finite-lower-star-lax-monoidal", "def-sfb-finite-upper-lower-star-adjunction", "sk-def-sfb-sheaf-tensor"]
lean = ["AlgebraicGeometry.ProEtale.isIso_η_upperStar"]
+++
Let $\mathcal A$ be a closed symmetric monoidal Grothendieck abelian category and
$g\colon Z\to Y$ a morphism of schemes. The map $g^*\mathbf 1\to\mathbf 1$, mate under
$g^*\dashv g_*$ ([def-sfb-finite-upper-lower-star-adjunction]) of the unit map
$\mathbf 1\to g_*\mathbf 1$ of [def-sfb-finite-lower-star-lax-monoidal], is an isomorphism.
