+++
id = "def-sfb-finite-extension-by-zero-adjunction"
kind = "definition"
title = "The adjunction $j_!\\dashv j^*$"
order = 2486
uses = ["def-weil-extension-by-zero", "def-sfb-finite-upper-star"]
lean = ["AlgebraicGeometry.ProEtale.openImmersionLowerShriekUpperStarAdjunction"]
+++
For an open immersion $j\colon U\to X$, the extension by zero $j_!$ of
[def-weil-extension-by-zero] is left adjoint to the pullback $j^*$ of
[def-sfb-finite-upper-star]. The pullback is computed by restriction:
$(j^*G)(T\to U)\cong G(T\to U\to X)$.
