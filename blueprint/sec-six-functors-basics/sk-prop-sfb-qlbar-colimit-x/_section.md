+++
id = "sk-prop-sfb-qlbar-colimit-x"
kind = "proposition"
title = "$\\overline{\\mathbf Q}_{\\ell,X}=\\colim_E E_X$"
order = 1495
uses = ["sk-def-sfb-pulled-back-coefficients"]
lean = ["AlgebraicGeometry.ProEtale.padicSubfieldRingObj", "AlgebraicGeometry.ProEtale.padicAlgClRingObj", "AlgebraicGeometry.ProEtale.padicAlgClRingObjCocone", "AlgebraicGeometry.ProEtale.isColimitPadicAlgClRingObjCocone"]
tags = ["sketch"]
+++
Let $\ell$ be a prime. Let $E$ run over the finite subextensions
$\mathbb Q_\ell\subseteq E\subseteq\Qlb$, ordered by inclusion; this is a
filtered poset. Let $\underline E$ be the condensed ring of continuous maps to
$E$ ([sk-def-sfb-condensed-ring]), and let $\underline{\Qlb}$ be the
condensed ring of [sk-def-sfb-qlbar-condensed]. For a scheme $X$, put
([sk-def-sfb-pulled-back-coefficients])
$$
E_X:=p_X^*\underline E,\qquad \overline{\mathbf Q}_{\ell,X}:=p_X^*\underline{\Qlb}.
$$
These are ring objects of $\Sh(X_{\mathrm{proét}},\Ab)$.

For $E\subseteq F$, the inclusions $\underline E\to\underline F\to\underline{\Qlb}$
induce maps $E_X\to F_X\to\overline{\mathbf Q}_{\ell,X}$. The maps
$E_X\to\overline{\mathbf Q}_{\ell,X}$ exhibit $\overline{\mathbf Q}_{\ell,X}$ as
the filtered colimit of the $E_X$ in $\Sh(X_{\mathrm{proét}},\Ab)$:
$$
\overline{\mathbf Q}_{\ell,X}=\colim_E E_X .
$$
