+++
id = "def-sfb-derived-restrict-levelwise"
kind = "definition"
title = "Derived restriction of scalars is termwise"
order = 1573
uses = ["lem-sfb-extend-scalars-kflat", "sk-def-sfb-change-of-scalars", "sk-def-sfb-derived-categories"]
lean = ["CategoryTheory.Mod.rightDerivedComapIsoMapDerivedCategory"]
+++
In the situation of [lem-sfb-extend-scalars-kflat], there is a canonical
isomorphism $R(\operatorname{Res}_\varphi)\cong D(\operatorname{Res}_\varphi)$ between the
right derived restriction of scalars and the functor
$D(\Mod_{\mathcal S})\to D(\Mod_{\mathcal R})$ that restricts scalars termwise.
