+++
id = "def-sfb-finite-upper-star"
kind = "definition"
title = "Pullback $g^*$ along base change"
order = 1493
uses = ["def-sfb-finite-lower-star", "def-weil-pbc-proetale-site"]
lean = ["AlgebraicGeometry.ProEtale.upperStar"]
+++
Let $\mathcal A$ and $g\colon Z\to Y$ be as in [def-sfb-finite-lower-star], with
$b\colon Y_{\mathrm{proét}}\to Z_{\mathrm{proét}}$ the base change functor. The *pullback*

$$
g^*\colon\Sh(Y_{\mathrm{proét}},\mathcal A)\to\Sh(Z_{\mathrm{proét}},\mathcal A),
\qquad g^*F:=\operatorname{sheafify}\bigl(\operatorname{Lan}_{b^{\mathrm{op}}}F\bigr),
$$

is the left Kan extension of the underlying presheaf of $F$ along
$b^{\mathrm{op}}$, followed by sheafification on $Z_{\mathrm{proét}}$.
