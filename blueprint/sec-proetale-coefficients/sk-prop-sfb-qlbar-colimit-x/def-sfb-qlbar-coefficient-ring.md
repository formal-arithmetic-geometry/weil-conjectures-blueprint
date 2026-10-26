+++
id = "def-sfb-qlbar-coefficient-ring"
kind = "definition"
title = "The coefficient ring $\\overline{\\mathbf Q}_{\\ell,X}$"
order = 1197
uses = ["det-def-sfb-pulled-back-coefficients", "det-def-sfb-qlbar-condensed"]
lean = ["AlgebraicGeometry.ProEtale.padicAlgClRingObj"]
+++
Let $\ell$ be a prime and let $\underline{\Qlb}$ be the condensed ring of
[det-def-sfb-qlbar-condensed]. For a scheme $X$, put
$\overline{\mathbf Q}_{\ell,X}:=p_X^*\underline{\Qlb}$. By
[det-def-sfb-pulled-back-coefficients], this is a commutative ring object of
$\Sh(X_{\mathrm{proét}},\Ab)$.
