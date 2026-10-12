+++
id = "def-sfb-qlbar-coefficient-ring"
kind = "definition"
title = "The coefficient ring $\\overline{\\mathbf Q}_{\\ell,X}$"
order = 1548
uses = ["sk-def-sfb-pulled-back-coefficients", "sk-def-sfb-qlbar-condensed"]
lean = ["AlgebraicGeometry.ProEtale.padicAlgClRingObj"]
+++
Let $\ell$ be a prime and let $\underline{\Qlb}$ be the condensed ring of
[sk-def-sfb-qlbar-condensed]. For a scheme $X$, put
$\overline{\mathbf Q}_{\ell,X}:=p_X^*\underline{\Qlb}$. By
[sk-def-sfb-pulled-back-coefficients], this is a commutative ring object of
$\Sh(X_{\mathrm{proét}},\Ab)$.
