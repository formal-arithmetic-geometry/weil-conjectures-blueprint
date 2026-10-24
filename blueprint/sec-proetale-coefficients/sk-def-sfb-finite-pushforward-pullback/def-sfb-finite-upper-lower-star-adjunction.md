+++
id = "def-sfb-finite-upper-lower-star-adjunction"
kind = "definition"
title = "The adjunction $g^*\\dashv g_*$"
order = 913
uses = ["def-sfb-finite-lower-star", "def-sfb-finite-upper-star"]
lean = ["AlgebraicGeometry.ProEtale.upperStarLowerStarAdjunction"]
+++
For every morphism $g\colon Z\to Y$ the pullback $g^*$ of [def-sfb-finite-upper-star] is
left adjoint to the pushforward $g_*$ of [def-sfb-finite-lower-star]:

$$
\Hom(g^*F,G)\cong\Hom(F,g_*G)
$$

naturally in $F\in\Sh(Y_{\mathrm{proét}},\mathcal A)$ and
$G\in\Sh(Z_{\mathrm{proét}},\mathcal A)$.
