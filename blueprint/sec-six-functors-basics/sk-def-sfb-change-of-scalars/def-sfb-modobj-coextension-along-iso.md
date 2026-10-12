+++
id = "def-sfb-modobj-coextension-along-iso"
kind = "definition"
title = "Coextension along an isomorphism is restriction along the inverse"
order = 1578
uses = ["def-sfb-modobj-restrict-coextend-adjunction", "def-sfb-modobj-restriction-equivalence"]
lean = ["CategoryTheory.Mod.coextendScalarsIsoComapInv"]
+++
In the situation of [def-sfb-modobj-restriction-equivalence], there is a natural
isomorphism
$$
\operatorname{Coext}_\varphi\cong\operatorname{Res}_{\varphi^{-1}}
$$
of functors $\Mod_{\mathcal R}(\mathcal C)\to\Mod_{\mathcal S}(\mathcal C)$.
