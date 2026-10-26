+++
id = "def-sfb-integers-to-subfield"
kind = "definition"
title = "The inclusion $\\mathcal O_{E,X}\\to E_X$"
order = 1186
uses = ["def-sfb-integers-to-subfield-point", "det-def-sfb-pullback-from-point", "det-def-sfb-pulled-back-coefficients"]
lean = ["AlgebraicGeometry.ProEtale.padicIntegersToPadicSubfield"]
+++
For a scheme $X$, the morphism of ring objects
$$
\varphi=p_X^*(\underline{\cO}_E\to\underline E)\colon\cO_{E,X}=p_X^*\underline{\cO}_E\to E_X=p_X^*\underline E
$$
of $\Sh(X_{\mathrm{proét}},\Ab)$ is the image under $p_X^*$ [det-def-sfb-pullback-from-point]
of the morphism of [def-sfb-integers-to-subfield-point], between the coefficient rings of
[det-def-sfb-pulled-back-coefficients].
