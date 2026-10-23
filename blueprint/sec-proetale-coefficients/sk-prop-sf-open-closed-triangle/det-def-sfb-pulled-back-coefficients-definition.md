+++
id = "det-def-sfb-pulled-back-coefficients-definition"
kind = "definition"
title = "The coefficient ring $\\Lambda_X=p_X^*\\Lambda$"
uses = ["def-sfb-upper-star-from-point", "det-def-sfb-ring-object-transport", "det-def-sfb-ring-object"]
lean = ["AlgebraicGeometry.ProEtale.coefficientRing", "AlgebraicGeometry.ProEtale.condensedRingObj"]
order = 1164
+++
Let $(\Lambda,\mu,\eta)$ be a ring object of $\Sh(*_{\mathrm{proét}},\Ab)$, for instance the
underlying ring object of a condensed ring ([det-def-sfb-ring-object]). Let $X$ be a scheme and let
$p_X^*\colon\Sh(*_{\mathrm{proét}},\Ab)\to\Sh(X_{\mathrm{proét}},\Ab)$ be the inverse image from the
point of [def-sfb-upper-star-from-point], a strong monoidal braided functor, with tensor
comparison isomorphisms $\delta_{F,G}\colon p_X^*F\otimes p_X^*G\xrightarrow{\sim}p_X^*(F\otimes G)$
and unit comparison isomorphism $\epsilon\colon\underline{\mathbf Z}\xrightarrow{\sim}p_X^*\underline{\mathbf Z}$.
The *pulled-back coefficient ring* is
$$
\Lambda_X:=p_X^*\Lambda\in\Sh(X_{\mathrm{proét}},\Ab),
$$
with multiplication and unit
$$
\mu_X\colon p_X^*\Lambda\otimes p_X^*\Lambda\xrightarrow{\ \delta_{\Lambda,\Lambda}\ }p_X^*(\Lambda\otimes\Lambda)\xrightarrow{\ p_X^*\mu\ }p_X^*\Lambda,
\qquad
\eta_X\colon\underline{\mathbf Z}\xrightarrow{\ \epsilon\ }p_X^*\underline{\mathbf Z}\xrightarrow{\ p_X^*\eta\ }p_X^*\Lambda .
$$
For a morphism $\varphi\colon\Lambda\to\Lambda'$ of ring objects, put $\varphi_X:=p_X^*\varphi\colon\Lambda_X\to\Lambda'_X$.
