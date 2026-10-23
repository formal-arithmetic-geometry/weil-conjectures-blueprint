+++
id = "def-sfb-module-open-lower-shriek-adjunction"
kind = "definition"
title = "The adjunction $j_!\\dashv j^*$ on module objects"
order = 2539
uses = ["def-sfb-module-open-lower-shriek", "def-sfb-module-upper-star", "def-sfb-module-linear-open-lower-shriek", "det-def-sfb-change-of-scalars"]
lean = ["AlgebraicGeometry.ProEtale.CondensedRing.openImmersionLowerShriekUpperStarAdjunction"]
+++
Let $\Lambda$ be a commutative condensed ring and $j\colon U\to X$ an open immersion.
The extension by zero $j_!$ of [def-sfb-module-open-lower-shriek] is left adjoint to
the pullback $j^*=\operatorname{Ext}_{\alpha_j}\circ\operatorname{mapMod}(j^*_{\Ab})$
of [def-sfb-module-upper-star], by the adjunction obtained by composing
$\operatorname{Res}_{\alpha_j}\dashv\operatorname{Coext}_{\alpha_j}$
([det-def-sfb-change-of-scalars]) with
$j^{\mathrm{lin}}_!\dashv\operatorname{mapMod}(j^*_{\Ab})$
([def-sfb-module-linear-open-lower-shriek]), and identifying
$\operatorname{Coext}_{\alpha_j}\cong\operatorname{Ext}_{\alpha_j}$.
