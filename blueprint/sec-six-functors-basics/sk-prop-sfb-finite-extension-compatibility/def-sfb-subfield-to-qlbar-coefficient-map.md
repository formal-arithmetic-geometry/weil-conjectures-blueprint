+++
id = "def-sfb-subfield-to-qlbar-coefficient-map"
kind = "definition"
title = "The coefficient change $E_X\\to\\overline{\\mathbf Q}_{\\ell,X}$"
order = 1750
uses = ["sk-def-sfb-qlbar-condensed", "sk-prop-sfb-qlbar-colimit-point", "sk-def-sfb-pulled-back-coefficients", "def-sfb-coefficient-map"]
lean = ["AlgebraicGeometry.ProEtale.padicSubfieldRingObjToPadicAlgCl"]
+++
Let $\ell$ be a prime, $E$ a finite extension of $\mathbf Q_\ell$ inside $\Qlb$, and $X$ a
scheme. The inclusion $E_X\to\overline{\mathbf Q}_{\ell,X}$ is the coefficient change ([def-sfb-coefficient-map])
on $X$ of the inclusion $\underline E\to\underline{\Qlb}$ of condensed rings
([sk-def-sfb-qlbar-condensed], [sk-prop-sfb-qlbar-colimit-point]), a morphism between the
pulled-back coefficient rings $E_X=p_X^*\underline E$ and $\overline{\mathbf Q}_{\ell,X}=p_X^*\underline{\Qlb}$
([sk-def-sfb-pulled-back-coefficients]).
