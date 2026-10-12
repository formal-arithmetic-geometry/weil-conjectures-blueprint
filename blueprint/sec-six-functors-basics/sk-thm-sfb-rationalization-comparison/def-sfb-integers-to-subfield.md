+++
id = "def-sfb-integers-to-subfield"
kind = "definition"
title = "The inclusion $\\mathcal O_{E,X}\\to E_X$"
order = 1630
uses = ["def-sfb-integers-to-subfield-point", "sk-def-sfb-pullback-from-point", "sk-def-sfb-pulled-back-coefficients"]
lean = ["AlgebraicGeometry.ProEtale.padicIntegersToPadicSubfield"]
+++
For a scheme $X$, the morphism of ring objects
$$
\varphi=p_X^*(\underline{\cO}_E\to\underline E)\colon\cO_{E,X}=p_X^*\underline{\cO}_E\to E_X=p_X^*\underline E
$$
of $\Sh(X_{\mathrm{proét}},\Ab)$ is the image under $p_X^*$ [sk-def-sfb-pullback-from-point]
of the morphism of [def-sfb-integers-to-subfield-point], between the coefficient rings of
[sk-def-sfb-pulled-back-coefficients].
