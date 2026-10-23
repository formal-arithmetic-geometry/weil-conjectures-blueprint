+++
id = "def-sfb-subfield-coefficient-ring"
kind = "definition"
title = "The coefficient ring $E_X$"
order = 1218
uses = ["det-def-sfb-condensed-ring", "det-def-sfb-pulled-back-coefficients"]
lean = ["AlgebraicGeometry.ProEtale.padicSubfieldRingObj"]
+++
Let $\ell$ be a prime and $E\subseteq\Qlb$ a finite extension of
$\mathbb Q_\ell$. Let $\underline E$ be the condensed ring of continuous maps
to $E$ ([det-def-sfb-condensed-ring]). For a scheme $X$, put
$E_X:=p_X^*\underline E$. By [det-def-sfb-pulled-back-coefficients], this is a
commutative ring object of $\Sh(X_{\mathrm{proét}},\Ab)$.
