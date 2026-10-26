+++
id = "def-sfb-derived-extend-restrict-adjunction"
kind = "definition"
title = "Derived adjunction between extension and restriction of scalars"
order = 2529
uses = ["lem-sfb-extend-scalars-kflat", "det-def-sfb-change-of-scalars", "det-def-sfb-derived-categories"]
lean = ["CategoryTheory.Mod.derivedExtendRestrictAdjunction"]
+++
In the situation of [lem-sfb-extend-scalars-kflat], the adjunction
$\operatorname{Ext}_\varphi\dashv\operatorname{Res}_\varphi$ [det-def-sfb-change-of-scalars]
derives to an adjunction
$$
L(\operatorname{Ext}_\varphi)\dashv R(\operatorname{Res}_\varphi)
$$
between the left derived extension of scalars and the right derived restriction of
scalars on the unbounded derived categories.
