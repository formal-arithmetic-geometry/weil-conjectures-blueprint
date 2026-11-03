+++
id = "def-sfb-finite-derived-pullback-iso"
kind = "definition"
title = "$Lg^*\\cong D(g^*)$"
order = 2343
uses = ["def-sfb-finite-upper-star", "lem-sfb-finite-upper-star-exact", "det-def-sfb-derived-categories"]
lean = ["AlgebraicGeometry.ProEtale.leftDerivedUpperStarIsoMapDerivedCategory"]
+++
Let $\mathcal A$ be a closed symmetric monoidal Grothendieck abelian category with additive
tensor product and functorial flat resolutions, and $g\colon Z\to Y$ a morphism. The left
derived functor $Lg^*=L(g^*)$ of the pullback of [def-sfb-finite-upper-star], computed on
K-flat resolutions [det-def-sfb-derived-categories], is isomorphic to the functor

$$
D(g^*)\colon D(Y_{\mathrm{proét}},\mathcal A)\to D(Z_{\mathrm{proét}},\mathcal A)
$$

obtained by applying $g^*$ levelwise.
