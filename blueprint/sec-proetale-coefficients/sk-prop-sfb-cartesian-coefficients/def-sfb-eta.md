+++
id = "def-sfb-eta"
kind = "definition"
title = "The coefficient morphism $\\eta_f$"
order = 1254
uses = ["def-sfb-alpha", "def-sfb-finite-upper-lower-star-adjunction"]
lean = ["AlgebraicGeometry.ProEtale.condensedPushforwardHom"]
+++
Let $\Lambda$ be a condensed ring and $f\colon X\to Y$ a morphism of schemes.
The morphism
$$
\eta_f\colon\Lambda_Y\longrightarrow f_*f^*\Lambda_Y\xrightarrow{\ f_*\alpha_f\ }f_*\Lambda_X
$$
is the unit of the adjunction $f^*\dashv f_*$
([def-sfb-finite-upper-lower-star-adjunction]) followed by $f_*$ of $\alpha_f$
([def-sfb-alpha]). In other words, it is the mate of $\alpha_f$.
