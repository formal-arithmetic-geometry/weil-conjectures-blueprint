+++
id = "def-sfb-derived-extend-levelwise-adjunction"
kind = "definition"
title = "Derived extension of scalars is left adjoint to termwise restriction"
order = 1612
uses = ["lem-sfb-extend-scalars-kflat", "def-sfb-derived-extend-restrict-adjunction", "def-sfb-derived-restrict-levelwise"]
lean = ["CategoryTheory.Mod.derivedExtendMapDerivedCategoryAdjunction"]
+++
In the situation of [lem-sfb-extend-scalars-kflat], there is an adjunction
$$
\mathcal S\otimes^{\mathrm L}_{\mathcal R}-\dashv D(\operatorname{Res}_\varphi)
$$
between the derived extension of scalars and the termwise restriction of scalars.
