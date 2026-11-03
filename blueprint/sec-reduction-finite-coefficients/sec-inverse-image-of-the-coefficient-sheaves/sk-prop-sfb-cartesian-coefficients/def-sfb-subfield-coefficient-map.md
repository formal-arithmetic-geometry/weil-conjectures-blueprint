+++
id = "def-sfb-subfield-coefficient-map"
kind = "definition"
title = "The coefficient change $E_X\\to F_X$"
order = 1298
uses = ["det-prop-sfb-qlbar-colimit-point", "det-def-sfb-pulled-back-coefficients", "def-sfb-coefficient-map"]
lean = ["AlgebraicGeometry.ProEtale.padicSubfieldRingObjMap"]
+++
Let $\ell$ be a prime, $E\le F$ finite extensions of $\mathbf Q_\ell$ inside $\Qlb$, and $X$ a
scheme. The inclusion $E_X\to F_X$ is the coefficient change ([def-sfb-coefficient-map]) on $X$
of the inclusion $\underline E\to\underline F$ of condensed rings
([det-prop-sfb-qlbar-colimit-point]), a morphism between the pulled-back coefficient rings
$E_X=p_X^*\underline E$ and $F_X=p_X^*\underline F$ ([det-def-sfb-pulled-back-coefficients]).
