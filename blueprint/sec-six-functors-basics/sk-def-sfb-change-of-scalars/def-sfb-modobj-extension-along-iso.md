+++
id = "def-sfb-modobj-extension-along-iso"
kind = "definition"
title = "Extension along an isomorphism is restriction along the inverse"
order = 1577
uses = ["def-sfb-modobj-extend-restrict-adjunction", "def-sfb-modobj-restriction-equivalence"]
lean = ["CategoryTheory.Mod.extendScalarsIsoComapInv"]
+++
In the situation of [def-sfb-modobj-restriction-equivalence], there is a natural
isomorphism
$$
\operatorname{Ext}_\varphi\cong\operatorname{Res}_{\varphi^{-1}}
$$
of functors $\Mod_{\mathcal R}(\mathcal C)\to\Mod_{\mathcal S}(\mathcal C)$.
