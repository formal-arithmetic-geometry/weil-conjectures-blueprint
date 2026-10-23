+++
id = "def-sfb-derived-restrict-levelwise"
kind = "definition"
title = "Derived restriction of scalars is termwise"
order = 2549
uses = ["lem-sfb-extend-scalars-kflat", "det-def-sfb-change-of-scalars", "det-def-sfb-derived-categories"]
lean = ["CategoryTheory.Mod.rightDerivedComapIsoMapDerivedCategory"]
+++
In the situation of [lem-sfb-extend-scalars-kflat], there is a canonical
isomorphism $R(\operatorname{Res}_\varphi)\cong D(\operatorname{Res}_\varphi)$ between the
right derived restriction of scalars and the functor
$D(\Mod_{\mathcal S})\to D(\Mod_{\mathcal R})$ that restricts scalars termwise.
