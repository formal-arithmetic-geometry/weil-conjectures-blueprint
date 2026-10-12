+++
id = "thm-sfb-finite-proper-pushforward-left-adjoint"
kind = "theorem"
title = "$Rg_*$ has a right adjoint for proper $g$"
order = 1672
uses = ["def-sfb-finite-lower-star", "sk-def-sfb-derived-categories"]
lean = ["AlgebraicGeometry.ProEtale.isLeftAdjoint_rightDerivedLowerStar_of_isProper"]
+++
Let $\mathcal A$ be a Grothendieck abelian category and $g\colon Z\to Y$ a proper morphism.
Then the derived pushforward

$$
Rg_*=R(g_*)\colon D(Z_{\mathrm{proét}},\mathcal A)\to D(Y_{\mathrm{proét}},\mathcal A)
$$

(the right derived functor [sk-def-sfb-derived-categories] of the pushforward of
[def-sfb-finite-lower-star]) has a right adjoint, denoted $Rg^!$.
