+++
id = "lemma-inverse-image-coefficient-sheaves"
kind = "lemma"
title = "Inverse image of the coefficient sheaves"
order = 187
lean = ["AlgebraicGeometry.ProEtale.cartesianCoefficients", "AlgebraicGeometry.ProEtale.isIso_condensedPullbackHom"]
uses = ["definition-ind-etale-pro-etale-weakly", "lemma-stability", "definition-small-pro-etale-site", "proposition-topos-functoriality", "example-locally-constant-functions-w-local", "definition-tate-twists"]
+++
Let $f:X\to Y$ be a morphism of schemes.

1. For every admissible $\Lambda$, the canonical map
   $$
   f^{-1}\Lambda_Y\longrightarrow\Lambda_X
   $$
   is an isomorphism of sheaves of rings. If $\ell$ is invertible on $Y$,
   the same holds for its Tate twists, including the twists of a finite
   ring $A$.
2. If $E\subset E'$ is a finite extension, then $\mathcal O_{E',X}$ is a
   finite free $\mathcal O_{E,X}$-module and $E'_X$ is a finite free
   $E_X$-module.
