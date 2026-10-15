+++
id = "lem-sfb-finite-upper-star-tensor"
kind = "lemma"
title = "$g^*$ commutes with the tensor product"
order = 1517
uses = ["def-sfb-finite-lower-star-lax-monoidal", "def-sfb-finite-upper-lower-star-adjunction", "sk-def-sfb-sheaf-tensor"]
lean = ["AlgebraicGeometry.ProEtale.isIso_δ_upperStar"]
+++
Let $\mathcal A$ and $g\colon Z\to Y$ be as in [lem-sfb-finite-upper-star-unit]. For
sheaves $F,G$ on $Y_{\mathrm{proét}}$, the map

$$
g^*(F\otimes G)\to g^*F\otimes g^*G,
$$

mate under $g^*\dashv g_*$ ([def-sfb-finite-upper-lower-star-adjunction]) of the lax
structure of [def-sfb-finite-lower-star-lax-monoidal], is an isomorphism.
