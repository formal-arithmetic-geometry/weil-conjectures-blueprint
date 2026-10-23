+++
id = "sk-prop-sfb-cartesian-coefficients"
kind = "lemma"
title = "Inverse image of the coefficient sheaves"
order = 1248
uses = ["sk-prop-sfb-qlbar-colimit-x", "sk-def-sp-tate-twist"]
lean = ["AlgebraicGeometry.ProEtale.isIso_condensedPullbackHom", "AlgebraicGeometry.ProEtale.condensedPushforwardHom_id", "AlgebraicGeometry.ProEtale.condensedPushforwardHom_comp"]
tags = ["sketch"]
+++
Because all coefficient sheaves are pulled back from the point, they are compatible with
inverse image. The same holds for their Tate twists ([sk-def-sp-tate-twist]), and a finite
extension of coefficient fields gives a finite free extension of coefficient sheaves.

Let $f\colon X\to Y$ be a morphism of schemes.

1. For every admissible $\Lambda$, the canonical map
   $$
   f^{-1}\Lambda_Y\longrightarrow\Lambda_X
   $$
   is an isomorphism of sheaves of rings on $X_{\mathrm{proét}}$ (this is the map $\alpha_f$
   of [det-def-sfb-coefficient-morphisms]). The same holds for its Tate twists, including the
   twists of a finite ring $A$.
2. If $E\subset F$ is a finite extension, then $\cO_{F,X}$ is a finite free
   $\cO_{E,X}$-module and $F_X$ is a finite free $E_X$-module.

By (1), the pullback $f^*\colon\Mod(Y_{\mathrm{proét}},\Lambda)\to\Mod(X_{\mathrm{proét}},\Lambda)$
of modules over these sheaves is the exact functor $f^{-1}$.
