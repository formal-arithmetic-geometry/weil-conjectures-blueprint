+++
id = "thm-sfb-finite-proper-pushforward-left-adjoint"
kind = "theorem"
title = "$Rg_*$ has a right adjoint for proper $g$ (étale site)"
lean = ["AlgebraicGeometry.Etale.isLeftAdjoint_rightDerivedLowerStar_of_isProper"]
order = 2549
uses = ["def-weil-pbc-direct-image", "det-def-sfb-derived-categories", "lem-amb-proper-coproducts"]
+++
Let $\Lambda$ be a finite ring and $g\colon Z\to Y$ a proper morphism of schemes. Then the
derived pushforward

$$
Rg_*\colon D(Z_{\et},\Lambda)\to D(Y_{\et},\Lambda)
$$

on the unbounded derived categories of étale sheaves of $\Lambda$-modules (the right derived
functor [det-def-sfb-derived-categories] of the pushforward of [def-weil-pbc-direct-image]) has
a right adjoint, denoted $Rg^!$.

On the pro-étale site the corresponding statement is false: for the structure morphism of an
elliptic curve over $\overline{\mathbf F}_p$ and $\mathbf F_r$-coefficients, $r\ne p$, the
pro-étale $Rg_*$ does not preserve countable coproducts, even on $D^+$.
